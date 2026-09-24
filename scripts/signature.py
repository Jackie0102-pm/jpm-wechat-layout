# SPDX-License-Identifier: AGPL-3.0-only
"""Compact theme-aware author footer. Unknown identity remains editable display text."""
def signature(c,b):
 m=c.m;key=getattr(c,'theme','neon-notes' if c.neon else 'blue-grid')
 palettes={'blue-grid':('#205BA7','#EAF3FC','#24384F','#58718F','#CBD8E8'),'purple-future':('#5120CC','#F3EFFC','#302B37','#635B70','#DED9E8'),'orange-aqua':('#AD330D','#EAF2F2','#443D36','#66564D','#DABDAE'),'neon-notes':('#123B20','#E7FF6B','#123B20','#41644A','#DCE9CE'),'black-lime':('#CFFF70','#242A1B','#F3F4EF','#B7BDB0','#62685A'),'retro-record':('#344E88','#F5D48A','#34384B','#665335','#B59763'),'gray-portfolio':('#2C2A29','#F0F0ED','#2C2A29','#74716E','#DDDCD9'),'blue-olive':('#3E659A','#EBEBDD','#2F3538','#656F72','#D9DDCF')}
 accent,pale,ink,muted,line=palettes[key]
 badge=c.box(c.p('✦','font-size:21px;line-height:42px;text-align:center;color:'+accent+';'),'width:42px;height:42px;flex-shrink:0;background:'+pale+';border-radius:'+('4' if key in ['blue-grid','gray-portfolio','retro-record'] else '12')+'px;')
 identity=c.box(c.p(b['name'],'font-size:15px;line-height:1.6;font-weight:650;color:'+ink+';')+(c.p(b['bio'],'font-size:12px;line-height:1.75;color:'+muted+';margin-top:4px;') if b.get('bio') else ''),'flex:1;min-width:0;padding-left:14px;')
 row=c.box(badge+identity,'display:flex;align-items:center;')
 cta=c.p(b['cta'],'font-size:12px;line-height:1.85;color:'+muted+';margin-top:16px;') if b.get('cta') else ''
 return c.box(row+cta,'margin:28px 24px 0;padding:20px 0 26px;border-top:1px solid '+line+';')
