# -*- coding: utf-8 -*-
# SPDX-License-Identifier: AGPL-3.0-only
# JPM modified distribution, 2026-09-24. See package-root NOTICE.md and CHANGES.md.
# Reusable visual components from user-approved local layouts.
import re,html
blocks={}
EMPHASIS=False
BRAND_NAME=""
def norm(t):return str(t)
def take(i):return blocks[i]
BLUE='#5120CC'

LINE='#DED9E8'

PALE='#F3EFFC'

INK='#302B37'

FONT="-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif"

GRAD='linear-gradient(125deg,#191E35 0%,#224475 35%,#637FC1 70%,#C5B4D3 100%)'

def star(purple=True,size=52):
 bg=BLUE if purple else '#090909'
 return sec(sec(plain('✳','font-family:Arial,sans-serif;font-size:'+str(round(size*.58))+'px;line-height:'+str(size-12)+'px;color:white;text-align:center;'),'border:1px solid #FFFFFF;border-radius:50%;height:'+str(size-10)+'px;'),'width:'+str(size)+'px;height:'+str(size)+'px;flex-shrink:0;padding:4px;border-radius:50%;background:'+bg+';')

def pill(t,dark=False):
 return sec(plain(t,'font-size:10px;line-height:1.5;font-weight:650;color:white;text-align:center;'),'display:inline-block;background:'+('#090909' if dark else BLUE)+';border-radius:30px;padding:7px 13px;')

def leaf(t):return '<span leaf="">'+html.escape(norm(t),quote=False)+'</span>'

def sec(c,s=''):return '<section style="box-sizing:border-box;'+s+'">'+c+'</section>'

def plain(t,s=''):return '<p style="margin:0;'+s+'">'+leaf(t)+'</p>'

def inline(t):
 parts=re.split(r'(\*\*.*?\*\*|`[^`]+`|\[[^\]]+\]\([^)]+\))',t)
 out=''
 for v in parts:
  if v.startswith('**'):out+='<span style="color:'+BLUE+';border-bottom:1px solid #AD91EB;padding-bottom:2px;">'+leaf(v[2:-2])+'</span>'
  elif v.startswith('`'):out+='<span style="font-family:Consolas,monospace;font-size:13px;background:'+PALE+';color:'+BLUE+';padding:2px 3px;overflow-wrap:anywhere;">'+leaf(v[1:-1])+'</span>'
  elif re.match(r'^\[.*\]\(',v):
   m=re.match(r'\[([^\]]+)\]\(([^)]+)\)',v);out+='<a href="'+html.escape(m[2],quote=True)+'" style="color:'+BLUE+';text-decoration:underline;text-underline-offset:3px;overflow-wrap:anywhere;">'+leaf(m[1])+'</a>'
  else:out+=leaf(v)
 return out

def textp(i,small=False):
 return '<p style="margin:0 22px 23px;font-size:'+('13' if small else '15')+'px;line-height:1.95;letter-spacing:.1px;color:'+INK+';overflow-wrap:anywhere;">'+inline(take(i))+'</p>'

def tag(t,white=False):return plain(t,'font-size:10px;line-height:1.7;letter-spacing:1.2px;color:'+('#EEEEEE' if white else '#5B5568')+';')

def subheading(i):
 t=take(i)
 return '<h3 style="margin:36px 22px 17px;font-size:19px;font-weight:750;line-height:1.55;color:#090909;overflow-wrap:anywhere;">'+leaf(t)+'</h3>'

def chapter(i,n):
 number=take(i);take(i+1);title=take(i+2);subtitle=take(i+3)
 top=sec(pill('PART '+number)+sec(plain(number,'font-size:12px;line-height:30px;text-align:center;'),'width:32px;height:32px;border:1px solid #151515;border-radius:11px;'),'display:flex;align-items:center;justify-content:space-between;')
 content=sec(plain(title,'font-size:32px;line-height:1.3;font-weight:850;letter-spacing:-1px;color:#080808;')+plain(subtitle,'font-size:11px;line-height:1.8;color:#635B70;margin-top:13px;'),'flex:1;min-width:0;padding-right:12px;')
 return '<!-- chapter'+str(n)+' -->'+sec(top+sec(content+star(n%2==0,46),'display:flex;align-items:center;margin-top:26px;'),'margin:56px 22px 27px;padding-top:16px;')

