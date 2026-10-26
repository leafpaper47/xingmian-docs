---
title: StarAFK
createTime: 2026/10/24
---

# 挂机检测 · StarAFK

> 分类 🧰 基础工具 · 版本 `0.2.0` · 指令 1 条 · api-version `1.21`

::: tip 自动与手动挂机状态管理
星冕服自研的挂机插件，负责判断谁在挂机、把挂机状态显示给所有人看。玩家可手动切换，长时间不动也会被自动判定为挂机，挂机时 Tab 列表图标变化、头顶飘 Zzz、视距降低。与 LuckPerms 配合做豁免与静默授权。
:::

## 什么时候会用到它

- 玩家长时间站着不动，需要自动把他标成挂机，免得其他人以为人还在电脑前
- 玩家主动离开一会儿，想手动进入挂机状态并让大家都知道
- 想给服里的活动管理员做豁免：明明坐着挂机也不该被判定为 AFK
- 想来去无痕：进出挂机状态不刷屏广播，避免打扰聊天区
- 改完配置后想让新设置立刻生效又不想重启服务器

## 上手流程

1. 确认权限：普通玩家默认就有 starafk.use 和 starafk.auto，一般不用额外配置
2. 需要豁免或静默的人在 LuckPerms 里单独授予 starafk.bypass 或 starafk.silent
3. 进游戏用 /afk 试一下，观察 Tab 图标和头顶 Zzz 是否正常出现、退出时是否恢复
4. 改了配置文件后用 /afk reload 重载，再抽查几个玩家的状态

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/afk` | 切换自己的挂机状态；带 reload 则重载插件配置<br>别名 `/starafk`、`/guaji` | `/afk [reload]` | — |

## 指令详解

### `/afk` — 切换自己的挂机状态；带 reload 则重载插件配置

- **语法**：`/afk [reload]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `reload` | 可选 | 可选，填 reload 时执行配置重载，需要 starafk.reload 权限；不填则切换自己的挂机状态 |


- **示例**：

```
/afk
/afk reload
```

- **别名**：`/starafk`、`/guaji`
- **备注**：另有别名 /starafk 和 /guaji，效果一样。切换挂机状态需要 starafk.use，重载需要 starafk.reload（默认仅 OP）。被授予 starafk.silent 的玩家进出挂机不会广播。

## 注意事项

::: warning
- 这是星冕服自研插件，具体参数与子指令以游戏内 help 为准，不要照搬其它挂机插件的写法
- starafk.bypass 和 starafk.silent 默认不授予任何人，需要时用 LuckPerms 单独给，别整组批量给
- /afk 是每个玩家切换自己的状态，没有针对别人的参数；想改别人的状态请让对方自己执行
- 自动挂机依赖 starafk.auto，如果某组玩家没反应，先查这条权限是不是被负权限节点顶掉了
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `starafk.auto` | 参与自动挂机判定 | True |
| `starafk.bypass` | 永不被自动挂机（不进 AFK 状态）。默认不授予任何人，需要豁免时用 LuckPerms 单独给 | — |
| `starafk.reload` | 允许 /afk reload | op |
| `starafk.silent` | 其进出 AFK 不广播。默认不授予任何人，需要静默时用 LuckPerms 单独给 | — |
| `starafk.use` | 允许使用 /afk | True |

## 相关插件

[LuckPerms](/commands/core/luckperms.md)、[Essentials](/commands/essentials/essentials.md)、[TAB](/commands/chat/tab.md)
