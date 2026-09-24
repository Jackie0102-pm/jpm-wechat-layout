# 灰阶作品集

主题 ID：`gray-portfolio`。视觉原则：黑灰双层标题、细线目录、开放分栏。

## 设计变量

```json
{
  "INK": "#2C2A29",
  "MUTED": "#858380",
  "LINE": "#DDDCD9",
  "PALE": "#F5F5F3",
  "BLUE": "#2C2A29",
  "GOLD": "#F5F5F3",
  "FONT": "-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif",
  "SERIF": "-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif",
  "ROUND": "-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif",
  "GRID": "background-color:#FCFCFB;background-image:linear-gradient(#F0F0ED 1px,transparent 1px),linear-gradient(90deg,#F0F0ED 1px,transparent 1px);background-size:24px 24px;"
}
```

## 组件示例

### 章节标题

```html
<!-- chapter1 --><section style="box-sizing:border-box;margin:55px 0 32px;border-top:1px solid #DDDCD9;border-bottom:1px solid #DDDCD9;"><section style="box-sizing:border-box;display:flex;"><section style="box-sizing:border-box;flex:1;min-width:0;padding:30px 22px;"><p style="margin:0;font-size:24px;letter-spacing:-1px;font-weight:400;line-height:1.15;color:#858380;"><span leaf="">SECTION</span></p><p style="margin:0;font-size:24px;font-weight:400;line-height:1.5;color:#2C2A29;margin-top:3px;"><span leaf="">章节标题</span></p><p style="margin:0;font-size:22px;line-height:1;color:#A09E9A;margin-top:32px;"><span leaf="">↘</span></p></section><section style="box-sizing:border-box;width:50px;padding:30px 10px;border-left:1px solid #DDDCD9;background-color:#FCFCFB;background-image:linear-gradient(#F0F0ED 1px,transparent 1px),linear-gradient(90deg,#F0F0ED 1px,transparent 1px);background-size:24px 24px;"><p style="margin:0;font-size:11px;line-height:29px;text-align:center;color:white;background:#2C2A29;width:29px;height:29px;border-radius:50%;"><span leaf="">01</span></p><p style="margin:0;font-size:20px;font-weight:300;line-height:1;color:#AAA8A4;margin-top:55px;text-align:center;"><span leaf="">+</span></p></section></section><section style="box-sizing:border-box;padding:15px 22px;border-top:1px solid #DDDCD9;"><p style="margin:0;font-size:11px;line-height:1.8;color:#74716E;"><span leaf="">SECTION · 章节说明</span></p></section></section>
```

### 正文强调

```html
<p style="margin:0 24px 25px;font-family:-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif;font-size:16px;line-height:1.95;color:#2C2A29;overflow-wrap:anywhere;"><span leaf="">段落正文与</span><span style="color:#2C2A29;font-weight:600;border-bottom:1px solid #9C9A96;padding-bottom:2px;"><span leaf="">重点短语</span></span><span leaf="">。</span></p>
```

### 引用

```html
<section style="box-sizing:border-box;margin:35px 24px;padding:28px 0;border-top:1px solid #DDDCD9;border-bottom:1px solid #DDDCD9;"><p style="margin:0;font-family:Georgia,serif;font-size:24px;line-height:1;color:#95938F;margin-bottom:14px;"><span leaf="">“</span></p><p style="margin:0;font-size:22px;line-height:1.65;font-weight:400;color:#2C2A29;"><span leaf="">关键引语。</span></p><p style="margin:0;font-size:13px;line-height:1.95;color:#76736F;margin-top:24px;overflow-wrap:anywhere;"><span leaf="">引用来源</span></p></section>
```

### 步骤列表

```html
<section style="box-sizing:border-box;margin:32px 24px;border-bottom:1px solid #DDDCD9;"><section style="box-sizing:border-box;display:flex;padding:21px 0;border-top:1px solid #DDDCD9;"><section style="box-sizing:border-box;width:42px;flex-shrink:0;"><p style="margin:0;font-size:13px;line-height:1.95;color:#858380;"><span leaf="">(01)</span></p></section><section style="box-sizing:border-box;flex:1;min-width:0;"><p style="margin:0;font-size:15px;line-height:1.95;color:#2C2A29;overflow-wrap:anywhere;"><span leaf="">第一步</span></p></section><section style="box-sizing:border-box;width:17px;text-align:right;flex-shrink:0;"><p style="margin:0;font-size:16px;line-height:1.9;color:#999792;"><span leaf="">+</span></p></section></section><section style="box-sizing:border-box;display:flex;padding:21px 0;border-top:1px solid #DDDCD9;"><section style="box-sizing:border-box;width:42px;flex-shrink:0;"><p style="margin:0;font-size:13px;line-height:1.95;color:#858380;"><span leaf="">(02)</span></p></section><section style="box-sizing:border-box;flex:1;min-width:0;"><p style="margin:0;font-size:15px;line-height:1.95;color:#2C2A29;overflow-wrap:anywhere;"><span leaf="">第二步</span></p></section><section style="box-sizing:border-box;width:17px;text-align:right;flex-shrink:0;"><p style="margin:0;font-size:16px;line-height:1.9;color:#999792;"><span leaf="">+</span></p></section></section></section>
```

## 装配与映射

封面 → 原文导语 → 按原文顺序使用章节、正文、引用、步骤、数据和图片 → 原文结尾。没有的内容不补造。

教程重点使用步骤与说明；观点文章重点使用正文与引用；复盘重点使用指标与事实；无论题材均保持本主题色值、字重、边框和装饰语法。

所有段落/章节映射见输入契约，渲染由 `scripts/themes/gray_portfolio.py` 实现。封面由渲染器采用本主题配方，标题任意换行，作者与日期仅来自输入。模板有意保存已确认样式，改变外观需要另存版本。
