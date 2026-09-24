# 使用与分享

本包包含完整可编辑源码。许可和作者信息见 [NOTICE.md](NOTICE.md)，完整条款见 [LICENSE](LICENSE)。

## 安装与使用

将解压得到的 jpm-wechat-layout 文件夹放入所用 Agent 的 Skill 目录。让 Agent 读取 SKILL.md，提供文章并指定主题，或说“直接排”允许自动选样式。

只运行排版脚本需要 Python 3，无需安装额外的Python库：

```bash
python3 scripts/render.py evals/fixtures/article.json --theme all --out /tmp/jpm-layout-demo
```

输出目录必须是新目录。打开其中的排版总览.html，或单主题预览页，点击“复制到公众号”后在编辑器粘贴。Word导入才需要可选的 python-docx 1.2或更新的1.x版本，要求列在 requirements-word.txt。

测试：

```bash
python3 -m unittest discover -s tests -v
```

未提供可选Word库时对应测试跳过，不影响核心排版。

## 转发本包

- 连同源码、LICENSE、NOTICE.md 和修改说明一起分享，不仅转发运行结果或删减后的文件。
- 自己继续修改时记录改动与日期，并依 AGPL-3.0 提供适用源码、版权与许可声明。
- 你可以免费分享；不要额外加“接收者只能非商用”等限制。软件许可权利以 LICENSE 为准。
- 若将修改版本作为可远程交互的网络服务提供，按 LICENSE 第13条向相应用户提供源码获取方式。

这份说明不是额外许可，也不替代 LICENSE。需要分享的是当前文件夹或对应分享版ZIP；项目的历史归档、参考截图和其他文章不属于本包。
