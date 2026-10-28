---
title: PVPPlugin
createTime: 2026/10/24
---

# PVP管理 · PVPPlugin

> 分类 ⚔️ 战斗与 RPG · 版本 `1.2.28` · 指令 1 条 · api-version `1.21`

::: tip 玩家间决斗与公平排位的可视化管理插件
这是星冕服务器自研的 PVP 决斗插件，负责玩家约战、团战房间、下注赌钱决斗、观战以及按月结算的公平排位赛季。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 看决斗相关子指令 | /pvp help | — |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/pvp` | 决斗与排位总入口，含下注、观战、团战、竞技场设置与赛季<br>别名 `/duel` | `/pvp [bet｜spectate｜accept｜deny｜team｜seta｜setb｜relo…` | — |

## 指令详解

### `/pvp` — 决斗与排位总入口，含下注、观战、团战、竞技场设置与赛季

- **语法**：`/pvp [bet｜spectate｜accept｜deny｜team｜seta｜setb｜reload｜help｜rank(join｜spectate｜cancel｜top｜stats｜season｜claim)]`

- **示例**：

```
/pvp help
/pvp team
```

- **别名**：`/duel`
- **备注**：别名 /duel，两者等价。参数位分别是下注决斗、观战、接受、拒绝、团战房间、设置 A 方出生点、设置 B 方出生点、重载、帮助、排位相关子命令；seta / …

## 注意事项

::: warning
- 这是星冕自研插件，版本迭代快，具体参数与子指令以游戏内 help 为准，手册里的写法不要当成唯一答案
- seta / setb 改的是竞技场真实坐标，改完务必自己打一场验证传送与重生位置，别直接在排位赛期间动
- 涉及下注赌钱的模式会真实动经济，活动前先确认对局双方余额与规则，避免赛后扯皮
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `pvp.admin` | 管理权限（设置竞技场坐标、重载配置） | op |
| `pvp.bypass` | 跳过竞技场传送 / 飞行限制（OP 默认拥有） | op |
| `pvp.team` | 允许创建团战房间 | True |
| `pvp.use` | 允许使用 PVP 决斗功能 | True |
