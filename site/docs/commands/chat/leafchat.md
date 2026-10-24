---
title: LeafChat
createTime: 2026/10/24
---

# LeafChat

> 版本 `1.0.5` · 指令 8 条 · api-version `1.21` · 文件 `leafchat-1.0.5.jar`

现代化聊天管理插件（聊天颜色 / 物品展示 / 私聊 / 禁言 / 跨服）

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/chatcolor help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/chatcolor` | 设置或打开聊天颜色选择 | `leafchat.chatcolor` |
| `/leafchat` | LeafChat 主命令（重载配置等） | — |
| `/leafchatview` | 聊天物品展示后端（由 [inv]/[ec] 链接触发，无需手动使用） | — |
| `/msg` | 发送私聊消息 | `leafchat.msg` |
| `/mute` | 禁言玩家（留空时长=永久） | `leafchat.mute` |
| `/r` | 回复上次私聊对象 | `leafchat.msg` |
| `/spymsg` | 切换管理员私聊监听 | `leafchat.spy` |
| `/unmute` | 解除玩家禁言 | `leafchat.unmute` |

## 详细用法

### /chatcolor

- **说明**：设置或打开聊天颜色选择
- **用法**：`/chatcolor [颜色ID] | /chatcolor gradient &lt;起色&gt; &lt;止色&gt;`
- **权限**：`leafchat.chatcolor`

### /leafchat

- **说明**：LeafChat 主命令（重载配置等）
- **用法**：`/leafchat reload`

### /leafchatview

- **说明**：聊天物品展示后端（由 [inv]/[ec] 链接触发，无需手动使用）
- **用法**：`/leafchatview`

### /msg

- **说明**：发送私聊消息
- **用法**：`/msg &lt;玩家&gt; &lt;消息&gt;`
- **权限**：`leafchat.msg`

### /mute

- **说明**：禁言玩家（留空时长=永久）
- **用法**：`/mute &lt;玩家&gt; [时长]`
- **权限**：`leafchat.mute`

### /r

- **说明**：回复上次私聊对象
- **用法**：`/r &lt;消息&gt;`
- **权限**：`leafchat.msg`

### /spymsg

- **说明**：切换管理员私聊监听
- **用法**：`/spymsg`
- **权限**：`leafchat.spy`

### /unmute

- **说明**：解除玩家禁言
- **用法**：`/unmute &lt;玩家&gt;`
- **权限**：`leafchat.unmute`

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
