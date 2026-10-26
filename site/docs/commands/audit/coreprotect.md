---
title: CoreProtect
createTime: 2026/10/24
---

# 方块日志 · CoreProtect

> 分类 📊 记录与性能 · 版本 `24.2-dev` · 指令 1 条 · api-version `1.16`

::: tip 方块日志：查谁动过箱子、回滚破坏
把服务器上每一次方块放置/破坏、箱子存取、杀怪、聊天都记进数据库，事后能查「这块石头是谁挖的、这个箱子里的钻石是谁拿的」，也能把某段时间、某个区域的改动整体回滚或恢复。是处理熊孩子、误拆建筑、找回掉落物的第一工具。
:::

## 什么时候会用到它

- 玩家举报「我的箱子被偷了」，查这个箱子最近有谁打开过、拿走了什么
- 有人用 TNT/岩浆大面积拆家，把最近 1 小时那片区域的改动整体回滚
- 自己用 WorldEdit 手滑选错区域，把改动恢复回去
- 查某块地是谁建的、什么时候建的（判定地盘纠纷）
- 线上卡顿时清理过老的日志数据（purge）
- 回滚完发现搞错了，用 undo 撤销上一次回滚

## 上手流程

1. 先把主指令敲一下看有没有装好：`/co version`，再 `/co help` 看子指令列表
2. 查证据：`/co i` 打开检查器模式（左键方块看放置记录、右键看破坏/交互记录），或 `/co l <参数>` 直接列出记录
3. 要回滚就先用 `l` 把条件试准（时间范围 + 玩家 + 半径），再换成 `rb` 执行，条件保持一致
4. 回滚完先别急着收工，去现场看一圈；不对就 `/co undo` 撤销
5. 玩家纠纷结束后关掉检查器：`/co i` 再敲一次

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/co` | 日志系统总入口：lookup 查记录、rollback 回滚、restore 恢复、purge 清理 | `/co <子指令> [参数]` | `coreprotect.co` |

## 指令详解

### `/co` — 日志系统总入口：lookup 查记录、rollback 回滚、restore 恢复、purge 清理

- **语法**：`/co <子指令> [参数]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `<子指令>` | 必填 | i / inspect、l / lookup、rb / rollback、rs / restore、undo、purge、near、status、reload、version、help 等 |
| `[参数]` | 可选 | 常用参数：u:玩家名、t:时间（如 t:1h、t:2d）、r:半径（r:10 或 r:#global）、a:动作（a:+block 放置、a:-block 破坏、a:container 容器） |


- **示例**：

```
/co i
/co l u:Steve t:1h r:10
/co rb u:Steve t:1h r:10
/co undo
/co help
```

- **权限**：`coreprotect.co`
- **备注**：`/co`、`/core`、`/coreprotect` 三个都等价。参数用 `键:值` 形式，可以多个叠加，顺序不限。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `i` | 打开/关闭检查器模式：左键方块=看放置记录，右键方块=看破坏与容器交互记录 | `/co i` |
| `l <参数>` | 列出符合条件的记录（不改动任何东西，只查询） | `/co l u:Steve t:1h r:10` |
| `l a:container` | 只查容器类操作（开箱、取放物品） | `/co l a:container t:2h` |
| `rb <参数>` | 回滚：把符合条件的改动撤掉（方块恢复原状、被拿走的物品还回箱子） | `/co rb u:Steve t:1h r:10` |
| `rs <参数>` | 恢复：把被回滚掉的改动重新做一遍 | `/co rs u:Steve t:1h r:10` |
| `undo` | 撤销自己上一次的 rollback / restore | `/co undo` |
| `near` | 列出附近最近的方块改动 | `/co near` |
| `purge <参数>` | 清理超过指定时间的日志数据，减小数据库体积 | `/co purge t:30d` |
| `status` | 查看日志库状态：记录条数、体积、许可证 | `/co status` |
| `reload` | 重载配置（改完 config.yml 后用） | `/co reload` |
| `version` | 查看插件版本与数据库类型 | `/co version` |

## 注意事项

::: warning
- `rb` 会真的改动世界，**先用 `l` 把同样的参数跑一遍看结果**，确认范围没问题再换成 `rb`
- 半径 `r:` 是球体范围，不填默认只处理你站的这一片；大范围回滚很吃性能，尽量挑在线人数少的时候做
- 回滚一般只回滚「方块与容器内容」，玩家背包里的东西、造成的伤害不会自动还原
- 做完立刻用 `undo` 是唯一稳妥的后悔药，隔太久或又做了别的回滚就没法撤销了
- 日志默认会一直增长，`purge` 前确认服务器对纠纷追溯的要求，删了的数据找不回来
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `coreprotect.*` | 授予所有 CoreProtect 操作与命令的访问权限 | op |
| `coreprotect.co` | 拥有访问 CoreProtect /co 命令的权限 | True |
| `coreprotect.consumer` | 拥有使用消费者命令的权限 | op |
| `coreprotect.core` | 拥有访问 CoreProtect /core 命令的权限 | — |
| `coreprotect.coreprotect` | 拥有访问 CoreProtect /coreprotect 命令的权限 | — |
| `coreprotect.give` | 拥有使用 give 命令的权限 | — |
| `coreprotect.help` | 拥有使用帮助命令的权限 | op |
| `coreprotect.inspect` | 拥有使用检查模式的权限 | op |
| `coreprotect.lookup` | 拥有使用查询命令的权限 | op |
| `coreprotect.lookup.block` | 拥有查询方块数据的权限 | op |
| `coreprotect.lookup.chat` | 拥有查询聊天消息的权限 | op |
| `coreprotect.lookup.click` | 拥有查询玩家交互的权限 | op |
| `coreprotect.lookup.command` | 拥有查询玩家命令的权限 | op |
| `coreprotect.lookup.container` | 拥有查询容器交易的权限 | op |
| `coreprotect.lookup.inventory` | 拥有查询背包交易的权限 | op |
| `coreprotect.lookup.item` | 拥有查询物品交易的权限 | op |
| `coreprotect.lookup.kill` | 拥有查询实体击杀的权限 | op |
| `coreprotect.lookup.near` | 拥有使用 near 命令查询附近改动的权限 | op |
| `coreprotect.lookup.session` | 拥有查询玩家会话的权限 | op |
| `coreprotect.lookup.sign` | 拥有查询告示牌消息的权限 | op |
| `coreprotect.lookup.spawn` | 拥有查询实体生成的权限 | op |
| `coreprotect.lookup.username` | 拥有查询玩家改名记录的权限 | op |
| `coreprotect.networking` | 拥有使用网络 API 的权限 | op |
| `coreprotect.purge` | 拥有使用清理命令的权限 | op |
| `coreprotect.reload` | 拥有使用重载命令的权限 | op |
| `coreprotect.restore` | 拥有执行恢复的权限 | op |
| `coreprotect.rollback` | 拥有执行回滚的权限 | op |
| `coreprotect.status` | 拥有使用状态命令的权限 | op |
| `coreprotect.teleport` | 拥有使用传送命令的权限 | op |

## 相关插件

[WorldGuardGUI](/commands/protect/worldguardgui.md)、[Residence](/commands/protect/residence.md)、[PlugManX](/commands/core/plugmanx.md)
