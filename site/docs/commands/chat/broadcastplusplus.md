---
title: BroadcastPlusPlus
createTime: 2026/10/24
---

# 公告广播 · BroadcastPlusPlus

> 分类 💬 聊天与社交 · 版本 `2.6.0` · 指令 1 条 · api-version `1.20`

::: tip 公告广播
把全服公告收进一套预设，支持聊天栏、大标题、动作栏与 BOSS 血条四种通道，可按场景或指定玩家定向发送，并带预览与校验。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 全服发一条聊天公告 | /bc chat 服务器将在 10 分钟后重启，请提前保存 | 临时文本用引号包住，避免空格被拆 |
| 用预设发大标题 | /bc title reboot | reboot 是配置里的预设名 |
| 只发给一个玩家 | /bc to Steve chat welcome | 通道 + 预设/文本 |
| 上线前先看效果 | /bc preview title reboot | 预览只对自己可见 |
| 改了预设文件 | /bc validate | 先校验再 /bc reload |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/broadcast` | 发送广播 / 预览 / 管理预设<br>别名 `/bc` | `/broadcast <chat｜title｜actionbar｜bossbar｜scene｜to｜…` | — |

## 指令详解

### `/broadcast` — 发送广播 / 预览 / 管理预设

- **语法**：`/broadcast <chat｜title｜actionbar｜bossbar｜scene｜to｜preview｜list｜validate｜reload｜studio> [参数]`

- **示例**：

```
/bc chat 活动开始，欢迎参加
/bc list
```

- **别名**：`/bc`
- **备注**：指令名 broadcast，别名 bc；三级权限 send / studio / admin

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/bc chat <预设｜文本>` | 聊天栏广播 | `/bc chat 活动开始，欢迎参加` |
| `/bc title <预设｜文本>` | 屏幕大标题（title/subtitle） | `/bc title reboot` |
| `/bc actionbar <预设｜文本>` | 动作栏（准星下方）提示 | `/bc actionbar 活动进行中` |
| `/bc bossbar <预设｜文本>` | 顶部 BOSS 血条样式公告 | `/bc bossbar boss_warning` |
| `/bc scene <预设> [玩家]` | 播放一个场景（多通道组合预设），可只对指定玩家 | `/bc scene reboot Steve` |
| `/bc to <玩家> <通道> <预设｜文本>` | 向指定玩家的指定通道发送 | `/bc to Steve actionbar 你已进入活动区` |
| `/bc preview <通道> <预设｜文本>` | 只对自己预览效果 | `/bc preview title reboot` |
| `/bc list [类型]` | 列出已配置的预设 | `/bc list` |
| `/bc validate` | 校验预设配置是否合法 | `/bc validate` |
| `/bc reload` | 重载预设与配置 | `/bc reload` |
| `/bc studio` | 打开图形化预设编辑界面 | `/bc studio` |

## 注意事项

::: warning
- 改完预设先 /bc validate 再 /bc reload，校验不过硬重载会让预设整体失效。
- broadcastplusplus.send 就能对全服广播，只给信任的职员，避免误发刷屏。
- 带空格的临时文本要用引号包住，否则会被拆成多个参数导致只发出第一段。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `broadcastplusplus.admin` | 校验、重载与预设管理 | op |
| `broadcastplusplus.send` | 发送与预览广播 | op |
| `broadcastplusplus.studio` | 使用 /bc studio 图形化编辑 | op |
