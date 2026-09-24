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
BLUE='#205BA7'

LINE='#CBD8E8'

PALE='#EAF3FC'

INK='#24384F'

FONT="-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif"

GRAD='linear-gradient(125deg,#191E35 0%,#224475 35%,#637FC1 70%,#C5B4D3 100%)'

def leaf(t):return '<span leaf="">'+html.escape(norm(t),quote=False)+'</span>'

def sec(c,s=''):return '<section style="box-sizing:border-box;'+s+'">'+c+'</section>'

def plain(t,s=''):return '<p style="margin:0;'+s+'">'+leaf(t)+'</p>'

def inline(t):
 parts=re.split(r'(\*\*.*?\*\*|`[^`]+`|\[[^\]]+\]\([^)]+\))',t)
 out=''
 for v in parts:
  if v.startswith('**'):out+='<span style="color:'+BLUE+';border-bottom:1px solid #9EB8DC;padding-bottom:2px;">'+leaf(v[2:-2])+'</span>'
  elif v.startswith('`'):out+='<span style="font-family:Consolas,monospace;font-size:13px;background:'+PALE+';color:'+BLUE+';padding:2px 3px;overflow-wrap:anywhere;">'+leaf(v[1:-1])+'</span>'
  elif re.match(r'^\[.*\]\(',v):
   m=re.match(r'\[([^\]]+)\]\(([^)]+)\)',v);out+='<a href="'+html.escape(m[2],quote=True)+'" style="color:'+BLUE+';text-decoration:underline;text-underline-offset:3px;overflow-wrap:anywhere;">'+leaf(m[1])+'</a>'
  else:out+=leaf(v)
 return out

def textp(i,small=False):
 t=take(i)
 return '<p style="margin:0 20px 22px;font-size:'+('13' if small else '15')+'px;line-height:1.95;letter-spacing:.15px;color:'+INK+';overflow-wrap:anywhere;">'+inline(t)+'</p>'

def tag(t,white=False):return plain(t,'font-size:10px;line-height:1.6;letter-spacing:1.3px;color:'+('#E5EEFF' if white else BLUE)+';')

def subheading(i):return '<h3 style="margin:32px 20px 16px;padding-top:18px;border-top:1px solid '+LINE+';font-size:18px;font-weight:500;line-height:1.7;color:'+BLUE+';overflow-wrap:anywhere;">'+leaf(take(i))+'</h3>'

def chapter(i,n):
 number=take(i);take(i+1);title=take(i+2);subtitle=take(i+3)
 return '<!-- chapter'+str(n)+' -->'+sec(sec(plain(number,'font-size:45px;line-height:1.1;font-weight:300;color:'+BLUE+';'),'width:76px;flex-shrink:0;padding:24px 12px;border-right:1px solid '+LINE+';')+sec(tag('PART / '+subtitle.split(' · ')[0])+plain(title,'font-size:26px;line-height:1.4;font-weight:400;color:'+BLUE+';margin-top:8px;')+plain(subtitle,'font-size:11px;line-height:1.8;color:#58718F;margin-top:10px;'),'flex:1;min-width:0;padding:24px 18px;'),'display:flex;border-top:1px solid '+LINE+';border-bottom:1px solid '+LINE+';margin:46px 0 26px;background:'+PALE+';')

def quote(i):
 dark=EMPHASIS;q=take(i);note=take(i+1)
 fg='#FFFFFF' if dark else BLUE
 return sec(plain(q,'font-size:20px;line-height:1.8;font-weight:400;color:'+fg+';')+plain(note,'font-size:12px;line-height:1.9;color:'+('#DFEAF9' if dark else '#58718F')+';margin-top:18px;overflow-wrap:anywhere;'),'margin:28px 0;padding:28px 22px;background:'+(BLUE if dark else PALE)+';border-top:1px solid '+LINE+';border-bottom:1px solid '+LINE+';')

def note(i,end):
 head=take(i);content=''.join('<p style="margin:10px 0 0;font-size:13px;line-height:1.9;overflow-wrap:anywhere;">'+inline(take(j))+'</p>' for j in range(i+1,end))
 return sec(plain(head,'font-size:12px;font-weight:500;color:'+BLUE+';')+content,'padding:18px;margin:0 20px 24px;background:'+PALE+';border-left:2px solid '+BLUE+';')

def rows(titleidx,start,count,step=3,metric=False):
 title=take(titleidx)
 cells=[]
 for x in range(count):
  j=start+x*step;a,b,c=take(j),take(j+1),take(j+2)
  if metric:
   cells.append(sec(plain(a,'font-size:39px;line-height:1.15;font-weight:300;color:'+BLUE+';')+plain(b,'font-size:14px;line-height:1.6;color:'+BLUE+';margin-top:12px;overflow-wrap:anywhere;')+plain(c,'font-size:11px;line-height:1.8;color:#58718F;margin-top:9px;overflow-wrap:anywhere;'),'width:50%;padding:20px 16px;border-right:1px solid '+LINE+';border-bottom:1px solid '+LINE+';'))
  else:
   cells.append(sec(sec(plain(a,'font-size:12px;color:'+BLUE+';line-height:1.8;'),'width:74px;flex-shrink:0;padding:16px 10px;border-right:1px solid '+LINE+';background:'+PALE+';')+sec(plain(b,'font-size:14px;font-weight:500;line-height:1.7;color:'+BLUE+';overflow-wrap:anywhere;')+plain(c,'font-size:12px;line-height:1.8;color:'+INK+';margin-top:6px;overflow-wrap:anywhere;'),'flex:1;min-width:0;padding:16px 12px;'),'display:flex;border-bottom:1px solid '+LINE+';'))
 return sec(plain(title,'font-size:15px;color:'+BLUE+';font-weight:500;padding:16px;border-bottom:1px solid '+LINE+';')+sec(''.join(cells),'display:flex;flex-wrap:wrap;' if metric else ''),'margin:24px 20px;border:1px solid '+LINE+';border-bottom:0;')

WRAPPER='max-width:600px;margin:0 auto;background:white;font-family:' + FONT + ';color:' + INK + ';border-left:1px solid ' + LINE + ';border-right:1px solid ' + LINE + ';'

def flow(items):
 content=''
 for k,t in enumerate(items):
  number=str(k+1).zfill(2)
  content+=sec(sec(plain(number,'font-size:24px;line-height:1.2;font-weight:300;color:'+BLUE+';'),'width:48px;flex-shrink:0;padding:20px 8px;border-right:1px solid '+LINE+';')+sec(plain(t,'font-size:14px;line-height:1.95;color:'+INK+';overflow-wrap:anywhere;'),'padding:20px 14px;flex:1;min-width:0;'),'display:flex;border-bottom:1px solid '+LINE+';background:'+(PALE if k%2==0 else 'white')+';')
 return sec(content,'margin:24px 20px;border:1px solid '+LINE+';border-bottom:0;')
