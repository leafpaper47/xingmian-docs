---
title: LeafChat
createTime: 2026/10/24
---

# 聊天管理 · LeafChat

> 分类 💬 聊天与社交 · 版本 `1.0.5` · 指令 8 条 · api-version `1.21`

::: tip 统一管理聊天格式、私聊、禁言与物品展示
LeafChat 接管服务器的公屏与私聊，提供聊天颜色、渐变与彩虹字、@提及、背包物品展示链接、私聊与禁言管理。管理员用它统一聊天样式和处罚口径，普通玩家用它发彩色消息、私聊和展示手上的物品。它和权限插件配合控制谁能用颜色、谁能禁言。
:::

## 什么时候会用到它

- 玩家想让自己说的话带颜色、渐变或彩虹效果时，用 /chatcolor 挑颜色
- 玩家想私聊某人，或回复刚刚私聊过自己的人时，用 /msg 和 /r
- 有人在公屏刷屏、骂人，需要临时或永久闭麦时，用 /mute 和 /unmute
- 服主排查玩家举报的私聊纠纷，用 /spymsg 打开私聊监听抄送
- 改完配置想立刻生效，用 /leafchat reload 重载，不用重启服务器

## 上手流程

1. 先确认插件已加载，聊天里能看到 LeafChat 处理过的格式（颜色/前缀），说明接管成功
2. 用权限插件给不同组分配 leafchat.chatcolor、leafchat.color.use、leafchat.color.gradient 等节点，决定谁能用颜色和渐变
3. 让玩家试一次 /chatcolor 打开颜色面板或用 /chatcolor 颜色ID 直接设定，确认显示正常
4. 日常管理时用 /mute 与 /unmute 处理违规，用 /spymsg 随时开关私聊监听
5. 改过配置后执行 /leafchat reload，并留意控制台是否有报错

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/chatcolor` | 打开聊天颜色选择界面或直接设定颜色 | `/chatcolor [颜色ID]` | `leafchat.chatcolor` |
| `/leafchat` | 插件主命令，目前用于重载配置 | `/leafchat reload` | — |
| `/leafchatview` | 物品展示链接的后端入口，由聊天里的标记自动触发 | `/leafchatview` | — |
| `/msg` | 给指定玩家发送私聊消息 | `/msg 玩家名 消息内容` | `leafchat.msg` |
| `/mute` | 禁言玩家，不填时长即永久禁言 | `/mute 玩家名 [时长]` | `leafchat.mute` |
| `/r` | 回复上一位和自己私聊过的玩家 | `/r 消息内容` | `leafchat.msg` |
| `/spymsg` | 开关自己的私聊监听，抄送他人的私聊内容 | `/spymsg` | `leafchat.spy` |
| `/unmute` | 解除指定玩家的禁言 | `/unmute 玩家名` | `leafchat.unmute` |

## 指令详解

### `/chatcolor` — 打开聊天颜色选择界面或直接设定颜色

- **语法**：`/chatcolor [颜色ID]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `颜色ID` | 可选 | 颜色标识，留空则打开颜色选择界面；具体可用的 ID 以游戏内提示为准 |


- **示例**：

```
/chatcolor
/chatcolor red
```

- **权限**：`leafchat.chatcolor`
- **备注**：另有渐变写法：/chatcolor gradient 起色 止色，两种颜色各填一个颜色 ID，需具备 leafchat.color.gradient 权限；能否用单色、渐变、彩虹分别由 leafchat.color.* 下的节点控制。

### `/leafchat` — 插件主命令，目前用于重载配置

- **语法**：`/leafchat reload`

- **示例**：

```
/leafchat reload
```

- **备注**：重载需要 leafchat.reload 权限（默认仅管理员）；改完配置文件后执行，若控制台报错通常是配置项写坏了，改回后再重载。

### `/leafchatview` — 物品展示链接的后端入口，由聊天里的标记自动触发

- **语法**：`/leafchatview`

- **示例**：

```
/leafchatview
```

- **备注**：正常玩法中不需要手动输入：玩家在聊天里发 [inv] 或 [ec] 这类标记时插件会自己生成可点击的展示链接。管理员用 leafchat.admin 权限可以直接查看他人背包/末影箱内容，而普通人只能看别人主动展示出来的那份。

