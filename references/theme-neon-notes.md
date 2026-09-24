# 荧光便签

主题 ID：`neon-notes`。视觉原则：奶油方格、绿色粗框、黄粉便签。

## 设计变量

```json
{
  "BLUE": "#236336",
  "LINE": "#DCE8CC",
  "PALE": "#EDF6E6",
  "INK": "#123B20",
  "GREEN": "#2DCC59",
  "LIME": "#E7FF6B",
  "PINK": "#F58AE3",
  "CREAM": "#F8FAED",
  "MONO": "'Menlo','Consolas',monospace",
  "GRID": "background-color:#F8FAED;background-image:linear-gradient(#E9EED5 1px,transparent 1px),linear-gradient(90deg,#E9EED5 1px,transparent 1px);background-size:24px 24px;",
  "FONT": "-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Microsoft YaHei',sans-serif",
  "GRAD": "linear-gradient(125deg,#191E35 0%,#224475 35%,#637FC1 70%,#C5B4D3 100%)"
}
```

## 组件示例

### 章节标题

```html
<!-- chapter1 --><section style="box-sizing:border-box;padding:28px 12px;margin:40px 0 26px;background-color:#F8FAED;background-image:linear-gradient(#E9EED5 1px,transparent 1px),linear-gradient(90deg,#E9EED5 1px,transparent 1px);background-size:24px 24px;"><section style="box-sizing:border-box;display:flex;align-items:flex-end;padding:0 10px;margin-bottom:-3px;"><section style="box-sizing:border-box;display:inline-block;padding:8px 11px 10px;border-radius:15px 15px 0 0;background:#F58AE3;"><p style="margin:0;font-family:'Menlo','Consolas',monospace;font-size:10px;line-height:1.7;color:#123B20;"><span leaf="">PART 01</span></p></section><section style="box-sizing:border-box;display:inline-block;padding:8px 11px 10px;border-radius:15px 15px 0 0;background:#E7FF6B;"><p style="margin:0;font-family:'Menlo','Consolas',monospace;font-size:10px;line-height:1.7;color:#123B20;"><span leaf="">SECTION</span></p></section></section><section style="box-sizing:border-box;border:9px solid #2DCC59;border-radius:25px;padding:22px 15px;background:white;"><section style="box-sizing:border-box;display:flex;align-items:flex-start;"><section style="box-sizing:border-box;flex:1;min-width:0;padding-right:10px;"><p style="margin:0;font-size:28px;line-height:1.35;font-weight:850;letter-spacing:-.8px;color:#123B20;"><span leaf="">章节标题</span></p><p style="margin:0;font-size:11px;line-height:1.9;color:#436B4E;margin-top:16px;"><span leaf="">SECTION · 章节说明</span></p></section><p style="margin:0;font-family:'Menlo','Consolas',monospace;font-size:30px;line-height:1.2;font-weight:700;color:#123B20;"><span leaf="">01</span></p></section></section></section>
```

### 正文强调

```html
<p style="margin:0 22px 23px;font-size:15px;line-height:1.95;letter-spacing:.1px;color:#123B20;overflow-wrap:anywhere;"><span leaf="">段落正文与</span><span style="color:#123B20;font-weight:600;background:linear-gradient(transparent 62%,#E7FF6B 62%);padding-bottom:1px;"><span leaf="">重点短语</span></span><span leaf="">。</span></p>
```

### 引用

