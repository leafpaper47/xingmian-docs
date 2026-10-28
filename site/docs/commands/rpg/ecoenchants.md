---
title: EcoEnchants
createTime: 2026/10/24
---

# 自定义附魔 · EcoEnchants

> 分类 ⚔️ 战斗与 RPG · 版本 `2026.34` · 指令 3 条 · api-version `1.21.8`

::: tip 自定义附魔
给物品加原版没有的附魔（挖掘/战斗/工具类），附魔按权限与稀有度分发，可做附魔书、附魔台规则与描述开关。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 看有哪些自定义附魔 | /ee gui | 图形化浏览附魔清单 |
| 给自己打附魔 | /ee enchant &lt;附魔&gt; 3 | 第三个参数可指定玩家 |
| 发附魔书 | /ee givebook random | 活动奖励常用 |
| 改完配置生效 | /ee reload | 附魔表改完必须重载 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/ecoenchants` | 自定义附魔主指令 | `/ee <gui｜enchant｜givebook｜reload｜toggle>` | `ecoenchants.command.ecoenchants` |
| `/enchant` | 附魔物品 | — | `ecoenchants.command.enchant` |
| `/enchantinfo` | 显示关于附魔的信息 | — | `ecoenchants.command.enchantinfo` |

## 指令详解

### `/ecoenchants` — 自定义附魔主指令

- **语法**：`/ee <gui｜enchant｜givebook｜reload｜toggle>`

- **示例**：

```
/ee gui
```

- **权限**：`ecoenchants.command.ecoenchants`
- **备注**：命令名 ecoenchants，常用别名 /ee

### `/enchant` — 附魔物品

- **权限**：`ecoenchants.command.enchant`

### `/enchantinfo` — 显示关于附魔的信息

- **权限**：`ecoenchants.command.enchantinfo`

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/ee gui` | 打开展示所有附魔的图形界面 | `/ee gui` |
| `/ee enchant <附魔> [等级] [玩家]` | 给手持物品打上指定附魔 | `/ee enchant telepathy 3` |
| `/ee enchant <附魔> <等级> <玩家>` | 给指定玩家的手持物品打附魔 | `/ee enchant telepathy 3 Steve` |
| `/ee givebook random` | 随机发放一本附魔书 | `/ee givebook random` |
| `/ee givebook <附魔> [等级]` | 发放指定附魔的附魔书 | `/ee givebook telepathy 2` |
| `/ee toggle` | 开关附魔描述显示（物品 lore 里的说明） | `/ee toggle` |
| `/ee reload` | 重载全部附魔配置 | `/ee reload` |

## 注意事项

::: warning
- 附魔生效与「玩家有没有该附魔的权限」绑定，玩家拿到书也用不了多半是权限没给。
- 改了附魔属性/等级上限后，已存在的物品不会自动更新，需要重新打附魔。
- toggle 只影响描述显示，不影响附魔实际效果，别拿它当开关用。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `ecoenchants.*` | 所有ecoenchants权限 | op |
| `ecoenchants.anvil.*` | 所有铁砧特权 | op |
| `ecoenchants.anvil.color` | 允许在砧座中使用颜色代码 | op |
| `ecoenchants.command.*` | 所有指令 | op |
| `ecoenchants.command.ecoenchants` | 允许使用/ecoenchants。 | True |
| `ecoenchants.command.enchant` | 允许使用/enchant。 | op |
| `ecoenchants.command.enchantinfo` | 允许使用/enchantinfo。 | True |
| `ecoenchants.command.giverandombook` | 允许随机赠送图书 | op |
| `ecoenchants.command.gui` | 允许使用/ecoenchants gui。 | True |
| `ecoenchants.command.reload` | 允许重新加载配置 | op |
| `ecoenchants.command.toggledescriptions` | 允许使用/ecoenchants切换描述。 | True |
| `ecoenchants.enchant` | 使用 /ee enchant 打附魔 | — |
| `ecoenchants.enchant.<附魔>` | 允许玩家使用/获得某个具体附魔 | — |
| `ecoenchants.givebook` | 发放附魔书 | — |
| `ecoenchants.gui` | 打开附魔界面 | — |
| `ecoenchants.reload` | 重载配置 | — |
