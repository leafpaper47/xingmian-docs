---
title: XaeroTracker
createTime: 2026/10/24
---

# 小地图追踪 · XaeroTracker

> 分类 🗺️ 世界与地图 · 版本 `1.4.0-xm` · 指令 1 条 · api-version `1.20`

::: tip 在小地图上显示与追踪玩家
XaeroTracker 是配合 Xaero 小地图使用的服务端追踪插件，负责决定玩家在地图上能不能看到别人、别人能不能看到自己。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 看被追踪的玩家 | /xt tracked | 对方需开启共享 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/xaerotracker` | 切换自己的地图追踪相关设置<br>别名 `/xt` | `/xt 模式，模式取 tracked、town 或 seeall` | `xaerotracker.use` |

## 指令详解

### `/xaerotracker` — 切换自己的地图追踪相关设置

- **语法**：`/xt 模式，模式取 tracked、town 或 seeall`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `模式` | 必填 | 取值 tracked、town 或 seeall，分别对应该玩家是否被追踪、是否看得见同镇成员、是否看得见全服玩家，每个模式对应一个独立权限节点 |


- **示例**：

```
/xt tracked
/xt town
```

- **别名**：`/xt`
- **权限**：`xaerotracker.use`
- **备注**：主命令有别名 /xt；三个模式分别受 xaerotracker.tracked、xaerotracker.town、xaerotracker.seeall 控制…

## 注意事项

::: warning
- 具体参数以游戏内 help 为准，各服版本可能有差异，子模式请用 /xt 加帮助参数或查插件文档确认
- seeall 默认不给任何人，包括 OP，授予前想清楚会不会变成全服透视
- tracked 是「自己是否被追踪」的开关，关掉后别人小地图上就看不到自己，玩家问「为什么看不到队友」多半是这个
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `xaerotracker.*` | XaeroTracker 全部权限 | — |
| `xaerotracker.admin` | 管理其他玩家的追踪设置 | — |
| `xaerotracker.seeall` | 看得见地图上的所有玩家。默认连 OP 也不拥有 | — |
| `xaerotracker.town` | 开关是否看得见同镇成员 | True |
| `xaerotracker.tracked` | 开关自己是否被追踪 | True |
| `xaerotracker.tracker` | 追踪指定玩家（动态权限，实际为 xaerotracker.tracker.&lt;玩家名&gt;） | — |
| `xaerotracker.use` | 使用 /xt 命令 | True |
