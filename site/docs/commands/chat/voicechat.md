---
title: voicechat
createTime: 2026/10/24
---

# 语音聊天 · voicechat

> 分类 💬 聊天与社交 · 版本 `2.6.21` · 指令 1 条 · api-version `1.13`

::: tip 近距离语音聊天与临时语音群组
这是 Simple Voice Chat（简称 SVC）的服务端插件，让玩家在游戏里用麦克风按距离实时说话，远处听不清、隔墙更闷，也可以临时拉一个小群组当对讲机用。它需要玩家客户端也装同名 mod 才能听见声音，纯原版客户端只能看图标不能发声。服务端侧主要靠权限节点控制谁能听、谁能说、谁能建群组，配合 LuckPerms 分发即可。
:::

## 什么时候会用到它

- 玩家反馈听不到队友说话，要快速判断是玩家自己的麦克风/端口问题还是服务端没给权限
- 建筑小队、活动分组需要临时开一个独立语音频道，不想用外部语音软件时
- 刚接手服务器，要确认语音插件是否装好、UDP 端口是否放行、玩家进服后图标是否正常显示
- 给不同身份分组开关语音（例如访客只能听不能说）时对照权限节点配置

## 上手流程

1. 先确认服务端已装 Simple Voice Chat 服务端插件，并让玩家客户端装对应版本的 mod（版本号要与服务端兼容）
2. 在防火墙和服务商安全组放行语音端口（默认 UDP 24454），跨服/代理架构还要额外装 voicechat-proxy 或按代理文档配置
3. 用 LuckPerms 给普通玩家默认组授予 voicechat.speak、voicechat.listen，需要群组功能的再加 voicechat.groups，管理组加 voicechat.admin
4. 玩家进服后按 V 打开语音界面，确认麦克风设备选对、能说话也能听到；管理员随后用 /voicechat test 玩家名 排查个别玩家的连接

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
/voicechat join 建筑组
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
- /voicechat join 用群名时只在群名唯一的情况下有效，重名会失败，这时让被邀请的玩家点接受邀请，游戏内部走的是群组 ID
- 群组语音和距离语音是两套逻辑，玩家在群组里时不再受距离衰减影响，排查「说话没声音」前要先确认他是不是还在某个群组里
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `voicechat.admin` | 允许测试语音聊天连接 | — |
| `voicechat.groups` | 允许加入群组 | — |
| `voicechat.listen` | 允许收听语音聊天 | — |
| `voicechat.speak` | 允许语音聊天 | — |

## 相关插件

[LuckPerms](/commands/core/luckperms.md)
