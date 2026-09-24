# 曜黑酸柠

主题 ID：`black-lime`。视觉原则：通篇黑底、白色轻标题、酸柠渐变。

## 设计变量

```json
{
  "BLUE": "#CFFF70",
  "LINE": "#62685A",
  "PALE": "#242A1B",
  "INK": "#D7D8D3",
  "FONT": "-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif",
  "GRAD": "linear-gradient(110deg,#B0FF00 0%,#DCFA75 56%,#FFF2B2 100%)"
}
```

## 组件示例

### 章节标题

```html
<!-- chapter1 --><section style="box-sizing:border-box;padding:0 22px;margin:65px 0 34px;"><section style="box-sizing:border-box;display:flex;justify-content:space-between;align-items:center;margin-bottom:31px;"><section style="box-sizing:border-box;display:inline-block;padding:6px 12px;border-radius:25px;background-color:#C3FF32;background-image:linear-gradient(110deg,#B0FF00 0%,#DCFA75 56%,#FFF2B2 100%);"><p style="margin:0;font-size:10px;line-height:1.6;font-weight:600;color:#10120C;"><span leaf="">PART 01</span></p></section><section style="box-sizing:border-box;width:36px;height:36px;flex-shrink:0;border:1px solid #777972;border-radius:50%;"><p style="margin:0;font-family:Arial,sans-serif;font-size:18px;line-height:34px;font-weight:300;color:white;text-align:center;"><span leaf="">→</span></p></section></section><p style="margin:0;font-size:36px;line-height:1.35;font-weight:300;letter-spacing:-1.2px;color:white;"><span leaf="">章节标题</span></p><p style="margin:0;font-size:11px;line-height:1.9;color:#B8BDB0;margin-top:18px;"><span leaf="">SECTION · 章节说明</span></p></section>
```

### 正文强调

```html
<p style="margin:0 22px 24px;font-size:15px;line-height:2;letter-spacing:.1px;color:#D7D8D3;overflow-wrap:anywhere;"><span leaf="">段落正文与</span><span style="color:#D3FF76;border-bottom:1px solid #708544;padding-bottom:2px;"><span leaf="">重点短语</span></span><span leaf="">。</span></p>
```

### 引用

```html
<section style="box-sizing:border-box;margin:30px 12px;padding:28px 22px;border-radius:22px;border:1px solid #656A5D;"><p style="margin:0;font-size:23px;line-height:1.65;font-weight:350;letter-spacing:-.3px;color:white;"><span leaf="">关键引语。</span></p><p style="margin:0;font-size:12px;line-height:1.95;color:#B7BDB0;margin-top:24px;overflow-wrap:anywhere;"><span leaf="">引用来源</span></p></section>
```

### 步骤列表

```html
<section style="box-sizing:border-box;margin:28px 22px;"><section style="box-sizing:border-box;padding:23px 20px;margin-bottom:13px;border-radius:21px;background-color:#C3FF32;background-image:linear-gradient(110deg,#B0FF00 0%,#DCFA75 56%,#FFF2B2 100%);"><section style="box-sizing:border-box;display:flex;justify-content:space-between;align-items:center;margin-bottom:19px;"><p style="margin:0;font-size:28px;font-weight:350;line-height:1.3;color:#10120C;"><span leaf="">01</span></p><p style="margin:0;font-size:9px;line-height:1.6;letter-spacing:1px;color:#4C573C;"><span leaf="">STEP</span></p></section><p style="margin:0;font-size:14px;line-height:1.95;color:#10120C;overflow-wrap:anywhere;"><span leaf="">第一步</span></p></section><section style="box-sizing:border-box;padding:23px 20px;margin-bottom:13px;border-radius:21px;border:1px solid #6B7162;"><section style="box-sizing:border-box;display:flex;justify-content:space-between;align-items:center;margin-bottom:19px;"><p style="margin:0;font-size:28px;font-weight:350;line-height:1.3;color:#FFFFFF;"><span leaf="">02</span></p><p style="margin:0;font-size:9px;line-height:1.6;letter-spacing:1px;color:#AAB19F;"><span leaf="">STEP</span></p></section><p style="margin:0;font-size:14px;line-height:1.95;color:#FFFFFF;overflow-wrap:anywhere;"><span leaf="">第二步</span></p></section></section>
```

## 装配与映射

封面 → 原文导语 → 按原文顺序使用章节、正文、引用、步骤、数据和图片 → 原文结尾。没有的内容不补造。

教程重点使用步骤与说明；观点文章重点使用正文与引用；复盘重点使用指标与事实；无论题材均保持本主题色值、字重、边框和装饰语法。

所有段落/章节映射见输入契约，渲染由 `scripts/themes/black_lime.py` 实现。封面由渲染器采用本主题配方，标题任意换行，作者与日期仅来自输入。模板有意保存已确认样式，改变外观需要另存版本。
