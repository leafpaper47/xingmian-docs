---
title: SenluoCookbook
createTime: 2026/10/24
---

# SenluoCookbook

> 分类 📦 其他 · 版本 `1.0.0` · 指令 1 条 · api-version `1.21`

::: tip 森罗厨房图鉴：炒出或做出
森罗厨房图鉴：炒出或做出 kaleidoscopecookery 菜品即解锁，全菜品图鉴 GUI。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 查这道菜怎么做 | /cookbook 森罗炒饭 | 看不到就先用 /cookbook 列全部 |
| 看完整食谱列表 | /cookbook | 不分页时可加页码 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/cookbook` | 打开森罗厨房图鉴<br>别名 `/ckbook`、`/森罗图鉴`、`/厨房图鉴`、`/ckb` | `/cookbook [reload｜debug｜sync]` | — |

## 指令详解

### `/cookbook` — 打开森罗厨房图鉴

- **语法**：`/cookbook [reload｜debug｜sync]`

- **示例**：

```
/cookbook
/cookbook 64
```

- **别名**：`/ckbook`、`/森罗图鉴`、`/厨房图鉴`、`/ckb`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `cookbook.admin` | 允许重载图鉴配置 | op |
| `cookbook.use` | 允许使用森罗厨房图鉴 | True |
