---
title: MagicPointsLog
createTime: 2026/10/24
---

# 点券流水 · MagicPointsLog

> 分类 🪙 经济与商店 · 版本 `1.0.0` · 指令 1 条

::: tip PlayerPoints 点数变动记录
这是给 PlayerPoints 点券系统做的流水账本插件，把玩家点券的进出记录留存下来，方便事后查账、对账和做收支榜单。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 查点券流水 | /mpl | 玩家用 /mpl me 看自己 |

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
- **备注**：别名 magicpointslog，两个名字等价。具体子指令、参数写法以游戏内 /mpl 的帮助输出为准，本文不逐一列举。每条子功能由独立权限控制：magicp…

## 注意事项

::: warning
- 本插件的记录依赖 PlayerPoints，点券的加减必须真的走 PlayerPoints，直接改数据库或绕过它的操作不会被记进流水
- magicpointslog.clear 会清掉玩家记录，属于不可逆操作，执行前最好先备份插件的数据文件
- 具体参数与子指令以游戏内 help 为准，不同版本可能有差异，不要照抄其它服务器的教程
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `magicpointslog.all` | 查看全服点券收支汇总 | op |
| `magicpointslog.check` | 查看玩家点券收支与流水 | op |
| `magicpointslog.clear` | 清除玩家点券记录 | op |
| `magicpointslog.reload` | 重载插件配置 | op |
| `magicpointslog.top` | 查看点券收支榜单 | op |
