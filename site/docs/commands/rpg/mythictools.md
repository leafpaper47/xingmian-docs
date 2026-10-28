---
title: MythicTools
createTime: 2026/10/24
---

# 神话工具包 · MythicTools

> 分类 ⚔️ 战斗与 RPG · 版本 `1.0.4` · 指令 1 条 · api-version `1.20`

::: tip MythicMobs 掉落与 Boss 工具
它是 MythicMobs 的配套小工具，把掉落表、刷怪点、Boss 相关的东西收拢到一个管理界面和几条主命令里，省得管理员去翻一堆 YAML。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 看版本与 Boss 列表 | /mythictools info | — |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/mythictools` | 主命令，用来打开管理界面、重载插件、查信息和看 Boss/刷怪点<br>别名 `/mt`、`/mtools` | `/mythictools [gui｜reload｜info｜boss｜spawnpoint]` | `mythictools.command` |

## 指令详解

### `/mythictools` — 主命令，用来打开管理界面、重载插件、查信息和看 Boss/刷怪点

- **语法**：`/mythictools [gui｜reload｜info｜boss｜spawnpoint]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子命令` | 可选 | 可选值按插件提示为 gui（管理界面）、reload（重载）、info（信息）、boss（Boss 相关）、spawnpoint（刷怪点相关）；不带时一般显示帮助 |


- **示例**：

```
/mythictools info
/mythictools gui
```

- **别名**：`/mt`、`/mtools`
- **权限**：`mythictools.command`
- **备注**：别名 mt、mtools 均可用，例如 /mt reload。基础命令 mythictools.command 默认所有人都有，但打开编辑 GUI 要 myth…

## 注意事项

::: warning
- 具体参数与子指令以游戏内 help 为准，本页只写了输入数据里能确认的那几个选项，实际写法可能随版本变化
- 基础命令 mythictools.command 默认对全部玩家开放，记得检查并用权限插件收紧 mythictools.admin 与 mythictools.reload
- reload 只管 MythicTools 自己的配置；改了 MythicMobs 的怪物、掉落或技能文件，要用 MythicMobs 自己的重载方式才会生效
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `mythictools.*` | MythicTools 所有权限 | op |
| `mythictools.admin` | 打开并编辑管理 GUI | op |
| `mythictools.command` | 使用 MythicTools 基础命令 | True |
| `mythictools.reload` | 重载 MythicTools | op |
