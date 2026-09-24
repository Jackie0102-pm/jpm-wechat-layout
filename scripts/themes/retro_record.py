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
BLUE='#344E88'

LINE='#B59763'

PALE='#F5D48A'

INK='#34384B'

NAVY='#344E88'

RED='#C93630'

GOLD='#EDB234'

CREAM='#FFF0CD'

ROUND="'Arial Rounded MT Bold','Yuanti SC','PingFang SC',sans-serif"

SERIF="'Songti SC','STSong','Noto Serif CJK SC',serif"

FONT="-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif"

GRAD='linear-gradient(125deg,#191E35 0%,#224475 35%,#637FC1 70%,#C5B4D3 100%)'

def star(purple=True,size=52):
 center=sec(plain('●','font-size:10px;line-height:1;text-align:center;color:'+NAVY+';'),'width:'+str(size//3)+'px;height:'+str(size//3)+'px;border-radius:50%;background:'+GOLD+';display:flex;align-items:center;justify-content:center;')
 return sec(center,'width:'+str(size)+'px;height:'+str(size)+'px;border-radius:50%;flex-shrink:0;border:1px solid #CFAB65;display:flex;align-items:center;justify-content:center;background-color:#263A67;background-image:repeating-radial-gradient(circle,#263A67 0px,#263A67 3px,#425889 4px,#263A67 5px);')

def pill(t,dark=False):return sec(plain(t,'font-family:'+ROUND+';font-size:10px;line-height:1.7;font-weight:800;letter-spacing:.3px;color:'+GOLD+';'),'display:inline-block;padding:6px 11px;background:'+(RED if dark else NAVY)+';')

def leaf(t):return '<span leaf="">'+html.escape(norm(t),quote=False)+'</span>'

def sec(c,s=''):return '<section style="box-sizing:border-box;'+s+'">'+c+'</section>'

def plain(t,s=''):return '<p style="margin:0;'+s+'">'+leaf(t)+'</p>'

def inline(t):
 parts=re.split(r'(\*\*.*?\*\*|`[^`]+`|\[[^\]]+\]\([^)]+\))',t);out=''
 for v in parts:
  if v.startswith('**'):out+='<span style="color:#A12C28;font-weight:650;border-bottom:1px solid #C76F43;padding-bottom:2px;">'+leaf(v[2:-2])+'</span>'
  elif v.startswith('`'):out+='<span style="font-family:Consolas,monospace;font-size:13px;background:#F1DAB0;color:'+NAVY+';padding:2px 3px;overflow-wrap:anywhere;">'+leaf(v[1:-1])+'</span>'
  elif re.match(r'^\[.*\]\(',v):
   m=re.match(r'\[([^\]]+)\]\(([^)]+)\)',v);out+='<a href="'+html.escape(m[2],quote=True)+'" style="color:#A12C28;text-decoration:underline;overflow-wrap:anywhere;">'+leaf(m[1])+'</a>'
  else:out+=leaf(v)
 return out

def textp(i,small=False):return '<p style="margin:0 22px 24px;font-family:'+SERIF+';font-size:'+('13' if small else '16')+'px;line-height:2;letter-spacing:.15px;color:'+INK+';overflow-wrap:anywhere;">'+inline(take(i))+'</p>'

def tag(t,white=False):return plain(t,'font-size:10px;line-height:1.8;letter-spacing:1px;color:'+(CREAM if white else NAVY)+';')

def subheading(i):return '<h3 style="margin:36px 22px 17px;font-family:'+ROUND+';font-size:19px;font-weight:850;line-height:1.6;color:'+NAVY+';border-left:6px solid '+RED+';padding-left:12px;overflow-wrap:anywhere;">'+leaf(take(i))+'</h3>'

def chapter(i,n):
 number=take(i);take(i+1);title=take(i+2);subtitle=take(i+3)
 face=sec(tag('CHAPTER '+number,True)+plain(title,'font-family:'+ROUND+';font-size:29px;line-height:1.5;font-weight:850;color:'+GOLD+';margin-top:18px;')+plain(subtitle,'font-size:11px;line-height:1.85;color:'+CREAM+';margin-top:14px;'),'padding:26px 18px;flex:1;min-width:0;')
 side=sec(star(True,40)+plain(number,'font-family:'+ROUND+';font-size:24px;font-weight:850;line-height:1;color:'+GOLD+';margin-top:20px;text-align:center;'),'width:62px;flex-shrink:0;padding:24px 10px;background:'+RED+';')
 band=sec('','height:10px;background-color:'+GOLD+';')
 return '<!-- chapter'+str(n)+' -->'+sec(sec(face+side,'display:flex;background:'+NAVY+';')+band,'margin:48px 12px 30px;border:2px solid '+NAVY+';')

def quote(i):
 q=take(i);note=take(i+1);dark=EMPHASIS
 fg=GOLD if dark else NAVY;bg=NAVY if dark else '#F3C65F'
 return sec(plain('“','font-family:Georgia,serif;font-size:46px;line-height:.8;color:'+(GOLD if dark else RED)+';margin-bottom:12px;')+plain(q,'font-family:'+ROUND+';font-size:22px;line-height:1.7;font-weight:750;color:'+fg+';')+plain(note,'font-family:'+SERIF+';font-size:13px;line-height:1.95;color:'+(CREAM if dark else '#4D422E')+';margin-top:20px;overflow-wrap:anywhere;'),'margin:30px 17px 32px;padding:26px 20px;border:2px solid '+NAVY+';background:'+bg+';box-shadow:5px 5px 0 '+RED+';')

def note(i,end):
 content=''.join('<p style="margin:13px 0 0;font-family:'+SERIF+';font-size:14px;line-height:1.95;overflow-wrap:anywhere;">'+inline(take(j))+'</p>' for j in range(i+1,end))
 return sec(pill(take(i),True)+content,'padding:18px;margin:0 22px 28px;background:#F5D48A;border-bottom:4px solid '+NAVY+';')

def rows(titleidx,start,count,step=3,metric=False):
 title=take(titleidx);cells=[]
 for x in range(count):
  j=start+x*step;a,b,c=take(j),take(j+1),take(j+2)
  if metric:
   cell=sec(plain(a,'font-family:'+ROUND+';font-size:36px;line-height:1.2;font-weight:900;color:'+NAVY+';'),'padding:15px 10px;background:'+GOLD+';border-bottom:2px solid '+NAVY+';')+sec(plain(b,'font-family:'+ROUND+';font-size:14px;font-weight:800;line-height:1.65;color:'+NAVY+';overflow-wrap:anywhere;')+plain(c,'font-family:'+SERIF+';font-size:12px;line-height:1.85;color:'+INK+';margin-top:9px;overflow-wrap:anywhere;'),'padding:15px 10px;')
   cells.append(sec(sec(cell,'height:100%;border:2px solid '+NAVY+';background:'+CREAM+';'),'width:50%;padding:5px;'))
  else:
   cell=sec(plain(a,'font-family:'+ROUND+';font-size:11px;font-weight:800;color:'+CREAM+';line-height:1.8;'),'width:68px;flex-shrink:0;padding:15px 9px;background:'+NAVY+';')+sec(plain(b,'font-family:'+ROUND+';font-size:16px;font-weight:800;line-height:1.6;color:'+NAVY+';overflow-wrap:anywhere;')+plain(c,'font-family:'+SERIF+';font-size:13px;line-height:1.9;color:'+INK+';margin-top:6px;overflow-wrap:anywhere;'),'flex:1;min-width:0;padding:15px 12px;')
   cells.append(sec(cell,'display:flex;border-top:1px solid #B59763;background:#F7E6BE;'))
 return sec(plain(title,'font-family:'+ROUND+';font-size:18px;color:'+NAVY+';font-weight:850;line-height:1.65;margin:0 5px 17px;')+sec(''.join(cells),'display:flex;flex-wrap:wrap;' if metric else 'border:1px solid #B59763;border-top:0;'),'margin:29px 17px;')

WRAPPER='max-width:600px;margin:0 auto;background:#FFF0CD;font-family:' + FONT + ';color:' + INK + ';padding-top:6px;padding-bottom:1px;'

def flow(items):
 content=''
 for k,t in enumerate(items):
  number=str(k+1).zfill(2)
  left=sec(sec(plain(number,'font-family:'+ROUND+';font-size:15px;font-weight:850;line-height:34px;text-align:center;color:'+GOLD+';'),'width:36px;height:36px;border-radius:50%;border:1px solid '+GOLD+';background:'+NAVY+';'),'width:57px;flex-shrink:0;padding:23px 10px;background:#E9BB55;')
  right=sec(plain(t,'font-family:'+SERIF+';font-size:15px;line-height:1.95;color:'+INK+';overflow-wrap:anywhere;'),'flex:1;min-width:0;padding:22px 15px;background:'+CREAM+';')
  content+=sec(left+right,'display:flex;border-top:1px solid #C7A570;')
 return sec(sec(pill('SIDE A / WORKFLOW'),'padding:17px;background:'+GOLD+';')+content,'margin:28px 17px;border:2px solid '+NAVY+';')
