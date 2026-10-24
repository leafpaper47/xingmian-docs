---
title: DeluxeMenus
createTime: 2026/10/24
---

# DeluxeMenus

> 版本 `1.14.1-Release` · 指令 1 条 · api-version `1.13` · 文件 `DeluxeMenus-1.14.1-Release.jar`

All in one inventory menu system

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/deluxemenus help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/deluxemenus` | DeluxeMenus main commands | — |

## 详细用法

### /deluxemenus

- **说明**：DeluxeMenus main commands
- **别名**：`/dm`、`/deluxemenu`、`/dmenu`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `deluxemenus.admin` | admin commands | op |
| `deluxemenus.menu.*` | permission for all menus | op |
| `deluxemenus.open` | open a menu with /dm open &lt;menu&gt; | op |
| `deluxemenus.open.bypass` | attempt to open a menu for a viewer skipping view requirement checking for the player | op |
| `deluxemenus.open.others` | open a menu with /dm open &lt;menu&gt; &lt;player&gt; | op |
| `deluxemenus.openrequirement.bypass.*` | Allows the viewer to bypass all menu open requirements | op |
| `deluxemenus.placeholdersfor` | permission to parse menu placeholders with /dm open &lt;menu&gt; p:&lt;player&gt; | op |
| `deluxemenus.placeholdersfor.exempt` | exempt from placeholders being parsed when targeted with /dm open &lt;menu p:&lt;player&gt; for players with this permission | op |
