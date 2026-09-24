# 复古唱片

主题 ID：`retro-record`。视觉原则：黄红蓝、圆润标题、衬线正文、唱片装饰。

## 设计变量

```json
{
  "BLUE": "#344E88",
  "LINE": "#B59763",
  "PALE": "#F5D48A",
  "INK": "#34384B",
  "NAVY": "#344E88",
  "RED": "#C93630",
  "GOLD": "#EDB234",
  "CREAM": "#FFF0CD",
  "ROUND": "'Arial Rounded MT Bold','Yuanti SC','PingFang SC',sans-serif",
  "SERIF": "'Songti SC','STSong','Noto Serif CJK SC',serif",
  "FONT": "-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif",
  "GRAD": "linear-gradient(125deg,#191E35 0%,#224475 35%,#637FC1 70%,#C5B4D3 100%)"
}
```

## 组件示例

### 章节标题

```html
<!-- chapter1 --><section style="box-sizing:border-box;margin:48px 12px 30px;border:2px solid #344E88;"><section style="box-sizing:border-box;display:flex;background:#344E88;"><section style="box-sizing:border-box;padding:26px 18px;flex:1;min-width:0;"><p style="margin:0;font-size:10px;line-height:1.8;letter-spacing:1px;color:#FFF0CD;"><span leaf="">CHAPTER 01</span></p><p style="margin:0;font-family:'Arial Rounded MT Bold','Yuanti SC','PingFang SC',sans-serif;font-size:29px;line-height:1.5;font-weight:850;color:#EDB234;margin-top:18px;"><span leaf="">章节标题</span></p><p style="margin:0;font-size:11px;line-height:1.85;color:#FFF0CD;margin-top:14px;"><span leaf="">SECTION · 章节说明</span></p></section><section style="box-sizing:border-box;width:62px;flex-shrink:0;padding:24px 10px;background:#C93630;"><section style="box-sizing:border-box;width:40px;height:40px;border-radius:50%;flex-shrink:0;border:1px solid #CFAB65;display:flex;align-items:center;justify-content:center;background-color:#263A67;background-image:repeating-radial-gradient(circle,#263A67 0px,#263A67 3px,#425889 4px,#263A67 5px);"><section style="box-sizing:border-box;width:13px;height:13px;border-radius:50%;background:#EDB234;display:flex;align-items:center;justify-content:center;"><p style="margin:0;font-size:10px;line-height:1;text-align:center;color:#344E88;"><span leaf="">●</span></p></section></section><p style="margin:0;font-family:'Arial Rounded MT Bold','Yuanti SC','PingFang SC',sans-serif;font-size:24px;font-weight:850;line-height:1;color:#EDB234;margin-top:20px;text-align:center;"><span leaf="">01</span></p></section></section><section style="box-sizing:border-box;height:10px;background-color:#EDB234;"></section></section>
```

### 正文强调

```html
<p style="margin:0 22px 24px;font-family:'Songti SC','STSong','Noto Serif CJK SC',serif;font-size:16px;line-height:2;letter-spacing:.15px;color:#34384B;overflow-wrap:anywhere;"><span leaf="">段落正文与</span><span style="color:#A12C28;font-weight:650;border-bottom:1px solid #C76F43;padding-bottom:2px;"><span leaf="">重点短语</span></span><span leaf="">。</span></p>
```

### 引用

```html
<section style="box-sizing:border-box;margin:30px 17px 32px;padding:26px 20px;border:2px solid #344E88;background:#F3C65F;box-shadow:5px 5px 0 #C93630;"><p style="margin:0;font-family:Georgia,serif;font-size:46px;line-height:.8;color:#C93630;margin-bottom:12px;"><span leaf="">“</span></p><p style="margin:0;font-family:'Arial Rounded MT Bold','Yuanti SC','PingFang SC',sans-serif;font-size:22px;line-height:1.7;font-weight:750;color:#344E88;"><span leaf="">关键引语。</span></p><p style="margin:0;font-family:'Songti SC','STSong','Noto Serif CJK SC',serif;font-size:13px;line-height:1.95;color:#4D422E;margin-top:20px;overflow-wrap:anywhere;"><span leaf="">引用来源</span></p></section>
```

### 步骤列表

```html
<section style="box-sizing:border-box;margin:28px 17px;border:2px solid #344E88;"><section style="box-sizing:border-box;padding:17px;background:#EDB234;"><section style="box-sizing:border-box;display:inline-block;padding:6px 11px;background:#344E88;"><p style="margin:0;font-family:'Arial Rounded MT Bold','Yuanti SC','PingFang SC',sans-serif;font-size:10px;line-height:1.7;font-weight:800;letter-spacing:.3px;color:#EDB234;"><span leaf="">SIDE A / WORKFLOW</span></p></section></section><section style="box-sizing:border-box;display:flex;border-top:1px solid #C7A570;"><section style="box-sizing:border-box;width:57px;flex-shrink:0;padding:23px 10px;background:#E9BB55;"><section style="box-sizing:border-box;width:36px;height:36px;border-radius:50%;border:1px solid #EDB234;background:#344E88;"><p style="margin:0;font-family:'Arial Rounded MT Bold','Yuanti SC','PingFang SC',sans-serif;font-size:15px;font-weight:850;line-height:34px;text-align:center;color:#EDB234;"><span leaf="">01</span></p></section></section><section style="box-sizing:border-box;flex:1;min-width:0;padding:22px 15px;background:#FFF0CD;"><p style="margin:0;font-family:'Songti SC','STSong','Noto Serif CJK SC',serif;font-size:15px;line-height:1.95;color:#34384B;overflow-wrap:anywhere;"><span leaf="">第一步</span></p></section></section><section style="box-sizing:border-box;display:flex;border-top:1px solid #C7A570;"><section style="box-sizing:border-box;width:57px;flex-shrink:0;padding:23px 10px;background:#E9BB55;"><section style="box-sizing:border-box;width:36px;height:36px;border-radius:50%;border:1px solid #EDB234;background:#344E88;"><p style="margin:0;font-family:'Arial Rounded MT Bold','Yuanti SC','PingFang SC',sans-serif;font-size:15px;font-weight:850;line-height:34px;text-align:center;color:#EDB234;"><span leaf="">02</span></p></section></section><section style="box-sizing:border-box;flex:1;min-width:0;padding:22px 15px;background:#FFF0CD;"><p style="margin:0;font-family:'Songti SC','STSong','Noto Serif CJK SC',serif;font-size:15px;line-height:1.95;color:#34384B;overflow-wrap:anywhere;"><span leaf="">第二步</span></p></section></section></section>
```

## 装配与映射

封面 → 原文导语 → 按原文顺序使用章节、正文、引用、步骤、数据和图片 → 原文结尾。没有的内容不补造。

教程重点使用步骤与说明；观点文章重点使用正文与引用；复盘重点使用指标与事实；无论题材均保持本主题色值、字重、边框和装饰语法。

所有段落/章节映射见输入契约，渲染由 `scripts/themes/retro_record.py` 实现。封面由渲染器采用本主题配方，标题任意换行，作者与日期仅来自输入。模板有意保存已确认样式，改变外观需要另存版本。
