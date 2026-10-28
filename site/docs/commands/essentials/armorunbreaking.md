---
title: ArmorUnbreaking
createTime: 2026/10/24
---

# 盔甲免损耗 · ArmorUnbreaking

> 分类 🧰 基础工具 · 版本 `1.0.0` · 指令 1 条 · api-version `1.21`

::: tip 让护甲耐久附魔按概率豁免耐久扣减
护甲免损耗插件，把护甲上的耐久（Unbreaking）附魔从原版机制改成按等级算概率豁免耐久扣减，规则为等级除以等级加一，覆盖所有会产生耐久损耗的来源。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 看耐久豁免概率 | /armordura table | 调平衡前先看这张表 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/armordura` | 查看护甲耐久豁免概率表，或重载插件配置<br>别名 `/adura` | `/armordura table｜reload` | `armorunbreaking.admin` |

## 指令详解

### `/armordura` — 查看护甲耐久豁免概率表，或重载插件配置

- **语法**：`/armordura table｜reload`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `table 或 reload` | 必填 | table 查看概率表；reload 重新读取配置文件 |


- **示例**：

```
/armordura table
/armordura reload
```

- **别名**：`/adura`
- **权限**：`armorunbreaking.admin`
- **备注**：别名 adura 可直接替代 armordura。reload 只重读配置，不会补发或改动已有装备；权限节点为 armorunbreaking.admin，默认…

## 注意事项

::: warning
- 具体参数与子指令以游戏内 help 为准，本文只按官方用法说明整理
- 概率规则是等级除以等级加一，等级越高越接近但不等于完全免损耗，别向玩家承诺永不掉耐久
- reload 后建议用 table 复核一次，确认配置真的读进去了再对外公告
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `armorunbreaking.admin` | 允许使用 /armordura | op |
