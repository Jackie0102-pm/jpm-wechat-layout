# -*- coding: utf-8 -*-
# SPDX-License-Identifier: AGPL-3.0-only
# JPM modified distribution, 2026-09-24. See package-root NOTICE.md and CHANGES.md.
"""Semantic blocks and rendering orchestration for the JPM theme library."""
import re,html,copy
from urllib.parse import urlparse
EXTRA={'intro','toc','timeline','compare','cards','conclusion','signature','placeholder'}
VARIANTS={'quote':{'regular','key','aside'},'note':{'info','action','warning'},'code':{'light','dark'}}

def validate(d,base_check):
 basic=copy.deepcopy(d);basic['blocks']=[b for b in d['blocks'] if b.get('type') not in EXTRA]
 if not basic['blocks']:basic['blocks']=[{'type':'paragraph','text':''}]
 base_check(basic)
 def string(v):
  if not isinstance(v,str):raise ValueError('组件字段须为字符串')
 def items(v):
  if not isinstance(v,list) or not v:raise ValueError('组件列表不能为空')
 for b in d['blocks']:
  typ=b['type']
  if typ in VARIANTS and b.get('variant',next(iter(VARIANTS[typ]))) not in VARIANTS[typ]:raise ValueError('未知组件变体：'+str(b.get('variant')))
  if typ in {'intro','conclusion','placeholder'}:string(b['text'])
  if typ=='signature':
   string(b['name']);string(b.get('bio',''));string(b.get('cta',''))
   if not b['name'].strip():raise ValueError('署名不能为空')
  if typ=='toc':items(b['items']);[string(x) for x in b['items']]
  if typ=='timeline':
   items(b['items'])
   for x in b['items']:string(x['label']);string(x['text'])
  if typ=='compare':
   items(b['items'])
   if len(b['items'])!=2:raise ValueError('前后对比须为两项')
   for x in b['items']:string(x['title']);string(x['text'])
  if typ=='cards':
   items(b['items'])
   for x in b['items']:string(x.get('label',''));string(x['title']);string(x['text'])
 if sum(b['type']=='signature' for b in d['blocks'])>1:raise ValueError('署名区只允许一处，请先合并')
 sig=[i for i,b in enumerate(d['blocks']) if b['type']=='signature']
 if sig and sig[0]!=len(d['blocks'])-1:raise ValueError('署名区只能在末尾')
 for k in ['lines']:
  if k in d.get('cover',{}):items(d['cover'][k]);[string(x) for x in d['cover'][k]]
 if d.get('cover',{}).get('lines'):
  title=''.join(d['cover']['lines'])
  if re.sub(r'\s+','',title)!=re.sub(r'\s+','',d['title']):raise ValueError('封面分行必须完整保留原标题')
  focus=d['cover'].get('focus','')
  if focus and focus not in d['cover']['lines']:raise ValueError('封面大词须为标题分行之一')
 # Check all new fields for links too, not only the old block types.
 def walk(x):
  if isinstance(x,str):
   for u in re.findall(r'\]\(([^)]+)\)',x):
    if urlparse(u).scheme.lower() not in {'','http','https','file'}:raise ValueError('不支持的链接协议')
  elif isinstance(x,list):
   for v in x:walk(v)
  elif isinstance(x,dict):
   for v in x.values():walk(v)
 walk(d)

