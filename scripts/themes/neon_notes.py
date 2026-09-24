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
BLUE='#236336'

LINE='#DCE8CC'

PALE='#EDF6E6'

INK='#123B20'

GREEN='#2DCC59'

LIME='#E7FF6B'

PINK='#F58AE3'

CREAM='#F8FAED'

MONO="'Menlo','Consolas',monospace"

GRID='background-color:#F8FAED;background-image:linear-gradient(#E9EED5 1px,transparent 1px),linear-gradient(90deg,#E9EED5 1px,transparent 1px);background-size:24px 24px;'

FONT="-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif"

GRAD='linear-gradient(125deg,#191E35 0%,#224475 35%,#637FC1 70%,#C5B4D3 100%)'

def star(purple=True,size=52):
 return sec(plain('›','font-family:Arial,sans-serif;font-size:'+str(size-9)+'px;line-height:'+str(size-2)+'px;font-weight:300;color:'+INK+';text-align:center;'),'width:'+str(size)+'px;height:'+str(size)+'px;flex-shrink:0;border-radius:50%;background:'+GREEN+';')

def pill(t,dark=False):
 return sec(plain(t,'font-family:'+MONO+';font-size:10px;line-height:1.7;color:'+INK+';'),'display:inline-block;padding:8px 11px 10px;border-radius:15px 15px 0 0;background:'+(LIME if dark else PINK)+';')

def dot():return sec('','width:11px;height:11px;flex-shrink:0;border-radius:50%;background:'+CREAM+';')

def punch(content,bg=PINK):
 holes=sec(''.join(dot() for _ in range(4)),'width:28px;flex-shrink:0;display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:20px 0;')
 return sec(holes+sec(content,'padding:22px 18px 24px 6px;flex:1;min-width:0;'),'display:flex;background:'+bg+';border-radius:0 20px 20px 0;')

def tabs(a,b):return sec(pill(a)+pill(b,True),'display:flex;align-items:flex-end;padding:0 10px;margin-bottom:-3px;')

def leaf(t):return '<span leaf="">'+html.escape(norm(t),quote=False)+'</span>'

def sec(c,s=''):return '<section style="box-sizing:border-box;'+s+'">'+c+'</section>'

def plain(t,s=''):return '<p style="margin:0;'+s+'">'+leaf(t)+'</p>'

def inline(t):
 parts=re.split(r'(\*\*.*?\*\*|`[^`]+`|\[[^\]]+\]\([^)]+\))',t);out=''
 for v in parts:
  if v.startswith('**'):out+='<span style="color:'+INK+';font-weight:600;background:linear-gradient(transparent 62%,#E7FF6B 62%);padding-bottom:1px;">'+leaf(v[2:-2])+'</span>'
  elif v.startswith('`'):out+='<span style="font-family:Consolas,monospace;font-size:13px;background:#E7F5DD;color:'+INK+';padding:2px 3px;overflow-wrap:anywhere;">'+leaf(v[1:-1])+'</span>'
  elif re.match(r'^\[.*\]\(',v):
   m=re.match(r'\[([^\]]+)\]\(([^)]+)\)',v);out+='<a href="'+html.escape(m[2],quote=True)+'" style="color:#24633A;text-decoration:underline;text-underline-offset:3px;overflow-wrap:anywhere;">'+leaf(m[1])+'</a>'
  else:out+=leaf(v)
 return out

def textp(i,small=False):
 return '<p style="margin:0 22px 23px;font-size:'+('13' if small else '15')+'px;line-height:1.95;letter-spacing:.1px;color:'+INK+';overflow-wrap:anywhere;">'+inline(take(i))+'</p>'

def tag(t,white=False):return plain(t,'font-family:'+MONO+';font-size:10px;line-height:1.7;letter-spacing:.3px;color:'+INK+';')

def subheading(i):
 t=take(i)
 return '<h3 style="margin:35px 22px 17px;font-size:19px;font-weight:800;line-height:1.6;color:'+INK+';overflow-wrap:anywhere;">'+'<span style="border-bottom:5px solid '+LIME+';">'+leaf(t)+'</span></h3>'

