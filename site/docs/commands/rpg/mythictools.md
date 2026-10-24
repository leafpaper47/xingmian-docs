---
title: MythicTools
createTime: 2026/10/24
---

# MythicTools

> 版本 `1.0.4` · 指令 1 条 · api-version `1.20` · 文件 `MythicTools-1.0.4.jar`

MythicMobs 掉落、刷怪与 Boss 管理工具

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/mythictools help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/mythictools` | MythicTools 主命令 | `mythictools.command` |

## 详细用法

### /mythictools

- **说明**：MythicTools 主命令
- **用法**：`/&lt;command&gt; [gui|reload|info|boss|spawnpoint]`
- **别名**：`/mt`、`/mtools`
- **权限**：`mythictools.command`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `mythictools.*` | MythicTools 所有权限 | op |
| `mythictools.admin` | 打开并编辑管理 GUI | op |
| `mythictools.command` | 使用 MythicTools 基础命令 | True |
| `mythictools.reload` | 重载 MythicTools | op |