### `/msg` — 给指定玩家发送私聊消息

- **语法**：`/msg 玩家名 消息内容`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `玩家名` | 必填 | 接收私聊的目标玩家 |
| `消息内容` | 必填 | 要发送的文字，可一次输入整句 |


- **示例**：

```
/msg Steve 你好，在吗
```

- **权限**：`leafchat.msg`
- **备注**：需要 leafchat.msg 权限，默认所有人可用；被禁言的玩家通常也无法私聊。若服里开了私聊监听，具备 leafchat.spy 的管理员会同时看到这条内容。

### `/mute` — 禁言玩家，不填时长即永久禁言

- **语法**：`/mute 玩家名 [时长]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `玩家名` | 必填 | 被禁言的目标玩家 |
| `时长` | 可选 | 禁言持续时间，留空表示永久；具体时长格式以游戏内提示为准 |


- **示例**：

```
/mute Steve
/mute Steve 10m
```

- **权限**：`leafchat.mute`
- **备注**：需要 leafchat.mute 权限（默认仅管理员）。建议对骂人、刷屏先给短时长，反复违规再上永久；永久禁言记得到时候复查，别忘了解。

### `/r` — 回复上一位和自己私聊过的玩家

- **语法**：`/r 消息内容`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `消息内容` | 必填 | 要回复的文字 |


- **示例**：

```
/r 好，我马上到
```

- **权限**：`leafchat.msg`
- **备注**：需要 leafchat.msg 权限。只有本次在线期间有过一次私聊往来才有回复目标，服务器重启或对方下线后可能提示没有可回复的对象。

### `/spymsg` — 开关自己的私聊监听，抄送他人的私聊内容

- **语法**：`/spymsg`

- **示例**：

```
/spymsg
```

- **权限**：`leafchat.spy`
- **备注**：需要 leafchat.spy 权限（默认仅管理员），再执行一次即关闭。监听只对开关之后新发生的私聊生效，开启前已经聊过的内容看不到。

### `/unmute` — 解除指定玩家的禁言

- **语法**：`/unmute 玩家名`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `玩家名` | 必填 | 要解除禁言的目标玩家 |


- **示例**：

```
/unmute Steve
```

- **权限**：`leafchat.unmute`
- **备注**：需要 leafchat.unmute 权限（默认仅管理员）。玩家申诉或误封时用它恢复；解禁后让对方发一句话确认真的能说话了。

## 注意事项

::: warning
- 该插件为服务器自研/小众插件，具体参数与子指令以游戏内 help 为准，本文档中的用法来自插件自身命令表
- 颜色、渐变、彩虹、@全体 分属不同权限节点，权限没给全时玩家会看到「无权限」而不是报错，先查权限插件再怀疑插件坏了
- 禁言留空时长等于永久禁言，处理完记得 /unmute 或查记录，避免玩家长期无法说话
- 私聊监听涉及玩家隐私，只建议在处理举报时临时开启，用完立刻关闭
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `leafchat.admin` | 管理员直接查看他人背包/末影箱（聊天内 [inv]/[ec] 展示链接无需该权限） | op |
| `leafchat.chatcolor` | 允许使用聊天颜色 | True |
| `leafchat.color.*` | 授予所有聊天颜色权限（单色/渐变/彩虹） | op |
| `leafchat.color.gradient` | 允许使用所有预设渐变并自定义渐变 | op |
| `leafchat.color.rainbow` | 允许使用彩虹色 | op |
| `leafchat.color.use` | 允许在消息中使用颜色码（&amp; / § / MiniMessage 标签） | op |
| `leafchat.mention.all` | 允许使用 @全体 广播 | op |
| `leafchat.msg` | 允许发送私聊 | True |
| `leafchat.mute` | 允许禁言玩家 | op |
| `leafchat.reload` | 允许重载配置 | op |
| `leafchat.spy` | 允许监听私聊 | op |
| `leafchat.unmute` | 允许解除禁言 | op |

## 相关插件

[LuckPerms](/commands/core/luckperms.md)
