---
title: ArmoredElytra
createTime: 2026/10/24
---

# 装甲鞘翅 · ArmoredElytra

> 分类 🧰 基础工具 · 版本 `1.0.0` · 指令 1 条 · api-version `1.21`

::: tip 把胸甲和鞘翅合成一件带护甲的鞘翅
这个插件让玩家把胸甲与鞘翅在锻造台合成为「装甲鞘翅」，合出来的成品同时保留原胸甲的护甲值和附魔，还能和 EcoEnchants 的自定义附魔兼容。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 改完配置生效 | /armoredelytra reload | 鞘翅护甲参数 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/armoredelytra` | 装甲鞘翅的管理命令，用于重载插件配置 | `/armoredelytra reload` | `xingmian.armoredelytra.bypass` |

## 指令详解

### `/armoredelytra` — 装甲鞘翅的管理命令，用于重载插件配置

- **语法**：`/armoredelytra reload`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `reload` | 可选 | 重载插件配置与合成设定，不改文件时不带参数一般无效 |


- **示例**：

```
/armoredelytra reload
```

- **权限**：`xingmian.armoredelytra.bypass`
- **备注**：需要 xingmian.armoredelytra.bypass 权限（默认仅 OP）；普通玩家只有 xingmian.armoredelytra.use 时只…

## 注意事项

::: warning
- 合成需要 xingmian.armoredelytra.use 权限，玩家报「合不出来」时先查权限组
- xingmian.armoredelytra.bypass 默认只给 OP，是绕过锻造台合成限制用的，不要随手发给普通玩家
- 重载后建议自己合一件测试，确认护甲值和 EcoEnchants 附魔都没有丢失
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `xingmian.armoredelytra.bypass` | 绕过锻造台合成限制（OP使用） | op |
| `xingmian.armoredelytra.use` | 允许使用装甲鞘翅合成/穿戴 | — |
