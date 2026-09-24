#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""Compare source wording with semantic layout input; inspect rendered fields.

Prose layout whitespace and supported emphasis markers are ignored. Punctuation,
word order, code bytes, links and image identities are not silently normalized.
This is not a WeChat paste test or an OCR/import completeness guarantee.
"""
import argparse
import difflib
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

LABELS = {'风险提醒', '补充说明', '行动建议', '虚构示例', '提示', '数据'}
DEFAULT_SIGNATURE = {'name': '作者姓名', 'bio': '一句话介绍自己',
                     'cta': '感谢阅读。欢迎留言分享你的看法。'}
INLINE = re.compile(r'(\*\*.*?\*\*|==.*?==|\+\+.*?\+\+|~~.*?~~|`[^`]+`|\[[^\]]+\]\([^)]+\))')


def inline_text(value):
    result = []
    for part in INLINE.split(value):
        if part.startswith('`') and part.endswith('`'):
            result.append(part[1:-1])
        elif part.startswith(('**', '==', '++', '~~')) and len(part) >= 4:
            result.append(part[2:-2])
        elif re.fullmatch(r'\[[^\]]+\]\([^)]+\)', part):
            result.append(part[1:part.index('](')])
        else:
            result.append(part)
    return ''.join(result)


def compact(text):
    return re.sub(r'\s+', '', text)


def fields(block, prefix=''):
    """Fields in semantic reading order; labels that carry meaning stay here."""
    typ = block['type']
    keys = {
        'paragraph': ['text'], 'chapter': ['text', 'subtitle'], 'heading': ['text'],
        'intro': ['text', 'attribution'], 'quote': ['text', 'attribution'],
        'conclusion': ['title', 'text'], 'signature': ['name', 'bio', 'cta'],
        'placeholder': ['text'], 'image': ['alt', 'caption'], 'code': ['text'],
        'note': ['title'], 'toc': ['title'], 'list': [], 'steps': [],
        'cards': ['title'], 'compare': ['title'], 'timeline': [],
        'metrics': ['title'], 'table': ['title'], 'divider': [],
    }
    if typ not in keys:
        raise ValueError('文字核对不支持内容块：' + typ)
    result = [(prefix+'/'+k, block[k]) for k in keys[typ] if block.get(k)]
    for i, item in enumerate(block.get('items', [])):
        path = prefix+'/items/'+str(i)
        if isinstance(item, str):
            result.append((path, item))
        else:
            order = {'cards': ['label', 'title', 'text'], 'compare': ['title', 'text'],
                     'timeline': ['label', 'text'], 'metrics': ['value', 'label', 'detail']}[typ]
            result += [(path+'/'+k, item[k]) for k in order if item.get(k)]
    if typ == 'table':
        result += [(prefix+'/headers/'+str(i), v) for i, v in enumerate(block['headers'])]
        result += [(prefix+'/rows/'+str(i)+'/'+str(j), v)
                   for i, row in enumerate(block['rows']) for j, v in enumerate(row)]
    return result


def source_doc(path):
    path = Path(path)
    raw = path.read_text(encoding='utf-8')
    if path.suffix.lower() == '.json':
        return json.loads(raw), 'normalized-json'
    # Fail closed on syntax the basic importer cannot faithfully interpret.
    prose = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', raw, flags=re.M | re.S)
    unsupported = (r'^---\s*\n', r'^[ \t]+[-*+] ', r'^[ \t]+\d+[.)] ',
                   r'\[\^[^]]+\]', r'^\[[^]]+\]:', r'<[/A-Za-z]',
                   r'^~~~', r'(?m)^\t', r'(?m)^ {4}\S', r'!\[[^]]*\]\([^\n]*\([^\n]*\)')
    if any(re.search(pattern, prose, re.M) for pattern in unsupported):
        raise ValueError('原稿含复杂Markdown；请先逐项无损整理为 source.json 并人工核对，不能以基础解析结果声称原稿完整')
    from render import markdown
    return markdown(raw), 'markdown'


def additions(doc):
    result = {}
    for entry in doc.get('editorial_plan', {}).get('allowed_additions', []):
        if not isinstance(entry, dict):
            raise ValueError('allowed_additions 必须逐字段声明 path、text、kind')
        path, value, kind = entry['path'], entry['text'], entry['kind']
        if path in result:
            raise ValueError('重复附加字段：' + path)
        match = re.fullmatch(r'/blocks/(\d+)/(name|bio|cta|title)', path)
        if not match:
            raise ValueError('不能豁免正文或章节文字：' + path)
        block = doc['blocks'][int(match[1])]; key = match[2]
        if block.get(key) != value:
            raise ValueError('附加字段声明与实际文字不符：' + path)
        valid_signature = kind == 'signature' and block['type'] == 'signature' and DEFAULT_SIGNATURE.get(key) == value
        valid_label = kind == 'component_label' and block['type'] in {'note', 'cards', 'metrics', 'table'} and key == 'title' and value in LABELS
        if not (valid_signature or valid_label):
            raise ValueError('不在默认附加范围：' + path + '；用户另行提供的文案应纳入确认后的原稿基线')
        result[path] = value
    return result


def image_identity(src, base):
    parsed = urlparse(src)
    if parsed.scheme in {'http', 'https'}:
        return src
    p = Path(unquote(parsed.path)) if parsed.scheme == 'file' else Path(src)
    p = p if p.is_absolute() else Path(base)/p
    if not p.is_file():
        raise ValueError('核对图片不存在：' + str(p))
    return hashlib.sha256(p.read_bytes()).hexdigest()


def inventory(doc, base, excluded=None):
    excluded = excluded or {}
    chunks = [inline_text(doc['title']), inline_text(doc.get('subtitle', ''))]
    links = []; images = []; codes = []; inline_codes = []; field_count = 1
    for i, block in enumerate(doc['blocks']):
        for path, value in fields(block, '/blocks/'+str(i)):
            if path in excluded:
                continue
            field_count += 1
            if block['type'] == 'code':
                codes.append(value)
                chunks.append('\x00CODE'+str(len(codes))+'\x00')
            else:
                chunks.append(inline_text(value))
                inline_codes += re.findall(r'`([^`]+)`', value)
                links += re.findall(r'(?<!!)\[[^]]+\]\(([^)]+)\)', value)
        if block['type'] == 'image':
            images.append(image_identity(block['src'], base))
    for key in ['title', 'subtitle']:
        links += re.findall(r'(?<!!)\[[^]]+\]\(([^)]+)\)', doc.get(key, ''))
    return {'text': compact(''.join(chunks)), 'code': codes, 'links': links,
            'images': images, 'inline_code': inline_codes, 'fields': field_count}


def compare(source, doc, source_base='.', article_base='.'):
    excluded = additions(doc)
    before = inventory(source, source_base)
    after = inventory(doc, article_base, excluded)
    changes = []
    if before['text'] != after['text']:
        for tag, i, j, k, l in difflib.SequenceMatcher(None, before['text'], after['text'], autojunk=False).get_opcodes():
            if tag != 'equal':
                changes.append({'kind': tag, 'source_offset': i,
                                'before': before['text'][i:j], 'after': after['text'][k:l]})
    for key in ['code', 'inline_code', 'links', 'images']:
        if before[key] != after[key]:
            changes.append({'kind': key+'-changed', 'before': before[key], 'after': after[key]})
    return {'passed': not changes, 'changes': changes, 'allowed_additions': excluded,
            'source_fields': before['fields'], 'article_fields': after['fields'],
            'scope': '忽略正文排版空白和支持的强调标记；核对文字顺序、标点、代码、链接与图片。JSON基线需先人工核对原材料。'}


class FragmentText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.text = ''; self.links = []; self.images = []; self.code_lines = []; self.code_line = None
    def handle_data(self, data):
        self.text += data
        if self.code_line is not None: self.code_line += data
    def handle_endtag(self, tag):
        if tag == 'p' and self.code_line is not None:
            self.code_lines.append(self.code_line); self.code_line = None
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'p' and 'white-space:pre-wrap' in attrs.get('style','').replace(' ', ''): self.code_line = ''
        if tag == 'a': self.links.append(attrs.get('href', ''))
        if tag == 'img': self.images.append(attrs)


def inspect_rendered(doc, fragment, article_base='.', output_base='.', no_images=False):
    """Check fields within each generated block, then list all renderer additions."""
    failures = []; decorations = []; total = 0
    cover = fragment.split('<!-- jpm:block:0 -->')[0]
    cover_text = FragmentText(); cover_text.feed(cover)
    for key in ['title', 'subtitle']:
        expected = compact(inline_text(doc.get(key, '')))
        if expected and expected not in compact(cover_text.text): failures.append('/'+key)
    # Cover repeats/reorders metadata by design; record it rather than call it source.
    decorations.append({'area': 'cover', 'rendered_text': cover_text.text})
    for i, block in enumerate(doc['blocks']):
        match = re.search(r'<!-- jpm:block:'+str(i)+r' -->(.*?)<!-- jpm:end:'+str(i)+r' -->', fragment, re.S)
        if not match:
            failures.append('missing-block:'+str(i)); continue
        parser = FragmentText(); parser.feed(match[1]); remaining = compact(parser.text)
        values = fields(block, '/blocks/'+str(i))
        if block['type'] == 'image':
            values = [(p,v) for p,v in values if not p.endswith('/alt')]
            if not no_images:
                expected = image_identity(block['src'], article_base)
                if len(parser.images) != 1 or image_identity(parser.images[0]['src'], output_base) != expected or parser.images[0].get('alt','') != block.get('alt',''):
                    failures.append('image:'+str(i))
            else:
                decorations.append({'area': str(i), 'omitted_image': block['src']}); continue
        if block['type'] == 'code':
            expected_lines = [line or ' ' for line in block['text'].split('\n')]
            if parser.code_lines != expected_lines: failures.append('code-whitespace:'+str(i))
        # A table is rendered row by row with repeated column headings.
        if block['type'] == 'table':
            values = []
            for row in block['rows']:
                if block.get('title'): values.append(('', block['title']))
                for h,v in zip(block['headers'],row): values += [('', h),('', v)]
        extras = []
        for path, value in values:
            expected = compact(value if block['type']=='code' else inline_text(value))
            if not expected: continue
            at = remaining.find(expected)
            if at < 0:
                failures.append(path or 'table:'+str(i)); continue
            extras.append(remaining[:at]); remaining = remaining[at+len(expected):]; total += 1
        extras.append(remaining)
        if ''.join(extras): decorations.append({'area': str(i), 'text': ''.join(extras)})
        expected_links = [url for _,value in values for url in re.findall(r'(?<!!)\[[^]]+\]\(([^)]+)\)',value)] if block['type']!='code' else []
        if parser.links != expected_links: failures.append('links:'+str(i))
    return {'passed': not failures, 'missing_or_changed_fields': failures,
            'checked_fields': total, 'renderer_additions': decorations,
            'scope': '逐块检查文字字段与顺序，列出模板装饰；代码逐行比较（空行使用单空格占位）。微信未实贴。'}


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('source', type=Path); cli.add_argument('article', type=Path)
    args = cli.parse_args()
    source, kind = source_doc(args.source)
    doc = json.loads(args.article.read_text(encoding='utf-8'))
    report = compare(source, doc, args.source.parent, args.article.parent)
    report['source_kind'] = kind
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report['passed'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
