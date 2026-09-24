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
INK='#2F3538'

BLUE='#3E659A'

OLIVE='#979437'

DARK='#151515'

PAPER='#F7F6F0'

PALE='#EBEBDD'

LINE='#D9DDCF'

MUTED='#656F72'

GOLD=OLIVE

FONT="-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif"

SERIF=ROUND=FONT

LIGHTWAVE='background-color:'+PAPER+';background-image:radial-gradient(ellipse at 120% 78%,transparent 35%,#DCDDAB 47%,#E7E8CC 58%,transparent 69%);'

DARKWAVE='background-color:'+DARK+';background-image:radial-gradient(ellipse at 115% 87%,transparent 37%,#30312C 48%,#272923 58%,transparent 68%);'

def leaf(t):return '<span leaf="">'+html.escape(norm(t),quote=False)+'</span>'

def sec(c,s=''):return '<section style="box-sizing:border-box;'+s+'">'+c+'</section>'

def plain(t,s=''):return '<p style="margin:0;'+s+'">'+leaf(t)+'</p>'

def tag(t,white=False):return plain(t,'font-size:10px;line-height:1.8;color:'+('#D2D2CB' if white else BLUE)+';')

def brand(dark=False):return '<p style="margin:0;font-size:10px;line-height:1.8;color:'+('#E8E8E1' if dark else BLUE)+';"><span style="color:'+OLIVE+';font-size:17px;margin-right:7px;">'+leaf('✳')+'</span>'+leaf(BRAND_NAME)+'</p>'

def pill(t,dark=False):return plain(t,'display:inline-block;font-size:11px;line-height:1.7;font-weight:600;color:'+(OLIVE if dark else BLUE)+';border-bottom:2px solid '+OLIVE+';padding-bottom:5px;')

def inline(t):
 parts=re.split(r'(\*\*.*?\*\*|`[^`]+`|\[[^\]]+\]\([^)]+\))',t);result=''
 for v in parts:
  if v.startswith('**'):result+='<span style="color:'+BLUE+';font-weight:600;border-bottom:1px solid '+OLIVE+';padding-bottom:2px;">'+leaf(v[2:-2])+'</span>'
  elif v.startswith('`'):result+='<span style="font-family:Consolas,monospace;font-size:13px;background:'+PALE+';color:'+BLUE+';padding:2px 3px;overflow-wrap:anywhere;">'+leaf(v[1:-1])+'</span>'
  elif re.match(r'^\[.*\]\(',v):
   m=re.match(r'\[([^\]]+)\]\(([^)]+)\)',v);result+='<a href="'+html.escape(m[2],quote=True)+'" style="color:'+BLUE+';text-decoration:underline;overflow-wrap:anywhere;">'+leaf(m[1])+'</a>'
  else:result+=leaf(v)
 return result

def textp(i,small=False):return '<p style="margin:0 24px 26px;font-family:'+FONT+';font-size:'+('13' if small else '16')+'px;line-height:1.95;color:'+INK+';overflow-wrap:anywhere;">'+inline(take(i))+'</p>'

def subheading(i):return '<h3 style="margin:39px 24px 18px;font-size:19px;font-weight:500;line-height:1.65;color:'+BLUE+';overflow-wrap:anywhere;">'+leaf(take(i))+'</h3>'

def chapter(i,n):
 number=take(i);take(i+1);title=take(i+2);subtitle=take(i+3);dark=n in [1,3,5,6]
 eng=subtitle.split(' · ')[0]
 top=sec(brand(dark)+plain(number,'font-size:12px;line-height:1.8;font-weight:600;color:'+OLIVE+';'),'display:flex;justify-content:space-between;align-items:center;')
 titleblock=plain(eng,'font-size:24px;font-weight:400;line-height:1.04;letter-spacing:-.8px;white-space:pre-line;color:'+('#F1F1EA' if dark else BLUE)+';')+plain(title,'font-size:22px;line-height:1.6;font-weight:400;color:'+('#F1F1EA' if dark else BLUE)+';margin-top:15px;')
 return '<!-- chapter'+str(n)+' -->'+sec(top+sec(titleblock,'margin-top:55px;text-align:'+('right' if dark else 'left')+';')+plain(subtitle,'font-size:11px;line-height:1.9;color:'+('#C5C6BC' if dark else BLUE)+';margin-top:24px;'),'margin:51px 0 33px;padding:24px;'+(DARKWAVE if dark else LIGHTWAVE))

