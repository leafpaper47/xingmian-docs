---
title: 使用说明与维护
createTime: 2026/10/24
---

# 使用说明与维护

## 数据从哪来

- 通过 SFTP 以只读方式扫描服务器 `plugins/*.jar`（共 125 个 jar），直接读取每个 jar 内的 `plugin.yml` / `paper-plugin.yml`，解析出 `commands`（指令名、说明、用法、别名、权限节点）与 `permissions`。
- 只有 `plugin.yml` 里声明过的指令才会出现在本手册。**少数插件把指令写在代码里（如 FAWE/WorldEdit 的 `//` 系列、部分自研插件的子指令）不会出现**，这类以游戏内 `help` 为准。
- `plugin.yml` 的 `usage` 字段质量参差不齐：写得详细的插件（如自研 RPG、Residence）会列出完整子指令；写得敷衍的（如 CoreProtect 只写 `<params>`）只有主指令格式。文档没有编造用法。

## 怎么更新

服务器装了新插件、或插件升级后指令有变，按三步重跑：

```bash
python wcdoc/zipyml.py          # 重新从服务器拉取并解析 plugin.yml
python wcdoc/gen_docs.py        # 重新生成所有页面与侧边栏
cd wcdoc/site && npm run build  # 重新构建静态站
```

数据源文件：`wcdoc/data/plugin_commands.json`（原始解析结果，可直接用编辑器或 jq 查）。

## 本地预览

```bash
cd wcdoc/site
npm run dev     # http://localhost:8088
```

## 已知限制

- **只看 `plugin.yml`**：靠代码动态注册的指令（Skript 脚本自定义命令、DeluxeMenus 菜单指令、MythicMobs 技能内嵌命令等）不会出现在文档里。
- **子指令不展开**：`/lp`、`/co`、`/mm` 这类主指令下面有几十个子指令，文档只给主指令，具体请用该指令的 `help`。
- **权限默认值以插件声明为准**：部分插件不写 `default`，文档显示 “—”，实际生效值取决于 LuckPerms 的分组配置。
- **颜色码已去除**：`§x` 段落颜色码在生成时清理，避免复制到游戏里出现乱码。
- **别名不是 100% 唯一**：不同插件可能声明同名别名，实际生效的取决于服务器加载顺序。

## 发布注意

`site/docs/.vuepress/dist/` 是完整静态站，可直接丢到任意静态托管或 Nginx。**但它包含服务器权限节点结构，属于内部资料**，建议只在内网或加密码保护后发布，不要公开索引。
