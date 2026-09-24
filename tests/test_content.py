# SPDX-License-Identifier: AGPL-3.0-only
from pathlib import Path
import copy
import json
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from check_content import compare, inspect_rendered, source_doc
from render import markdown


class ContentTests(unittest.TestCase):
    def setUp(self):
        self.source = markdown('# 原标题\n\n原话: "不能改。"\n\n## 验证\n\n12条记录，不是真实客户数据。\n\n先看原话。\n\n再做验证。')

    def test_visual_emphasis_and_layout_conversion_preserve_wording(self):
        doc = copy.deepcopy(self.source)
        doc['blocks'][2]['text'] = '++12条记录++，不是真实客户数据。'
        doc['blocks'][3:] = [{'type':'steps','items':['先看原话。','再做验证。']}]
        self.assertTrue(compare(self.source, doc)['passed'])

    def test_deletion_rewrite_punctuation_number_order_and_undeclared_intro_fail(self):
        for change in ['delete','rewrite','punctuation','number','order','toc']:
            doc = copy.deepcopy(self.source)
            if change=='delete':doc['blocks'].pop()
            if change=='rewrite':doc['blocks'][-1]['text']='再去验证。'
            if change=='punctuation':doc['blocks'][0]['text']='原话：“不能改。”'
            if change=='number':doc['blocks'][2]['text']='13条记录，不是真实客户数据。'
            if change=='order':doc['blocks'][-2:]=reversed(doc['blocks'][-2:])
            if change=='toc':doc['blocks'].insert(0,{'type':'toc','items':['新导读。']})
            with self.subTest(change=change):self.assertFalse(compare(self.source,doc)['passed'])

    def test_additions_are_bounded_and_declared(self):
        doc = copy.deepcopy(self.source)
        index = len(doc['blocks'])
        doc['blocks'].append({'type':'signature','name':'作者姓名','bio':'一句话介绍自己','cta':'感谢阅读。欢迎留言分享你的看法。'})
        self.assertFalse(compare(self.source,doc)['passed'])
        doc['editorial_plan']={'allowed_additions':[{'path':f'/blocks/{index}/{k}','kind':'signature','text':v} for k,v in doc['blocks'][-1].items() if k!='type']}
        self.assertTrue(compare(self.source,doc)['passed'])
        doc['editorial_plan']['allowed_additions'].append({'path':'/blocks/0/text','text':doc['blocks'][0]['text'],'kind':'component_label'})
        with self.assertRaises(ValueError):compare(self.source,doc)

    def test_component_label_cannot_hide_new_factual_text(self):
        doc=copy.deepcopy(self.source);doc['blocks'][2]={'type':'note','title':'虚构示例','items':[doc['blocks'][2]['text']]}
        doc['editorial_plan']={'allowed_additions':[{'path':'/blocks/2/title','text':'虚构示例','kind':'component_label'}]}
        self.assertTrue(compare(self.source,doc)['passed'])
        doc['blocks'][2]['title']='新增结论';doc['editorial_plan']['allowed_additions'][0]['text']='新增结论'
        with self.assertRaises(ValueError):compare(self.source,doc)

    def test_code_whitespace_and_link_targets_are_checked(self):
        source=markdown('# 代码\n\n```python\nif True:\n    print("12")\n```\n\n[来源](https://example.com/a)')
        doc=copy.deepcopy(source);doc['blocks'][0]['text']=doc['blocks'][0]['text'].replace('    ','  ')
        self.assertFalse(compare(source,doc)['passed'])
        inline=markdown('# 标题\n\n命令 `x  y`。')
        edited=copy.deepcopy(inline);edited['blocks'][0]['text']='命令 `x y`。'
        self.assertFalse(compare(inline,edited)['passed'])
        doc=copy.deepcopy(source);doc['blocks'][1]['text']='[来源](https://example.com/b)'
        self.assertFalse(compare(source,doc)['passed'])

    def test_complex_source_is_not_claimed_as_verified(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'source.md';path.write_text('# 标题\n\n- 第一层\n  - 嵌套内容')
            with self.assertRaises(ValueError):source_doc(path)

    def test_flat_lists_with_blank_lines_are_supported(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'source.md';path.write_text('# 标题\n\n1. 先观察。\n2. 再验证。\n\n- 保留原话。')
            doc,kind=source_doc(path)
            self.assertEqual(kind,'markdown');self.assertEqual(doc['blocks'][0]['items'],['先观察。','再验证。'])

    def test_image_omission_is_caught(self):
        source=json.loads((ROOT/'evals/fixtures/article.json').read_text())
        doc=copy.deepcopy(source);doc['blocks']=[b for b in doc['blocks'] if b['type']!='image']
        self.assertFalse(compare(source,doc,ROOT/'evals/fixtures',ROOT/'evals/fixtures')['passed'])

    def test_json_requires_source_unverified_is_explicit(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'output';fixture=ROOT/'evals/fixtures/article.json'
            cmd=[sys.executable,str(ROOT/'scripts/render.py'),str(fixture),'--theme','1','--out',str(out)]
            result=subprocess.run(cmd,text=True,capture_output=True)
            self.assertNotEqual(result.returncode,0);self.assertFalse(out.exists())
            subprocess.run(cmd+['--allow-unverified'],check=True,capture_output=True)
            report=json.loads((out/'检查记录.json').read_text())
            self.assertFalse(report['content']['passed']);self.assertIn('未核对',report['content']['status'])

    def test_all_themes_preserve_original_and_natural_signature(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp=Path(tmp);source=tmp/'source.md';source.write_text('# 保留原文\n\n原话: "12条，仅为虚构示例。"\n\n## 下一步\n\n先记录，再验证。')
            doc=markdown(source.read_text());index=len(doc['blocks']);doc['blocks'].append({'type':'signature','name':'作者姓名','bio':'一句话介绍自己','cta':'感谢阅读。欢迎留言分享你的看法。'})
            doc['editorial_plan']={'allowed_additions':[{'path':f'/blocks/{index}/{k}','kind':'signature','text':v} for k,v in doc['blocks'][-1].items() if k!='type']}
            path=tmp/'article.json';path.write_text(json.dumps(doc,ensure_ascii=False));out=tmp/'rendered'
            subprocess.run([sys.executable,str(ROOT/'scripts/render.py'),str(path),'--source',str(source),'--theme','all','--out',str(out)],check=True,capture_output=True)
            report=json.loads((out/'文字核对.json').read_text());self.assertTrue(report['source_comparison']['passed']);self.assertEqual(len(report['themes']),8)
            for f in out.glob('*-正文.html'):
                html=f.read_text();self.assertNotIn('{{',html);self.assertEqual(html.count('作者姓名'),1);self.assertTrue(inspect_rendered(doc,html)['passed'])
                changed=html.replace('12条','13条')
                self.assertFalse(inspect_rendered(doc,changed)['passed'])

    def test_mismatch_stops_before_output_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp=Path(tmp);source=tmp/'source.md';source.write_text('# 标题\n\n12条记录。');doc=markdown('# 标题\n\n13条记录。');path=tmp/'article.json';path.write_text(json.dumps(doc));out=tmp/'rendered'
            result=subprocess.run([sys.executable,str(ROOT/'scripts/render.py'),str(path),'--source',str(source),'--theme','all','--out',str(out)],capture_output=True)
            self.assertNotEqual(result.returncode,0);self.assertFalse(out.exists())

if __name__=='__main__':unittest.main()
