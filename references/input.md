# 输入契约

渲染器仅依赖 Python 标准库。支持 Markdown 的一级标题、二级章节、三级至六级小标题、段落、粗体、行内代码、链接、整行图片、平铺列表、引用、代码围栏、简单表格。嵌套列表、多段图片混排、脚注等复杂语法由 Agent 无损转为 JSON，或说明尚未支持的部分，不能直接漏掉。

article.json 顶层：`title`（必填）、`author`、`date`、`series`、`subtitle`、`kicker`（可选）、`blocks`（非空数组）。封面不填未知作者、日期；末尾 signature 按 SKILL.md 显示“作者姓名 / 一句话介绍自己”占位，不显示双大括号，不虚构身份。

内容块：

| type | 字段 | 说明 |
|---|---|---|
| paragraph | text | 保留正文，可含粗体、链接、行内代码 |
| chapter | text, label?, subtitle? | 顺序自动编号；label 应匹配章节，不继承旧案例英文 |
| heading | text | 小标题 |
| quote | text, attribution?, emphasis? | 引语与来源，不虚构署名 |
| note | title?, items:字符串数组 | 提示或补充说明 |
| list | items:字符串数组 | 普通平铺列表 |
| steps | items:字符串数组 | 按主题呈现流程，可任意步数 |
| metrics | title?, items | 每项 value、label、detail 均为字符串，数据必须来自原文 |
| image | src, alt?, caption? | HTTP(S) 或实际本地路径；本地相对路径以输入文件目录为准 |
| code | text, language? | 原样保留换行与字符 |
| table | headers, rows, title? | 行宽必须与表头一致；移动版展开成标记字段，保留所有单元格 |
| divider | 无 | 仅分隔，不增加文字 |

可运行最小例：

```json
{"title":"一次工作复盘","blocks":[{"type":"paragraph","text":"先记录**实际发生的事情**。"},{"type":"chapter","text":"下一次如何改进","label":"NEXT"},{"type":"steps","items":["记录事实","验证改动"]}]}
```

本地图片复制到新输出目录，不依赖原文件长期存在。网络图片保留链接，不自动上传。无图版记录移除的来源。基础解析将 HTML 当文字；正式语义整理须识别<u> 下划线并转为 ++，代码内保持原样；恶意协议链接被拒绝。

正式生成使用 `--source 原稿.md` 或已人工核对的 source.json。附加字段声明见 [文字保真规则](content-preservation.md)。基础解析不保证复杂Markdown、Word、PDF导入完整。

## 产物

- `article.json`：本次语义化正文，供比对和再次渲染。
- `<theme-id>-正文.html`：可复制的干净正文。
- `<theme-id>-预览.html`：章节定位和复制按钮。
- `排版总览.html`：所有本次选定主题的切换预览。
- `文字核对.json`：原稿对比、允许的附加、逐主题字段核对及模板装饰清单。
- `检查记录.json`：主题、移除图片和静态校验记录。浏览器及内容检查由执行者另行记录真实结果。

Markdown 解析只是基础工具。用户“排版”不等于授权改写；复杂语法或不确定的表格归属应先用已有上下文判断，确实影响内容时只追问关键缺口。