```html
<section style="box-sizing:border-box;margin:28px 12px;"><section style="box-sizing:border-box;display:flex;background:#E7FF6B;border-radius:0 20px 20px 0;"><section style="box-sizing:border-box;width:28px;flex-shrink:0;display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:20px 0;"><section style="box-sizing:border-box;width:11px;height:11px;flex-shrink:0;border-radius:50%;background:#F8FAED;"></section><section style="box-sizing:border-box;width:11px;height:11px;flex-shrink:0;border-radius:50%;background:#F8FAED;"></section><section style="box-sizing:border-box;width:11px;height:11px;flex-shrink:0;border-radius:50%;background:#F8FAED;"></section><section style="box-sizing:border-box;width:11px;height:11px;flex-shrink:0;border-radius:50%;background:#F8FAED;"></section></section><section style="box-sizing:border-box;padding:22px 18px 24px 6px;flex:1;min-width:0;"><p style="margin:0;font-size:22px;line-height:1.65;font-weight:750;color:#123B20;"><span leaf="">关键引语。</span></p><p style="margin:0;font-size:12px;line-height:1.9;color:#274E33;margin-top:18px;overflow-wrap:anywhere;"><span leaf="">引用来源</span></p></section></section></section>
```

### 步骤列表

```html
<section style="box-sizing:border-box;margin:28px 12px;"><section style="box-sizing:border-box;display:flex;align-items:flex-end;padding:0 10px;margin-bottom:-3px;"><section style="box-sizing:border-box;display:inline-block;padding:8px 11px 10px;border-radius:15px 15px 0 0;background:#F58AE3;"><p style="margin:0;font-family:'Menlo','Consolas',monospace;font-size:10px;line-height:1.7;color:#123B20;"><span leaf="">WORKFLOW</span></p></section><section style="box-sizing:border-box;display:inline-block;padding:8px 11px 10px;border-radius:15px 15px 0 0;background:#E7FF6B;"><p style="margin:0;font-family:'Menlo','Consolas',monospace;font-size:10px;line-height:1.7;color:#123B20;"><span leaf="">2 STEPS</span></p></section></section><section style="box-sizing:border-box;border:7px solid #2DCC59;border-radius:24px;background:white;overflow:hidden;"><section style="box-sizing:border-box;padding:21px 18px;border-bottom:1px solid #DCE9CE;"><section style="box-sizing:border-box;display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;"><section style="box-sizing:border-box;width:39px;height:36px;border-radius:10px;background:#F58AE3;"><p style="margin:0;font-family:'Menlo','Consolas',monospace;font-size:20px;font-weight:800;line-height:36px;text-align:center;color:#123B20;"><span leaf="">01</span></p></section><p style="margin:0;font-family:'Menlo','Consolas',monospace;font-size:10px;color:#41644A;line-height:1.6;"><span leaf="">STEP →</span></p></section><p style="margin:0;font-size:14px;line-height:1.95;color:#123B20;overflow-wrap:anywhere;"><span leaf="">第一步</span></p></section><section style="box-sizing:border-box;padding:21px 18px;border-bottom:1px solid #DCE9CE;"><section style="box-sizing:border-box;display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;"><section style="box-sizing:border-box;width:39px;height:36px;border-radius:10px;background:#E7FF6B;"><p style="margin:0;font-family:'Menlo','Consolas',monospace;font-size:20px;font-weight:800;line-height:36px;text-align:center;color:#123B20;"><span leaf="">02</span></p></section><p style="margin:0;font-family:'Menlo','Consolas',monospace;font-size:10px;color:#41644A;line-height:1.6;"><span leaf="">STEP →</span></p></section><p style="margin:0;font-size:14px;line-height:1.95;color:#123B20;overflow-wrap:anywhere;"><span leaf="">第二步</span></p></section></section></section>
```

## 装配与映射

封面 → 原文导语 → 按原文顺序使用章节、正文、引用、步骤、数据和图片 → 原文结尾。没有的内容不补造。

教程重点使用步骤与说明；观点文章重点使用正文与引用；复盘重点使用指标与事实；无论题材均保持本主题色值、字重、边框和装饰语法。

所有段落/章节映射见输入契约，渲染由 `scripts/themes/neon_notes.py` 实现。封面由渲染器采用本主题配方，标题任意换行，作者与日期仅来自输入。模板有意保存已确认样式，改变外观需要另存版本。