def chapter(i,n):
 number=take(i);take(i+1);title=take(i+2);subtitle=take(i+3)
 inner=sec(plain(title,'font-size:28px;line-height:1.35;font-weight:850;letter-spacing:-.8px;color:'+INK+';')+plain(subtitle,'font-size:11px;line-height:1.9;color:#436B4E;margin-top:16px;'),'flex:1;min-width:0;padding-right:10px;')
 inner=sec(inner+plain(number,'font-family:'+MONO+';font-size:30px;line-height:1.2;font-weight:700;color:'+INK+';'),'display:flex;align-items:flex-start;')
 frame=sec(inner,'border:9px solid '+GREEN+';border-radius:25px;padding:22px 15px;background:white;')
 return '<!-- chapter'+str(n)+' -->'+sec(tabs('PART '+number,subtitle.split(' · ')[0])+frame,'padding:28px 12px;margin:40px 0 26px;'+GRID)

def quote(i):
 q=take(i);note=take(i+1)
 content=plain(q,'font-size:22px;line-height:1.65;font-weight:750;color:'+INK+';')+plain(note,'font-size:12px;line-height:1.9;color:#274E33;margin-top:18px;overflow-wrap:anywhere;')
 return sec(punch(content,PINK if EMPHASIS else LIME),'margin:28px 12px;')

def note(i,end):
 head=take(i);content=''.join('<p style="margin:12px 0 0;font-size:13px;line-height:1.9;overflow-wrap:anywhere;">'+inline(take(j))+'</p>' for j in range(i+1,end))
 return sec(sec(tag(head),'display:inline-block;padding:4px 9px;background:'+PINK+';border-radius:8px;margin-bottom:5px;')+content,'padding:19px;margin:0 22px 25px;background:#EDF6E6;border-radius:18px;')

def rows(titleidx,start,count,step=3,metric=False):
 title=take(titleidx);cells=[]
 for x in range(count):
  j=start+x*step;a,b,c=take(j),take(j+1),take(j+2)
  if metric:
   cell=plain(a,'font-family:'+MONO+';font-size:40px;line-height:1.1;font-weight:750;letter-spacing:-2px;color:'+INK+';')+plain(b,'font-size:14px;font-weight:700;line-height:1.6;color:'+INK+';margin-top:13px;overflow-wrap:anywhere;')+plain(c,'font-size:11px;line-height:1.9;color:#2D5136;margin-top:10px;overflow-wrap:anywhere;')
   cells.append(sec(sec(cell,'height:100%;padding:23px 14px;border-radius:21px;background:'+([LIME,GREEN,PINK][x%3])+';'),'width:50%;padding:5px;'))
  else:
   label=sec(plain(a,'font-family:'+MONO+';font-size:11px;line-height:1.6;color:'+INK+';'),'display:inline-block;padding:5px 9px;background:'+(PINK if x%2==0 else LIME)+';border-radius:9px 9px 0 0;margin-left:8px;')
   cell=plain(b,'font-size:17px;font-weight:750;line-height:1.5;color:'+INK+';overflow-wrap:anywhere;')+plain(c,'font-size:12px;line-height:1.9;color:#43614A;margin-top:8px;overflow-wrap:anywhere;')
   cells.append(sec(label+sec(cell,'padding:17px;border:2px solid #C5E6B4;border-radius:15px;background:white;'),'width:100%;padding:8px 0;'))
 return sec(plain(title,'font-size:18px;color:'+INK+';font-weight:750;line-height:1.6;margin:0 5px 14px;')+sec(''.join(cells),'display:flex;flex-wrap:wrap;'),'margin:28px 17px;')

WRAPPER='max-width:600px;margin:0 auto;background:#F8FAED;font-family:' + FONT + ';color:' + INK + ';padding-top:6px;padding-bottom:1px;'

def flow(items):
 content=''
 for k,t in enumerate(items):
  number=str(k+1).zfill(2)
  top=sec(sec(plain(number,'font-family:'+MONO+';font-size:20px;font-weight:800;line-height:36px;text-align:center;color:'+INK+';'),'width:39px;height:36px;border-radius:10px;background:'+(PINK if k%2==0 else LIME)+';')+plain('STEP →','font-family:'+MONO+';font-size:10px;color:#41644A;line-height:1.6;'),'display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;')
  content+=sec(top+plain(t,'font-size:14px;line-height:1.95;color:'+INK+';overflow-wrap:anywhere;'),'padding:21px 18px;border-bottom:1px solid #DCE9CE;')
 return sec(tabs('WORKFLOW',str(len(items))+' STEPS')+sec(content,'border:7px solid '+GREEN+';border-radius:24px;background:white;overflow:hidden;'),'margin:28px 12px;')
