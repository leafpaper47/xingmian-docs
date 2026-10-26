---
title: MythicTools
createTime: 2026/10/24
---

# 神话工具 · MythicTools

> 分类 ⚔️ 战斗与 RPG · 版本 `1.0.4` · 指令 1 条 · api-version `1.20`

::: tip MythicMobs 掉落/Boss/刷怪的辅助管理工具
它是 MythicMobs 的配套小工具，把掉落表、刷怪点、Boss 相关的东西收拢到一个管理界面和几条主命令里，省得管理员去翻一堆 YAML。它自己不做怪物和技能，全部数据来自 MythicMobs，所以必须和 MythicMobs 一起装才有意义。适合当 MythicMobs 的快捷查看与重载入口，不适合当成独立 RPG 核心。
:::

## 什么时候会用到它

- 想快速核对 MythicMobs 的掉落表、刷怪点和 Boss 配置，又不想逐个打开配置文件时
- 管理员需要临时打开管理界面查看或调整，而不改动服务器文件时
- 改完 MythicTools 自身配置后想立刻生效，不想重启整台服务器时
- 排查某个 Boss 没刷出来、某个掉落没生效，需要拿工具里的信息和游戏内实际表现对照时

## 上手流程

1. 先确认服务端已装好 MythicMobs，再把 MythicTools 放进 plugins 目录并重启服务端
2. 游戏内执行 /mythictools info，确认插件已正常加载、能看到它读到的配置情况
3. 按需执行 /mythictools gui 打开管理界面，或用 /mythictools boss、/mythictools spawnpoint 查看对应内容
4. 改完 MythicTools 自身配置后执行 /mythictools reload 生效，再回游戏里验证一遍掉落与刷怪

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
/mythictools reload
```

- **别名**：`/mt`、`/mtools`
- **权限**：`mythictools.command`
- **备注**：别名 mt、mtools 均可用，例如 /mt reload。基础命令 mythictools.command 默认所有人都有，但打开编辑 GUI 要 mythictools.admin、重载要 mythictools.reload，建议这两个只给管理员。

## 注意事项

::: warning
- 具体参数与子指令以游戏内 help 为准，本页只写了输入数据里能确认的那几个选项，实际写法可能随版本变化
- 基础命令 mythictools.command 默认对全部玩家开放，记得检查并用权限插件收紧 mythictools.admin 与 mythictools.reload
- reload 只管 MythicTools 自己的配置；改了 MythicMobs 的怪物、掉落或技能文件，要用 MythicMobs 自己的重载方式才会生效
- 它是 MythicMobs 的辅助工具，没装 MythicMobs 或版本不匹配时，涉及怪物与掉落的功能可能直接报错或空白
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `mythictools.*` | MythicTools 所有权限 | op |
| `mythictools.admin` | 打开并编辑管理 GUI | op |
| `mythictools.command` | 使用 MythicTools 基础命令 | True |
| `mythictools.reload` | 重载 MythicTools | op |

## 相关插件

[MythicMobs](/commands/rpg/mythicmobs.md)、[LuckPerms](/commands/core/luckperms.md)
