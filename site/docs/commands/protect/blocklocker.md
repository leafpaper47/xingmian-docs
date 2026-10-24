---
title: BlockLocker
createTime: 2026/10/24
---

# BlockLocker

> 版本 `1.14.1` · 指令 1 条 · api-version `1.20` · 文件 `blocklocker-1.14.1.jar`

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/blocklocker help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/blocklocker` | BlockLocker的管理命令。 | `blocklocker.reload` |

## 详细用法

### /blocklocker

- **说明**：BlockLocker的管理命令。
- **用法**：`/&lt;command&gt; reload`
- **别名**：`/b`、`/l`
- **权限**：`blocklocker.reload`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `blocklocker.admin` | Edit someone's protection signs, or remove the protection entirely. | op |
| `blocklocker.bypass` | Bypass someone else's protection, but don't allow destroying it. | op |
| `blocklocker.protect` | Protect containers and doors. | True |
| `blocklocker.reload` | Reload the plugin using /blocklocker reload. | op |
| `blocklocker.wilderness` | Place chests in the wilderness (outside of Towny claims) | True |
