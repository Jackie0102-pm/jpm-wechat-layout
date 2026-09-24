#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: AGPL-3.0-only
# JPM modified distribution, 2026-09-24. See package-root NOTICE.md and CHANGES.md.
"""Render semantic article JSON or simple Markdown with the eight fixed themes."""
from pathlib import Path
import argparse,html,importlib.util,json,re,shutil,subprocess,sys
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]
THEMES=json.loads((ROOT/'assets/themes.json').read_text())

def theme_module(t):
 p=ROOT/'scripts/themes'/(t['id'].replace('-','_')+'.py')
 spec=importlib.util.spec_from_file_location(t['id'],p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def markdown(text):
 lines=text.splitlines();blocks=[];title='';i=0
 while i<len(lines):
  line=lines[i].strip()
  if not line:i+=1;continue
  if line.startswith('```'):
   lang=line[3:].strip();code=[];i+=1
   while i<len(lines) and not lines[i].strip().startswith('```'):code.append(lines[i]);i+=1
   if i==len(lines):raise ValueError('代码围栏未关闭')
   blocks.append({'type':'code','text':'\n'.join(code),'language':lang});i+=1;continue
  if line.startswith('# ') and not title:title=line[2:];i+=1;continue
  if line.startswith('## '):blocks.append({'type':'chapter','text':line[3:]});i+=1;continue
  if re.match(r'^#{3,6} ',line):blocks.append({'type':'heading','text':line.lstrip('# ')});i+=1;continue
  if re.fullmatch(r'[-*_]{3,}',line):blocks.append({'type':'divider'});i+=1;continue
  im=re.fullmatch(r'!\[(.*?)\]\((.*?)\)',line)
  if im:blocks.append({'type':'image','src':im[2],'alt':im[1]});i+=1;continue
  if line.startswith('> '):
   q=[]
   while i<len(lines) and lines[i].strip().startswith('> '):q.append(lines[i].strip()[2:]);i+=1
   blocks.append({'type':'quote','text':'\n'.join(q)});continue
  if re.match(r'^(?:[-*+] |\d+[.)] )',line):
   items=[]
   while i<len(lines) and re.match(r'^(?:[-*+] |\d+[.)] )',lines[i].strip()):items.append(re.sub(r'^(?:[-*+] |\d+[.)] )','',lines[i].strip()));i+=1
   blocks.append({'type':'list','items':items});continue
  if '|' in line and i+1<len(lines) and re.fullmatch(r'[\s|:\-]+',lines[i+1]) and '-' in lines[i+1]:
   def cells(x):return [c.strip() for c in x.strip().strip('|').split('|')]
   headers=cells(line);rows=[];i+=2
   while i<len(lines) and '|' in lines[i]:rows.append(cells(lines[i]));i+=1
   blocks.append({'type':'table','headers':headers,'rows':rows});continue
  para=[line];i+=1
  while i<len(lines) and lines[i].strip() and not re.match(r'^(#{1,6} |>|```|!\[|[-*+] |\d+[.)] )',lines[i].strip()):para.append(lines[i].strip());i+=1
  blocks.append({'type':'paragraph','text':'\n'.join(para)})
 if not title:raise ValueError('缺少标题：请补 Markdown 一级标题，或使用 article.json')
 return {'title':title,'blocks':blocks}

def check_doc(doc):
 if not isinstance(doc,dict) or not isinstance(doc.get('title'),str) or not doc['title'].strip():raise ValueError('缺少非空文章标题')
 if not isinstance(doc.get('blocks'),list) or not doc['blocks']:raise ValueError('缺少正文 blocks')
 types={'paragraph','heading','chapter','quote','note','list','steps','metrics','image','code','table','divider'}
 for b in doc['blocks']:
  if not isinstance(b,dict) or b.get('type') not in types:raise ValueError('不支持的内容块类型：'+str(b))
  typ=b['type']
  if typ in {'paragraph','heading','chapter','quote','code'} and not isinstance(b.get('text'),str):raise ValueError('内容块缺少 text')
  if typ in {'list','steps','metrics','note'} and (not isinstance(b.get('items'),list) or not b['items']):raise ValueError('列表、注释、指标需要非空 items')
  if typ=='metrics' and any(not all(isinstance(x.get(k),str) for k in ['value','label','detail']) for x in b['items']):raise ValueError('指标需要 value、label、detail 字符串')
  if typ=='table' and (not b.get('headers') or not isinstance(b.get('rows'),list) or any(len(x)!=len(b['headers']) for x in b['rows'])):raise ValueError('表格列数不一致')
  if typ=='image' and not isinstance(b.get('src'),str):raise ValueError('图片缺少 src')
 for b in doc['blocks']:
  for url in re.findall(r'\]\(([^)]+)\)',json.dumps(b,ensure_ascii=False)) + ([b['src']] if b['type']=='image' else []):
   if urlparse(url).scheme.lower() not in {'','http','https','file'}:raise ValueError('不支持的链接协议')

def cover(m,t,d):
 title=m.plain(d['title'],'font-size:24px;line-height:1.55;font-weight:'+('800' if t['number'] in [2,4,6] else '400')+';overflow-wrap:anywhere;')
 meta=m.plain(' / '.join(str(d[k]) for k in ['author','date'] if d.get(k)),'font-size:11px;line-height:1.8;margin-top:25px;')
 summary=m.plain(d.get('subtitle',''),'font-size:13px;line-height:1.9;margin-top:22px;') if d.get('subtitle') else ''
 label=m.plain(d.get('series',''),'font-size:10px;line-height:1.8;margin-bottom:28px;') if d.get('series') else ''
 inner=label+title+summary+meta;n=t['number']
 if n==1:return m.sec(inner,'padding:35px 23px;color:white;background-color:#205BA7;background-image:'+m.GRAD+';border-bottom:1px solid '+m.LINE+';')
 if n==2:return m.sec(inner+m.sec(m.star(True,42),'margin-top:25px;'),'margin:12px;padding:29px 22px;background:#080808;color:white;border-radius:24px;border-bottom:12px solid '+m.BLUE+';')
 if n==3:return m.sec(inner,'padding:36px 24px;color:#FFFFFF;background:'+m.BLUE+';border-right:20px solid '+m.AQUA+';')
 if n==4:return m.sec(m.tabs(d.get('series','ARTICLE'),'NOTES')+m.sec(inner,'padding:27px 18px;background:white;border:9px solid '+m.GREEN+';border-radius:26px;'),'padding:30px 12px;'+m.GRID)
 if n==5:return m.sec(inner+m.sec(m.star(True,42),'margin-top:27px;'),'padding:35px 24px;color:white;background:#080808;border-bottom:5px solid #C3FF32;')
 if n==6:return m.sec(m.star(True,55)+m.sec(inner,'margin-top:24px;'),'margin:12px;padding:27px 20px;background:'+m.NAVY+';color:'+m.GOLD+';border-right:13px solid '+m.RED+';border-bottom:13px solid '+m.GOLD+';')
 if n==7:return m.sec(m.plain(d.get('kicker',''),'font-size:24px;color:'+m.MUTED+';line-height:1.2;margin-bottom:20px;')+inner,'padding:34px 24px;color:'+m.INK+';border-top:1px solid '+m.LINE+';border-bottom:1px solid '+m.LINE+';border-right:20px solid #F0F0ED;')
 return m.sec(m.brand()+m.sec(inner,'margin-top:43px;'),'padding:25px 24px 34px;color:'+m.BLUE+';'+m.LIGHTWAVE)

def article(d,t,source_dir,out,no_images=False):
 m=theme_module(t);m.BRAND_NAME=d.get('series','');content=cover(m,t,d);chapter=0;nav=[];omitted=[]
 def invoke(fn,values,*args):m.blocks=dict(enumerate(values));return getattr(m,fn)(0,*args)
 for b in d['blocks']:
  typ=b['type'];txt=b.get('text','')
  if typ=='paragraph':content+=invoke('textp',[txt])
  elif typ=='heading':content+=invoke('subheading',[txt])
  elif typ=='chapter':
   chapter+=1;nav.append((f'chapter{chapter}',txt));label=b.get('label','SECTION');subtitle=label+(' · '+b['subtitle'] if b.get('subtitle') else '')
   content+=invoke('chapter',[str(chapter).zfill(2),'PART',txt,subtitle],chapter)
  elif typ=='quote':m.EMPHASIS=b.get('emphasis',False);content+=invoke('quote',[txt,b.get('attribution','')])
  elif typ=='note':content+=invoke('note',[b.get('title','提示')]+b['items'],len(b['items'])+1)
  elif typ=='steps':content+=m.flow(b['items'])
  elif typ=='list':
   for num,item in enumerate(b['items'],1):content+=invoke('textp',[f'{num:02}  '+item])
  elif typ=='metrics':
   values=[b.get('title','数据'),'']
   for item in b['items']:values +=[item['value'],item['label'],item['detail']]
   content+=invoke('rows',values,2,len(b['items']),3,True)
  elif typ=='divider':content+=m.sec('','border-top:1px solid '+m.LINE+';margin:30px 22px;')
  elif typ=='image':
   if no_images:omitted.append(b['src']);continue
   src=b['src'];parsed=urlparse(src)
   if parsed.scheme not in ['https','http']:
    from urllib.parse import unquote
    p=Path(unquote(parsed.path)) if parsed.scheme=='file' else Path(src);p=p if p.is_absolute() else source_dir/p
    if not p.is_file():raise ValueError('图片文件不存在：'+src)
    asset=out/'images';asset.mkdir(exist_ok=True);dest=asset/(str(len(list(asset.iterdir())))+'-'+p.name);shutil.copy2(p,dest);src='images/'+dest.name
   content+=m.sec('<span leaf=""><img src="'+html.escape(src,quote=True)+'" alt="'+html.escape(b.get('alt',''),quote=True)+'" style="max-width:100%;height:auto;display:block;margin:0 auto;"></span>','margin:20px 22px;')
   if b.get('caption'):content+=invoke('textp',[b['caption']],True)
  elif typ=='code':
   lines=''.join(m.plain(x or ' ','font-family:monospace;font-size:13px;line-height:1.75;white-space:pre-wrap;overflow-wrap:anywhere;') for x in txt.split('\n'))
   content+=m.sec(lines,'margin:24px 22px;padding:18px;color:#F5F5F0;background:#222526;border-radius:6px;')
  elif typ=='table':
   # Semantic table serialized into labeled rows on narrow WeChat viewports; all values preserved.
   for row in b['rows']:content+=invoke('note',[b.get('title','数据')]+[h+'：'+str(v) for h,v in zip(b['headers'],row)],len(row)+1)
 clean=m.sec(content,m.WRAPPER)
 return clean,nav,omitted

def preview(clean,nav,title):
 data=json.dumps({'clean':clean,'nav':nav,'title':title},ensure_ascii=False).replace('</','<\\/')
 template=(ROOT/'assets/preview.html').read_text();return template.replace('__DATA__',data)

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);p.add_argument('--theme',required=True,help='1–8、中文名、主题 ID 或 all');p.add_argument('--out',type=Path,required=True);p.add_argument('--no-images',action='store_true');p.add_argument('--edition',choices=['stable','pilot','components'],default='components');a=p.parse_args()
 if a.out.exists():raise ValueError('输出目录已存在，请使用新目录，避免覆盖确认版')
 raw=a.input.read_text();doc=json.loads(raw) if a.input.suffix=='.json' else markdown(raw)
 if a.edition!='stable':
  import components_engine
  components_engine.validate(doc,check_doc)
 else:check_doc(doc)
 selected=([t for t in THEMES if t['number'] in [1,4]] if a.edition=='pilot' else THEMES) if a.theme=='all' else [t for t in THEMES if a.theme in [str(t['number']),t['name'],t['id']]]
 if a.edition=='pilot' and any(t['number'] not in [1,4] for t in selected):raise ValueError('试点只支持蓝调网格和荧光便签')
 if not selected:raise ValueError('主题必须是 1–8、中文名、ID 或 all')
 a.out.mkdir(parents=True);(a.out/'article.json').write_text(json.dumps(doc,ensure_ascii=False,indent=2));gallery=[]
 for t in selected:
  clean,nav,omitted=(components_engine.article(doc,t,a.input.parent,a.out,a.no_images,article,theme_module) if a.edition!='stable' else article(doc,t,a.input.parent,a.out,a.no_images));path=a.out/(t['id']+'-正文.html');path.write_text(clean)
  from check_fragment import inspect_fragment
  check=inspect_fragment(clean,base_dir=a.out)
  if check['issues']:raise ValueError(json.dumps(check,ensure_ascii=False))
  filename=t['id']+'-预览.html';(a.out/filename).write_text(preview(clean,nav,doc['title']+' / '+t['name']))
  gallery.append({**t,'url':filename,'omittedImages':omitted,'clean':clean,'nav':nav})
 (a.out/'检查记录.json').write_text(json.dumps({'edition':a.edition,'themes':[{k:v for k,v in t.items() if k not in ['clean','nav']} for t in gallery],'static':'passed','wechatPaste':'未测试'},ensure_ascii=False,indent=2))
 data=json.dumps(gallery,ensure_ascii=False).replace('</','<\\/')
 (a.out/'排版总览.html').write_text((ROOT/'assets/gallery.html').read_text().replace('__DATA__',data))
 print(str((a.out/'排版总览.html').resolve()))
if __name__=='__main__':
 try:main()
 except (ValueError,KeyError,TypeError,OSError,json.JSONDecodeError) as e:print('排版未完成：'+str(e),file=sys.stderr);sys.exit(1)
