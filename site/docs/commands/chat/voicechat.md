---
title: voicechat
createTime: 2026/10/24
---

# 语音聊天 · voicechat

> 分类 💬 聊天与社交 · 版本 `2.6.21` · 指令 1 条 · api-version `1.13`

::: tip 近距离语音聊天与临时语音
这是 Simple Voice Chat（简称 SVC）的服务端插件，让玩家在游戏里用麦克风按距离实时说话，远处听不清、隔墙更闷，也可以临时拉一个小群组当对讲机用。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 看语音相关子指令 | /voicechat help | 测连接也用这个 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/voicechat` | 语音聊天主指令，用于查看帮助、测试连接和组队语音 | `/voicechat help` | — |

## 指令详解

### `/voicechat` — 语音聊天主指令，用于查看帮助、测试连接和组队语音

- **语法**：`/voicechat help`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子指令` | 必填 | help 看全部子指令；另有 test、invite、join、leave，详见下方子指令表 |


- **示例**：

```
/voicechat help
/voicechat test Steve
```

- **备注**：所有子指令只能在游戏内由玩家执行，控制台无法使用，且执行者客户端必须装了 Simple Voice Chat，否则指令不会生效。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `help` | 列出所有可用的语音子指令 | `/voicechat help` |
| `test 玩家名` | 测试指定玩家的语音连接是否正常（需要 voicechat.admin 权限） | `/voicechat test Steve` |
| `invite 玩家名` | 把该玩家邀请进你当前所在的语音群组（需要 voicechat.groups 权限） | `/voicechat invite Alex` |
| `join 群组名` | 加入指定名字的语音群组，仅当同名群组只有一个时才可用；接受邀请时游戏会自动用群组 ID 执行这条指令 | `/voicechat join 建筑组` |
| `leave` | 退出当前所在的语音群组，回到普通近距离语音 | `/voicechat leave` |

## 注意事项

::: warning
- 只能在游戏内执行，控制台和纯原版客户端都不行；玩家必须装同名 mod，版本还要与服务端兼容，否则会出现听不到或图标不亮
- 最常见的问题是 UDP 24454 端口没放行（防火墙、安全组、云服务商网络策略），表现为玩家能连服但语音一直是红色断开图标
- 群组相关功能依赖 voicechat.groups 权限，没给的话 invite、join、leave 都用不了；/voicechat test 则需要 voicechat.admin，别只给自己 op 就以为万事大吉
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `voicechat.admin` | 允许测试语音聊天连接 | — |
| `voicechat.groups` | 允许加入群组 | — |
| `voicechat.listen` | 允许收听语音聊天 | — |
| `voicechat.speak` | 允许语音聊天 | — |
