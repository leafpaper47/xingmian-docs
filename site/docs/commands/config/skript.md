---
title: Skript
createTime: 2026/10/24
---

# Skript

> 版本 `2.16.1` · 指令 1 条 · api-version `1.21` · 文件 `Skript-2.16.1.jar`

用简单的英语句子编写简单的脚本，定制Minecraft的机制。

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/skript help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/skript` | Skript的主命令。键入“/skript help”以获取更多信息。 | `skript.admin` |

## 详细用法

### /skript

- **说明**：Skript的主命令。键入“/skript help”以获取更多信息。
- **用法**：`/skript help`
- **别名**：`/sk`
- **权限**：`skript.admin`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `skript.*` | — | — |
| `skript.admin` | Allows use of administrative commands and receiving notifications of new versions. | op |
| `skript.effectcommands` | Allows to use effects as commands, e.g. '!set health to 10' | — |
| `skript.reloadnotify` | Notifies when others are reloading script files. | — |
| `skript.see_runtime_errors` | Shows notifications in chat when runtime errors occur. | op |