class Components:
 def __init__(self,m,neon):
  self.m=m;self.neon=neon;self.ink=m.INK;self.accent=m.BLUE;self.line=m.LINE
 def box(self,c,s=''):return self.m.sec(c,s+'overflow-wrap:anywhere;')
 def p(self,t,s=''):return '<p style="margin:0;font-size:14px;line-height:1.9;overflow-wrap:anywhere;'+s+'">'+self.inline(t)+'</p>'
 def inline(self,t):
  parts=re.split(r'(\*\*.*?\*\*|==.*?==|\+\+.*?\+\+|~~.*?~~|`[^`]+`|\[[^\]]+\]\([^)]+\))',t);out=''
  for v in parts:
   style=None;body=v
   if v.startswith('**'):body=v[2:-2];style='font-weight:700;color:'+self.ink+';'
   elif v.startswith('++'):body=v[2:-2];style='border-bottom:2px solid '+('#80C587' if self.neon else '#9EB8DC')+';padding-bottom:2px;'
   elif v.startswith('=='):body=v[2:-2];style='background:'+('#E7FF6B' if self.neon else '#DCEAFB')+';color:'+self.ink+';padding:1px 3px;'
   elif v.startswith('~~'):body=v[2:-2];style='background:linear-gradient(transparent 58%,'+('#F6B7EA' if self.neon else '#C7DAF4')+' 58%);'
   elif v.startswith('`'):body=v[1:-1];style='font-family:monospace;font-size:13px;background:'+self.m.PALE+';'
   elif re.match(r'^\[.*\]\(',v):
    a=re.match(r'\[([^\]]+)\]\(([^)]+)\)',v);out+='<a style="color:'+self.accent+';text-decoration:underline;" href="'+html.escape(a[2],quote=True)+'">'+self.m.leaf(a[1])+'</a>';continue
   out+=('<span style="'+style+'">'+self.m.leaf(body)+'</span>') if style else self.m.leaf(v)
  return out
 def cover(self,d):
  c=d.get('cover',{});lines=c.get('lines',[d['title']]);focus=c.get('focus','');m=self.m
  title=''.join(self.p(x,'font-size:'+('56' if x==focus else '27')+'px;line-height:1.45;font-weight:'+('850' if self.neon else '300')+';'+('font-family:'+m.MONO+';' if self.neon and x==focus else '')+'margin:5px 0;') for x in lines)
  meta=' / '.join(d[k] for k in ['author','date'] if d.get(k));tag=c.get('label',d.get('series',''))
  strap=self.box(self.p(tag,'font-size:10px;flex:1;min-width:0;')+self.p(d.get('date',''),'font-size:10px;'),'display:flex;justify-content:space-between;padding:18px 20px;border-bottom:1px solid '+self.line+';')
  kicker=self.p(d.get('subtitle',''),'font-size:12px;margin-bottom:22px;') if d.get('subtitle') else ''
  foot=self.p(c.get('footer',''),'font-size:12px;flex:1;min-width:0;') if c.get('footer') else ''
  if self.neon:
   header=self.box(self.p(tag,'font-size:10px;')+self.p(d.get('date',''),'font-size:10px;'),'display:flex;justify-content:space-between;margin:0 10px 25px;')
   frame=self.box(kicker+title,'background:white;border:9px solid '+m.GREEN+';border-radius:26px;padding:24px 18px;')
   end=self.box(foot+self.m.star(True,44),'display:flex;align-items:center;gap:12px;background:'+m.LIME+';padding:20px 15px;border-radius:0 0 22px 22px;margin:16px 10px 0;')
   out=self.box(header+m.tabs(d.get('series','ARTICLE'),c.get('tab','NOTES'))+frame+end,'padding:26px 12px 24px;'+m.GRID)
  else:
   mesh='linear-gradient(90deg,transparent 24%,rgba(255,255,255,.15) 24.2%,transparent 24.4%,transparent 75%,rgba(255,255,255,.15) 75.2%,transparent 75.4%),'+m.GRAD
   out=self.box(strap+self.box(kicker+title,'padding:32px 20px 34px;')+self.box(self.box(foot,'flex:1;padding:18px 20px;min-width:0;')+self.p('↘','font-size:58px;line-height:1;width:80px;padding:12px;border-left:1px solid rgba(255,255,255,.25);'),'display:flex;border-top:1px solid rgba(255,255,255,.25);'),'color:white;background-color:'+m.BLUE+';background-image:'+mesh+';')
  if meta:out+=self.box(self.p(meta,'font-size:11px;color:'+self.accent+';'),'padding:20px 22px;border-bottom:1px solid '+self.line+';margin-bottom:24px;')
  return out
 def render(self,b):
  t=b['type'];m=self.m;title=b.get('title','');txt=b.get('text','');v=b.get('variant','regular');pad='margin:26px 22px;'
  if t=='paragraph':return self.p(txt,pad+'font-size:15px;line-height:1.95;')
  if t=='intro':
   return self.box(self.p(b.get('label','开篇'),'font-size:10px;margin-bottom:15px;')+self.p(txt,'font-size:19px;line-height:1.8;')+(self.p(b['attribution'],'font-size:11px;margin-top:18px;') if b.get('attribution') else ''),pad+'padding:24px 20px;'+('border:6px solid '+m.GREEN+';border-radius:24px;background:white;' if self.neon else 'border-top:1px solid '+m.BLUE+';border-bottom:1px solid '+m.BLUE+';'))
  if t=='toc':
   cells=''.join(self.box(self.p(str(i+1).zfill(2),'font-size:12px;width:35px;flex-shrink:0;')+self.p(x,'font-size:13px;flex:1;min-width:0;'),'display:flex;padding:13px 0;border-top:1px solid '+self.line+';') for i,x in enumerate(b['items']))
   return self.box(self.p(title or '这篇文章的看点','font-size:15px;font-weight:700;margin-bottom:18px;')+cells,pad+'padding:22px;'+('background:'+m.LIME+';border-radius:20px;' if self.neon else 'border:1px solid '+self.line+';'))
  if t=='quote':
   v=b.get('variant','key' if b.get('emphasis') else 'regular');attr=self.p(b['attribution'],'font-size:12px;margin-top:16px;') if b.get('attribution') else ''
   if v=='aside':return self.box(self.p(txt,'font-size:13px;')+attr,pad+'padding:6px 15px;border-left:2px solid '+self.line+';color:'+self.accent+';')
   inner=self.p(txt,'font-size:'+('22' if v=='key' else '17')+'px;font-weight:'+('700' if self.neon and v=='key' else '400')+';')+attr
   if self.neon:return self.box(m.punch(inner,m.PINK if v=='key' else m.LIME),pad)
   return self.box(inner,'margin:28px '+('0' if v=='key' else '22px')+';padding:26px 22px;background:'+(m.BLUE if v=='key' else m.PALE)+';color:'+('white' if v=='key' else m.INK)+';')
  if t=='note':
   v=b.get('variant','info');label={'info':'补充说明','action':'行动建议','warning':'风险提醒'}[v]
   body=self.p(title or label,'font-size:12px;font-weight:700;margin-bottom:13px;')+''.join(self.p(x,'margin-top:9px;font-size:14px;') for x in b['items'])
   if self.neon:
    bg={'info':m.PALE,'action':m.LIME,'warning':'#FAD0ED'}[v]
    return self.box(m.pill(label,v=='action')+self.box(body,'padding:20px;background:'+bg+';border-radius:0 20px 20px 20px;'),pad)
   return self.box(self.p(label,'font-size:10px;letter-spacing:1px;margin-bottom:12px;')+body,pad+'padding:18px;background:'+('#EEF2F8' if v=='warning' else m.PALE)+';border-left:'+('5' if v=='warning' else '2')+'px solid '+m.BLUE+';')
  if t=='list':
   return self.box(''.join(self.box(self.p(str(i+1).zfill(2) if b.get('ordered',False) else '•','width:30px;flex-shrink:0;font-size:13px;color:'+self.accent+';')+self.p(x,'flex:1;min-width:0;'),'display:flex;margin:10px 0;') for i,x in enumerate(b['items'])),pad)
  if t=='timeline':
   return self.box(''.join(self.box(self.p(x['label'],'font-size:11px;font-weight:700;margin-bottom:9px;')+self.p(x['text']),'border-left:2px solid '+(m.GREEN if self.neon else m.BLUE)+';padding:0 0 24px 18px;') for x in b['items']),pad)
  if t=='compare':
   cells=''
   for i,x in enumerate(b['items']):
    cells+=self.box(self.p(x['title'],'font-size:16px;font-weight:700;margin-bottom:14px;')+self.p(x['text'],'font-size:13px;'),'flex:1;min-width:0;padding:21px 14px;'+('background:'+(m.PINK if i==0 else m.LIME)+';border-radius:20px;' if self.neon else 'background:'+(m.PALE if i==0 else 'white')+';border:1px solid '+m.LINE+';'))
   return self.box((self.p(title,'font-size:16px;margin-bottom:16px;') if title else '')+self.box(cells,'display:flex;gap:'+('10' if self.neon else '0')+'px;'),pad)
  if t=='cards':
   values=[title,'']
   for x in b['items']:values += [x.get('label',''),x['title'],x['text']]
   m.blocks=dict(enumerate(values));return m.rows(0,2,len(b['items']),3,False)
  if t=='conclusion':
   return self.box(self.p(b.get('label','SUMMARY'),'font-size:10px;margin-bottom:24px;')+self.p(title or '下一步','font-size:26px;line-height:1.5;margin-bottom:20px;')+self.p(txt),'margin:42px 0 0;padding:30px 24px;'+('background:'+m.GREEN+';color:'+m.INK+';border-radius:25px 25px 0 0;' if self.neon else 'background:'+m.BLUE+';color:white;border-top:1px solid '+m.LINE+';'))
  if t=='signature':
   return self.box(self.p(b['name'],'font-size:14px;font-weight:700;')+(self.p(b['bio'],'font-size:12px;margin-top:10px;') if b.get('bio') else '')+(self.p(b['cta'],'font-size:12px;margin-top:20px;') if b.get('cta') else ''),'padding:26px 24px;border-top:1px solid '+m.LINE+';'+('background:'+m.LIME+';' if self.neon else 'background:'+m.PALE+';'))
  if t=='code':
   dark=b.get('variant','dark')=='dark';color='#F5F5EF' if dark else m.INK;bg='#222A26' if dark else m.PALE
   lines=''.join(m.plain(x or ' ','font:13px/1.7 monospace;white-space:pre-wrap;overflow-wrap:anywhere;') for x in txt.split('\n'))
   return self.box((m.plain(b['language'],'font:10px/1.8 monospace;margin-bottom:15px;') if b.get('language') else '')+lines,pad+'padding:20px;background:'+bg+';color:'+color+';border-radius:'+('15' if self.neon else '0')+'px;')
  if t=='placeholder':return self.box(self.p('◇','font-size:24px;')+self.p(txt,'font-size:12px;margin-top:12px;'),pad+'padding:28px 18px;text-align:center;background:'+m.PALE+';border:1px dashed '+m.LINE+';')
  return None

