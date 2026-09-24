# JPM 八套公众号排版

将已有文章排成八套固定视觉主题，生成可切换的预览页与可复制到公众号编辑器的正文。

**当前为 v0.2.0 测试版。** 欢迎试用并反馈问题；HTML结构检查不等同于微信编辑器兼容性保证。

## 来源与许可

本项目基于 [gzh-design-skill](https://github.com/isjiamu/gzh-design-skill) 修改与扩展。
原作者：**Copyright © 2026 甲木 × 摸鱼小李**。

本版本增加八套主题、语义组件、同文切换预览及包内检查，并替换了已识别的早期复用脚本。它可以独立运行；开发来源与修改历史仍予以保留。原作者不为本修改版本背书。

按 **AGPL-3.0-only** 提供完整源码。参见 [LICENSE](LICENSE)、[版权与来源](NOTICE.md)、[修改记录](CHANGES.md) 和 [分享说明](SHARING.md)。参考截图、其中的摄影素材及他人文章不在本仓库中；本许可不授予第三方作品的权利。

## 默认保留原文

不润色、不缩写、不补标题/导读/总结，不自动修改标点。AI仍可判断强调位置、选择步骤/引用/对比组件，调整字号与留白。章节编号与英文标签、固定组件标签、作者区和默认互动句作为附加单独记录。

作者占位显示为“作者姓名 / 一句话介绍自己”，使用紧凑署名样式，不显示双大括号。可要求不加作者区或互动句。

正式JSON排版须提供原稿：

```bash
python3 scripts/render.py article.json --source 原稿.md --theme all --out output
```

原稿与语义稿文字不一致会停止；各主题渲染后再逐块核对，并输出 `文字核对.json`。普通正文排版空白和强调标记不参与文字差异，标点、数字和顺序参与；代码块与行内代码另行核对。Word/PDF/复杂Markdown需先人工无损整理为source.json，不能把中间稿核对通过理解为原文件导入完整。

仅试样式可用 `--allow-unverified`，报告明确标记未核对原稿。它不能替代正式交付检查。详见 [文字保真规则](references/content-preservation.md)。

## 八套主题

| 编号 | 主题 | ID |
|---|---|---|
| 1 | 蓝调网格 | `blue-grid` |
| 2 | 黑紫未来 | `purple-future` |
| 3 | 橙青映像 | `orange-aqua` |
| 4 | 荧光便签 | `neon-notes` |
| 5 | 曜黑酸柠 | `black-lime` |
| 6 | 复古唱片 | `retro-record` |
| 7 | 灰阶作品集 | `gray-portfolio` |
| 8 | 雾蓝橄榄 | `blue-olive` |

## 作为 Skill 使用

下载仓库源码，或克隆：

```bash
git clone https://github.com/Jackie0102-pm/jpm-wechat-layout.git
```

把 `jpm-wechat-layout` 文件夹放入所用 Agent 的 Skill 目录，按宿主要求重新加载。让 Agent 读取 [SKILL.md](SKILL.md)，然后提供文章。例如：

> 使用 $jpm-wechat-layout，把这篇文章用雾蓝橄榄排版。

> 使用 $jpm-wechat-layout，同一篇文章生成八套，我切换着看。

支持已有文章、Markdown与纯文本；复杂内容由 Agent 按 [输入契约](references/input.md) 整理成 JSON。Word可用可选导入器。

## 不通过 Agent，直接测试

核心排版只需 Python 3，使用标准库，无需安装额外 Python 库。在仓库根目录运行：

```bash
python3 scripts/render.py evals/fixtures/article.json --source evals/fixtures/article.json --theme all --out demo-output
```

`demo-output` 必须是新目录。打开其中的 `排版总览.html` 切换主题；进入单主题预览，点击“复制到公众号”，在公众号编辑器粘贴并检查。单主题可把 `all` 换成主题 ID。

Word 导入另需可选依赖：

```bash
python3 -m pip install -r requirements-word.txt
python3 scripts/read_word.py 你的文章.docx --out word-review
```

Word结果是供核对的中间材料，需要再整理为排版输入。

## 测试与反馈

```bash
python3 -m unittest discover -s tests -v
```

缺少可选 Word 库时相应测试会跳过。已有结构、正文、图片及预览检查；曾收到用户粘贴可用的反馈，但没有完成八套主题在所有微信客户端上的测试。粘贴后请重点核对图片、表格、深色背景和换行；浏览器预览中的主题切换按钮不会进入正文。

可在 [Issues](https://github.com/Jackie0102-pm/jpm-wechat-layout/issues) 提供主题、复现步骤、脱敏后的最小文章及预览/粘贴效果差异。请勿提交客户资料或登录凭证。

## 目录

- `scripts/`：渲染、正文检查、Word读取和主题实现。
- `assets/`：预览与总览模板、主题清单。
- `references/`：组件、输入和主题规则。
- `evals/fixtures/`：可直接运行的测试文章和自制测试图片。
- `tests/`：自动化检查。

软件按现状提供，详细许可、担保排除与分享要求见随附文件。