def quote(i):
 dark=EMPHASIS;q=take(i);note=take(i+1)
 block=plain(q,'font-size:21px;line-height:1.65;font-weight:750;color:'+('white' if dark else '#0A0A0A')+';')+plain(note,'font-size:12px;line-height:1.9;color:'+('#E3DAF8' if dark else '#635B70')+';margin-top:18px;overflow-wrap:anywhere;')
 return sec(block,'margin:30px 12px;padding:26px 22px;background:'+(BLUE if dark else '#F2EFF8')+';border-radius:22px;')

def note(i,end):
 head=take(i);content=''.join('<p style="margin:12px 0 0;font-size:13px;line-height:1.9;overflow-wrap:anywhere;">'+inline(take(j))+'</p>' for j in range(i+1,end))
 return sec(pill(head,True)+content,'padding:20px;margin:0 22px 26px;background:#F3F1F7;border-radius:18px;')

def rows(titleidx,start,count,step=3,metric=False):
 title=take(titleidx);cells=[]
 for x in range(count):
  j=start+x*step;a,b,c=take(j),take(j+1),take(j+2)
  if metric:
   dark=x%3!=2;bg=(BLUE if x%3==1 else '#090909') if dark else '#F0EDF7';fg='#FFFFFF' if dark else '#090909';muted='#E9E3F5' if dark else '#655E74'
   cell=plain(a,'font-size:42px;line-height:1.1;font-weight:800;letter-spacing:-2px;color:'+fg+';')+plain(b,'font-size:14px;font-weight:700;line-height:1.6;color:'+fg+';margin-top:13px;overflow-wrap:anywhere;')+plain(c,'font-size:11px;line-height:1.8;color:'+muted+';margin-top:10px;overflow-wrap:anywhere;')
   cells.append(sec(sec(cell,'height:100%;padding:22px 14px;background:'+bg+';border-radius:18px;'),'width:50%;padding:4px;'))
  else:
   cell=sec(pill(a,x%2==0),'margin-bottom:12px;')+plain(b,'font-size:18px;font-weight:750;line-height:1.45;color:#090909;overflow-wrap:anywhere;')+plain(c,'font-size:12px;line-height:1.8;color:#585061;margin-top:10px;overflow-wrap:anywhere;')
   cells.append(sec(sec(cell,'height:100%;padding:18px 14px;border-radius:18px;background:#F3F1F7;'),'width:50%;padding:4px;'))
 return sec(plain(title,'font-size:18px;color:#090909;font-weight:750;margin:0 4px 14px;line-height:1.6;')+sec(''.join(cells),'display:flex;flex-wrap:wrap;'),'margin:26px 18px;')

WRAPPER='max-width:600px;margin:0 auto;background:white;font-family:' + FONT + ';color:' + INK + ';padding-top:6px;padding-bottom:1px;'

def flow(items):
 content=''
 for k,t in enumerate(items):
  number=str(k+1).zfill(2)
  dark=k in {0,len(items)-1};fg='white' if dark else '#2B2632';bg=('#090909' if k==0 else BLUE) if dark else '#F3F1F7'
  line=sec(plain(number,'font-size:27px;font-weight:800;line-height:1;color:'+('white' if dark else BLUE)+';')+plain('STEP','font-size:9px;letter-spacing:2px;line-height:1.5;color:'+('#E0D5F5' if dark else '#7A7285')+';'),'display:flex;justify-content:space-between;align-items:center;margin-bottom:18px;')
  content+=sec(line+plain(t,'font-size:14px;line-height:1.95;color:'+fg+';overflow-wrap:anywhere;'),'padding:23px 20px;margin-bottom:12px;border-radius:21px;background:'+bg+';')
 return sec(content,'margin:26px 22px;')
