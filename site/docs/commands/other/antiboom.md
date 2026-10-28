---
title: AntiBoom
createTime: 2026/10/24
---

# AntiBoom

> 分类 📦 其他 · 版本 `1.0.4` · 指令 1 条 · api-version `26.1.2`

::: tip 爆炸伤害防护与区域豁免
Explosion protection plugin for Paper 26.1.2+, including 26.2, and Folia
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 给玩家开防爆权限 | /antiboom Steve | 让他在爆炸中不受伤害 |
| 关掉某人的防爆 | /antiboom Steve off | 恢复默认 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/antiboom` | Manage AntiBoom plugin settings. | `/antiboom reload` | `antiboom.reload` |

## 指令详解

### `/antiboom` — Manage AntiBoom plugin settings.

- **语法**：`/antiboom reload`

- **示例**：

```
/antiboom reload
```

- **权限**：`antiboom.reload`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `antiboom.reload` | Allows reloading AntiBoom configuration. | op |
