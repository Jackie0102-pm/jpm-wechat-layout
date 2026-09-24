# 橙青映像

主题 ID：`orange-aqua`。视觉原则：橙青撞色、轻标题、错位分栏。

## 设计变量

```json
{
  "BLUE": "#F94C10",
  "LINE": "#DABDAE",
  "PALE": "#EAF2F2",
  "INK": "#443D36",
  "AQUA": "#83B1BB",
  "PAPER": "#FAF8F4",
  "TEXTORANGE": "#AD330D",
  "MONO": "'Menlo','Consolas',monospace",
  "FONT": "-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif",
  "GRAD": "linear-gradient(145deg,#83B1BB 0%,#D6977D 24%,#F94C10 53%,#F94C10 100%)"
}
```

## 组件示例

### 章节标题

```html
<!-- chapter1 --><section style="box-sizing:border-box;margin:50px 0 28px;background:#F94C10;"><section style="box-sizing:border-box;display:flex;"><section style="box-sizing:border-box;flex:1;min-width:0;padding:25px 20px;"><p style="margin:0;font-family:'Menlo','Consolas',monospace;font-size:11px;letter-spacing:-.2px;line-height:1.6;color:#491707;"><span leaf="">SECTION</span></p><p style="margin:0;font-size:30px;line-height:1.5;font-weight:350;letter-spacing:-.8px;color:#FFFFFF;margin-top:26px;"><span leaf="">章节标题</span></p></section><section style="box-sizing:border-box;width:72px;flex-shrink:0;display:flex;align-items:flex-end;justify-content:center;padding:20px 10px;border-left:1px solid rgba(255,255,255,.45);"><p style="margin:0;font-family:'Menlo','Consolas',monospace;font-size:36px;line-height:1.2;letter-spacing:-3px;color:#FFFFFF;"><span leaf="">01</span></p></section></section><p style="margin:0;font-size:11px;line-height:1.8;padding:13px 20px;color:#491707;border-top:1px solid rgba(255,255,255,.45);"><span leaf="">SECTION · 章节说明</span></p></section>
```

### 正文强调

```html
<p style="margin:0 22px 23px;font-size:15px;line-height:2;letter-spacing:.1px;color:#443D36;overflow-wrap:anywhere;"><span leaf="">段落正文与</span><span style="color:#AD330D;border-bottom:1px solid #E9977F;padding-bottom:2px;"><span leaf="">重点短语</span></span><span leaf="">。</span></p>
```

### 引用

```html
<section style="box-sizing:border-box;margin:30px 0 30px 22px;padding:27px 22px;background-color:#FAF8F4;background-image:repeating-linear-gradient(0deg,rgba(226,118,71,.06) 0px,rgba(226,118,71,.06) 3px,transparent 3px,transparent 9px);border-top:1px solid #D8B7A8;border-bottom:1px solid #D8B7A8;"><p style="margin:0;font-family:'Menlo','Consolas',monospace;font-size:30px;line-height:1;color:#AD330D;margin-bottom:18px;"><span leaf="">↗</span></p><p style="margin:0;font-size:23px;line-height:1.65;font-weight:400;letter-spacing:-.3px;color:#AD330D;"><span leaf="">关键引语。</span></p><p style="margin:0;font-size:12px;line-height:1.9;color:#784632;margin-top:22px;overflow-wrap:anywhere;"><span leaf="">引用来源</span></p></section>
```

### 步骤列表

```html
<section style="box-sizing:border-box;margin:28px 22px;border-bottom:1px solid #B9CECC;"><section style="box-sizing:border-box;display:flex;border-top:1px solid #B9CECC;"><section style="box-sizing:border-box;width:54px;flex-shrink:0;padding:22px 10px;background:#83B1BB;"><p style="margin:0;font-family:'Menlo','Consolas',monospace;font-size:24px;line-height:1.1;letter-spacing:-2px;color:#173F48;"><span leaf="">01</span></p><p style="margin:0;font-family:'Menlo','Consolas',monospace;font-size:24px;line-height:1.4;color:#173F48;margin-top:20px;"><span leaf="">↗</span></p></section><section style="box-sizing:border-box;flex:1;min-width:0;padding:22px 15px;background:#FAF8F4;"><p style="margin:0;font-size:14px;line-height:1.95;color:#443D36;overflow-wrap:anywhere;"><span leaf="">第一步</span></p></section></section><section style="box-sizing:border-box;display:flex;border-top:1px solid #B9CECC;"><section style="box-sizing:border-box;width:54px;flex-shrink:0;padding:22px 10px;background:#83B1BB;"><p style="margin:0;font-family:'Menlo','Consolas',monospace;font-size:24px;line-height:1.1;letter-spacing:-2px;color:#173F48;"><span leaf="">02</span></p><p style="margin:0;font-family:'Menlo','Consolas',monospace;font-size:24px;line-height:1.4;color:#173F48;margin-top:20px;"><span leaf="">↗</span></p></section><section style="box-sizing:border-box;flex:1;min-width:0;padding:22px 15px;background:#FAF8F4;"><p style="margin:0;font-size:14px;line-height:1.95;color:#443D36;overflow-wrap:anywhere;"><span leaf="">第二步</span></p></section></section></section>
```

## 装配与映射

封面 → 原文导语 → 按原文顺序使用章节、正文、引用、步骤、数据和图片 → 原文结尾。没有的内容不补造。

教程重点使用步骤与说明；观点文章重点使用正文与引用；复盘重点使用指标与事实；无论题材均保持本主题色值、字重、边框和装饰语法。

所有段落/章节映射见输入契约，渲染由 `scripts/themes/orange_aqua.py` 实现。封面由渲染器采用本主题配方，标题任意换行，作者与日期仅来自输入。模板有意保存已确认样式，改变外观需要另存版本。
