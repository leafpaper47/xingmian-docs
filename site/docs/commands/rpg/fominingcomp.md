---
title: FoMiningComp
createTime: 2026/10/24
---

# 挖矿竞赛 · FoMiningComp

> 分类 ⚔️ 战斗与 RPG · 版本 `1.6` · 指令 1 条 · api-version `1.21`

::: tip 挖矿竞赛活动插件
FoMiningComp 用来在服里办限时的挖矿比赛：统计玩家挖到的矿石数量并做排行榜，活动结束后按名次给奖励。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 看可用子指令 | /fominingcomp help | 管理操作需 admin |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/fominingcomp` | 插件主命令，用于查看帮助与执行管理操作<br>别名 `/miningcomp` | `/fominingcomp help` | `fominingcomp.admin` |

## 指令详解

### `/fominingcomp` — 插件主命令，用于查看帮助与执行管理操作

- **语法**：`/fominingcomp help`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `help` | 可选 | 查看子指令列表，具体参数以游戏内 help 输出为准 |


- **示例**：

```
/fominingcomp help
/miningcomp help
```

- **别名**：`/miningcomp`
- **权限**：`fominingcomp.admin`
- **备注**：别名 miningcomp 等价；需要 fominingcomp.admin 权限（默认仅 OP）。带子指令的具体写法以游戏内 help 为准。

## 注意事项

::: warning
- 具体参数与子指令以游戏内 help 为准，本文不列举未确认的写法
- 只给活动管理员 fominingcomp.admin 权限，避免普通玩家误开或误停比赛
- 改完配置建议重启服务器，而不是只 reload，避免数值不生效
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `fominingcomp.admin` | 访问所有FoMiningComp管理命令 | op |
