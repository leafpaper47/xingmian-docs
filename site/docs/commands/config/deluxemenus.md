---
title: DeluxeMenus
createTime: 2026/10/24
---

# DeluxeMenus

> 版本 `1.14.1-Release` · 指令 1 条 · api-version `1.13` · 文件 `DeluxeMenus-1.14.1-Release.jar`

一体化库存菜单系统

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/deluxemenus help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/deluxemenus` | DeluxeMenus主命令 | — |

## 详细用法

### /deluxemenus

- **说明**：DeluxeMenus主命令
- **别名**：`/dm`、`/deluxemenu`、`/dmenu`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `deluxemenus.admin` | 管理员指令 | op |
| `deluxemenus.menu.*` | 所有菜单的权限 | op |
| `deluxemenus.open` | 打开菜单，打开/dm &lt;menu&gt; | op |
| `deluxemenus.open.bypass` | 尝试为观众打开菜单，跳过播放器的观看要求检查 | op |
| `deluxemenus.open.others` | 打开菜单，打开/dm &lt;menu&gt; &lt;player&gt; | op |
| `deluxemenus.openrequirement.bypass.*` | 允许查看器绕过所有菜单打开要求 | op |
| `deluxemenus.placeholdersfor` | /dm open &lt;menu&gt; p解析菜单占位符的权限：&lt;player&gt; | op |
| `deluxemenus.placeholdersfor.exempt` | 当/dm为具有&lt;menu p:&lt;player&gt;此权限的玩家打开时，免于解析占位符 | op |
