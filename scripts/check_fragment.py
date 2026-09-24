#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
# JPM modified distribution, 2026-09-24. See package-root NOTICE.md and CHANGES.md.
"""Inspect a pasteable article fragment using JPM's explicit output contract.

Standard library only. This is a structural/local-resource check, not a simulation
of the publishing platform's sanitizer. Reports machine-readable issue codes.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import argparse
import json
import re

ELEMENTS = {'section', 'p', 'span', 'strong', 'em', 'b', 'i', 'a', 'img',
            'br', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}
ATTRIBUTES = {'style', 'leaf', 'href', 'src', 'alt', 'title'}
VOID = {'img', 'br'}

class FragmentInspector(HTMLParser):
    def __init__(self, base_dir=None):
        super().__init__(convert_charrefs=True)
        self.base_dir = Path(base_dir) if base_dir else None
        self.stack = []
        self.issues = []
        self.roots = []
        self.elements = 0
        self.text_nodes = 0
        self.images = 0
        self.links = 0

    def issue(self, code, detail):
        line, column = self.getpos()
        self.issues.append({'code': code, 'line': line, 'column': column,
                            'detail': detail})

    def handle_decl(self, decl):
        self.issue('document-shell', 'Expected a section fragment, not a document declaration')

    def handle_pi(self, data):
        self.issue('processing-instruction', 'Processing instructions are not article content')

    def check_url(self, raw, image=False):
        if not raw or any(ord(c) < 32 for c in raw):
            self.issue('invalid-url', 'Missing URL or control character in URL')
            return
        try:
            url = urlsplit(raw)
        except ValueError:
            self.issue('invalid-url', 'URL cannot be parsed')
            return
        if url.scheme.lower() not in {'', 'http', 'https'}:
            self.issue('url-scheme', 'Output accepts relative paths and HTTP(S) only')
        if url.scheme.lower() in {'http', 'https'} and not url.netloc:
            self.issue('invalid-url', 'HTTP(S) requires a host')
        if image and not url.scheme and not url.netloc:
            local = Path(unquote(url.path))
            if local.is_absolute() or '..' in local.parts:
                self.issue('image-path', 'Local images must remain within the output directory')
            elif self.base_dir and not (self.base_dir / local).is_file():
                self.issue('missing-image', 'Local image file not found: ' + raw)

    def check_style(self, style):
        # Generated CSS does not require escape sequences, comments, URL assets,
        # custom properties, expressions, or nested stylesheet rules.
        lower = style.lower()
        if any(x in lower for x in ['\\', '/*', '*/', '@', '{', '}', 'url(',
                                     'expression(', 'var(', 'behavior:', '-moz-binding']):
            self.issue('css-resource-or-code', 'Unsupported escape, resource, rule, or expression')
        for declaration in style.split(';'):
            if not declaration.strip():
                continue
            if ':' not in declaration:
                self.issue('css-declaration', 'CSS declaration has no colon')
                continue
            key, value = declaration.split(':', 1)
            key, value = key.strip().lower(), value.strip().lower()
            if key.startswith('--'):
                self.issue('css-variable', 'Use concrete inline values')
            compact = re.sub(r'\s+|!important', '', value)
            if key == 'position' and compact in {'absolute', 'fixed', 'sticky'}:
                self.issue('positioning', 'Out-of-flow positioning is not supported')
            if key == 'float' and compact != 'none':
                self.issue('float-layout', 'Floats are not supported')
            if key == 'display' and 'grid' in compact:
                self.issue('grid-layout', 'Grid layout is not supported')
            if key in {'animation', 'animation-name'} and compact != 'none':
                self.issue('animation', 'Animation is not supported in the article fragment')

    def handle_starttag(self, tag, attrs):
        self.elements += 1
        if not self.stack:
            self.roots.append(tag)
        if tag not in ELEMENTS:
            self.issue('element', 'Unsupported element: ' + tag)
        seen = set()
        data = dict(attrs)
        for key, value in attrs:
            if key in seen:
                self.issue('duplicate-attribute', key)
            seen.add(key)
            if key not in ATTRIBUTES:
                self.issue('attribute', 'Unsupported attribute: ' + key)
            if key == 'leaf' and tag != 'span':
                self.issue('leaf-element', 'leaf belongs on a text span')
            if key == 'href' and tag != 'a':
                self.issue('link-element', 'href belongs on a link')
            if key == 'src' and tag != 'img':
                self.issue('image-element', 'src belongs on an image')
        if data.get('style'):
            self.check_style(data['style'])
        if tag == 'a':
            self.links += 1
            self.check_url(data.get('href', ''))
        if tag == 'img':
            self.images += 1
            self.check_url(data.get('src', ''), image=True)
            styles = {k.strip().lower(): v.strip().lower() for k, v in
                      (item.split(':', 1) for item in data.get('style', '').split(';') if ':' in item)}
            if styles.get('max-width') != '100%' or styles.get('height') != 'auto':
                self.issue('image-sizing', 'Images need max-width:100% and height:auto')
            if styles.get('width') == '100%':
                self.issue('image-stretch', 'Do not enlarge small source images')
        if self.stack and self.stack[-1][0] == 'p' and tag in {'section', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}:
            self.issue('paragraph-nesting', 'Block element inside paragraph changes browser structure')
        if tag not in VOID:
            self.stack.append((tag, 'leaf' in data))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1][0] != tag:
            self.issue('closing-tag', 'Unmatched or out-of-order closing tag: ' + tag)
        else:
            self.stack.pop()

    def handle_data(self, data):
        if not data.strip():
            return
        self.text_nodes += 1
        if not self.stack or self.stack[-1] != ('span', True):
            self.issue('text-wrapper', 'Visible text must be directly inside span[leaf]')

    def finish(self):
        if self.stack:
            self.issue('unclosed-element', ', '.join(tag for tag, _ in self.stack))
        if self.roots != ['section']:
            self.issue('fragment-root', 'Exactly one section root is required')
        return {'passed': not self.issues, 'issues': self.issues,
                'counts': {'elements': self.elements, 'textNodes': self.text_nodes,
                           'images': self.images, 'links': self.links},
                'scope': 'Structural validation and local images; editor paste not tested'}


def inspect_fragment(source, base_dir=None):
    parser = FragmentInspector(base_dir)
    parser.feed(source)
    parser.close()
    return parser.finish()


def main():
    command = argparse.ArgumentParser(description=__doc__)
    command.add_argument('html', type=Path)
    command.add_argument('--report', type=Path)
    args = command.parse_args()
    result = inspect_fragment(args.html.read_text(encoding='utf-8'), args.html.parent)
    encoded = json.dumps(result, ensure_ascii=False, indent=2)
    if args.report:
        if args.report.exists():
            command.error('Report exists; choose a new path')
        args.report.write_text(encoded, encoding='utf-8')
    print(encoded)
    return 0 if result['passed'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
