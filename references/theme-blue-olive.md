# 雾蓝橄榄

主题 ID：`blue-olive`。视觉原则：米白与炭黑交替、雾蓝标题、橄榄编号。

## 设计变量

```json
{
  "INK": "#2F3538",
  "BLUE": "#3E659A",
  "OLIVE": "#979437",
  "DARK": "#151515",
  "PAPER": "#F7F6F0",
  "PALE": "#EBEBDD",
  "LINE": "#D9DDCF",
  "MUTED": "#656F72",
  "GOLD": "#979437",
  "FONT": "-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif",
  "SERIF": "-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif",
  "ROUND": "-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif",
  "LIGHTWAVE": "background-color:#F7F6F0;background-image:radial-gradient(ellipse at 120% 78%,transparent 35%,#DCDDAB 47%,#E7E8CC 58%,transparent 69%);",
  "DARKWAVE": "background-color:#151515;background-image:radial-gradient(ellipse at 115% 87%,transparent 37%,#30312C 48%,#272923 58%,transparent 68%);"
}
```

## 组件示例

### 章节标题

```html
<!-- chapter1 --><section style="box-sizing:border-box;margin:51px 0 33px;padding:24px;background-color:#151515;background-image:radial-gradient(ellipse at 115% 87%,transparent 37%,#30312C 48%,#272923 58%,transparent 68%);"><section style="box-sizing:border-box;display:flex;justify-content:space-between;align-items:center;"><p style="margin:0;font-size:10px;line-height:1.8;color:#E8E8E1;"><span style="color:#979437;font-size:17px;margin-right:7px;"><span leaf="">✳</span></span><span leaf=""></span></p><p style="margin:0;font-size:12px;line-height:1.8;font-weight:600;color:#979437;"><span leaf="">01</span></p></section><section style="box-sizing:border-box;margin-top:55px;text-align:right;"><p style="margin:0;font-size:24px;font-weight:400;line-height:1.04;letter-spacing:-.8px;white-space:pre-line;color:#F1F1EA;"><span leaf="">SECTION</span></p><p style="margin:0;font-size:22px;line-height:1.6;font-weight:400;color:#F1F1EA;margin-top:15px;"><span leaf="">章节标题</span></p></section><p style="margin:0;font-size:11px;line-height:1.9;color:#C5C6BC;margin-top:24px;"><span leaf="">SECTION · 章节说明</span></p></section>
```

### 正文强调

```html
<p style="margin:0 24px 26px;font-family:-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif;font-size:16px;line-height:1.95;color:#2F3538;overflow-wrap:anywhere;"><span leaf="">段落正文与</span><span style="color:#3E659A;font-weight:600;border-bottom:1px solid #979437;padding-bottom:2px;"><span leaf="">重点短语</span></span><span leaf="">。</span></p>
```

### 引用

```html
<section style="box-sizing:border-box;margin:34px 0;padding:30px 24px;background-color:#F7F6F0;background-image:radial-gradient(ellipse at 120% 78%,transparent 35%,#DCDDAB 47%,#E7E8CC 58%,transparent 69%);"><p style="margin:0;font-size:22px;line-height:1;color:#979437;margin-bottom:26px;"><span leaf="">✳</span></p><p style="margin:0;font-size:22px;line-height:1.65;font-weight:400;color:#3E659A;"><span leaf="">关键引语。</span></p><p style="margin:0;font-size:13px;line-height:1.95;color:#656F72;margin-top:26px;overflow-wrap:anywhere;"><span leaf="">引用来源</span></p></section>
```

### 步骤列表

```html
<section style="box-sizing:border-box;margin:31px 26px 31px 24px;"><p style="margin:0;font-size:10px;line-height:1.8;color:#3E659A;"><span leaf="">从输入，到交付。</span></p><section style="box-sizing:border-box;display:flex;"><section style="box-sizing:border-box;flex:1;min-width:0;padding:23px 18px 25px 0;"><p style="margin:0;font-size:13px;line-height:1.5;font-weight:600;color:#3E659A;text-align:right;margin-bottom:12px;"><span leaf="">01</span></p><p style="margin:0;font-size:15px;line-height:1.95;color:#2F3538;overflow-wrap:anywhere;"><span leaf="">第一步</span></p></section><section style="box-sizing:border-box;width:12px;padding-top:22px;flex-shrink:0;border-right:1px solid #3E659A;"><p style="margin:0;font-size:24px;line-height:1;color:#979437;text-align:right;margin-right:-5px;"><span leaf="">▪</span></p></section></section><section style="box-sizing:border-box;display:flex;"><section style="box-sizing:border-box;flex:1;min-width:0;padding:23px 18px 25px 0;"><p style="margin:0;font-size:13px;line-height:1.5;font-weight:600;color:#3E659A;text-align:right;margin-bottom:12px;"><span leaf="">02</span></p><p style="margin:0;font-size:15px;line-height:1.95;color:#2F3538;overflow-wrap:anywhere;"><span leaf="">第二步</span></p></section><section style="box-sizing:border-box;width:12px;padding-top:22px;flex-shrink:0;border-right:1px solid #3E659A;"><p style="margin:0;font-size:24px;line-height:1;color:#979437;text-align:right;margin-right:-5px;"><span leaf="">▪</span></p></section></section></section>
```

## 装配与映射

封面 → 原文导语 → 按原文顺序使用章节、正文、引用、步骤、数据和图片 → 原文结尾。没有的内容不补造。

教程重点使用步骤与说明；观点文章重点使用正文与引用；复盘重点使用指标与事实；无论题材均保持本主题色值、字重、边框和装饰语法。

所有段落/章节映射见输入契约，渲染由 `scripts/themes/blue_olive.py` 实现。封面由渲染器采用本主题配方，标题任意换行，作者与日期仅来自输入。模板有意保存已确认样式，改变外观需要另存版本。