def article(d,t,source_dir,out,no_images,base_article,theme_module):
 m=theme_module(t);m.BRAND_NAME=d.get('series','')
 if t['id'] in ['blue-grid','neon-notes']:c=Components(m,t['id']=='neon-notes')
 else:
  from extended_components import ExtendedComponents
  c=ExtendedComponents(m,t['id'])
 body=c.cover(d);nav=[];omitted=[];n=0
 for b in d['blocks']:
  if b['type']=='chapter':
   n+=1;nav.append(('chapter'+str(n),b['text']));m.blocks={0:('∞' if b.get('ending') and b is [x for x in d['blocks'] if x['type']=='chapter'][-1] else str(n).zfill(2)),1:'PART',2:b['text'],3:b.get('label','SECTION')+(' · '+b['subtitle'] if b.get('subtitle') else '')};cycle=((n-1)%6)+1 if t['id']=='blue-olive' else n;body+=m.chapter(0,cycle).replace('<!-- chapter'+str(cycle)+' -->','<!-- chapter'+str(n)+' -->');continue
  custom=c.render(b)
  if custom is not None:body+=custom;continue
  # Reuse stable media, headings, steps and metric components without their cover.
  sub={'title':'_','series':d.get('series',''),'blocks':[b]};clean,_,gone=base_article(sub,t,source_dir,out,no_images)
  from render import cover
  cover_module=theme_module(t);cover_module.BRAND_NAME=d.get('series','');old=cover(cover_module,t,sub);start=clean.find(old);assert start>=0
  body+=clean[start+len(old):-len('</section>')];omitted+=gone
 return m.sec(body,m.WRAPPER),nav,omitted
