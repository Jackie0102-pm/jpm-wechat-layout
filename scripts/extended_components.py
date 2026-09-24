# -*- coding: utf-8 -*-
# SPDX-License-Identifier: AGPL-3.0-only
# JPM modified distribution, 2026-09-24. See package-root NOTICE.md and CHANGES.md.
"""Six additional theme families; shared semantic contract, distinct compositions."""
import re,html
from components_engine import Components

class ExtendedComponents(Components):
 def __init__(self,m,theme):
  super().__init__(m,False);self.theme=theme
  self.accent=getattr(m,'TEXTORANGE',m.BLUE)
 def inline(self,t):
  m=self.m;key=self.theme
  bg={'purple-future':'#E5DCF8','orange-aqua':'#D7E9EB','black-lime':'#DDFB83','retro-record':'#EDB234','gray-portfolio':'#E4E3E0','blue-olive':'#E1E2BB'}[key]
  fg='#15200F' if key=='black-lime' else m.INK
  parts=re.split(r'(\*\*.*?\*\*|==.*?==|\+\+.*?\+\+|~~.*?~~|`[^`]+`|\[[^\]]+\]\([^)]+\))',t);out=''
  for v in parts:
   style=None;body=v
   if v.startswith('**'):body=v[2:-2];style='font-weight:700;'
   elif v.startswith('++'):body=v[2:-2];style='border-bottom:2px solid '+(m.OLIVE if key=='blue-olive' else self.accent)+';padding-bottom:2px;'
   elif v.startswith('=='):body=v[2:-2];style='background:'+bg+';color:'+fg+';padding:1px 3px;'
   elif v.startswith('~~'):body=v[2:-2];style=('background:'+bg+';color:'+fg+';' if key=='black-lime' else 'background:linear-gradient(transparent 58%,'+bg+' 58%);')
   elif v.startswith('`'):body=v[1:-1];style='font-family:monospace;font-size:13px;background:'+bg+';color:'+fg+';'
   elif re.match(r'^\[.*\]\(',v):
    a=re.match(r'\[([^\]]+)\]\(([^)]+)\)',v);out+='<a href="'+html.escape(a[2],quote=True)+'" style="color:inherit;text-decoration:underline;">'+m.leaf(a[1])+'</a>';continue
   out+=('<span style="'+style+'">'+m.leaf(body)+'</span>') if style else m.leaf(v)
  return out
 def pill(self,text,dark=False):
  m=self.m
  if self.theme=='black-lime':return self.box(self.p(text,'font-size:10px;color:#151B11;'),'display:inline-block;padding:6px 12px;border-radius:30px;background-image:'+m.GRAD+';')
  if self.theme=='purple-future':return self.box(self.p(text,'font-size:10px;color:white;'),'display:inline-block;padding:6px 12px;border-radius:30px;background:'+m.BLUE+';')
  return self.box(self.p(text,'font-size:10px;'),'display:inline-block;padding:4px 9px;border:1px solid '+m.LINE+';')
 def cover(self,d):
  m=self.m;k=self.theme;c=d.get('cover',{});lines=c.get('lines',[d['title']]);focus=c.get('focus','');label=c.get('label',d.get('series',''))
  meta=' / '.join(d[x] for x in ['author','date'] if d.get(x));title=''
  for i,x in enumerate(lines):
   size=('54' if x==focus else '27') if k not in ['gray-portfolio','blue-olive'] else ('34' if x==focus else '27')
   font=getattr(m,'ROUND',m.FONT) if k=='retro-record' else getattr(m,'MONO',m.FONT) if k=='orange-aqua' and x==focus else m.FONT
   color=('color:'+m.MUTED+';' if k=='gray-portfolio' and i>0 else '')
   title+=self.p(x,'font-family:'+font+';font-size:'+size+'px;line-height:1.45;font-weight:'+('850' if k in ['purple-future','retro-record'] else '350')+';margin:6px 0;'+color)
  subtitle=self.p(d.get('subtitle',''),'font-size:12px;line-height:1.9;') if d.get('subtitle') else ''
  footer=self.p(c.get('footer',''),'font-size:11px;line-height:1.8;flex:1;min-width:0;') if c.get('footer') else ''
  if k=='purple-future':
   head=self.box(self.pill(d.get('series',''))+self.p(label,'font-size:9px;'),'display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:20px;')
   hero=self.box(self.p(label,'font-size:10px;')+self.box(subtitle,'margin:26px 0 20px;')+title+self.box(footer,'margin-top:28px;'),'padding:28px 22px 38px;background:#080808;color:white;border-radius:24px;')
   badge=self.box(m.star(True,58),'width:66px;padding:4px;border-radius:50%;background:white;margin:-28px 17px 18px auto;')
   return self.box(head+hero+badge+self.p(meta,'font-size:11px;color:#635B70;margin:0 10px 30px;'),'padding:20px 12px 0;')
  if k=='orange-aqua':
   head=self.box(self.p(d.get('series',''),'font-size:11px;')+self.p(d.get('date',''),'font-size:10px;'),'display:flex;justify-content:space-between;color:#183F47;')
   hero=head+self.box(subtitle+title,'margin-top:68px;')+self.box(footer+self.p('✦ ─ ✦','font-size:18px;'),'display:flex;align-items:center;gap:12px;margin-top:30px;padding-top:18px;border-top:1px solid rgba(255,255,255,.5);')
   return self.box(hero,'padding:22px 20px;color:white;background-color:'+m.BLUE+';background-image:'+m.GRAD+';')+self.box(self.p(meta,'font-size:11px;color:#66564D;'),'padding:22px;')
  if k=='black-lime':
   head=self.box(self.box(self.p(d.get('series',''),'font-size:10px;color:#10120C;'),'background:white;border-radius:30px;padding:6px 12px;')+m.star(True,36),'display:flex;justify-content:space-between;align-items:center;')
   return self.box(head+self.box(title,'margin:43px 0 35px;color:white;')+self.pill(label)+self.box(subtitle+footer,'margin-top:26px;color:#D1D8C7;')+self.p(meta,'font-size:11px;color:#AAB19F;margin-top:27px;'),'padding:24px 22px 30px;border-bottom:1px solid '+m.LINE+';margin-bottom:30px;')
  if k=='retro-record':
   head=self.box(self.p(label,'font-size:10px;color:'+m.CREAM+';flex:1;min-width:0;')+m.star(True,60),'display:flex;justify-content:space-between;align-items:center;margin-bottom:26px;gap:10px;')
   hero=self.box(head+title+self.box(subtitle,'margin-top:28px;color:'+m.CREAM+';'),'padding:25px 19px 32px;background:'+m.NAVY+';color:'+m.GOLD+';border-right:13px solid '+m.RED+';')
   strip=self.box(footer,'padding:15px 19px;background:'+m.GOLD+';color:'+m.NAVY+';')
   return self.box(hero+strip,'margin:12px 12px 22px;border:3px solid '+m.NAVY+';box-shadow:4px 4px 0 #C6A267;')+self.box(self.p(meta,'font-size:11px;'),'padding:0 22px 28px;')
  if k=='gray-portfolio':
   strap=self.box(self.p(label,'font-size:10px;')+self.p(d.get('series',''),'font-size:10px;color:'+m.MUTED+';'),'padding:24px 22px;border-bottom:1px solid '+m.LINE+';')
   rail=self.box(self.p('+','font-size:20px;')+self.p('↘','font-size:22px;margin-top:170px;'),'width:39px;flex-shrink:0;padding:25px 8px;border-left:1px solid '+m.LINE+';'+m.GRID)
   hero=self.box(self.box(title,'padding:35px 22px;flex:1;min-width:0;')+rail,'display:flex;border-bottom:1px solid '+m.LINE+';')
   return strap+hero+self.box(self.pill(d.get('author',''))+self.pill(d.get('date','')),'display:flex;justify-content:space-between;padding:17px 22px;border-bottom:1px solid '+m.LINE+';')+self.box(subtitle+footer,'padding:26px 24px;')
  head=self.box(m.brand()+self.p(d.get('date',''),'font-size:10px;'),'display:flex;justify-content:space-between;align-items:center;')
  return self.box(head+self.p(label,'font-size:22px;line-height:1.15;margin-top:42px;')+self.box(title,'margin-top:35px;')+self.box(subtitle+footer,'margin-top:38px;'),'padding:23px 24px 28px;color:'+m.BLUE+';'+m.LIGHTWAVE)+self.box(self.p(meta,'font-size:11px;color:'+m.MUTED+';'),'padding:22px 24px;')
 def panel(self,body,role='regular'):
  m=self.m;k=self.theme
  if k=='purple-future':
   return self.box(body,'margin:28px 12px;padding:25px 22px;border-radius:22px;'+('background:'+m.BLUE+';color:white;' if role in ['key','action'] else 'background:#080808;color:white;' if role=='warning' else 'background:'+m.PALE+';color:'+m.INK+';'))
  if k=='orange-aqua':
   bg=m.AQUA if role in ['key','action'] else '#FAF8F4';fg='#173F48' if role in ['key','action'] else m.TEXTORANGE
   return self.box(body,'margin:30px '+('22px 30px 0' if role=='warning' else '0 30px 22px')+';padding:26px 22px;background:'+bg+';color:'+fg+';border-top:1px solid '+m.LINE+';border-bottom:1px solid '+m.LINE+';'+('border-left:7px solid '+m.BLUE+';' if role=='warning' else ''))
  if k=='black-lime':
   return self.box(body,'margin:28px 12px;padding:27px 22px;border-radius:22px;'+('background-image:'+m.GRAD+';color:#10120C;' if role in ['key','action'] else 'background:#F3F4EF;color:#10120C;' if role=='warning' else 'border:1px solid '+m.LINE+';color:#D7D8D3;'))
  if k=='retro-record':
   dark=role=='key';return self.box(body,'margin:30px 17px 32px;padding:25px 20px;border:2px solid '+m.NAVY+';background:'+(m.NAVY if dark else m.PALE)+';color:'+(m.GOLD if dark else m.NAVY)+';box-shadow:5px 5px 0 '+(m.RED if role in ['key','warning'] else m.GOLD)+';')
  if k=='gray-portfolio':
   return self.box(body,'margin:30px 24px;padding:25px '+('18px' if role=='warning' else '0')+';border-top:1px solid '+m.LINE+';border-bottom:1px solid '+m.LINE+';'+('background:'+m.PALE+';' if role=='warning' else ''))
  dark=role=='key';return self.box(body,'margin:32px 0;padding:28px 24px;color:'+('#F0F0E9' if dark else m.BLUE)+';'+(m.DARKWAVE if dark else m.LIGHTWAVE)+('border-left:5px solid '+m.OLIVE+';' if role=='warning' else ''))
 def render(self,b):
  k=self.theme;m=self.m;t=b['type'];txt=b.get('text','');title=b.get('title','')
  if t=='paragraph':return self.p(txt,'margin:0 24px 26px;font-size:15px;line-height:1.95;'+('font-family:'+m.SERIF+';' if k=='retro-record' else ''))
  if t=='intro':
   inner=self.p(b.get('label','开篇'),'font-size:10px;margin-bottom:20px;')+self.p(txt,'font-size:19px;')+(self.p(b['attribution'],'font-size:11px;margin-top:18px;') if b.get('attribution') else '')
   return self.panel(inner,'regular')
  if t=='quote':
   v=b.get('variant','key' if b.get('emphasis') else 'regular');attr=self.p(b['attribution'],'font-size:12px;margin-top:18px;') if b.get('attribution') else ''
   if v=='aside':return self.box(self.p(txt,'font-size:13px;')+attr,'margin:24px;padding:5px 15px;border-left:2px solid '+m.LINE+';')
   deco='“' if k in ['gray-portfolio','retro-record'] else '↗' if k=='orange-aqua' else '✳' if k in ['purple-future','blue-olive'] else '→'
   content=self.p(deco,'font-size:26px;line-height:1;margin-bottom:20px;')+self.p(txt,'font-size:'+('22' if v=='key' else '17')+'px;'+('font-family:'+m.ROUND+';font-weight:750;' if k=='retro-record' else 'font-weight:700;' if k=='purple-future' else ''))+attr
   return self.panel(content,v)
  if t=='note':
   v=b.get('variant','info');label={'info':'补充说明','action':'行动建议','warning':'风险提醒'}[v]
   inner=self.p(label,'font-size:10px;letter-spacing:1px;margin-bottom:16px;')+self.p(title or label,'font-size:15px;font-weight:700;margin-bottom:12px;')+''.join(self.p(x,'margin-top:9px;') for x in b['items'])
   return self.panel(inner,v)
  if t=='toc':
   if k in ['gray-portfolio','orange-aqua']:
    cells=''.join(self.box(self.p('('+str(i+1).zfill(2)+')','width:45px;font-size:12px;flex-shrink:0;')+self.p(x,'flex:1;min-width:0;font-size:13px;')+self.p('+','padding-left:8px;'),'display:flex;border-top:1px solid '+m.LINE+';padding:14px 0;') for i,x in enumerate(b['items']))
    return self.box(self.p(title or '本文看点','font-size:21px;line-height:1.3;margin-bottom:26px;')+cells,'margin:24px;padding-bottom:24px;border-bottom:1px solid '+m.LINE+';color:'+self.accent+';')
   cells=''.join(self.box(self.p(str(i+1).zfill(2),'font-size:12px;margin-bottom:10px;')+self.p(x,'font-size:13px;'),'padding:17px 0;border-top:1px solid '+m.LINE+';') for i,x in enumerate(b['items']))
   return self.panel(self.p(title or '本文看点','font-size:17px;margin-bottom:20px;')+cells,'key' if k=='blue-olive' else 'regular')
  if t=='timeline':
   content=''
   for i,x in enumerate(b['items']):
    text=self.p(x['label'],'font-size:12px;font-weight:700;margin-bottom:12px;')+self.p(x['text'],'font-size:14px;')
    if k=='purple-future':text=self.pill(str(i+1).zfill(2))+self.box(text,'margin-top:13px;');style='padding:20px;background:'+m.PALE+';border-radius:18px;margin-bottom:10px;'
    elif k=='black-lime':style='padding:22px 0;border-top:1px solid '+m.LINE+';'
    elif k=='retro-record':style='padding:20px;border:2px solid '+m.NAVY+';border-left:12px solid '+(m.RED if i%2 else m.GOLD)+';margin-bottom:10px;'
    elif k=='blue-olive':style='padding:20px 18px 26px 0;border-right:2px solid '+m.OLIVE+';text-align:right;'
    else:style='padding:0 0 24px 18px;border-left:1px solid '+self.accent+';'
    content+=self.box(text,style)
   return self.box(content,'margin:30px 24px;')
  if t=='compare':
   cells=''
   for i,x in enumerate(b['items']):
    inner=self.p(x['title'],'font-size:17px;font-weight:600;margin-bottom:16px;')+self.p(x['text'],'font-size:13px;')
    if k=='purple-future':style='background:'+('#080808' if i==0 else m.BLUE)+';color:white;border-radius:20px;'
    elif k=='black-lime':style='border:1px solid '+m.LINE+';border-radius:20px;'+('background-image:'+m.GRAD+';color:#10120C;' if i else 'color:#F3F4EF;')
    elif k=='orange-aqua':style='background:'+(m.AQUA if i else '#FFEAE0')+';color:#173F48;border-top:2px solid '+m.BLUE+';'
    elif k=='retro-record':style='background:'+(m.GOLD if i else m.NAVY)+';color:'+(m.NAVY if i else m.GOLD)+';border:2px solid '+m.NAVY+';'
    elif k=='gray-portfolio':style='border:1px solid '+m.LINE+';background:'+(m.PALE if i else 'white')+';'
    else:style=(m.LIGHTWAVE if i else m.DARKWAVE)+'color:'+(m.BLUE if i else '#EFEFE8')+';'
    cells+=self.box(inner,'flex:1;min-width:0;padding:22px 14px;'+style)
   return self.box((self.p(title,'font-size:17px;margin-bottom:18px;') if title else '')+self.box(cells,'display:flex;gap:'+('0' if k=='gray-portfolio' else '8')+'px;'),'margin:30px 22px;')
  if t=='conclusion':
   return self.panel(self.p(b.get('label','SUMMARY'),'font-size:10px;margin-bottom:25px;')+self.p(title or '下一步','font-size:28px;line-height:1.45;margin-bottom:22px;')+self.p(txt),'key')
  if t=='signature':
   from signature import signature
   return signature(self,b)
  if t=='code' and k=='black-lime':
   dark=b.get('variant','dark')=='dark';body=''.join(m.plain(x or ' ','font:13px/1.7 monospace;white-space:pre-wrap;overflow-wrap:anywhere;') for x in txt.split('\n'))
   return self.box((m.plain(b['language'],'font:10px/1.8 monospace;margin-bottom:15px;') if b.get('language') else '')+body,'margin:25px 22px;padding:20px;border:1px solid '+m.LINE+';border-radius:17px;background:'+('#171D12' if dark else '#F1F4EA')+';color:'+('#ECF0E5' if dark else '#18220D')+';')
  return super().render(b)
