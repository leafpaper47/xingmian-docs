---
title: EcoEnchants
createTime: 2026/10/24
---

# 自定义附魔 · EcoEnchants

> 分类 ⚔️ 战斗与 RPG · 版本 `2026.34` · 指令 3 条 · api-version `1.21.8`

::: tip 自定义附魔系统，给物品加全新附魔
EcoEnchants 给服务器加一整套自定义附魔，超过原版附魔表能覆盖的效果，附魔以附魔书形式流通，可以在铁砧里合成叠加。它负责让装备和玩法有长期养成目标，通常和 EcoItems、EcoArmor 这类同作者插件以及经济、RPG 属性系统一起用。
:::

## 什么时候会用到它

- 想给玩家一套原版没有的附魔效果，比如爆炸挖矿、吸血、跳跃提升
- 需要发附魔书做活动奖励、开箱掉落或商店商品
- 玩家反馈铁砧里看不到附魔说明文字，要开关描述显示
- 排查某个附魔到底叫什么、效果范围多大，用指令快速查
- 管理员手动给玩家或手上物品点附魔做测试

## 上手流程

1. 先看权限：默认只有 op 能用 /enchant，普通玩家只开了 /ecoenchants 图形界面和 /enchantinfo
2. 用 /ecoenchants gui 打开附魔列表界面，确认插件已正常加载附魔数据
3. 用 /enchantinfo 查一个附魔的实际名称与效果，再决定怎么发给玩家
4. 发书用 /ecoenchants givebook 或 /ecoenchants giverandombook，玩家右键书即可附魔
5. 改完配置用 /ecoenchants reload 生效，不需要重启服务器

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/ecoenchants` | 主命令，打开界面、重载配置、发附魔书 | `/ecoenchants` | `ecoenchants.command.ecoenchants` |
| `/enchant` | 给玩家手上的物品附上指定自定义附魔 | `/enchant 附魔名 [等级]` | `ecoenchants.command.enchant` |
| `/enchantinfo` | 查看某个附魔的名称、等级与效果说明 | `/enchantinfo 附魔名` | `ecoenchants.command.enchantinfo` |

## 指令详解

### `/ecoenchants` — 主命令，打开界面、重载配置、发附魔书

- **语法**：`/ecoenchants`

- **示例**：

```
/ecoenchants
/ecoenchants gui
/ecoenchants reload
```

- **权限**：`ecoenchants.command.ecoenchants`
- **备注**：不带参数一般显示帮助与子指令列表。玩家权限 ecoenchants.command.ecoenchants 默认开启，但 gui 子指令另需 ecoenchants.command.gui，reload 另需 ecoenchants.command.reload（默认 op）。

### `/enchant` — 给玩家手上的物品附上指定自定义附魔

- **语法**：`/enchant 附魔名 [等级]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `附魔名` | 必填 | 自定义附魔的 id 或名称，可先用 /enchantinfo 确认 |
| `等级` | 可选 | 整数等级，省略时按默认一级处理 |


- **示例**：

```
/enchant explosive_mining
/enchant explosive_mining 3
```

- **权限**：`ecoenchants.command.enchant`
- **备注**：先把要附魔的物品拿在主手再执行。该命令权限 ecoenchants.command.enchant 默认仅 op，普通玩家无法使用。

### `/enchantinfo` — 查看某个附魔的名称、等级与效果说明

- **语法**：`/enchantinfo 附魔名`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `附魔名` | 必填 | 要查询的自定义附魔，支持按名称检索 |


- **示例**：

```
/enchantinfo explosive_mining
```

- **权限**：`ecoenchants.command.enchantinfo`
- **备注**：权限 ecoenchants.command.enchantinfo 默认对玩家开放，适合让玩家自己查附魔来源和效果。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `ecoenchants gui` | 打开附魔列表图形界面，可浏览全部自定义附魔 | `/ecoenchants gui` |
| `ecoenchants list` | 在聊天栏列出所有已加载的自定义附魔 | `/ecoenchants list` |
| `ecoenchants reload` | 重新加载配置与附魔数据，改完配置文件后用 | `/ecoenchants reload` |
| `ecoenchants givebook 玩家名 附魔名 等级` | 给指定玩家一本指定的附魔书 | `/ecoenchants givebook Steve explosive_mining 2` |
| `ecoenchants giverandombook 玩家名` | 给玩家一本随机附魔书，做奖励最常用 | `/ecoenchants giverandombook Steve` |
| `ecoenchants toggledescriptions` | 开关自己看到的附魔说明文字 | `/ecoenchants toggledescriptions` |

## 注意事项

::: warning
- 自定义附魔和原版附魔共用铁砧、附魔台入口，冲突或等级上限异常时先看 EcoEnchants 的配置与附魔定义，不要先怀疑原版机制
- 给玩家开 /enchant 权限前想清楚：这条命令可以绕过经济与获取难度直接上附魔，一般只留给管理员
- 改配置后一定要 /ecoenchants reload 并实际拿书试一次，部分附魔效果要重载后才注册进事件
- 附魔描述在铁砧里显示不全是客户端与权限问题，先让玩家执行 toggledescriptions 或检查 anvil.color 类权限
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

## 相关插件

EcoItems、EcoArmor、[Vault](/commands/core/vault.md)、[PlaceholderAPI](/commands/config/placeholderapi.md)
