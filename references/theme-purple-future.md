# 黑紫未来

主题 ID：`purple-future`。视觉原则：黑紫撞色、粗标题、圆角块、星形标记。

## 设计变量

```json
{
  "BLUE": "#5120CC",
  "LINE": "#DED9E8",
  "PALE": "#F3EFFC",
  "INK": "#302B37",
  "FONT": "-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif",
  "GRAD": "linear-gradient(125deg,#191E35 0%,#224475 35%,#637FC1 70%,#C5B4D3 100%)"
}
```

## 组件示例

### 章节标题

```html
<!-- chapter1 --><section style="box-sizing:border-box;margin:56px 22px 27px;padding-top:16px;"><section style="box-sizing:border-box;display:flex;align-items:center;justify-content:space-between;"><section style="box-sizing:border-box;display:inline-block;background:#5120CC;border-radius:30px;padding:7px 13px;"><p style="margin:0;font-size:10px;line-height:1.5;font-weight:650;color:white;text-align:center;"><span leaf="">PART 01</span></p></section><section style="box-sizing:border-box;width:32px;height:32px;border:1px solid #151515;border-radius:11px;"><p style="margin:0;font-size:12px;line-height:30px;text-align:center;"><span leaf="">01</span></p></section></section><section style="box-sizing:border-box;display:flex;align-items:center;margin-top:26px;"><section style="box-sizing:border-box;flex:1;min-width:0;padding-right:12px;"><p style="margin:0;font-size:32px;line-height:1.3;font-weight:850;letter-spacing:-1px;color:#080808;"><span leaf="">章节标题</span></p><p style="margin:0;font-size:11px;line-height:1.8;color:#635B70;margin-top:13px;"><span leaf="">SECTION · 章节说明</span></p></section><section style="box-sizing:border-box;width:46px;height:46px;flex-shrink:0;padding:4px;border-radius:50%;background:#090909;"><section style="box-sizing:border-box;border:1px solid #FFFFFF;border-radius:50%;height:36px;"><p style="margin:0;font-family:Arial,sans-serif;font-size:27px;line-height:34px;color:white;text-align:center;"><span leaf="">✳</span></p></section></section></section></section>
```

### 正文强调

```html
<p style="margin:0 22px 23px;font-size:15px;line-height:1.95;letter-spacing:.1px;color:#302B37;overflow-wrap:anywhere;"><span leaf="">段落正文与</span><span style="color:#5120CC;border-bottom:1px solid #AD91EB;padding-bottom:2px;"><span leaf="">重点短语</span></span><span leaf="">。</span></p>
```

### 引用

```html
<section style="box-sizing:border-box;margin:30px 12px;padding:26px 22px;background:#F2EFF8;border-radius:22px;"><p style="margin:0;font-size:21px;line-height:1.65;font-weight:750;color:#0A0A0A;"><span leaf="">关键引语。</span></p><p style="margin:0;font-size:12px;line-height:1.9;color:#635B70;margin-top:18px;overflow-wrap:anywhere;"><span leaf="">引用来源</span></p></section>
```

### 步骤列表

```html
<section style="box-sizing:border-box;margin:26px 22px;"><section style="box-sizing:border-box;padding:23px 20px;margin-bottom:12px;border-radius:21px;background:#090909;"><section style="box-sizing:border-box;display:flex;justify-content:space-between;align-items:center;margin-bottom:18px;"><p style="margin:0;font-size:27px;font-weight:800;line-height:1;color:white;"><span leaf="">01</span></p><p style="margin:0;font-size:9px;letter-spacing:2px;line-height:1.5;color:#E0D5F5;"><span leaf="">STEP</span></p></section><p style="margin:0;font-size:14px;line-height:1.95;color:white;overflow-wrap:anywhere;"><span leaf="">第一步</span></p></section><section style="box-sizing:border-box;padding:23px 20px;margin-bottom:12px;border-radius:21px;background:#5120CC;"><section style="box-sizing:border-box;display:flex;justify-content:space-between;align-items:center;margin-bottom:18px;"><p style="margin:0;font-size:27px;font-weight:800;line-height:1;color:white;"><span leaf="">02</span></p><p style="margin:0;font-size:9px;letter-spacing:2px;line-height:1.5;color:#E0D5F5;"><span leaf="">STEP</span></p></section><p style="margin:0;font-size:14px;line-height:1.95;color:white;overflow-wrap:anywhere;"><span leaf="">第二步</span></p></section></section>
```

## 装配与映射

封面 → 原文导语 → 按原文顺序使用章节、正文、引用、步骤、数据和图片 → 原文结尾。没有的内容不补造。

教程重点使用步骤与说明；观点文章重点使用正文与引用；复盘重点使用指标与事实；无论题材均保持本主题色值、字重、边框和装饰语法。

所有段落/章节映射见输入契约，渲染由 `scripts/themes/purple_future.py` 实现。封面由渲染器采用本主题配方，标题任意换行，作者与日期仅来自输入。模板有意保存已确认样式，改变外观需要另存版本。
