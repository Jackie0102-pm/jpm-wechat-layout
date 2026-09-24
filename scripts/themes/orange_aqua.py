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
BLUE='#F94C10'

LINE='#DABDAE'

PALE='#EAF2F2'

INK='#443D36'

AQUA='#83B1BB'

PAPER='#FAF8F4'

TEXTORANGE='#AD330D'

MONO="'Menlo','Consolas',monospace"

FONT="-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif"

GRAD='linear-gradient(145deg,#83B1BB 0%,#D6977D 24%,#F94C10 53%,#F94C10 100%)'

def star(purple=True,size=52):
 return plain('✦','font-size:'+str(size//2)+'px;line-height:1;color:'+('#F94C10' if purple else '#83B1BB')+';')

def pill(t,dark=False):
 return plain(t,'font-family:'+MONO+';font-size:10px;line-height:1.6;letter-spacing:.6px;color:'+('#245761' if dark else TEXTORANGE)+';')

def leaf(t):return '<span leaf="">'+html.escape(norm(t),quote=False)+'</span>'

def sec(c,s=''):return '<section style="box-sizing:border-box;'+s+'">'+c+'</section>'

def plain(t,s=''):return '<p style="margin:0;'+s+'">'+leaf(t)+'</p>'

def inline(t):
 parts=re.split(r'(\*\*.*?\*\*|`[^`]+`|\[[^\]]+\]\([^)]+\))',t);out=''
 for v in parts:
  if v.startswith('**'):out+='<span style="color:'+TEXTORANGE+';border-bottom:1px solid #E9977F;padding-bottom:2px;">'+leaf(v[2:-2])+'</span>'
  elif v.startswith('`'):out+='<span style="font-family:Consolas,monospace;font-size:13px;background:#E9F2F3;color:#245761;padding:2px 3px;overflow-wrap:anywhere;">'+leaf(v[1:-1])+'</span>'
  elif re.match(r'^\[.*\]\(',v):
   m=re.match(r'\[([^\]]+)\]\(([^)]+)\)',v);out+='<a href="'+html.escape(m[2],quote=True)+'" style="color:'+TEXTORANGE+';text-decoration:underline;overflow-wrap:anywhere;">'+leaf(m[1])+'</a>'
  else:out+=leaf(v)
 return out

def textp(i,small=False):
 return '<p style="margin:0 22px 23px;font-size:'+('13' if small else '15')+'px;line-height:2;letter-spacing:.1px;color:'+INK+';overflow-wrap:anywhere;">'+inline(take(i))+'</p>'

def tag(t,white=False):return plain(t,'font-family:'+MONO+';font-size:10px;line-height:1.7;letter-spacing:.4px;color:'+('white' if white else TEXTORANGE)+';')

def subheading(i):
 return '<h3 style="margin:34px 22px 17px;font-size:18px;font-weight:500;line-height:1.65;color:'+TEXTORANGE+';padding-top:16px;border-top:1px solid #E9C6B8;overflow-wrap:anywhere;">'+leaf(take(i))+'</h3>'

def chapter(i,n):
 number=take(i);take(i+1);title=take(i+2);subtitle=take(i+3)
 aqua=n in {2,5};bg=AQUA if aqua else BLUE;fg='#173E47' if aqua else '#FFFFFF';small='#204B54' if aqua else '#491707'
 left=sec(plain(subtitle.split(' · ')[0],'font-family:'+MONO+';font-size:11px;letter-spacing:-.2px;line-height:1.6;color:'+small+';')+plain(title,'font-size:30px;line-height:1.5;font-weight:350;letter-spacing:-.8px;color:'+fg+';margin-top:26px;'),'flex:1;min-width:0;padding:25px 20px;')
 right=sec(plain(number,'font-family:'+MONO+';font-size:36px;line-height:1.2;letter-spacing:-3px;color:'+fg+';'),'width:72px;flex-shrink:0;display:flex;align-items:flex-end;justify-content:center;padding:20px 10px;border-left:1px solid rgba(255,255,255,.45);')
 return '<!-- chapter'+str(n)+' -->'+sec(sec(left+right,'display:flex;')+plain(subtitle,'font-size:11px;line-height:1.8;padding:13px 20px;color:'+small+';border-top:1px solid rgba(255,255,255,.45);'),'margin:50px 0 28px;background:'+bg+';')

def quote(i):
 color=TEXTORANGE;bg=PAPER;dark=EMPHASIS
 if dark:bg=AQUA;color='#173F48'
 inner=plain('↗','font-family:'+MONO+';font-size:30px;line-height:1;color:'+color+';margin-bottom:18px;')+plain(take(i),'font-size:23px;line-height:1.65;font-weight:400;letter-spacing:-.3px;color:'+color+';')+plain(take(i+1),'font-size:12px;line-height:1.9;color:'+('#25535C' if dark else '#784632')+';margin-top:22px;overflow-wrap:anywhere;')
 return sec(inner,'margin:30px 0 30px 22px;padding:27px 22px;background-color:'+bg+';'+('' if dark else 'background-image:repeating-linear-gradient(0deg,rgba(226,118,71,.06) 0px,rgba(226,118,71,.06) 3px,transparent 3px,transparent 9px);')+'border-top:1px solid #D8B7A8;border-bottom:1px solid #D8B7A8;')

def note(i,end):
 head=take(i);content=''.join('<p style="margin:12px 0 0;font-size:13px;line-height:1.95;overflow-wrap:anywhere;">'+inline(take(j))+'</p>' for j in range(i+1,end))
 return sec(plain(head,'font-family:'+MONO+';font-size:12px;color:#22505A;line-height:1.8;')+content,'padding:19px 17px;margin:0 22px 26px;background:#EAF2F2;border-left:4px solid '+AQUA+';')

def rows(titleidx,start,count,step=3,metric=False):
 title=take(titleidx);cells=[]
 for x in range(count):
  j=start+x*step;a,b,c=take(j),take(j+1),take(j+2)
  if metric:
   cell=plain(a,'font-family:'+MONO+';font-size:41px;line-height:1.1;font-weight:400;letter-spacing:-3px;color:'+TEXTORANGE+';')+plain(b,'font-size:14px;line-height:1.7;color:#493B34;margin-top:12px;overflow-wrap:anywhere;')+plain(c,'font-size:11px;line-height:1.85;color:#746356;margin-top:10px;overflow-wrap:anywhere;')
   cells.append(sec(cell,'width:50%;padding:22px 14px;border-top:1px solid #DABDAE;'+('border-right:1px solid #DABDAE;' if x%2==0 else '')+'background:'+(PAPER if x%3 else '#EAF2F2')+';'))
  else:
   cell=sec(plain(a,'font-family:'+MONO+';font-size:13px;line-height:1.8;color:'+TEXTORANGE+';'),'width:65px;flex-shrink:0;padding:17px 6px 17px 0;')+sec(plain(b,'font-size:17px;font-weight:400;line-height:1.5;color:'+TEXTORANGE+';overflow-wrap:anywhere;')+plain(c,'font-size:12px;line-height:1.85;color:#66564D;margin-top:8px;overflow-wrap:anywhere;'),'flex:1;min-width:0;padding:17px 0 17px 10px;')
   cells.append(sec(cell,'display:flex;border-top:1px solid #DABDAE;'))
 return sec(plain(title,'font-family:'+MONO+';font-size:17px;color:'+TEXTORANGE+';font-weight:400;margin:0 0 18px;line-height:1.7;')+sec(''.join(cells),'display:flex;flex-wrap:wrap;' if metric else ''),'margin:28px 22px;border-bottom:1px solid #DABDAE;')

WRAPPER='max-width:600px;margin:0 auto;background:#FAF8F4;font-family:' + FONT + ';color:' + INK + ';padding-top:6px;padding-bottom:1px;'

def flow(items):
 content=''
 for k,t in enumerate(items):
  number=str(k+1).zfill(2)
  left=sec(plain(number,'font-family:'+MONO+';font-size:24px;line-height:1.1;letter-spacing:-2px;color:#173F48;')+plain('↗','font-family:'+MONO+';font-size:24px;line-height:1.4;color:#173F48;margin-top:20px;'),'width:54px;flex-shrink:0;padding:22px 10px;background:'+AQUA+';')
  right=sec(plain(t,'font-size:14px;line-height:1.95;color:'+INK+';overflow-wrap:anywhere;'),'flex:1;min-width:0;padding:22px 15px;background:'+PAPER+';')
  content+=sec(left+right,'display:flex;border-top:1px solid #B9CECC;')
 return sec(content,'margin:28px 22px;border-bottom:1px solid #B9CECC;')
