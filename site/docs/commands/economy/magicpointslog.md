---
title: MagicPointsLog
createTime: 2026/10/24
---

# 点券流水 · MagicPointsLog

> 分类 🪙 经济与商店 · 版本 `1.0.0` · 指令 1 条

::: tip 记录并查询 PlayerPoints 点券的收支流水
这是给 PlayerPoints 点券系统做的流水账本插件，把玩家点券的进出记录留存下来，方便事后查账、对账和做收支榜单。它本身不发行点券，点券的实际加减仍由 PlayerPoints 及其它调用点券的插件（商店、任务、活动奖励等）完成，MagicPointsLog 只在旁边记账。适合服主处理玩家“点券怎么少了”“这笔钱谁给的”这类纠纷。
:::

## 什么时候会用到它

- 玩家来问自己的点券为什么变少或变多，需要翻具体收支记录时
- 发放活动奖励、补偿点券后，事后核对有没有发错人、发重了
- 想看点券收支排行，判断全服点券是在膨胀还是在回收时
- 怀疑有人刷点券或管理误操作，需要清掉某个玩家的记录重新统计时

## 上手流程

1. 先确认服务端已安装 PlayerPoints 且点券功能正常，否则本插件的流水没有数据来源
2. 进游戏用 /mpl 打开主界面或命令入口，先看一眼默认的帮助输出，确认当前版本支持哪些子指令
3. 按需给管理员分配 magicpointslog.check 查单个玩家、magicpointslog.top 看榜单、magicpointslog.all 看全服汇总这几项权限
4. 改过配置后用带 magicpointslog.reload 权限的账号重载，再复查一次数据是否正常

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/mpl` | 点券流水插件的主命令入口，查看帮助与各项查询功能<br>别名 `/magicpointslog` | `/mpl` | — |

## 指令详解

### `/mpl` — 点券流水插件的主命令入口，查看帮助与各项查询功能

- **语法**：`/mpl`

- **示例**：

```
/mpl
```

- **别名**：`/magicpointslog`
- **备注**：别名 magicpointslog，两个名字等价。具体子指令、参数写法以游戏内 /mpl 的帮助输出为准，本文不逐一列举。每条子功能由独立权限控制：magicpointslog.check 查玩家收支与流水、magicpointslog.top 看榜单、magicpointslog.all 看全服汇总、magicpointslog.clear 清记录、magicpointslog.reload 重载配置，默认仅 OP 拥有。

## 注意事项

::: warning
- 本插件的记录依赖 PlayerPoints，点券的加减必须真的走 PlayerPoints，直接改数据库或绕过它的操作不会被记进流水
- magicpointslog.clear 会清掉玩家记录，属于不可逆操作，执行前最好先备份插件的数据文件
- 具体参数与子指令以游戏内 help 为准，不同版本可能有差异，不要照抄其它服务器的教程
- 重载配置只能刷新设置，不能补回已经丢失的流水数据；涉及数据结构变化的更新建议重启服务端
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `magicpointslog.all` | 查看全服点券收支汇总 | op |
| `magicpointslog.check` | 查看玩家点券收支与流水 | op |
| `magicpointslog.clear` | 清除玩家点券记录 | op |
| `magicpointslog.reload` | 重载插件配置 | op |
| `magicpointslog.top` | 查看点券收支榜单 | op |

## 相关插件

PlayerPoints、[Vault](/commands/core/vault.md)
