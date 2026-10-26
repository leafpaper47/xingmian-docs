---
title: BroadcastPlusPlus
createTime: 2026/10/24
---

# 公告广播 · BroadcastPlusPlus

> 分类 💬 聊天与社交 · 版本 `2.6.0` · 指令 1 条 · api-version `1.20`

::: tip 统一管理全服公告广播与多种显示通道
BroadcastPlusPlus 把服务器公告统一收进一套预设里，支持聊天栏、大标题、动作栏、BOSS 血条等多条显示通道，也能按玩家或场景定向发送。管理员用 /bc 套用预设或临时写一段文本，先在游戏内预览确认效果再对全服发出。它解决的是公告写法散乱、颜色代码容易出错、发完全服才发现文案有问题这类麻烦，通常和权限插件配合给职员分级授权。
:::

## 什么时候会用到它

- 开服活动、节假日福利、版本更新时向全服统一发通知
- 需要比聊天栏更醒目的提示（大标题、动作栏、BOSS 血条）时
- 只提醒某一个玩家，或只对某个场景内的玩家播报时，用 to 或 scene 定向发送
- 正式活动前先预览效果，避免颜色代码写错或文案过长被截断
- 改完预设配置文件后自检与热重载

## 上手流程

1. 先确认自己的账号有 broadcastplusplus.send 或 broadcastplusplus.admin 权限，没权限时所有广播指令都会被拒绝
2. 用 /bc list 看现有预设有哪些，决定是直接套预设还是临时写一段文本
3. 先用 /bc preview 或 /bc to 指定自己试发一次，确认颜色、换行、BOSS 血条停留时长都符合预期
4. 确认无误后用 /bc chat 或 /bc scene 对全服正式广播
5. 如果改过预设文件，先 /bc validate 校验通过再 /bc reload 生效

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/broadcast` | 发送广播、预览效果、管理预设与重载配置<br>别名 `/bc` | `/bc chat｜title｜actionbar｜bossbar 预设名或文本，/bc scene …` | — |

## 指令详解

### `/broadcast` — 发送广播、预览效果、管理预设与重载配置

- **语法**：`/bc chat｜title｜actionbar｜bossbar 预设名或文本，/bc scene 预设名 玩家，/bc to 玩家 通道 预设名或文本，/bc preview 通道 预设名或文本，/bc list 类型，/bc validate，/bc reload，/bc studio`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `通道` | 必填 | chat 为聊天栏，title 为大标题，actionbar 为动作栏，bossbar 为头顶 BOSS 血条；另有管理分支 scene、to、preview、list、validate、reload、studio |
| `预设名或文本` | 必填 | 填配置里已有的预设名，或直接用引号包住一段临时文本 |
| `玩家` | 可选 | to 分支填接收者玩家名，scene 分支可指定单个玩家；不填时一般面向全服 |
| `类型` | 可选 | list 分支可选，用来只看某一类通道的预设清单 |


- **示例**：

```
/bc chat 服务器将在 10 分钟后重启，请提前保存
/bc title 活动开始
/bc preview actionbar 这是一条测试文本
/bc to Steve chat 请到主城集合
/bc list
/bc validate
/bc reload
```

- **别名**：`/bc`
- **备注**：指令名是 broadcast，日常用别名 /bc 最省事。权限分三级：broadcastplusplus.send 负责发送与预览，broadcastplusplus.studio 负责打开 Broadcast Studio 界面，broadcastplusplus.admin 是完全控制（发送、Studio、重载）。改完预设先 /bc validate 再 /bc reload，出现报错时先看控制台，不要反复重载。

## 注意事项

::: warning
- 具体参数与子指令以游戏内 help 为准，本手册按当前版本的用法整理，升级后可能新增通道类型或分支
- broadcastplusplus.send 就能对全服广播，只给信任的职员，避免误发、刷屏或把内部通知发给玩家
- 改完预设文件要按顺序走：先 /bc validate 校验，通过后再 /bc reload；校验不过还硬重载容易让预设整体失效
- title 和 bossbar 对玩家客户端侵入感较强，正式活动前务必先用 /bc preview 或 /bc to 自己看一遍，确认文案长度和停留时间
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `broadcastplusplus.admin` | 完全控制—发送、单间公寓、重新加载。 | op |
| `broadcastplusplus.send` | 发送广播和预览预设。 | op |
| `broadcastplusplus.studio` | 打开Broadcast Studio GUI。 | op |

## 相关插件

[PlaceholderAPI](/commands/config/placeholderapi.md)、[LuckPerms](/commands/core/luckperms.md)
