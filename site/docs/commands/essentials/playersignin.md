---
title: PlayerSignIn
createTime: 2026/10/24
---

# 每日签到 · PlayerSignIn

> 分类 🧰 基础指令 · 版本 `1.4.0` · 指令 1 条 · api-version `1.13`

::: tip 玩家签到
每日签到累积奖励，支持补签卡、跨服/离线玩家补发签到卡，以及签到数据格式升级。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 玩家签到 | /psi | 默认子指令即签到，等价 /psi signIn |
| 看自己的签到卡 | /psi card | 查连签天数与累计次数 |
| 给玩家发补签卡 | /psi giveSignCard Steve 1 | 数量按需，别一次给太多 |
| 改完配置生效 | /psi reload | 签到奖励改完必须重载 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/playerSignIn` | 签到系统主指令<br>别名 `/psi` | `/playerSignIn <signIn｜card｜giveSignCard｜convert｜re…` | — |

## 指令详解

### `/playerSignIn` — 签到系统主指令

- **语法**：`/playerSignIn <signIn｜card｜giveSignCard｜convert｜reload>`

- **示例**：

```
/psi
/psi card
/psi giveSignCard Steve 1
```

- **别名**：`/psi`
- **备注**：别名 psi，写 /psi 即可

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/psi signIn` | 执行每日签到（/psi 不带参数也是签到） | `/psi signIn` |
| `/psi card` | 查看自己的签到卡（连签天数、累计次数） | `/psi card` |
| `/psi giveSignCard <玩家> <数量>` | 给玩家发放补签卡 | `/psi giveSignCard Steve 1` |
| `/psi convert` | 转换/升级历史签到数据（升级后用一次） | `/psi convert` |
| `/psi reload` | 重载签到配置与奖励表 | `/psi reload` |

## 注意事项

::: warning
- 补签卡是可消耗道具，giveSignCard 直接进背包，发错要手动回收。
- convert 会改写签到数据文件，执行前备份 plugins/PlayerSignIn/。
- 奖励表改了要 reload，否则玩家签到仍按旧配置发放。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `playerSignIn.*` | 以上全部 | — |
| `playerSignIn.card` | 查看签到卡 | op |
| `playerSignIn.convert` | 转换历史签到数据 | op |
| `playerSignIn.default` | 普通玩家签到与查看签到卡 | True |
| `playerSignIn.giveSignCard` | 发放补签卡 | op |
| `playerSignIn.reload` | 重载配置 | op |
| `playerSignIn.signIn` | 执行签到 | True |
