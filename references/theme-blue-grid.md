# 蓝调网格

主题 ID：`blue-grid`。视觉原则：蓝紫渐变、细网格、轻字重、直角分栏。

## 设计变量

```json
{
  "BLUE": "#205BA7",
  "LINE": "#CBD8E8",
  "PALE": "#EAF3FC",
  "INK": "#24384F",
  "FONT": "-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif",
  "GRAD": "linear-gradient(125deg,#191E35 0%,#224475 35%,#637FC1 70%,#C5B4D3 100%)"
}
```

## 组件示例

### 章节标题

```html
<!-- chapter1 --><section style="box-sizing:border-box;display:flex;border-top:1px solid #CBD8E8;border-bottom:1px solid #CBD8E8;margin:46px 0 26px;background:#EAF3FC;"><section style="box-sizing:border-box;width:76px;flex-shrink:0;padding:24px 12px;border-right:1px solid #CBD8E8;"><p style="margin:0;font-size:45px;line-height:1.1;font-weight:300;color:#205BA7;"><span leaf="">01</span></p></section><section style="box-sizing:border-box;flex:1;min-width:0;padding:24px 18px;"><p style="margin:0;font-size:10px;line-height:1.6;letter-spacing:1.3px;color:#205BA7;"><span leaf="">PART / SECTION</span></p><p style="margin:0;font-size:26px;line-height:1.4;font-weight:400;color:#205BA7;margin-top:8px;"><span leaf="">章节标题</span></p><p style="margin:0;font-size:11px;line-height:1.8;color:#58718F;margin-top:10px;"><span leaf="">SECTION · 章节说明</span></p></section></section>
```

### 正文强调

```html
<p style="margin:0 20px 22px;font-size:15px;line-height:1.95;letter-spacing:.15px;color:#24384F;overflow-wrap:anywhere;"><span leaf="">段落正文与</span><span style="color:#205BA7;border-bottom:1px solid #9EB8DC;padding-bottom:2px;"><span leaf="">重点短语</span></span><span leaf="">。</span></p>
```

### 引用

```html
<section style="box-sizing:border-box;margin:28px 0;padding:28px 22px;background:#EAF3FC;border-top:1px solid #CBD8E8;border-bottom:1px solid #CBD8E8;"><p style="margin:0;font-size:20px;line-height:1.8;font-weight:400;color:#205BA7;"><span leaf="">关键引语。</span></p><p style="margin:0;font-size:12px;line-height:1.9;color:#58718F;margin-top:18px;overflow-wrap:anywhere;"><span leaf="">引用来源</span></p></section>
```

### 步骤列表

```html
<section style="box-sizing:border-box;margin:24px 20px;border:1px solid #CBD8E8;border-bottom:0;"><section style="box-sizing:border-box;display:flex;border-bottom:1px solid #CBD8E8;background:#EAF3FC;"><section style="box-sizing:border-box;width:48px;flex-shrink:0;padding:20px 8px;border-right:1px solid #CBD8E8;"><p style="margin:0;font-size:24px;line-height:1.2;font-weight:300;color:#205BA7;"><span leaf="">01</span></p></section><section style="box-sizing:border-box;padding:20px 14px;flex:1;min-width:0;"><p style="margin:0;font-size:14px;line-height:1.95;color:#24384F;overflow-wrap:anywhere;"><span leaf="">第一步</span></p></section></section><section style="box-sizing:border-box;display:flex;border-bottom:1px solid #CBD8E8;background:white;"><section style="box-sizing:border-box;width:48px;flex-shrink:0;padding:20px 8px;border-right:1px solid #CBD8E8;"><p style="margin:0;font-size:24px;line-height:1.2;font-weight:300;color:#205BA7;"><span leaf="">02</span></p></section><section style="box-sizing:border-box;padding:20px 14px;flex:1;min-width:0;"><p style="margin:0;font-size:14px;line-height:1.95;color:#24384F;overflow-wrap:anywhere;"><span leaf="">第二步</span></p></section></section></section>
```

## 装配与映射

封面 → 原文导语 → 按原文顺序使用章节、正文、引用、步骤、数据和图片 → 原文结尾。没有的内容不补造。

教程重点使用步骤与说明；观点文章重点使用正文与引用；复盘重点使用指标与事实；无论题材均保持本主题色值、字重、边框和装饰语法。

所有段落/章节映射见输入契约，渲染由 `scripts/themes/blue_grid.py` 实现。封面由渲染器采用本主题配方，标题任意换行，作者与日期仅来自输入。模板有意保存已确认样式，改变外观需要另存版本。
