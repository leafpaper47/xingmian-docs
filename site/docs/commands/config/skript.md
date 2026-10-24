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
| `skript.admin` | 允许使用管理命令并接收新版本的通知。 | op |
| `skript.effectcommands` | 允许将效果用作命令，例如“! set health to 10” | — |
| `skript.reloadnotify` | 当其他人正在重新加载脚本文件时通知。 | — |
| `skript.see_runtime_errors` | 发生运行时错误时在聊天中显示通知。 | op |
