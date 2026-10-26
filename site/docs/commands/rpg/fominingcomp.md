---
title: FoMiningComp
createTime: 2026/10/24
---

# 挖矿加成 · FoMiningComp

> 分类 ⚔️ 战斗与 RPG · 版本 `1.6` · 指令 1 条 · api-version `1.21`

::: tip 挖矿竞赛活动插件，按挖矿量排名发奖
FoMiningComp 用来在服里办限时的挖矿比赛：统计玩家挖到的矿石数量并做排行榜，活动结束后按名次给奖励。它的特点是配置项多但运行开销小，适合人多时也不卡服。常和权限插件配合，把管理指令收在管理员组里。
:::

## 什么时候会用到它

- 开服活动、节假日福利场，想让玩家集中去挖矿比一比
- 新版本上线矿石后，办一场限时挖矿赛拉活跃
- 需要按挖矿数量自动排名并发放奖励时

## 上手流程

1. 把插件放进 plugins 目录并重启服务器，让它生成配置文件
2. 打开配置，设置比赛时长、允许计数的矿石种类和奖励内容
3. 给活动管理员发 fominingcomp.admin 权限（默认仅 OP 拥有）
4. 用 /miningcomp help 查看可用的子指令，按提示开启一场比赛

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
- 比赛期间统计口径（哪些矿石计数、是否计时运掉落）务必先在配置里确认清楚
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `fominingcomp.admin` | 访问所有FoMiningComp管理命令 | op |

## 相关插件

[LuckPerms](/commands/core/luckperms.md)、[Vault](/commands/core/vault.md)、[PlaceholderAPI](/commands/config/placeholderapi.md)
