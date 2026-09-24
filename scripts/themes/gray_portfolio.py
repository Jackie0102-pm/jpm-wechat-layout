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
INK='#2C2A29'

MUTED='#858380'

LINE='#DDDCD9'

PALE='#F5F5F3'

BLUE=INK

GOLD=PALE

FONT="-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif"

SERIF=ROUND=FONT

GRID='background-color:#FCFCFB;background-image:linear-gradient(#F0F0ED 1px,transparent 1px),linear-gradient(90deg,#F0F0ED 1px,transparent 1px);background-size:24px 24px;'

def leaf(t):return '<span leaf="">'+html.escape(norm(t),quote=False)+'</span>'

def sec(c,s=''):return '<section style="box-sizing:border-box;'+s+'">'+c+'</section>'

def plain(t,s=''):return '<p style="margin:0;'+s+'">'+leaf(t)+'</p>'

def tag(t,white=False):return plain(t,'font-size:10px;line-height:1.8;color:'+MUTED+';')

def pill(t,dark=False):return sec(plain(t,'font-size:10px;line-height:1.6;color:'+INK+';'),'display:inline-block;padding:3px 7px;border:1px solid #C9C8C5;border-radius:4px;')

def inline(t):
 parts=re.split(r'(\*\*.*?\*\*|`[^`]+`|\[[^\]]+\]\([^)]+\))',t);result=''
 for v in parts:
  if v.startswith('**'):result+='<span style="color:'+INK+';font-weight:600;border-bottom:1px solid #9C9A96;padding-bottom:2px;">'+leaf(v[2:-2])+'</span>'
  elif v.startswith('`'):result+='<span style="font-family:Consolas,monospace;font-size:13px;background:'+PALE+';color:'+INK+';padding:2px 3px;overflow-wrap:anywhere;">'+leaf(v[1:-1])+'</span>'
  elif re.match(r'^\[.*\]\(',v):
   m=re.match(r'\[([^\]]+)\]\(([^)]+)\)',v);result+='<a href="'+html.escape(m[2],quote=True)+'" style="color:'+INK+';text-decoration:underline;overflow-wrap:anywhere;">'+leaf(m[1])+'</a>'
  else:result+=leaf(v)
 return result

def textp(i,small=False):return '<p style="margin:0 24px 25px;font-family:'+FONT+';font-size:'+('13' if small else '16')+'px;line-height:1.95;color:'+INK+';overflow-wrap:anywhere;">'+inline(take(i))+'</p>'

def subheading(i):return '<h3 style="margin:38px 24px 18px;font-size:19px;font-weight:600;line-height:1.65;color:'+INK+';overflow-wrap:anywhere;">'+leaf(take(i))+'</h3>'

def chapter(i,n):
 number=take(i);take(i+1);title=take(i+2);subtitle=take(i+3)
 eng=subtitle.split(' · ')[0]
 heading=sec(plain(eng,'font-size:24px;letter-spacing:-1px;font-weight:400;line-height:1.15;color:'+MUTED+';')+plain(title,'font-size:24px;font-weight:400;line-height:1.5;color:'+INK+';margin-top:3px;')+plain('↘','font-size:22px;line-height:1;color:#A09E9A;margin-top:32px;'),'flex:1;min-width:0;padding:30px 22px;')
 rail=sec(plain(number,'font-size:11px;line-height:29px;text-align:center;color:white;background:'+INK+';width:29px;height:29px;border-radius:50%;')+plain('+','font-size:20px;font-weight:300;line-height:1;color:#AAA8A4;margin-top:55px;text-align:center;'),'width:50px;padding:30px 10px;border-left:1px solid '+LINE+';'+GRID)
 return '<!-- chapter'+str(n)+' -->'+sec(sec(heading+rail,'display:flex;')+sec(plain(subtitle,'font-size:11px;line-height:1.8;color:#74716E;'),'padding:15px 22px;border-top:1px solid '+LINE+';'),'margin:55px 0 32px;border-top:1px solid '+LINE+';border-bottom:1px solid '+LINE+';')

def quote(i):
 q=take(i);note=take(i+1)
 return sec(plain('“','font-family:Georgia,serif;font-size:24px;line-height:1;color:#95938F;margin-bottom:14px;')+plain(q,'font-size:22px;line-height:1.65;font-weight:400;color:'+INK+';')+plain(note,'font-size:13px;line-height:1.95;color:#76736F;margin-top:24px;overflow-wrap:anywhere;'),'margin:35px 24px;padding:28px 0;border-top:1px solid '+LINE+';border-bottom:1px solid '+LINE+';')

def note(i,end):
 content=''.join('<p style="margin:13px 0 0;font-size:14px;line-height:1.95;overflow-wrap:anywhere;color:'+INK+';">'+inline(take(j))+'</p>' for j in range(i+1,end))
 return sec(pill(take(i))+content,'padding:20px 18px;margin:0 24px 27px;background:'+PALE+';border-left:1px solid #C2C0BB;')

def rows(titleidx,start,count,step=3,metric=False):
 title=take(titleidx);cells=[]
 for x in range(count):
  j=start+x*step;a,b,c=take(j),take(j+1),take(j+2)
  if metric:
   cell=plain(a,'font-size:24px;font-weight:400;line-height:1.3;color:'+INK+';')+plain(b,'font-size:13px;font-weight:600;line-height:1.8;margin-top:18px;color:'+INK+';')+plain(c,'font-size:11px;line-height:1.9;color:#76736F;margin-top:8px;overflow-wrap:anywhere;')
   cells.append(sec(cell,'width:50%;padding:22px 14px;border-top:1px solid '+LINE+';'+('border-right:1px solid '+LINE+';' if x%2==0 else '')))
  else:
   left=sec(plain(a,'font-size:11px;line-height:1.8;color:'+MUTED+';'),'width:68px;flex-shrink:0;padding:19px 8px 19px 0;')
   right=sec(plain(b,'font-size:16px;font-weight:500;line-height:1.6;color:'+INK+';overflow-wrap:anywhere;')+plain(c,'font-size:13px;line-height:1.85;color:#76736F;margin-top:7px;overflow-wrap:anywhere;'),'flex:1;min-width:0;padding:19px 0 19px 15px;border-left:1px solid '+LINE+';')
   cells.append(sec(left+right,'display:flex;border-top:1px solid '+LINE+';'))
 return sec(plain(title,'font-size:16px;color:'+INK+';font-weight:500;line-height:1.65;margin:0 0 20px;')+sec(''.join(cells),('display:flex;flex-wrap:wrap;' if metric else '')+'border-bottom:1px solid '+LINE+';'),'margin:32px 24px;')

WRAPPER='max-width:600px;margin:0 auto;background:#FDFCFA;font-family:' + FONT + ';color:' + INK + ';padding-top:6px;padding-bottom:1px;'

def flow(items):
 content=''
 for k,t in enumerate(items):
  number=str(k+1).zfill(2)
  content+=sec(sec(plain('('+number+')','font-size:13px;line-height:1.95;color:'+MUTED+';'),'width:42px;flex-shrink:0;')+sec(plain(t,'font-size:15px;line-height:1.95;color:'+INK+';overflow-wrap:anywhere;'),'flex:1;min-width:0;')+sec(plain('+','font-size:16px;line-height:1.9;color:#999792;'),'width:17px;text-align:right;flex-shrink:0;'),'display:flex;padding:21px 0;border-top:1px solid '+LINE+';')
 return sec(content,'margin:32px 24px;border-bottom:1px solid '+LINE+';')
