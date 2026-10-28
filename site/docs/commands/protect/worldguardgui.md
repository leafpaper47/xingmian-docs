---
title: WorldGuardGUI
createTime: 2026/10/24
---

# 保护区界面 · WorldGuardGUI

> 分类 🔒 领地与保护 · 版本 `1.0.6` · 指令 1 条 · api-version `1.20`

::: tip WorldGuard 区域
把 WorldGuard 那套要背指令的区域管理搬进箱子界面：列出玩家自己名下的区域，点几下就能查看信息、调整归属和常用开关，不用记 /rg 的复杂参数。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 打开区域管理界面 | /wggui | — |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/wggui` | 打开 WorldGuard 区域管理图形界面 | `/wggui` | — |

## 指令详解

### `/wggui` — 打开 WorldGuard 区域管理图形界面

- **语法**：`/wggui`

- **示例**：

```
/wggui
```

- **备注**：具体能改哪些项目取决于界面里实际摆出的按钮，别按网上别的 WorldGuardGUI 版本的截图对照。有 wggui.use 只能看到并管自己名下的区域，wgg…

## 注意事项

::: warning
- 这是 WorldGuard 的界面外壳，不是替代品：区域保护规则、优先级、父子区域这些概念完全沿用 WorldGuard，遇到保护为什么不生效仍要去查 WorldGuard 本身
- 权限给错会出问题：只给 wggui.use 的玩家按理只能动自己的区域，但不同版本对“自己的区域”判定可能不同，建议先给一两个人试，别一上来就全组放开 wggui.admin
- 界面里的操作会直接改动线上区域数据，动手前先备份 WorldGuard 的 regions.yml，尤其是批量给人开管理员权限之前
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `wggui.admin` | 允许管理所有区域 | op |
| `wggui.use` | 允许使用 /wggui 管理自己的区域 | op |
