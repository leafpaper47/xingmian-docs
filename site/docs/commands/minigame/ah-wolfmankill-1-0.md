---
title: Ah-WolfmanKill-1.0
createTime: 2026/10/24
---

# 狼人杀 · Ah-WolfmanKill-1.0

> 分类 🎲 小游戏与娱乐 · 版本 `1.0` · 指令 1 条 · api-version `1.21`

::: tip 狼人杀小游戏的开局与场地管理插件
Ah-WolfmanKill 是星冕服务器上的狼人杀（WolfmanKill）玩法插件，把一个房间从建图、开桌到结算的流程打包成一条主指令。管理员用它可以设置大厅与地图、选择或随机地图、重置房间并开始一局，玩家则通过菜单加入、离开或进入观战位。插件只提供一套 wolfmankill.use / wolfmankill.admin 权限，日常使用基本不用额外授权。
:::

## 什么时候会用到它

- 在服务器上开一局狼人杀，让玩家排队进场
- 给狼人杀场地配置大厅点与地图，供开局传送使用
- 活动时临时重置房间、重新开桌或换地图
- 让已出局或被淘汰的玩家切到观战视角看后续
- 调整房间列表、白天饥饿与苹果等玩法开关

## 上手流程

1. 先给管理员加 wolfmankill.admin 权限，普通玩家保留 wolfmankill.use 即可
2. 用 /wk setlobby 设好等待大厅，再用 /wk setmap 或 /wk randommap 准备可用地图
3. 玩家用 /wk join 进场、/wk watch 进观战，人数够了管理员 /wk start 开局
4. 一局结束后 /wk reset 清场，需要时 /wk reload 重载配置再开下一局

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/wk` | 狼人杀主指令，通过子指令完成建房、开局、地图与设置管理 | `/wk [menu｜join｜leave｜watch｜unwatch｜start｜reset｜set…` | — |

## 指令详解

### `/wk` — 狼人杀主指令，通过子指令完成建房、开局、地图与设置管理

- **语法**：`/wk [menu｜join｜leave｜watch｜unwatch｜start｜reset｜setlobby｜setmap｜select｜randommap｜reload｜roles｜maps｜settings｜setlist｜closelist｜apple｜hunger]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子指令` | 必填 | 功能分支，如 menu 菜单、join 加入、watch 观战、start 开局、setlobby 设大厅、setmap 设地图、reset 重置、reload 重载 |


- **示例**：

```
/wk menu
/wk join
/wk start
/wk setlobby
```

- **备注**：不带子指令时一般只显示帮助；需要 wolfmankill.admin 的子指令（开局、建图、重载）普通玩家点了会被拒。

## 注意事项

::: warning
- 具体参数以游戏内 help 为准，各子指令的附加参数与顺序请以服务器实际配置为准
- 开局前务必确认大厅点与地图已设好，否则玩家可能被传送到错误位置或开局失败
- wolfmankill.admin 默认只给 OP，请通过权限组显式授予，避免误把建图权限给到普通玩家
- 一局结束请先 reset 再开下一局，直接 start 可能带着上一局的残余状态；改完配置可用 reload 生效，但正在进行的对局不要中途 reload
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `wolfmankill.admin` | 管理员权限 | op |
| `wolfmankill.use` | 基础使用权限 | True |

## 相关插件

[LuckPerms](/commands/core/luckperms.md)、[Vault](/commands/core/vault.md)、[PlaceholderAPI](/commands/config/placeholderapi.md)