def quote(i):
 q=take(i);note=take(i+1);dark=EMPHASIS
 return sec(plain('✳','font-size:22px;line-height:1;color:'+OLIVE+';margin-bottom:26px;')+plain(q,'font-size:22px;line-height:1.65;font-weight:400;color:'+('#F0F0E9' if dark else BLUE)+';')+plain(note,'font-size:13px;line-height:1.95;color:'+('#C7C8BD' if dark else MUTED)+';margin-top:26px;overflow-wrap:anywhere;'),'margin:34px 0;padding:30px 24px;'+(DARKWAVE if dark else LIGHTWAVE))

def note(i,end):
 content=''.join('<p style="margin:15px 0 0;font-size:14px;line-height:1.95;overflow-wrap:anywhere;color:'+INK+';">'+inline(take(j))+'</p>' for j in range(i+1,end))
 return sec(pill(take(i))+content,'padding:22px 19px;margin:0 24px 28px;background:'+PALE+';')

def rows(titleidx,start,count,step=3,metric=False):
 title=take(titleidx);cells=[]
 for x in range(count):
  j=start+x*step;a,b,c=take(j),take(j+1),take(j+2)
  if metric:
   cell=plain(a,'font-size:24px;font-weight:400;line-height:1.3;color:'+OLIVE+';')+plain(b,'font-size:13px;font-weight:500;line-height:1.8;margin-top:15px;color:#F1F1EB;')+plain(c,'font-size:11px;line-height:1.9;color:#C7C8BD;margin-top:7px;overflow-wrap:anywhere;')
   cells.append(sec(cell,'width:50%;padding:23px 13px 25px 0;border-top:1px solid #37392F;'))
  else:
   cell=plain(a,'font-size:11px;line-height:1.8;color:'+OLIVE+';font-weight:600;')+plain(b,'font-size:16px;font-weight:500;line-height:1.6;color:'+BLUE+';margin-top:7px;overflow-wrap:anywhere;')+plain(c,'font-size:13px;line-height:1.9;color:'+MUTED+';margin-top:8px;overflow-wrap:anywhere;')
   cells.append(sec(cell,'width:50%;padding:18px 14px 23px 0;'))
 headline=plain(title,'font-size:18px;color:'+('#F0F0E9' if metric else BLUE)+';font-weight:400;line-height:1.65;margin:0 0 24px;')
 return sec(headline+sec(''.join(cells),'display:flex;flex-wrap:wrap;')+(brand(True) if metric else ''),'margin:32px '+('0' if metric else '24px')+';'+('padding:30px 24px;'+DARKWAVE if metric else ''))

WRAPPER='max-width:600px;margin:0 auto;background:#F7F6F0;font-family:' + FONT + ';color:' + INK + ';padding-top:6px;padding-bottom:1px;'

def flow(items):
 content=''
 for k,t in enumerate(items):
  number=str(k+1).zfill(2)
  copy=plain(number,'font-size:13px;line-height:1.5;font-weight:600;color:'+BLUE+';text-align:right;margin-bottom:12px;')+plain(t,'font-size:15px;line-height:1.95;color:'+INK+';overflow-wrap:anywhere;')
  content+=sec(sec(copy,'flex:1;min-width:0;padding:23px 18px 25px 0;')+sec(plain('▪','font-size:24px;line-height:1;color:'+OLIVE+';text-align:right;margin-right:-5px;'),'width:12px;padding-top:22px;flex-shrink:0;border-right:1px solid '+BLUE+';'),'display:flex;')
 return sec(tag('从输入，到交付。')+content,'margin:31px 26px 31px 24px;')
