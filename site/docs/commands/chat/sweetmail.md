---
title: SweetMail
createTime: 2026/10/24
---

# 邮件 · SweetMail

> 分类 💬 聊天与社交 · 版本 `1.1.12-unstable` · 指令 1 条 · api-version `1.13`

::: tip 玩家之间离线寄信与寄物品的邮件系统
SweetMail 给服务器加了一套游戏内邮箱：玩家可以给不在线的玩家写信、附带物品，收件人上线后开箱领取。它把「当面给不了的东西」变成异步投递，常用于玩家互助、活动奖励发放和服主补偿。邮资、图标、过期时间这些都靠权限节点控制，可以按组或个人放开。
:::

## 什么时候会用到它

- 玩家想把自己挖的矿、做的装备送给当时不在线的朋友
- 服主或管理员给某个玩家补发掉落损失、活动奖励，不想等对方上线
- 开新服或做活动时，往全体玩家邮箱里塞新手礼包或公告信
- 玩家之间约交易但时间对不上，先用邮件把东西寄过去留底

## 上手流程

1. 确认插件已加载，用 /sweetmail 或别名 /sm、/mail 打开邮件界面看能不能正常显示
2. 检查权限组：默认组要有 sweetmail.icon.default、sweetmail.price.default 等基础节点，否则玩家没法选图标或寄信
3. 自己先给一个小号寄一封带附件的测试信，确认收件方能正常打开并取走物品
4. 按需调整过期时间相关的节点，避免邮件长期堆积或附件丢失投诉

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/sweetmail` | 打开邮件界面，管理收发信件与附件<br>别名 `/sm`、`/mail` | `/sweetmail` | — |

## 指令详解

### `/sweetmail` — 打开邮件界面，管理收发信件与附件

- **语法**：`/sweetmail`

- **示例**：

```
/sweetmail
/sm
/mail
```

- **别名**：`/sm`、`/mail`
- **备注**：别名 sm、mail 完全等价。多数操作在打开的图形界面里完成，不是靠敲参数；具体子指令与参数请以游戏内输入 /sweetmail 后看到的提示或 help 为准。

## 注意事项

::: warning
- 具体参数与子指令以游戏内 help 为准，本手册不臆测用法，装好后先自己点一遍界面确认流程
- 附件物品一旦被取走或邮件过期，通常无法找回，重要物品建议让玩家先确认收件人身份
- sweetmail.price.default 关系到寄信要不要花邮资，改动前先看清楚经济插件那边扣的是什么货币
- sweetmail.outdate.default 与 sweetmail.draft.outdate.default 控制普通邮件和草稿的保留时长，调短前先公告，否则会有玩家抱怨信被清掉
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `sweetmail.attachment.item` | — | True |
| `sweetmail.draft.outdate.default` | — | True |
| `sweetmail.icon.default` | — | True |
| `sweetmail.outdate.default` | — | True |
| `sweetmail.price.default` | — | True |

## 相关插件

[Vault](/commands/core/vault.md)、[PlaceholderAPI](/commands/config/placeholderapi.md)
