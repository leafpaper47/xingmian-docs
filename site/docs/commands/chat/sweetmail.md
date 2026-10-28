---
title: SweetMail
createTime: 2026/10/24
---

# 邮件 · SweetMail

> 分类 💬 聊天与社交 · 版本 `1.1.12-unstable` · 指令 1 条 · api-version `1.13`

::: tip 站内邮件
玩家之间发邮件、带附件与时限，支持草稿箱、收件箱、跨服新邮件提醒，管理员可向全体或指定人群群发。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 给玩家发邮件带物品 | /sm send Steve 补偿 | 发出后附件就挂上，撤回要走草稿箱 |
| 看自己收件箱 | /sm | 主指令直接开界面，附件要点领取才入包 |
| 群发全服 | /sm send all 公告 | 需管理员权限，别在有活动时误发 |
| 改完配置生效 | /sm admin reload | 改数据库相关配置要走 reload_database |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/sweetmail` | 邮件主指令：收发、草稿、群发与管理<br>别名 `/sm`、`/mail` | `/sm <send｜inbox｜outbox｜draft｜admin ...>` | — |

## 指令详解

### `/sweetmail` — 邮件主指令：收发、草稿、群发与管理

- **语法**：`/sm <send｜inbox｜outbox｜draft｜admin ...>`

- **示例**：

```
/sm
```

- **别名**：`/sm`、`/mail`
- **备注**：别名 /sm、/mail；不带参数= 打开收件箱

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/sm send <玩家> [标题]` | 给玩家发邮件，附件在界面里添加 | `/sm send Steve 活动补偿` |
| `/sm send all [标题]` | 向全服群发（需管理员） | `/sm send all 维护公告` |
| `/sm inbox` | 打开收件箱（未读会标出） | `/sm inbox` |
| `/sm outbox` | 打开发件箱，查看已发送记录 | `/sm outbox` |
| `/sm draft` | 打开草稿箱，继续编辑未发出的邮件 | `/sm draft` |
| `/sm admin reload` | 重载配置与界面文案 | `/sm admin reload` |
| `/sm admin reload_database` | 重载数据库连接（改了库配置才用） | `/sm admin reload_database` |

## 注意事项

::: warning
- 附件必须在收件人点「领取」后才进背包，玩家说「没收到东西」先让他看收件箱。
- 邮件有过期时间（outdate），过期后附件退不回来，补偿类邮件要设长时限。
- 识别方式是 UUID 还是玩家名由配置决定，**插件上线后不要改**，改了历史邮件会全部对不上号。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `sweetmail.attachment.item` | 可在邮件里附带物品（默认开启） | True |
| `sweetmail.draft.outdate.default` | — | True |
| `sweetmail.icon.default` | 使用默认邮件图标 | True |
| `sweetmail.outdate.default` | 使用默认过期时限 | True |
| `sweetmail.price.default` | 使用默认邮费档位 | True |
