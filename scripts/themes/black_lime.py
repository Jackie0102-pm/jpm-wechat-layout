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
BLUE='#CFFF70'

LINE='#62685A'

PALE='#242A1B'

INK='#D7D8D3'

FONT="-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif"

GRAD='linear-gradient(110deg,#B0FF00 0%,#DCFA75 56%,#FFF2B2 100%)'

def star(purple=True,size=52):
 return sec(plain('→','font-family:Arial,sans-serif;font-size:'+str(size//2)+'px;line-height:'+str(size-2)+'px;font-weight:300;color:white;text-align:center;'),'width:'+str(size)+'px;height:'+str(size)+'px;flex-shrink:0;border:1px solid #777972;border-radius:50%;')

def pill(t,dark=False):
 return sec(plain(t,'font-size:10px;line-height:1.6;font-weight:600;color:'+('#FFFFFF' if dark else '#10120C')+';'),'display:inline-block;padding:6px 12px;border-radius:25px;'+('border:1px solid #777972;' if dark else 'background-color:#C3FF32;background-image:'+GRAD+';'))

def leaf(t):return '<span leaf="">'+html.escape(norm(t),quote=False)+'</span>'

def sec(c,s=''):return '<section style="box-sizing:border-box;'+s+'">'+c+'</section>'

def plain(t,s=''):return '<p style="margin:0;'+s+'">'+leaf(t)+'</p>'

def inline(t,light=False):
 parts=re.split(r'(\*\*.*?\*\*|`[^`]+`|\[[^\]]+\]\([^)]+\))',t);out=''
 fg='#354D08' if light else '#D3FF76';line='#89A93F' if light else '#708544'
 for v in parts:
  if v.startswith('**'):out+='<span style="color:'+fg+';border-bottom:1px solid '+line+';padding-bottom:2px;">'+leaf(v[2:-2])+'</span>'
  elif v.startswith('`'):out+='<span style="font-family:Consolas,monospace;font-size:13px;background:'+('#E8EBD9' if light else '#272C1E')+';color:'+fg+';padding:2px 3px;overflow-wrap:anywhere;">'+leaf(v[1:-1])+'</span>'
  elif re.match(r'^\[.*\]\(',v):
   m=re.match(r'\[([^\]]+)\]\(([^)]+)\)',v);out+='<a href="'+html.escape(m[2],quote=True)+'" style="color:'+fg+';text-decoration:underline;text-underline-offset:3px;overflow-wrap:anywhere;">'+leaf(m[1])+'</a>'
  else:out+=leaf(v)
 return out

def textp(i,small=False):
 return '<p style="margin:0 22px 24px;font-size:'+('13' if small else '15')+'px;line-height:2;letter-spacing:.1px;color:#D7D8D3;overflow-wrap:anywhere;">'+inline(take(i))+'</p>'

def tag(t,white=False):return plain(t,'font-size:10px;line-height:1.7;letter-spacing:.5px;color:#D0D2C9;')

def subheading(i):
 return '<h3 style="margin:37px 22px 18px;font-size:19px;font-weight:450;line-height:1.6;color:white;overflow-wrap:anywhere;">'+leaf(take(i))+'</h3>'

def chapter(i,n):
 number=take(i);take(i+1);title=take(i+2);subtitle=take(i+3)
 head=sec(pill('PART '+number)+star(True,36),'display:flex;justify-content:space-between;align-items:center;margin-bottom:31px;')
 return '<!-- chapter'+str(n)+' -->'+sec(head+plain(title,'font-size:36px;line-height:1.35;font-weight:300;letter-spacing:-1.2px;color:white;')+plain(subtitle,'font-size:11px;line-height:1.9;color:#B8BDB0;margin-top:18px;'),'padding:0 22px;margin:65px 0 34px;')

def quote(i):
 q=take(i);note=take(i+1);bright=EMPHASIS
 content=plain(q,'font-size:23px;line-height:1.65;font-weight:350;letter-spacing:-.3px;color:'+('#10120C' if bright else 'white')+';')+plain(note,'font-size:12px;line-height:1.95;color:'+('#374322' if bright else '#B7BDB0')+';margin-top:24px;overflow-wrap:anywhere;')
 return sec(content,'margin:30px 12px;padding:28px 22px;border-radius:22px;'+('background-color:#C3FF32;background-image:'+GRAD+';' if bright else 'border:1px solid #656A5D;'))

def note(i,end):
 head=take(i);content=''.join('<p style="margin:13px 0 0;font-size:13px;line-height:1.95;color:#34372F;overflow-wrap:anywhere;">'+inline(take(j),True)+'</p>' for j in range(i+1,end))
 return sec(plain(head,'font-size:12px;font-weight:650;line-height:1.8;color:#10120C;')+content,'padding:21px 18px;margin:0 22px 27px;background:#F6F6F0;border-radius:19px;')

def rows(titleidx,start,count,step=3,metric=False):
 title=take(titleidx);cells=[]
 for x in range(count):
  j=start+x*step;a,b,c=take(j),take(j+1),take(j+2)
  if metric:
   cell=plain(a,'font-size:42px;line-height:1.1;font-weight:350;letter-spacing:-2px;color:#10120C;')+plain(b,'font-size:14px;font-weight:550;line-height:1.6;color:#10120C;margin-top:12px;overflow-wrap:anywhere;')+plain(c,'font-size:11px;line-height:1.9;color:#3F4A2F;margin-top:10px;overflow-wrap:anywhere;')
   cells.append(sec(sec(cell,'height:100%;padding:20px 12px;border-radius:17px;background-color:#C3FF32;background-image:'+GRAD+';'),'width:50%;padding:5px;'))
  else:
   cell=sec(plain(a,'font-size:11px;line-height:1.8;color:#465C23;'),'width:66px;flex-shrink:0;padding-right:8px;')+sec(plain(b,'font-size:17px;font-weight:400;line-height:1.6;color:#10120C;overflow-wrap:anywhere;')+plain(c,'font-size:12px;line-height:1.9;color:#4F5349;margin-top:7px;overflow-wrap:anywhere;'),'flex:1;min-width:0;')
   cells.append(sec(cell,'display:flex;padding:19px 4px;border-top:1px solid #D4D8CA;'))
 return sec(plain(title,'font-size:'+('24' if metric else '19')+'px;color:#10120C;font-weight:350;line-height:1.5;margin:0 5px 21px;letter-spacing:-.5px;')+sec(''.join(cells),'display:flex;flex-wrap:wrap;' if metric else ''),'margin:30px 12px;padding:24px 10px 15px;background:#F6F6F0;border-radius:23px;')

WRAPPER='max-width:600px;margin:0 auto;background:#080808;font-family:' + FONT + ';color:' + INK + ';padding-top:6px;padding-bottom:1px;'

def flow(items):
 content=''
 for k,t in enumerate(items):
  number=str(k+1).zfill(2)
  mode=k%3;dark=mode==1;fg='#FFFFFF' if dark else '#10120C';muted='#AAB19F' if dark else '#4C573C'
  bg=('background-color:#C3FF32;background-image:'+GRAD+';') if mode==0 else ('border:1px solid #6B7162;' if dark else 'background:#F6F6F0;')
  head=sec(plain(number,'font-size:28px;font-weight:350;line-height:1.3;color:'+fg+';')+plain('STEP','font-size:9px;line-height:1.6;letter-spacing:1px;color:'+muted+';'),'display:flex;justify-content:space-between;align-items:center;margin-bottom:19px;')
  content+=sec(head+plain(t,'font-size:14px;line-height:1.95;color:'+fg+';overflow-wrap:anywhere;'),'padding:23px 20px;margin-bottom:13px;border-radius:21px;'+bg)
 return sec(content,'margin:28px 22px;')
