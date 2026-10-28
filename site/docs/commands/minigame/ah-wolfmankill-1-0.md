---
title: Ah-WolfmanKill-1.0
createTime: 2026/10/24
---

# 狼人杀 · Ah-WolfmanKill-1.0

> 分类 🎲 小游戏与娱乐 · 版本 `1.0` · 指令 1 条 · api-version `1.21`

::: tip 狼人杀小游戏的开局与场地
Ah-WolfmanKill 是星冕服务器上的狼人杀（WolfmanKill）玩法插件，把一个房间从建图、开桌到结算的流程打包成一条主指令。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 打开狼人杀菜单 | /wk menu | 建房、开局都在这里 |

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
```

- **备注**：不带子指令时一般只显示帮助；需要 wolfmankill.admin 的子指令（开局、建图、重载）普通玩家点了会被拒。

## 注意事项

::: warning
- 具体参数以游戏内 help 为准，各子指令的附加参数与顺序请以服务器实际配置为准
- 开局前务必确认大厅点与地图已设好，否则玩家可能被传送到错误位置或开局失败
- wolfmankill.admin 默认只给 OP，请通过权限组显式授予，避免误把建图权限给到普通玩家
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `wolfmankill.admin` | 管理员权限 | op |
| `wolfmankill.use` | 基础使用权限 | True |
