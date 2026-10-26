---
title: ArmoredElytra
createTime: 2026/10/24
---

# 鞘翅护甲 · ArmoredElytra

> 分类 🧰 基础工具 · 版本 `1.0.0` · 指令 1 条 · api-version `1.21`

::: tip 把胸甲和鞘翅合成一件带护甲的鞘翅
这个插件让玩家把胸甲与鞘翅在锻造台合成为「装甲鞘翅」，合出来的成品同时保留原胸甲的护甲值和附魔，还能和 EcoEnchants 的自定义附魔兼容。它解决的是玩家为了飞就得脱掉胸甲的痛点，让飞行不再牺牲生存能力。通常和 EcoEnchants、背包/装备管理类插件、以及服务器的权限组配合使用。
:::

## 什么时候会用到它

- 玩家想在保留胸甲防护的同时使用鞘翅飞行
- 服务器想给飞行装备加一道门槛，只允许有权限的玩家合成装甲鞘翅
- 管理员需要给特定玩家或活动奖励发放带护甲的鞘翅
- 需要调整合成限制、临时放开或收回玩家合成资格时

## 上手流程

1. 确认插件已放进 plugins 目录并重启服务器，让配置和合成配方生效
2. 给需要使用该功能的玩家组授予 xingmian.armoredelytra.use 权限，否则无法合成或穿戴
3. 拿一件胸甲和一件鞘翅，按插件设定的方式合成出装甲鞘翅，先自己测一件确认护甲值和附魔都保留了
4. 改完配置后用 /armoredelytra reload 重载，再让玩家实际验证一次

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
- **备注**：需要 xingmian.armoredelytra.bypass 权限（默认仅 OP）；普通玩家只有 xingmian.armoredelytra.use 时只能合成和穿戴，用不了这条管理命令

## 注意事项

::: warning
- 合成需要 xingmian.armoredelytra.use 权限，玩家报「合不出来」时先查权限组
- xingmian.armoredelytra.bypass 默认只给 OP，是绕过锻造台合成限制用的，不要随手发给普通玩家
- 重载后建议自己合一件测试，确认护甲值和 EcoEnchants 附魔都没有丢失
- 具体参数与子指令以游戏内 help 为准
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `xingmian.armoredelytra.bypass` | 绕过锻造台合成限制（OP使用） | op |
| `xingmian.armoredelytra.use` | 允许使用装甲鞘翅合成/穿戴 | — |

## 相关插件

[EcoEnchants](/commands/rpg/ecoenchants.md)、[LuckPerms](/commands/core/luckperms.md)、[Vault](/commands/core/vault.md)
