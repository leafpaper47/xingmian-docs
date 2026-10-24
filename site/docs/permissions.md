---
title: 权限节点总表
createTime: 2026/10/24
---

# 权限节点总表

下表汇总了各插件 `plugin.yml` 中声明的权限节点。默认值 `op` 表示仅管理员组默认拥有，`true` 表示所有玩家默认拥有。

::: warning
LuckPerms 等权限插件会覆盖这里的默认值。实际生效权限请以 `lp group <组> permission info` 或游戏内测试为准。
:::

## 🛡️ 基础与权限

| 插件 | 节点 | 说明 | 默认 |
| --- | --- | --- | --- |
| [ConsoleSpamFixReborn](/commands/core/consolespamfixreborn.md) | `csf.admin` | 管理员命令访问。 | op |
| [MaintenanceMode](/commands/core/maintenancemode.md) | `maintenance.bypass` | 免除维护模式限制（不被踢、可进服） | op |
| [MaintenanceMode](/commands/core/maintenancemode.md) | `maintenance.use` | 允许使用维护模式指令 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.admin` | 允许使用所有PlugMan命令。 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.check` | 允许使用check命令。 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.check.all` | 允许使用check all命令。 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.deps` | 允许使用deps命令。 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.disable` | 允许使用disable命令。 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.disable.all` | 允许使用disable all命令。 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.dump` | 允许使用dump命令。 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.enable` | 允许使用enable命令。 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.enable.all` | 允许使用enable all命令。 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.help` | 允许使用help命令。 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.info` | 允许使用info命令。 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.list` | 允许使用list命令。 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.load` | 允许使用load命令。 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.lookup` | 允许使用查找命令。 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.reload` | 允许使用reload命令。 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.reloadconfig` | 允许使用reload config命令。 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.reloadmode` | 允许使用reload mode命令。 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.restart` | 允许使用重新启动命令。 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.restart.all` | 允许使用RESTART ALL命令。 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.unload` | 允许使用unload命令。 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.update` | 允许玩家查看更新警报。 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.usage` | 允许使用usage命令。 | op |
| [Vault](/commands/core/vault.md) | `vault.admin` | 授予对管理工具的访问权限。 | op |
| [Vault](/commands/core/vault.md) | `vault.update` | 当避难所需要更新时通知玩家。 | op |

## 🧰 基础工具

| 插件 | 节点 | 说明 | 默认 |
| --- | --- | --- | --- |
| [ALCERecipeViewer](/commands/essentials/alcerecipeviewer.md) | `alcerecipeviewer.admin` | 允许使用管理命令（重载数据） | op |
| [ALCERecipeViewer](/commands/essentials/alcerecipeviewer.md) | `alcerecipeviewer.use` | 允许使用 /alcerecipes 查看合成配方 | True |
| [ArmoredElytra](/commands/essentials/armoredelytra.md) | `xingmian.armoredelytra.bypass` | 绕过锻造台合成限制（OP使用） | op |
| [ArmoredElytra](/commands/essentials/armoredelytra.md) | `xingmian.armoredelytra.use` | 允许使用装甲鞘翅合成/穿戴 | — |
| [ArmorUnbreaking](/commands/essentials/armorunbreaking.md) | `armorunbreaking.admin` | 允许使用 /armordura | op |
| [BookEdit](/commands/essentials/bookedit.md) | `bookedit.use` | 允许修改自己写的书（作者改匿名、设为破旧） | True |
| [CraftBench](/commands/essentials/craftbench.md) | `craftbench.admin` | 允许管理配方 | op |
| [CraftBench](/commands/essentials/craftbench.md) | `craftbench.use` | 允许使用合成台 | True |
| [Essentials](/commands/essentials/essentials.md) | `essentials.*` | 默认让 OP 玩家拥有全部权限 | op |
| [Essentials](/commands/essentials/essentials.md) | `essentials.afk` | 允许访问/afk命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.afk.auto` | 拥有此权限的玩家在配置文件中定义的无操作时间段后将被设置为afk | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.afk.kickexempt` | 拥有此权限的玩家不会因为是AFK而被踢出 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.afk.message` | 允许玩家设置自定义AFK消息 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.afk.others` | 允许玩家设置其他玩家的AFK状态 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.antioch` | 允许访问/antioch命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.anvil` | 允许访问/anvil命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.back` | 允许访问/back命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.back.into.<world>` | 允许玩家使用/back命令前往特定世界 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.back.ondeath` | 拥有此权限的玩家将在死亡期间存储返回位置 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.back.onteleport` | 拥有此权限的玩家将在任何传送过程中存储返回位置 | True |
| [Essentials](/commands/essentials/essentials.md) | `essentials.back.others` | 允许其他玩家访问/back命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.backup` | 允许访问/backup命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.balance` | 允许访问/balance命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.balance.others` | 允许使用/balance命令查看其他玩家的余额 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.balancetop` | 允许访问/balancetop命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.balancetop.exclude` | 拥有此权限的玩家将被排除在平衡台之外 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.balancetop.force` | 允许访问强制刷新平衡顶列表 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ban` | 允许访问/ban命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ban.exempt` | 防止指定的群组或玩家被封禁 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ban.notify` | 允许在玩家被禁用时通知持有人 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ban.offline` | 允许离线玩家访问/ban命令，这可能反过来用于禁止离线的豁免玩家 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.banip` | 允许访问/banip命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.banip.notify` | 允许在玩家被禁用时通知持有人 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.beezooka` | 允许访问/beezooka命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.bigtree` | 允许访问/bigtree命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.book` | 允许访问/book命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.book.author` | 允许使用/book命令访问编辑图书作者 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.book.others` | 允许使用/book命令编辑其他玩家的书籍 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.book.title` | 允许使用/book命令编辑图书标题 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.bottom` | 允许访问/bottom命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.break` | 允许访问/break命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.break.bedrock` | 允许访问基岩的/break命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.broadcast` | 允许访问/broadcast命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.broadcastworld` | 允许访问/broadcastworld命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.burn` | 允许访问/burn命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.cartographytable` | 允许访问/cartographytable命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.chat.ignoreexempt` | 拥有此权限的人员将不会被忽略，即使他们在其他人员忽略列表中 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.chat.spy` | 允许承载者查看所有本地聊天消息，无论其是否靠近发件人 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.chat.spy.exempt` | 允许承载免除本地聊天间谍权限 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.clearinventory` | 允许访问/clearinventory命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.clearinventory.all` | 允许使用/clearinventory命令清除所有玩家的库存 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.clearinventory.others` | 允许使用/clearinventory命令清除其他玩家的库存 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.clearinventoryconfirmtoggle` | 允许访问/clearinventoryconfirmtoggle命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.commandcooldowns.bypass` | 允许绕过所有命令冷却时间 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.commandcooldowns.bypass.<commandname>` | 允许绕过特定命令的冷却时间 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.compass` | 允许访问/compass命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.condense` | 允许访问/condense命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.createkit` | 允许访问/createkit命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.customtext` | 允许访问/customtext命令和所有别名 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.delhome` | 允许访问/delhome命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.delhome.others` | 允许使用/delhome命令删除其他玩家主页 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.deljail` | 允许访问/deljail命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.delkit` | 允许访问/delkit命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.delwarp` | 允许访问/delwarp命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.depth` | 允许访问/depth命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.disposal` | 允许访问/disposal命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.eco` | 允许访问/eco命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.eco.loan` | 允许持有人拥有负余额 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.editsign` | 允许访问/editsign命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.editsign.color` | 允许持有人在标志上使用颜色代码 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.editsign.format` | 允许持有人在标志上使用格式代码 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.editsign.magic` | 允许持有人在标志上使用魔法代码 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.editsign.rgb` | 允许持有人在标志上使用RGB代码 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.editsign.unlimited` | 允许持有人超过标志上的15个字符限制 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.editsign.waxed.exempt` | 允许持有人编辑打蜡标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.enchant` | 允许访问/enchant命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.enchantments.<enchantment>` | 允许持有人使用/enchant命令使用特定的魔法 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.enchantments.allowunsafe` | 允许携带者使用不安全的附魔物品 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.enderchest` | 允许访问/enderchest命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.enderchest.modify` | 允许持有人修改其他玩家的义务 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.enderchest.others` | 允许其他玩家访问/enderchest命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.essentials` | 允许访问/essentials命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.exempt` | 豁免许多版主操作的父级权限 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.exp` | 允许使用 /exp 指令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.exp.give` | 允许持有人为自己提供经验 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.exp.give.others` | 允许持有人为其他玩家提供经验 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.exp.others` | 允许持有人查看其他玩家的体验 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.exp.set` | 允许持有人为自己设置体验 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.exp.set.others` | 允许持有人为其他玩家设置经验 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ext` | 允许访问/ext命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ext.others` | 允许其他玩家访问/ext命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.feed` | 允许访问/feed命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.feed.others` | 允许其他玩家访问/feed命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball` | 允许访问/fireball命令。每种类型的火球都需要额外的权限。 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.arrow` | 允许访问/fireball命令中的箭头 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.dragon` | 允许在/fireball命令中使用龙 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.egg` | 允许访问/fireball命令中的egg | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.fireball` | 允许访问/fireball命令中的fireball | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.large` | 允许访问/fireball命令中的大火球 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.lingeringpotion` | 允许在/fireball命令中使用挥之不去的药水 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.skull` | 允许在/fireball命令中使用头骨 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.small` | 允许访问/fireball命令中的小火球 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.snowball` | 允许访问/fireball命令中的雪球 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.splashpotion` | 允许访问/fireball命令中的飞溅药水 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.trident` | 允许访问/fireball命令中的三叉戟 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.firework` | 允许访问/firework命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.firework.fire` | 允许携带者使用烟花命令启动手中的烟花副本 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.firework.multiple` | 允许携带者使用烟花指令发射多支烟花 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fly` | 允许访问/fly命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fly.others` | 允许其他玩家访问/fly命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fly.safelogin` | 如果此权限的持有者在空中登录，他们将被置于飞行模式 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.gamemode` | 允许访问/gamemode命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.gamemode.*` | 允许使用/gamemode命令访问所有游戏模式 | op |
| [Essentials](/commands/essentials/essentials.md) | `essentials.gamemode.adventure` | 允许使用/gamemode命令访问冒险游戏模式 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.gamemode.all` | 允许使用/gamemode命令访问所有游戏模式 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.gamemode.creative` | 允许使用/gamemode命令访问创意游戏模式 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.gamemode.others` | 允许其他玩家访问/gamemode命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.gamemode.spectator` | 允许使用/gamemode命令访问旁观者游戏模式 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.gamemode.survival` | 允许使用/gamemode命令访问生存游戏模式 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.gc` | 允许访问/gc命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.getpos` | 允许访问/getpos命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.getpos.others` | 允许其他玩家访问/getpos命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.give` | 允许访问/give命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.give.item-<item-name>` | 允许在启用基于权限的项目生成时访问特定项目的/give命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.give.item-all` | 允许在启用基于权限的项目生成时访问所有项目的/give命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.god` | 允许访问/god命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.god.others` | 允许其他玩家访问/god命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.god.pvp` | 允许持有者在上帝模式下攻击玩家 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.grindstone` | 允许访问/grindstone命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.hat` | 允许访问/hat命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.hat.ignore-binding` | 允许持有者在为物品配备了绑定诅咒时使用/hat命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.hat.prevent-type.<item-name>` | 防止玩家对指定项目使用/hat命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.heal` | 允许访问/heal命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.heal.others` | 允许其他玩家访问/heal命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.help` | 允许访问/help命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.help.<plugin-name>` | 允许访问特定插件的/help命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.helpop` | 允许访问/helpop命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.helpop.receive` | 允许持有人接收帮助消息 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.home` | 允许访问/home命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.home.bed` | 允许访问床的/home命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.home.compass` | 将玩家的指南针指向他们的第一个主页。需要在配置中启用compass-towards-home-per | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.home.others` | 允许使用/home命令传送到其他玩家家园 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ice` | 允许使用 /ice 指令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ice.others` | 允许对其他玩家使用 /ice 指令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ignore` | 允许访问/ignore命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.info` | 允许访问/info命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.invsee` | 允许访问/invsee命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.invsee.equip` | 允许使用/invsee命令查看盔甲槽中的项目 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.invsee.modify` | 允许使用/invsee命令访问修改其他玩家库存中的项目 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.invsee.preventmodify` | 防止其他玩家修改玩家库存。 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.item` | 允许访问/item命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemdb` | 允许访问/itemdb命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemlore` | 允许访问/itemlore命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemname` | 允许访问/itemname命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemname.color` | 允许使用彩色文本访问/itemname命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemname.format` | 允许访问带有格式文本的/itemname命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemname.magic` | 允许使用魔术文本访问/itemname命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemname.prevent-type.<item-name>` | 防止玩家对指定项目使用/itemname命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemname.rgb` | 允许访问带有RGB文本的/itemname命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemspawn.exempt` | 允许持有人生成项目黑名单中的项目 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemspawn.meta-author` | 允许承载使用作者元数据生成项目 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemspawn.meta-book` | 允许承载从book.txt中生成具有预填充内容的项目 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemspawn.meta-chapter-<chapter>` | 仅允许持有人使用/give命令从book.txt.中生成特定的书籍。 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemspawn.meta-firework` | 允许持有者使用烟花元数据生成项目 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemspawn.meta-head` | 允许持有人生成具有头部元数据的项目 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemspawn.meta-lore` | 允许持有人生成具有知识元数据的项目 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemspawn.meta-title` | 允许持有人生成具有标题元数据的项目 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jail.allow-block-damage` | 允许持有人在入狱期间损坏格挡 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jail.allow-break` | 允许持票人在入狱时打破障碍 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jail.allow-interact` | 允许持有人在入狱时与区块进行交互 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jail.allow-place` | 允许持有人在入狱时放置区块 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jail.allow.<command>` | 允许持有人在被监禁时使用指定的命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jail.exempt` | 防止指定的组或玩家被监禁 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jail.notify` | 允许在其他玩家被监禁时通知持有人 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jailedplayers` | 允许访问/jailedplayers命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jails` | 允许访问/jails命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.joinfullserver` | 允许加入服务器，即使服务器已满 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jump` | 允许访问/jump命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jump.lock` | 允许访问/jump lock命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.keepinv` | 控制玩家是否在死亡时保留库存。 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.keepxp` | 允许用户在死亡时保留经验值，而不是将其丢弃。 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kick` | 允许访问/kick命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kick.exempt` | 防止玩家被踢出。 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kick.notify` | 允许在其他玩家被踢出时通知持有人 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kickall` | 允许访问/kickall命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kickall.exempt` | 防止玩家被/kickall踢出 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kill` | 允许访问/kill命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kill.exempt` | 防止玩家被击杀/击杀 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kill.force` | 允许持票人被杀/杀死，即使他们的死亡被取消 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kit` | 允许访问/kit命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kit.exemptdelay` | 免除您的套件延迟功能，这会影响标志和命令。 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kit.others` | 允许其他玩家访问/kit命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kitreset` | 允许访问/kitreset命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kitreset.others` | 允许使用/kitreset命令重置其他玩家套件 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kits.*` | 允许访问所有套件 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kits.<kit-name>` | 允许访问特定套件 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kittycannon` | 允许访问/kittycannon命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.lightning` | 允许访问/lightning命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.lightning.others` | 允许其他玩家访问/lightning命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.list` | 允许访问/list命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.list.hidden` | 允许在/list命令中查看隐藏的玩家 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.loom` | 允许访问/loom命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mail` | 允许访问/mail命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mail.clear.others` | 允许使用/mail命令清除其他玩家的邮件 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mail.clearall` | 允许使用/mail命令清除所有邮件 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mail.send` | 允许使用/mail命令访问发送邮件 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mail.sendall` | 允许使用/mail命令向所有玩家发送邮件 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mail.sendtemp` | 允许使用/mail命令访问发送临时邮件 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.me` | 允许访问/me命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.more` | 允许访问/more命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.motd` | 允许访问/motd命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.msg` | 允许访问/msg命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.msg.color` | 允许使用彩色文本访问/msg命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.msg.format` | 允许访问带有格式文本的/msg命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.msg.magic` | 允许使用魔术文本访问/msg命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.msg.multiple` | 允许使用/msg命令向多个玩家发送消息 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.msg.rgb` | 允许使用RGB文本访问/msg命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.msg.url` | 允许访问/msg命令中的发送URL | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.msgtoggle` | 允许访问/msgtoggle命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.msgtoggle.bypass` | 允许持有人绕过其他玩家的msgtoggle设置 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.msgtoggle.others` | 允许其他玩家访问/msgtoggle命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mute` | 允许访问/mute命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mute.exempt` | 防止指定的组或玩家被静音 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mute.notify` | 允许在其他玩家被静音时通知持有人 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mute.offline` | 允许访问静音离线播放器 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mute.unlimited` | 允许持有人覆盖最大静音时间设置 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.near` | 允许访问/near命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.near.exclude` | 如果玩家应被排除在近距离查找之外。 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.near.maxexempt` | 允许承载绕过/near命令的半径限制 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.near.others` | 允许其他玩家访问/near命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nick` | 允许访问/nick命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nick.allowunsafe` | 如果玩家有这个，他们可以将其用户名设置为任何值。请谨慎使用，因为这有可能破坏用户数据文件。 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nick.blacklist.bypass` | 允许持有人绕过昵称黑名单 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nick.changecolors` | 允许持有人* *仅* *更改其昵称的颜色 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nick.color` | 允许使用彩色文本访问/nick命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nick.format` | 允许访问带有格式文本的/nick命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nick.hideprefix` | 拥有此权限的玩家将不会应用昵称前缀 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nick.magic` | 允许使用魔术文本访问/nick命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nick.others` | 允许其他玩家访问/nick命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nick.rgb` | 允许访问带有RGB文本的/nick命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nocommandcost.<command>` | 允许持有人免费使用指定的命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nocommandcost.all` | 允许持有人免费使用所有命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nuke` | 允许访问/nuke命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.oversizedstacks` | 允许承载生成超大堆栈 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.pay` | 允许访问/pay命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.pay.multiple` | 允许使用/pay命令向多个玩家付款 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.pay.offline` | 允许使用/pay命令向离线玩家付款 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.payconfirmtoggle` | 允许访问/payconfirmtoggle命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.paytoggle` | 允许访问/paytoggle命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ping` | 允许访问/ping命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.playtime` | 允许访问/playtime命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.playtime.others` | 允许其他玩家访问/playtime命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.potion` | 允许访问/potion命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.potion.<potion-type>` | 允许访问特定药剂类型的/potion命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.potion.apply` | 允许访问/potion apply命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.powertool` | 允许访问/powertool命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.powertool.append` | 允许访问将多个命令添加到动力工具 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.powertoollist` | 允许访问/powertoollist命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.powertooltoggle` | 允许访问/powertooltoggle命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ptime` | 允许访问/ptime命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ptime.others` | 允许其他玩家访问/ptime命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.pvpdelay.exempt` | 允许承载绕过pvp延迟设置 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.pweather` | 允许访问/pweather命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.pweather.others` | 允许其他玩家访问/pweather命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.realname` | 允许访问/realname命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.recipe` | 允许访问/recipe命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.remove` | 允许访问/remove命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.renamehome` | 允许访问/renamehome命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.renamehome.others` | 允许使用/renamehome命令重命名其他玩家主页 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.repair` | 允许访问/repair命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.repair.all` | 允许访问/repair all命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.repair.armor` | 允许访问/repair armor命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.repair.enchanted` | 允许访问对附魔物品使用/repair命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.rest` | 允许访问/rest命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.rest.others` | 允许其他玩家访问/rest命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.rtoggle` | 允许访问/rtoggle命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.rules` | 允许访问/rules命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.seen` | 允许访问/seen命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.seen.alts` | 允许使用alts访问/seen命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.seen.banreason` | 允许使用禁止原因访问/seen命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.seen.extra` | 允许访问带有额外信息的/seen命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.seen.firstlogin` | 允许在首次登录时访问/seen命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.seen.ip` | 允许使用IP地址访问/seen命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.seen.ipsearch` | 允许使用/seen命令访问IP地址 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.seen.location` | 允许通过位置访问/seen命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.seen.uuid` | 允许使用UUID访问/seen命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.seen.whitelist` | 允许以白名单状态访问/seen命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sell` | 允许访问/sell命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sell.bulk` | 允许使用/sell命令访问批量销售项目 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sell.hand` | 允许使用/sell命令出售手头的商品 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sethome` | 允许访问/sethome命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sethome.bed` | 允许玩家在白天右键单击床以更新其“床”主页。 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sethome.multiple` | 允许使用/sethome命令设置多个房源 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sethome.multiple.<set name>` | 将房源数量限制提高到配置中定义的特定数量 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sethome.multiple.unlimited` | 允许使用/sethome命令设置无限个房源 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sethome.others` | 允许使用/sethome命令设置其他玩家主页 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.setjail` | 允许访问/setjail命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.settpr` | 允许访问/settpr命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.setwarp` | 允许访问/setwarp命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.setworth` | 允许访问/setworth命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.showkit` | 允许访问/showkit命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.balance` | 允许持票人打破平衡标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.buy` | 允许持票人打破买入标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.disposal` | 允许持有人打破处置标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.enchant` | 允许持有人打破附魔标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.free` | 允许持票人打破自由标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.gamemode` | 允许持有人打破游戏模式标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.heal` | 允许持有人打破治疗标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.info` | 允许持有人破坏信息标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.kit` | 允许持有人打破试剂盒标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.mail` | 允许持票人打破邮件标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.protection` | 允许承载者打破保护标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.repair` | 允许持票人打破维修标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.sell` | 允许持票人打破卖出标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.spawnmob` | 允许持有人打破产卵怪迹象 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.time` | 允许持有人打破时间标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.trade` | 允许持票人打破贸易标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.warp` | 允许持有人打破曲速标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.weather` | 允许持票人打破天气标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.color` | 允许持有人创建和使用彩色标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.balance` | 允许持有人创建平衡标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.buy` | 允许持票人创建购买标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.disposal` | 允许持有人创建处置标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.enchant` | 允许持有人创建附魔标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.free` | 允许持有人创建免费标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.gamemode` | 允许持有人创建游戏模式标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.heal` | 允许持有人创建治疗标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.info` | 允许持有人创建信息标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.kit` | 允许持有人创建试剂盒标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.mail` | 允许持票人创建邮件标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.protection` | 允许持有人创建保护标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.repair` | 允许持有人创建维修标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.sell` | 允许持有人创建卖出标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.spawnmob` | 允许持有人创建spawnmob标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.time` | 允许持有人创建时间标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.trade` | 允许持票人创建商标 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.warp` | 允许持有人创建经纱标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.weather` | 允许持有人创建天气标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.enchant.allowunsafe` | 允许持有人创建和使用不安全的附魔标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.format` | 允许持有人创建和使用格式标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.magic` | 允许持有人创建和使用魔法标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.protection.override` | 允许持有人打破其他玩家创建的标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.rgb` | 允许持有人创建和使用RGB标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.trade.override` | 允许持票人打破其他玩家创建的商标 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.trade.override.collect` | 允许持票人从其他玩家创建的商标中收集道具 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.balance` | 允许持票人使用平衡标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.buy` | 允许持票人使用购买标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.disposal` | 允许持有人使用处置标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.enchant` | 允许持有人使用附魔标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.free` | 允许持有人使用自由标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.gamemode` | 允许持有人使用游戏模式标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.heal` | 允许持有者使用治疗告示牌 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.info` | 允许持有人使用信息标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.kit` | 允许持有人使用套件标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.mail` | 允许持票人使用邮件标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.protection` | 允许持有人使用保护标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.repair` | 允许持票人使用维修标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.sell` | 允许持有人使用卖出标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.spawnmob` | 允许持有人使用spawnmob标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.time` | 允许持有人使用时间标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.trade` | 允许持票人使用商标 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.warp` | 允许持有人使用经纱标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.weather` | 允许持有人使用天气标志 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.silentjoin` | 允许静默加入 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.silentjoin.vanish` | 允许静默加入，并进入消失模式 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.silentquit` | 禁止具有此权限的用户离开/退出消息。 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.skull` | 允许访问/skull命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.skull.modify` | 允许使用/skull命令修改其他玩家的头骨 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.skull.others` | 允许使用/skull命令创建其他玩家的头骨 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.skull.spawn` | 允许使用/skull命令生成头骨 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sleepingignored` | 允许持票人无需睡觉即可度过夜晚 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.smithingtable` | 允许访问/smithingtable命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.socialspy` | 允许访问/socialspy命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.socialspy.others` | 允许其他玩家访问/socialspy命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.spawner` | 允许访问/spawner命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.spawner.*` | 允许访问使用/spawner命令将spawner的类型设置为所有类型 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.spawner.<mob-type>` | 允许访问使用/spawner命令将spawner的类型设置为特定类型 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.spawner.delay` | 允许使用/spawner命令访问以设置生成器的延迟 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.spawnerconvert.*` | 允许承载者放置任何类型的产卵器 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.spawnerconvert.<mob-type>` | 允许持有人放置特定类型的产卵器 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.spawnmob` | 允许访问/spawnmob命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.spawnmob.*` | 允许使用/spawnmob命令生成所有mob | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.spawnmob.<mob-type>` | 允许使用/spawnmob命令生成特定的mob | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.spawnmob.stack` | 允许使用/spawnmob命令访问堆栈中的生成mob | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.speed` | 允许访问/speed命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.speed.bypass` | 允许承载绕过配置中设置的速度限制 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.speed.fly` | 允许访问飞行速度的/speed命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.speed.others` | 允许其他玩家访问/speed命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.speed.walk` | 允许访问步行速度的/speed命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.stonecutter` | 允许访问/stonecutter命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sudo` | 允许访问/sudo命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sudo.exempt` | 防止玩家被其他用户使用 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sudo.multiple` | 允许多个玩家访问/sudo命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.suicide` | 允许多个玩家访问/suicide命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.teleport.cooldown.bypass.back` | 如果玩家没有此权限，/back将具有冷却时间，即使使用父旁路烫印 | True |
| [Essentials](/commands/essentials/essentials.md) | `essentials.teleport.cooldown.bypass.tpa` | 如果玩家没有此权限，/tpa将具有冷却时间，即使有父旁路perm | True |
| [Essentials](/commands/essentials/essentials.md) | `essentials.teleport.timer.bypass` | 允许承载绕过传送延迟 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.teleport.timer.move` | 允许携带者在等待传送时移动 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tempban` | 允许访问/tempban命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tempban.exempt` | 防止指定的组或玩家被临时禁用 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tempban.offline` | 允许访问临时禁用离线玩家 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tempban.unlimited` | 允许持有人覆盖max-tempban-time设置 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tempbanip` | 允许访问/tempbanip命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.thunder` | 允许访问/thunder命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.time` | 允许访问/time命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.time.set` | 允许访问使用/time命令设置时间 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.time.world.all` | 允许访问使用/time命令设置所有世界的时间 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.togglejail` | 允许访问/togglejail命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.togglejail.offline` | 允许离线玩家访问/togglejail命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.top` | 允许访问/top命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tp` | 允许访问/tp命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tp.others` | 允许使用/tp命令远程传送给其他用户 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tp.position` | 允许使用/tp命令传送到某个位置 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpa` | 允许访问/tpa命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpaall` | 允许访问/tpaall命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpacancel` | 允许访问/tpaccept命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpaccept` | 允许访问/tpaccept命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpahere` | 允许访问/tpahere命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpall` | 允许访问/tpall命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpauto` | 允许访问/tpauto命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpauto.others` | 允许其他玩家访问/tpauto命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpdeny` | 允许访问/tpdeny命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tphere` | 允许访问/tphere命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpo` | 允许访问/tpo命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpoffline` | 允许访问/tpoffline命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpohere` | 允许访问/tpohere命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tppos` | 允许访问/tppos命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpr` | 允许访问/tpr命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tptoggle` | 允许访问/tptoggle命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tptoggle.others` | 允许其他玩家访问/tptoggle命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tree` | 允许访问/tree命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.unban` | 允许访问/unban命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.unbanip` | 允许访问/unbanip命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.unlimited` | 允许访问/unlimited命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.unlimited.item-<item-name>` | 允许在启用基于权限的项目生成时访问特定项目的/unlimited命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.unlimited.item-all` | 允许在启用基于权限的项目生成时访问所有项目的/unlimited命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.unlimited.item-bucket` | 允许访问水桶和熔岩的/unlimited命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.unlimited.others` | 允许其他玩家访问/unlimited命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.updatecheck` | 持有人将收到EssentialsX更新的通知 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.vanish` | 允许访问/vanish命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.vanish.effect` | 在消失模式下对玩家应用隐身效果 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.vanish.interact` | 允许持有人在消失模式下与玩家互动 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.vanish.others` | 允许其他玩家访问/vanish命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.vanish.pickup` | 允许持票人在消失模式下领取物品 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.vanish.pvp` | 允许持有者在消失模式下攻击玩家 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.vanish.see` | 允许持有人在消失模式下看到其他玩家 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.version` | 允许访问/version命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.warp` | 允许访问/warp命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.warp.list` | 允许访问/warp list命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.warp.others` | 允许其他玩家访问/warp命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.warp.overwrite.*` | 允许承载覆盖所有翘曲 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.warp.overwrite.<warp-name>` | 允许承载覆盖特定曲线 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.warpinfo` | 允许访问/warpinfo命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.weather` | 允许访问/weather命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.whitelist.bypass` | 允许玩家加入服务器，即使他们没有列入白名单。 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.whois` | 允许访问/whois命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.whois.ip` | 允许使用IP地址访问/whois命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.workbench` | 允许访问/workbench命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.world` | 允许访问/world命令 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.worlds.<world-name>` | 允许使用各种命令访问特定世界 | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.worth` | 允许访问/worth命令 | — |
| [InBlock](/commands/essentials/inblock.md) | `Inblock.give` | 允许给予自定义方块物品 | op |
| [InBlock](/commands/essentials/inblock.md) | `Inblock.open` | 允许打开仓库界面 | op |
| [InBlock](/commands/essentials/inblock.md) | `Inblock.reload` | 允许重载配置 | op |
| [InfiniteFuel](/commands/essentials/infinitefuel.md) | `infinitefuel.admin` | — | op |
| [InvSaver](/commands/essentials/invsaver.md) | `invSaver.list` | — | op |
| [InvSaver](/commands/essentials/invsaver.md) | `invSaver.preview` | — | op |
| [InvSaver](/commands/essentials/invsaver.md) | `invSaver.reload` | — | op |
| [InvSaver](/commands/essentials/invsaver.md) | `invSaver.restore` | — | op |
| [InvSaver](/commands/essentials/invsaver.md) | `invSaver.save` | — | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.admin` | 拥有该插件的全部权限 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.bypass.*` | 拥有该插件的全部权限 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.bypass.censure` | 编辑项目时绕过单词限制 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.bypass.lore_length_limit` | 在配置上设置的知识线最大长度的旁路限制 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.bypass.lore_line_limit` | 绕过配置上设置的知识线数量的限制 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.bypass.lore_type_restriction` | 编辑项目知识时绕过类型限制 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.bypass.rename_length_limit` | 绕过配置上设置的重命名行最大长度的限制 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.bypass.rename_type_restriction` | 重命名项目时绕过类型限制 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.creativeuser` | 拥有该插件的全部权限 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.*` | 授予对command/itemedit的完全访问权限 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.amount` | 允许编辑项目金额 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.armortrim` | 允许在盔甲上设置修剪 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.axolotlvariant` | 允许在axolotl桶上编辑axolotl变体 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.banner` | 允许编辑横幅 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.bookauthor` | 允许编辑图书作者 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.bookenchant` | 允许编辑书籍附魔剂 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.bookenchant.bypass_max_level` | 允许编辑高于香草限制的书籍附魔剂 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.booktype` | 允许编辑图书类型 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.color` | 允许编辑项目颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.color.firework_star` | 允许编辑烟花星星颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.color.leather` | 允许编辑皮革颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.color.potion` | 允许编辑药水颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.color.tipped_arrow` | 允许编辑提示箭头颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.compass` | 允许编辑罗盘位置 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.custommodeldata` | 允许编辑项目的自定义模型数据 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.damage` | 允许编辑项目耐久度-伤害 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.enchant` | 允许编辑物品附魔 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.enchant.bypass_max_level` | 允许编辑高于香草限制的物品附魔剂 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.equipment` | 允许设置设备属性 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.fireresistent` | 允许设置此堆栈的耐火性 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.firework` | 允许使用GUI编辑烟花 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.fireworkpower` | 允许编辑烟花动力 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.food` | 允许编辑药水效果 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.food.bypass_limits` | 允许编辑2级以上的药水效果 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.glider` | 允许设置项目行为 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.glow` | 允许设置发光视觉效果 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.goathornsound` | 允许编辑山羊喇叭声 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.hide` | 允许编辑项目标记 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.hideall` | 允许一次隐藏所有项目标志 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.hidetooltip` | 允许隐藏工具提示 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.itemmodel` | 允许设置项目纹理模型 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.listaliases` | 显示别名 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore` | 允许编辑物品的说明文本 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.*` | 允许编辑项目知识并使用所有颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.aqua` | 允许编辑项目知识并使用水蓝色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.black` | 允许编辑项目知识并使用黑色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.blue` | 允许编辑项目知识并使用蓝色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.dark_aqua` | 允许编辑项目知识并使用dark_aqua颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.dark_blue` | 允许编辑项目知识并使用DARK_BLUE颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.dark_gray` | 允许编辑项目知识并使用DARK_GREY颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.dark_green` | 允许编辑项目知识并使用DARK_GREEN颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.dark_purple` | 允许编辑项目知识并使用DARK_PURPLE颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.dark_red` | 允许编辑项目知识并使用DARK_RED颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.gold` | 允许编辑项目知识并使用金色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.gray` | 允许编辑项目知识并使用灰色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.green` | 允许编辑项目知识并使用绿色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.hexa` | 允许编辑项目知识并使用十六进制颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.light_purple` | 允许编辑项目知识并使用LIGHT_PURPLE颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.red` | 允许编辑项目知识并使用红色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.white` | 允许编辑项目知识并使用白色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.yellow` | 允许编辑项目知识并使用黄色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.copy` | 允许使用lore子命令copy, copybook和copyfile | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.format.*` | 允许编辑项目知识并使用所有格式 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.format.bold` | 允许编辑项目知识并使用粗体格式 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.format.italic` | 允许编辑项目知识并使用斜体格式 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.format.magic` | 允许编辑项目知识并使用魔法格式 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.format.reset` | 允许编辑项目知识并使用重置格式 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.format.strikethrough` | 允许编辑项目知识并使用删除线格式 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.format.underline` | 允许编辑项目知识并使用下划线格式 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.minimessage` | 允许使用最小消息占位符编辑项目知识 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.maxstacksize` | 允许设置最大堆栈大小 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.potioneffect` | 允许编辑药水效果 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.potioneffect.bypass_limits` | 允许编辑2级以上的药水效果 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rarity` | 允许设置项目的稀有度 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename` | 允许编辑项目名称 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.*` | 允许编辑项目名称并使用所有颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.aqua` | 允许编辑项目名称并使用水蓝色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.black` | 允许编辑项目名称并使用黑色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.blue` | 允许编辑项目名称并使用蓝色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.dark_aqua` | 允许编辑项目名称并使用dark_aqua颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.dark_blue` | 允许编辑项目名称并使用DARK_BLUE颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.dark_gray` | 允许编辑项目名称并使用DARK_GREY颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.dark_green` | 允许编辑项目名称并使用DARK_GREEN颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.dark_purple` | 允许编辑项目名称并使用DARK_PURPLE颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.dark_red` | 允许编辑项目名称并使用DARK_RED颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.gold` | 允许编辑项目名称并使用金色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.gray` | 允许编辑项目名称并使用灰色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.green` | 允许编辑项目名称并使用绿色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.hexa` | 允许编辑项目名称并使用十六进制颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.light_purple` | 允许编辑项目名称并使用LIGHT_PURPLE颜色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.red` | 允许编辑项目名称并使用红色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.white` | 允许编辑项目名称并使用白色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.yellow` | 允许编辑项目名称并使用黄色 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.format.*` | 允许编辑项目名称并使用所有格式 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.format.bold` | 允许编辑项目名称并使用粗体格式 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.format.italic` | 允许编辑项目名称并使用斜体格式 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.format.magic` | 允许编辑项目名称并使用魔术格式 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.format.reset` | 允许编辑项目名称并使用重置格式 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.format.strikethrough` | 允许编辑项目名称并使用删除线格式 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.format.underline` | 允许编辑项目名称并使用下划线格式 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.minimessage` | 允许使用最小消息占位符编辑项目名称 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.repaircost` | 允许编辑维修费用 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.repaircost.without_durability` | 即使在没有耐久性的物品上也允许设置维修成本 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.skullowner` | 允许编辑颅骨皮肤所有者 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.spawnereggtype` | 允许编辑怪物的蛋 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.tropicalfish` | 允许编辑热带鱼桶 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.type` | 允许编辑物料材料 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.unbreakable` | 允许编辑项目不可破解 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemeditimport` | 授予对命令/itemeditimport的完全访问权限 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemeditinfo` | 授予对command/itemeditinfo的完全访问权限 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemeditreload` | 授予对命令/itemeditreload的完全访问权限 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemstorage.*` | 提供对命令/itemstorage | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemstorage.delete` | 允许删除已存储的物品 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemstorage.get` | 允许获取存储的物料 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemstorage.save` | 允许存储物品 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemstorage.show` | 允许查看已存储的物品 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemstorage.update` | 允许更新已存储的物品 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.*` | 授予对命令/serveritem | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.buy` | 允许购买固定数量的存储项目 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.buymax` | 允许购买已存储的物品 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.delete` | 允许删除已存储的物品 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.drop` | 允许删除存储的项目 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.give` | 允许提供存储的物料 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.save` | 允许存储物品 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.sell` | 允许销售固定数量的存储项目 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.sellmax` | 允许出售存储的物品 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.setnick` | 允许为存储的项目设置昵称 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.show` | 允许查看已存储的物品 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.take` | 允许取用存储的物料 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.update` | 允许更新已存储的物品 | op |
| [LeafHat](/commands/essentials/leafhat.md) | `leafhat.reload` | 允许使用 /hat reload 重载配置 | op |
| [LeafHat](/commands/essentials/leafhat.md) | `leafhat.use` | 允许使用 /hat 与 /unhat | op |
| [OpenInv](/commands/essentials/openinv.md) | `openinv` | — | — |
| [PlayerSignIn](/commands/essentials/playersignin.md) | `playerSignIn.*` | 离线变量 | — |
| [PlayerSignIn](/commands/essentials/playersignin.md) | `playerSignIn.card` | 管理虚拟补签卡 | op |
| [PlayerSignIn](/commands/essentials/playersignin.md) | `playerSignIn.convert` | 转换数据源 | op |
| [PlayerSignIn](/commands/essentials/playersignin.md) | `playerSignIn.default` | 默认权限 | True |
| [PlayerSignIn](/commands/essentials/playersignin.md) | `playerSignIn.giveSignCard` | 给予实体补签卡 | op |
| [PlayerSignIn](/commands/essentials/playersignin.md) | `playerSignIn.reload` | 重新加载配置 | op |
| [PlayerSignIn](/commands/essentials/playersignin.md) | `playerSignIn.signIn` | 签到gui | True |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.*` | 玩家任务插件 | — |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.addDemand` | 新增任务目标 | op |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.addNpcTask` | 新增NPC任务 | op |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.addReward` | 新增任务奖励 | op |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.addShop` | 新增任务币商品 | op |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.changeItem` | 将对应id的任务转化成物品 | op |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.coin` | 任务币处理 | op |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.convert` | 转换数据源 | op |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.create` | 创建任务 | op |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.delToday` | 删除今日的任务 | op |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.edit` | 编辑任务 | op |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.getToday` | 立即获取今日任务 | op |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.import` | 从配置文件导入任务 | op |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.open` | 查看任务 | True |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.openMeNpcTask` | 打开自己领取的的NPC任务列表 | op |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.openNpc` | 打开NPC菜单 | op |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.reload` | 重新加载配置 | op |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.setDescription` | 设置任务描述 | op |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.setEnableCommand` | 设置领取npc任务执行的命令 | op |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.setRarity` | 设置稀有度 | op |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.shop` | 查看任务币商城 | True |
| [PlayerTask](/commands/essentials/playertask.md) | `playerTask.view` | 管理任务 | op |
| [StarAFK](/commands/essentials/starafk.md) | `starafk.auto` | 参与自动挂机判定 | True |
| [StarAFK](/commands/essentials/starafk.md) | `starafk.bypass` | 永不被自动挂机（不进 AFK 状态）。默认不授予任何人，需要豁免时用 LuckPerms 单独给 | — |
| [StarAFK](/commands/essentials/starafk.md) | `starafk.reload` | 允许 /afk reload | op |
| [StarAFK](/commands/essentials/starafk.md) | `starafk.silent` | 其进出 AFK 不广播。默认不授予任何人，需要静默时用 LuckPerms 单独给 | — |
| [StarAFK](/commands/essentials/starafk.md) | `starafk.use` | 允许使用 /afk | True |

## 🌀 传送与出生点

| 插件 | 节点 | 说明 | 默认 |
| --- | --- | --- | --- |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.*` | — | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.biome` | 特定生物群落的RTP | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.bypass.*` | — | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.bypass.cooldown` | 绕过冷却时间 | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.bypass.delay` | 绕过延迟 | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.bypass.economy` | 旁路经济 | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.bypass.hunger` | 绕过饥饿 | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.edit` | 编辑自定义/默认世界rtp中心/半径 | op |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.group.*` | 使用权限组以不同的限制进行rtp | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.info` | 查看有关rtp将工作的所有世界的信息 | op |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.location` | 使用特定位置的RTP | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.player` | RTP其他玩家 | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.reload` | 重新加载配置 | op |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.sign` | 能够创建RTP标志 | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.test` | 启用调试器后，能够测试粒子、药水效果和声音 | op |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.updater` | 获取有关新更新的通知 | op |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.use` | 使用RTP命令 | True |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.version` | 查看正在运行的版本 | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.world` | 使用世界命令 | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.world.*` | 所有已启用世界中的RTP | — |
| [EssentialsSpawn](/commands/teleport/essentialsspawn.md) | `essentials.setspawn` | 允许访问/setspawn命令 | — |
| [EssentialsSpawn](/commands/teleport/essentialsspawn.md) | `essentials.spawn` | 允许访问/spawn命令 | — |
| [EssentialsSpawn](/commands/teleport/essentialsspawn.md) | `essentials.spawn-on-join.exempt` | 当spawn-on-join为true时，在加入时绕过spawn传送 | — |
| [EssentialsSpawn](/commands/teleport/essentialsspawn.md) | `essentials.spawn.others` | 允许其他玩家访问/spawn命令 | — |

## 🗺️ 世界与地图

| 插件 | 节点 | 说明 | 默认 |
| --- | --- | --- | --- |
| [ArtMap](/commands/world/artmap.md) | `artmap.admin` | 允许管理命令 | op |
| [ArtMap](/commands/world/artmap.md) | `artmap.artist` | 允许玩家在他们拥有或是其成员的任何区域中绘画和放置/打破画架。 | op |
| [ArtMap](/commands/world/artmap.md) | `artmap.artkit` | 使用画架时为玩家提供一套艺术用品 | op |
| [ArtMap](/commands/world/artmap.md) | `artmap.menu` | 允许玩家打开ArtMap菜单 | True |
| [ArtMap](/commands/world/artmap.md) | `artmap.prevent.afk` | 在画架上，玩家不会因为是AFK而被踢出。支持Eseentials和CMI。 | — |
| [ArtMap](/commands/world/artmap.md) | `artmap.region.member` | 允许玩家在他们是成员但不拥有的地区放置/打破画架。 | op |
| [MeteorShowers](/commands/world/meteorshowers.md) | `meteorshowers.admin` | 访问所有MeteorShowers管理命令 | op |
| [Mirrora](/commands/world/mirrora.md) | `mirrora.admin` | — | op |
| [WeatherCard](/commands/world/weathercard.md) | `weathercard.give` | 允许发放天气卡 | op |
| [WeatherCard](/commands/world/weathercard.md) | `weathercard.use` | 允许使用天气卡 | op |
| [XaeroTracker](/commands/world/xaerotracker.md) | `xaerotracker.*` | XaeroTracker 全部权限 | — |
| [XaeroTracker](/commands/world/xaerotracker.md) | `xaerotracker.admin` | 管理其他玩家的追踪设置 | — |
| [XaeroTracker](/commands/world/xaerotracker.md) | `xaerotracker.seeall` | 看得见地图上的所有玩家。默认连 OP 也不拥有 | — |
| [XaeroTracker](/commands/world/xaerotracker.md) | `xaerotracker.town` | 开关是否看得见同镇成员 | True |
| [XaeroTracker](/commands/world/xaerotracker.md) | `xaerotracker.tracked` | 开关自己是否被追踪 | True |
| [XaeroTracker](/commands/world/xaerotracker.md) | `xaerotracker.tracker` | 追踪指定玩家（动态权限，实际为 xaerotracker.tracker.&lt;玩家名&gt;） | — |
| [XaeroTracker](/commands/world/xaerotracker.md) | `xaerotracker.use` | 使用 /xt 命令 | True |

## 🔒 领地与保护

| 插件 | 节点 | 说明 | 默认 |
| --- | --- | --- | --- |
| [BlockLocker](/commands/protect/blocklocker.md) | `blocklocker.admin` | 编辑某人的防护标志，或完全取消防护。 | op |
| [BlockLocker](/commands/protect/blocklocker.md) | `blocklocker.bypass` | 绕过他人的保护，但不要允许破坏它。 | op |
| [BlockLocker](/commands/protect/blocklocker.md) | `blocklocker.protect` | 保护容器和门。 | True |
| [BlockLocker](/commands/protect/blocklocker.md) | `blocklocker.reload` | 使用/blocklocker reload重新加载插件。 | op |
| [BlockLocker](/commands/protect/blocklocker.md) | `blocklocker.wilderness` | 在荒野中放置宝箱（在Towny领地之外） | True |
| [Residence](/commands/protect/residence.md) | `residence.admin` | 允许您访问/resadmin | op |
| [Residence](/commands/protect/residence.md) | `residence.admin.move` | 允许覆盖移动标志 | op |
| [Residence](/commands/protect/residence.md) | `residence.admin.tp` | 允许覆盖tp标志 | op |
| [Residence](/commands/protect/residence.md) | `residence.bypass.command` | 在驻留中绕过命令标志 | op |
| [Residence](/commands/protect/residence.md) | `residence.bypass.nofly` | 在住宅内绕过禁飞旗 | op |
| [Residence](/commands/protect/residence.md) | `residence.chatcolor` | 允许更改住宅聊天颜色 | True |
| [Residence](/commands/protect/residence.md) | `residence.chatkick` | 允许将玩家从住宅聊天中踢出 | True |
| [Residence](/commands/protect/residence.md) | `residence.chatprefix` | 允许更改住宅聊天前缀 | op |
| [Residence](/commands/protect/residence.md) | `residence.command.area` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.auto` | 允许创建最大住宅 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.bank` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.check` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.clearflags` | 允许访问特定命令 | op |
| [Residence](/commands/protect/residence.md) | `residence.command.command` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.compass` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.confirm` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.contract` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.create` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.current` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.expand` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.flags` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.give` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.gset` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.gui` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.info` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.kick` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.lease` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.limits` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.list` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.list.others` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.listall` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.listallhidden` | 允许访问特定命令 | op |
| [Residence](/commands/protect/residence.md) | `residence.command.listhidden` | 允许访问特定命令 | op |
| [Residence](/commands/protect/residence.md) | `residence.command.lists` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.lset` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.market` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.material` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.message` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.message.enter` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.message.enter.remove` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.message.leave` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.message.leave.remove` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.mirror` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.padd` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.pdel` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.pset` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.rc` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.reload` | 允许访问特定命令 | op |
| [Residence](/commands/protect/residence.md) | `residence.command.remove` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.removeall` | 允许访问特定命令 | op |
| [Residence](/commands/protect/residence.md) | `residence.command.removeworld` | 允许访问特定命令 | op |
| [Residence](/commands/protect/residence.md) | `residence.command.rename` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.renamearea` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.resadmin` | 允许访问特定命令 | op |
| [Residence](/commands/protect/residence.md) | `residence.command.resbank` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.reset` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.rt` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.select` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.server` | 允许访问特定命令 | op |
| [Residence](/commands/protect/residence.md) | `residence.command.set` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.setdefaultflags` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.setmain` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.setowner` | 允许访问特定命令 | op |
| [Residence](/commands/protect/residence.md) | `residence.command.shop` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.show` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.siege` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.signconvert` | 允许访问特定命令 | op |
| [Residence](/commands/protect/residence.md) | `residence.command.signupdate` | 允许访问特定命令 | op |
| [Residence](/commands/protect/residence.md) | `residence.command.sublist` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.subzone` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.tool` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.tp` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.tpconfirm` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.tpset` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.unstuck` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.command.version` | 允许访问特定命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.compass` | 允许设置指向驻留的指南针指针 | True |
| [Residence](/commands/protect/residence.md) | `residence.contract` | 允许您签约居住 | True |
| [Residence](/commands/protect/residence.md) | `residence.contract.subzone` | 允许您签约住宅子区 | True |
| [Residence](/commands/protect/residence.md) | `residence.create` | 允许您创建住宅 | True |
| [Residence](/commands/protect/residence.md) | `residence.create.subzone` | 允许您创建住宅子区域 | True |
| [Residence](/commands/protect/residence.md) | `residence.delete` | 允许您删除住宅 | True |
| [Residence](/commands/protect/residence.md) | `residence.delete.subzone` | 允许您删除住宅子区域 | True |
| [Residence](/commands/protect/residence.md) | `residence.expand` | 允许您扩展住所 | True |
| [Residence](/commands/protect/residence.md) | `residence.expand.subzone` | 允许您扩展住宅子区域 | True |
| [Residence](/commands/protect/residence.md) | `residence.newguyresidence` | 允许在胸部位置自动创建居所 | True |
| [Residence](/commands/protect/residence.md) | `residence.randomtp` | 允许使用/res rt命令 | True |
| [Residence](/commands/protect/residence.md) | `residence.rename` | 允许您重命名住宅 | True |
| [Residence](/commands/protect/residence.md) | `residence.resize` | 允许您调整区域的大小 | True |
| [Residence](/commands/protect/residence.md) | `residence.select` | 允许您选择一个区域来建造住宅 | True |
| [Residence](/commands/protect/residence.md) | `residence.select.auto.others` | 允许为其他玩家打开自动选择 | op |
| [Residence](/commands/protect/residence.md) | `residence.topadmin` | 允许您访问/resreload和/resload命令 | op |
| [Residence](/commands/protect/residence.md) | `residence.versioncheck` | 连接后通知新版本 | op |
| [TownPlugin](/commands/protect/townplugin.md) | `town.admin` | 城镇系统管理权限 | op |
| [TownPlugin](/commands/protect/townplugin.md) | `town.use` | 允许使用城镇功能 | True |
| [TownPlugin](/commands/protect/townplugin.md) | `town.warehouse.clear` | 城镇仓库清理权限（清理任意城镇仓库） | op |
| [WorldGuardGUI](/commands/protect/worldguardgui.md) | `wggui.admin` | 允许管理所有区域 | op |
| [WorldGuardGUI](/commands/protect/worldguardgui.md) | `wggui.use` | 允许使用 /wggui 管理自己的区域 | op |

## 🪙 经济与商店

| 插件 | 节点 | 说明 | 默认 |
| --- | --- | --- | --- |
| [AfDianPay](/commands/economy/afdianpay.md) | `afDianPay.*` | 爱发电支付 | — |
| [AfDianPay](/commands/economy/afdianpay.md) | `afDianPay.convert` | 转化数据库 | op |
| [AfDianPay](/commands/economy/afdianpay.md) | `afDianPay.done` | 完成订单 | op |
| [AfDianPay](/commands/economy/afdianpay.md) | `afDianPay.look` | 查看订单信息 | op |
| [AfDianPay](/commands/economy/afdianpay.md) | `afDianPay.reload` | 重载插件 | op |
| [AfDianPay](/commands/economy/afdianpay.md) | `afDianPay.reward` | 根据订单号发送奖励 | op |
| [AfDianPay](/commands/economy/afdianpay.md) | `afDianPay.send` | 发送赞助链接 | True |
| [DummyPool](/commands/economy/dummypool.md) | `dummypool.admin` | 执行管理命令（reloadconfig / reloadmessages） | op |
| [DummyPool](/commands/economy/dummypool.md) | `dummypool.ball` | 领取球物品（/dummypool ball get）——默认仅 OP，防止普通玩家刷球 | op |
| [DummyPool](/commands/economy/dummypool.md) | `dummypool.create` | 创建球台 | op |
| [DummyPool](/commands/economy/dummypool.md) | `dummypool.remove` | 删除球台 | op |
| [DummyPool](/commands/economy/dummypool.md) | `dummypool.use` | 使用 DummyPool 的基础功能（打开界面、参与对局、查看球台列表） | True |
| [MagicPointsLog](/commands/economy/magicpointslog.md) | `magicpointslog.all` | 查看全服点券收支汇总 | op |
| [MagicPointsLog](/commands/economy/magicpointslog.md) | `magicpointslog.check` | 查看玩家点券收支与流水 | op |
| [MagicPointsLog](/commands/economy/magicpointslog.md) | `magicpointslog.clear` | 清除玩家点券记录 | op |
| [MagicPointsLog](/commands/economy/magicpointslog.md) | `magicpointslog.reload` | 重载插件配置 | op |
| [MagicPointsLog](/commands/economy/magicpointslog.md) | `magicpointslog.top` | 查看点券收支榜单 | op |
| [SenluoBuyer](/commands/economy/senluobuyer.md) | `senluobuyer.admin` | 允许重载配置 | op |
| [SenluoBuyer](/commands/economy/senluobuyer.md) | `senluobuyer.use` | 允许使用森罗收购 | True |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.*` | 无障碍通道 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.admin` | 创建和修改管理员店主 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.bypass` | 绕过玩家商店限制（进入其他玩家的商店） | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.citizen` | 创建公民NPC店主 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.cleanup-citizen-shopkeepers` | 通过命令删除无效的公民店主 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.create` | 允许通过命令创建店主 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.debug` | 切换调试模式并访问调试命令 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.delete-unspawnable-shopkeepers` | 通过命令删除不可生成的店主 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.edit-villagers` | 编辑常规村民 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.edit-wandering-traders` | 编辑经常流浪的商人 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.entity.*` | 创建任何类型的店主 | True |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.give` | 通过命令给商店创建道具 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.givecurrency` | 通过命令提供货币道具 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.hanging-sign` | 创建吊牌店主 | True |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.help` | 显示命令帮助 | True |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.hire` | 允许雇佣店主 | True |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.history.admin` | 查看他人和管理员商店的交易历史记录 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.history.own` | 查看您自己的交易历史记录 | True |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.list.admin` | 列出管理员商店 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.list.others` | 列出其他玩家的玩家商店 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.list.own` | 列出您自己的玩家商店 | True |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.maxshops.unlimited` | 允许创建无限数量的商店 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.notify.trades` | 允许通过命令为您打开或关闭交易通知 | True |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.player` | 创建任何类型的玩家店主 | True |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.player.book` | 创建出售玩家店主的书籍 | — |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.player.buy` | 创建购买玩家店主 | — |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.player.sell` | 创建销售玩家店主 | — |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.player.trade` | 创建交易玩家店主 | — |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.reload` | 重新加载插件 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.remote` | 通过命令远程打开商店 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.remote.otherplayers` | 为其他玩家远程开放商店 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.remoteedit` | 通过命令远程编辑商店 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.remove-all.admin` | 通过命令删除所有管理员商店 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.remove-all.others` | 通过命令移除其他玩家的所有商店 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.remove-all.own` | 通过命令移除您自己的所有商店 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.remove-all.player` | 通过命令移除所有玩家的商店 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.remove.admin` | 通过命令删除管理员商店 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.remove.others` | 通过命令移除其他玩家的商店 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.remove.own` | 通过命令移除您自己的商店 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.setcurrency` | 通过命令设置货币项目 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.setforhire` | 将店主设置为出租 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.settradedcommand` | 为持有的道具设置交易命令 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.settradeperm` | 设置管理员商店的交易权限 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.sign` | 创建标志店主 | True |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.snapshot` | 访问店主快照命令 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.teleport` | 通过命令传送给店主 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.teleport.others` | 将其他玩家传送给店主 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.trade` | 允许与店主交易 | True |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.trade-notifications.admin` | 接收管理员商店的交易通知 | — |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.trade-notifications.player` | 接收玩家商店的交易通知 | — |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.transfer` | 转让玩家商店的所有权 | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.updateitems` | 更新第三方餐点 | op |
| [WineSuite](/commands/economy/winesuite.md) | `winebook.admin` | 允许管理图鉴 | op |
| [WineSuite](/commands/economy/winesuite.md) | `winebook.use` | 允许使用酿酒图鉴 | True |
| [WineSuite](/commands/economy/winesuite.md) | `winebuyer.admin` | 允许重载/重置收购配置 | op |
| [WineSuite](/commands/economy/winesuite.md) | `winebuyer.use` | 允许使用酒水收购 | True |

## ⚔️ 战斗与 RPG

| 插件 | 节点 | 说明 | 默认 |
| --- | --- | --- | --- |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.*` | 所有ecoenchants权限 | op |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.anvil.*` | 所有铁砧特权 | op |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.anvil.color` | 允许在砧座中使用颜色代码 | op |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.command.*` | 所有指令 | op |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.command.ecoenchants` | 允许使用/ecoenchants。 | True |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.command.enchant` | 允许使用/enchant。 | op |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.command.enchantinfo` | 允许使用/enchantinfo。 | True |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.command.giverandombook` | 允许随机赠送图书 | op |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.command.gui` | 允许使用/ecoenchants gui。 | True |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.command.reload` | 允许重新加载配置 | op |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.command.toggledescriptions` | 允许使用/ecoenchants切换描述。 | True |
| [EliteMobs](/commands/rpg/elitemobs.md) | `elitemobs.admin` | 管理 EliteMobs（开关/重载/刷怪） | op |
| [EnchantInfuser](/commands/rpg/enchantinfuser.md) | `infuser.use` | 允许使用铁匠铺 | True |
| [FoMiningComp](/commands/rpg/fominingcomp.md) | `fominingcomp.admin` | 访问所有FoMiningComp管理命令 | op |
| [KaoguGuide](/commands/rpg/kaoguguide.md) | `kaoguguide.admin` | 允许重载图鉴数据 | op |
| [KaoguGuide](/commands/rpg/kaoguguide.md) | `kaoguguide.use` | 允许使用考古图鉴 | True |
| [KaoguPlugin](/commands/rpg/kaoguplugin.md) | `kaogu.admin` | 考古插件管理权限 | op |
| [KaoguPlugin](/commands/rpg/kaoguplugin.md) | `kaogu.use` | 使用考古插件基础功能 | True |
| [MythicMobs](/commands/rpg/mythicmobs.md) | `mythicmobs.admin` | 方便您使用所有设施！ | op |
| [MythicMobs](/commands/rpg/mythicmobs.md) | `mythicmobs.reload` | 允许访问/mm重新加载！ | op |
| [MythicMobs](/commands/rpg/mythicmobs.md) | `mythicmobs.signal` | 提供接入/mm信号！ | op |
| [MythicTools](/commands/rpg/mythictools.md) | `mythictools.*` | MythicTools 所有权限 | op |
| [MythicTools](/commands/rpg/mythictools.md) | `mythictools.admin` | 打开并编辑管理 GUI | op |
| [MythicTools](/commands/rpg/mythictools.md) | `mythictools.command` | 使用 MythicTools 基础命令 | True |
| [MythicTools](/commands/rpg/mythictools.md) | `mythictools.reload` | 重载 MythicTools | op |
| [PVPPlugin](/commands/rpg/pvpplugin.md) | `pvp.admin` | 管理权限（设置竞技场坐标、重载配置） | op |
| [PVPPlugin](/commands/rpg/pvpplugin.md) | `pvp.bypass` | 跳过竞技场传送 / 飞行限制（OP 默认拥有） | op |
| [PVPPlugin](/commands/rpg/pvpplugin.md) | `pvp.team` | 允许创建团战房间 | True |
| [PVPPlugin](/commands/rpg/pvpplugin.md) | `pvp.use` | 允许使用 PVP 决斗功能 | True |
| [StarPact](/commands/rpg/starpact.md) | `starpact.admin` | 星之契约管理权限 | op |
| [XingmianElement](/commands/rpg/xingmianelement.md) | `xingmianelement.admin` | 元素之力管理权限 | op |
| [XingmianRPG](/commands/rpg/xingmianrpg.md) | `xingmianrpg.admin` | RPG 世界管理权限 | op |
| [XingmianRPG](/commands/rpg/xingmianrpg.md) | `xingmianrpg.bypass` | 无视 RPG 世界的传送封锁（进出都放行）、命令拦截与鞘翅限制（OP 已自动拥有） | op |
| [XingmianRPG](/commands/rpg/xingmianrpg.md) | `xingmianrpg.use` | 使用 RPG 菜单与进入 RPG 世界 | True |
| [XingmianRPG](/commands/rpg/xingmianrpg.md) | `zjbuyer.admin` | 重载紫荆收购配置 | op |
| [XingmianRPG](/commands/rpg/xingmianrpg.md) | `zjbuyer.use` | 使用紫荆的怪物材料收购 | True |

## 🧟 生物与展示

| 插件 | 节点 | 说明 | 默认 |
| --- | --- | --- | --- |
| [BossBarHealth](/commands/entity/bossbarhealth.md) | `BossBarHealth.Admin` | 授予对所有命令的访问权限 | op |
| [BossBarHealth](/commands/entity/bossbarhealth.md) | `BossBarHealth.Hide` | 允许访问/bbh hide | True |
| [BossBarHealth](/commands/entity/bossbarhealth.md) | `BossBarHealth.Show` | 允许访问/bbh节目 | True |
| [EditableStands](/commands/entity/editablestands.md) | `editablestands.arms.add` | 允许用木棍给盔甲架添加手臂 | True |
| [EditableStands](/commands/entity/editablestands.md) | `editablestands.arms.remove` | 允许用剪刀移除盔甲架的手臂 | True |
| [EditableStands](/commands/entity/editablestands.md) | `editablestands.feather.nogravity` | 允许用羽毛让盔甲架失去重力 | True |
| [EditableStands](/commands/entity/editablestands.md) | `editablestands.ingot.gravity` | 允许用铁锭让盔甲架恢复重力 | True |
| [EditableStands](/commands/entity/editablestands.md) | `editablestands.limit.invisible` | 放宽隐身盔甲架的数量上限（普通玩家限 1 个，详见 config 的 limitUnlimited） | op |
| [EditableStands](/commands/entity/editablestands.md) | `editablestands.limit.nogravity` | 放宽无重力盔甲架的数量上限（普通玩家限 1 个，详见 config 的 limitUnlimited | op |
| [EditableStands](/commands/entity/editablestands.md) | `editablestands.milk.show` | 允许用奶桶让盔甲架恢复显示 | True |
| [EditableStands](/commands/entity/editablestands.md) | `editablestands.name.visible` | 允许用荧光墨囊让盔甲架的名字变为常显 | True |
| [EditableStands](/commands/entity/editablestands.md) | `editablestands.plate.add` | 允许用平滑石台阶给盔甲架添加底盘 | True |
| [EditableStands](/commands/entity/editablestands.md) | `editablestands.plate.remove` | 允许用镐移除盔甲架的底盘 | True |
| [EditableStands](/commands/entity/editablestands.md) | `editablestands.potion.hide` | 允许用隐身药水让盔甲架隐形 | True |
| [EditableStands](/commands/entity/editablestands.md) | `editablestands.size.big` | 允许用木棍把盔甲架变回大型 | True |
| [EditableStands](/commands/entity/editablestands.md) | `editablestands.size.small` | 允许用斧把盔甲架变为小型 | True |
| [FancyNpcsGUI](/commands/entity/fancynpcsgui.md) | `fancynpcsgui.actions` | — | op |
| [FancyNpcsGUI](/commands/entity/fancynpcsgui.md) | `fancynpcsgui.admin` | 授予所有NPC GUI权限 | op |
| [FancyNpcsGUI](/commands/entity/fancynpcsgui.md) | `fancynpcsgui.create` | — | op |
| [FancyNpcsGUI](/commands/entity/fancynpcsgui.md) | `fancynpcsgui.delete` | — | op |
| [FancyNpcsGUI](/commands/entity/fancynpcsgui.md) | `fancynpcsgui.edit` | — | op |
| [FancyNpcsGUI](/commands/entity/fancynpcsgui.md) | `fancynpcsgui.use` | — | op |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.config` | 允许玩家检查Lib的伪装配置的值 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.count` | 允许用户查看有多少伪装处于活动状态 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.debug` | 允许服务器管理员测试玩家伪装在计分板上是否正常 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.disguiseanimation` | 在您自己的伪装上播放受支持的动画 | op |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.disguiseentityanimation` | 在右键单击的实体的伪装上播放支持的动画 | op |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.disguiseplayeranimation` | 在玩家/UUID的伪装上播放支持的动画 | op |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.disguiseradiusanimation` | 在半径范围内的所有受支持的伪装上播放受支持的动画 | op |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.disguiseselectoranimation` | 通过实体选择器在所有受支持的伪装上播放受支持的动画 | op |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.grabhead` | 允许用户使用/grabhead命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.hidename` | 允许玩家忽略被迫高于伪装的名称 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.json` | 允许玩家将保留的项目解析为json | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.metainfo` | 允许玩家获取元信息 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.mods` | 允许用户查看正在使用的MOD。 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.multiname` | 允许命令用户设置不同高度的名称 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.noactionbar` | 隐藏操作栏，即使在配置中启用 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.permtest` | 允许玩家测试权限 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.pve` | 允许玩家忽略pve限制。 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.pvp` | 允许玩家忽略pvp限制。 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.ratelimitbypass` | 允许活着的玩家绕过伪装命令的500ms速率限制，用于防止崩溃 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.reload` | 允许用户重新加载LibsDisguises。 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.scoreboardtest` | 测试计分板是否有效，这是一个简单的测试。 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd` | 在选项卡完成中查看所有命令 | True |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.copydisguise` | 请参阅TAB 补全中的/copydisguise命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguise` | 请参阅TAB 补全中的/disguise命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseanimation` | 参见TAB 补全中的/disguiseanimation命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseclone` | 请参阅TAB 补全中的/disguiseclone命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseentity` | 请参阅TAB 补全中的/disguiseentity命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseentityanimation` | 请参阅TAB 补全中的/disguiseentityanimation命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguisehelp` | 请参阅选项卡完成中的/disguisehelp命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguisemodify` | 请参阅TAB 补全中的/disguisemodify命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguisemodifyentity` | 请参阅TAB 补全中的/disguisemodifyentity命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguisemodifyplayer` | 请参阅选项卡完成中的/disguisemodifyplayer命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguisemodifyradius` | 请参阅TAB 补全中的/disguisemodifyradius命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguisemodifyselector` | 请参阅TAB 补全中的/disguisemodifyselector命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseplayer` | 请参阅制表符完成中的/disguiseplayer命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseplayeranimation` | 请参阅制表符完成中的/disguiseplayeranimation命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseradius` | 请参阅TAB 补全中的/disguiseradius命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseradiusanimation` | 请参阅TAB 补全中的/disguiseradiusanimation命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseselector` | 请参阅选项卡完成中的/disguiseselector命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseselectoranimation` | 请参阅TAB 补全中的/disguiseselectoranimation命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseviewbar` | 请参阅选项卡完成中的/disguiseviewbar命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseviewself` | 请参阅TAB 补全中的/disguiseviewself命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.grabhead` | 在TAB 补全中查看/grabhead命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.grabskin` | 在选项卡完成中查看/grabskin命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.savedisguise` | 在选项卡完成中查看/savedisguise命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.undisguise` | 请参阅TAB 补全中的/undisguise命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.undisguiseentity` | 请参阅TAB 补全中的/undisguiseentity命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.undisguiseplayer` | 请参阅制表符完成中的/undisguiseplayer命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.undisguiseradius` | 请参阅TAB 补全中的/undisguiseradius命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.undisguiseselector` | 请参阅TAB 补全中的/undisguiseselector命令 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seethrough` | 允许玩家看穿伪装。 | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.selfdisguises` | 控制玩家是否可以查看自我伪装，默认为true。仅在伪装开始和切换自我伪装命令时选中。如果玩家有权访问 | True |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.update` | 允许用户更新Libs伪装 | — |
| [ModelEngine](/commands/entity/modelengine.md) | `modelengine.command` | 访问所有模型引擎命令。 | op |
| [YiyunCEskin](/commands/entity/yiyunceskin.md) | `yiyunceskin.admin` | YiyunCEskin的管理员权限 | op |
| [YiyunCEskin](/commands/entity/yiyunceskin.md) | `yiyunceskin.use` | 基本皮肤使用权限 | true |

## 💬 聊天与社交

| 插件 | 节点 | 说明 | 默认 |
| --- | --- | --- | --- |
| [BroadcastPlusPlus](/commands/chat/broadcastplusplus.md) | `broadcastplusplus.admin` | 完全控制—发送、单间公寓、重新加载。 | op |
| [BroadcastPlusPlus](/commands/chat/broadcastplusplus.md) | `broadcastplusplus.send` | 发送广播和预览预设。 | op |
| [BroadcastPlusPlus](/commands/chat/broadcastplusplus.md) | `broadcastplusplus.studio` | 打开Broadcast Studio GUI。 | op |
| [LeafChat](/commands/chat/leafchat.md) | `leafchat.admin` | 管理员直接查看他人背包/末影箱（聊天内 [inv]/[ec] 展示链接无需该权限） | op |
| [LeafChat](/commands/chat/leafchat.md) | `leafchat.chatcolor` | 允许使用聊天颜色 | True |
| [LeafChat](/commands/chat/leafchat.md) | `leafchat.color.*` | 授予所有聊天颜色权限（单色/渐变/彩虹） | op |
| [LeafChat](/commands/chat/leafchat.md) | `leafchat.color.gradient` | 允许使用所有预设渐变并自定义渐变 | op |
| [LeafChat](/commands/chat/leafchat.md) | `leafchat.color.rainbow` | 允许使用彩虹色 | op |
| [LeafChat](/commands/chat/leafchat.md) | `leafchat.color.use` | 允许在消息中使用颜色码（&amp; / § / MiniMessage 标签） | op |
| [LeafChat](/commands/chat/leafchat.md) | `leafchat.mention.all` | 允许使用 @全体 广播 | op |
| [LeafChat](/commands/chat/leafchat.md) | `leafchat.msg` | 允许发送私聊 | True |
| [LeafChat](/commands/chat/leafchat.md) | `leafchat.mute` | 允许禁言玩家 | op |
| [LeafChat](/commands/chat/leafchat.md) | `leafchat.reload` | 允许重载配置 | op |
| [LeafChat](/commands/chat/leafchat.md) | `leafchat.spy` | 允许监听私聊 | op |
| [LeafChat](/commands/chat/leafchat.md) | `leafchat.unmute` | 允许解除禁言 | op |
| [PlayerTitle](/commands/chat/playertitle.md) | `playerTitle.*` | 玩家称号 | — |
| [PlayerTitle](/commands/chat/playertitle.md) | `playerTitle.buff` | 称号buff相关 | op |
| [PlayerTitle](/commands/chat/playertitle.md) | `playerTitle.buff.ignoreWorld` | 忽略世界禁用属性限制 | op |
| [PlayerTitle](/commands/chat/playertitle.md) | `playerTitle.card` | 称号卡相关 | op |
| [PlayerTitle](/commands/chat/playertitle.md) | `playerTitle.clear` | 清理数据 | op |
| [PlayerTitle](/commands/chat/playertitle.md) | `playerTitle.coin` | 称号币相关 | op |
| [PlayerTitle](/commands/chat/playertitle.md) | `playerTitle.convert` | 转化数据库 | op |
| [PlayerTitle](/commands/chat/playertitle.md) | `playerTitle.getIp` | 获取服务信息 | op |
| [PlayerTitle](/commands/chat/playertitle.md) | `playerTitle.open` | 称号仓库 | True |
| [PlayerTitle](/commands/chat/playertitle.md) | `playerTitle.particle` | 称号粒子相关 | op |
| [PlayerTitle](/commands/chat/playertitle.md) | `playerTitle.player` | 玩家称号相关 | op |
| [PlayerTitle](/commands/chat/playertitle.md) | `playerTitle.reload` | 重载插件 | op |
| [PlayerTitle](/commands/chat/playertitle.md) | `playerTitle.reward` | 称号数量奖励 | op |
| [PlayerTitle](/commands/chat/playertitle.md) | `playerTitle.shop` | 称号商城 | True |
| [PlayerTitle](/commands/chat/playertitle.md) | `playerTitle.shop.custom` | 自定义称号 | True |
| [PlayerTitle](/commands/chat/playertitle.md) | `playerTitle.title` | 称号相关 | op |
| [PlayerTitle](/commands/chat/playertitle.md) | `playerTitle.view` | 查看管理 | op |
| [SweetMail](/commands/chat/sweetmail.md) | `sweetmail.attachment.item` | — | True |
| [SweetMail](/commands/chat/sweetmail.md) | `sweetmail.draft.outdate.default` | — | True |
| [SweetMail](/commands/chat/sweetmail.md) | `sweetmail.icon.default` | — | True |
| [SweetMail](/commands/chat/sweetmail.md) | `sweetmail.outdate.default` | — | True |
| [SweetMail](/commands/chat/sweetmail.md) | `sweetmail.price.default` | — | True |
| [TAB](/commands/chat/tab.md) | `tab.admin` | 授予所有标签页权限 | op |
| [TAB](/commands/chat/tab.md) | `tab.announce.bar` | 允许玩家运行/tab bossbar公告 | op |
| [TAB](/commands/chat/tab.md) | `tab.announce.scoreboard` | 允许玩家运行/tab 计分板公告 | op |
| [TAB](/commands/chat/tab.md) | `tab.bossbar.toggle` | 允许玩家运行/tab bossbar | op |
| [TAB](/commands/chat/tab.md) | `tab.bypass` | 如果启用了绕过权限，则使每个世界玩家列表的玩家绕过 | op |
| [TAB](/commands/chat/tab.md) | `tab.change.*` | 允许玩家使用命令更改属性 | op |
| [TAB](/commands/chat/tab.md) | `tab.cpu` | 允许播放器运行/tab cpu | op |
| [TAB](/commands/chat/tab.md) | `tab.dump` | 允许播放器运行/tab 转储 &lt;player&gt; | op |
| [TAB](/commands/chat/tab.md) | `tab.group.*` | 如果通过权限分配，则考虑组中的玩家 | op |
| [TAB](/commands/chat/tab.md) | `tab.groupinfo` | 允许播放器运行/tab 组 &lt;group&gt; | op |
| [TAB](/commands/chat/tab.md) | `tab.grouplist` | 允许玩家运行/tab 组 | op |
| [TAB](/commands/chat/tab.md) | `tab.mysql.download` | 允许播放器运行/tab mysql下载 | op |
| [TAB](/commands/chat/tab.md) | `tab.mysql.upload` | 允许播放器运行/tab mysql上传 | op |
| [TAB](/commands/chat/tab.md) | `tab.nametag.toggle` | 允许玩家运行/tab 名称标签切换 | op |
| [TAB](/commands/chat/tab.md) | `tab.nametag.toggle.other` | 允许玩家运行/tab 名称标签切换[其他玩家] | op |
| [TAB](/commands/chat/tab.md) | `tab.parse` | 允许播放器运行/tab 解析 &lt;player&gt; &lt;placeholder&gt; | op |
| [TAB](/commands/chat/tab.md) | `tab.reload` | 允许播放器运行/tab 重新加载 | op |
| [TAB](/commands/chat/tab.md) | `tab.remove` | 允许玩家使用命令删除组/user | op |
| [TAB](/commands/chat/tab.md) | `tab.scoreboard.show` | 允许玩家运行/tab 记分板显示 | op |
| [TAB](/commands/chat/tab.md) | `tab.scoreboard.show.other` | 允许玩家为其他玩家运行/tab 计分板显示 | op |
| [TAB](/commands/chat/tab.md) | `tab.scoreboard.toggle` | 允许玩家运行/tab 记分板 | op |
| [TAB](/commands/chat/tab.md) | `tab.scoreboard.toggle.other` | 允许玩家为其他玩家运行/tab 记分板 | op |
| [TAB](/commands/chat/tab.md) | `tab.seevanished` | 将玩家标记为能够看到消失的玩家，因为功能挂钩到消失的插件中 | op |
| [TAB](/commands/chat/tab.md) | `tab.send.bar` | 允许玩家运行/tab BOSSBAR发送 | op |
| [TAB](/commands/chat/tab.md) | `tab.setcollision` | 允许玩家运行/tab setcollision &lt;player&gt; &lt;true/fa | op |
| [TAB](/commands/chat/tab.md) | `tab.spectatorbypass` | 使玩家绕过旁观者修复 | op |
| [TAB](/commands/chat/tab.md) | `tab.staff` | 使玩家在% staffonline %占位符中计数 | op |
| [TAB](/commands/chat/tab.md) | `tab.tabcomplete` | 允许玩家完成所有选项卡命令 | op |
| [vcm](/commands/chat/vcm.md) | `vcm.admin` | 允许使用管理命令（/vcm give、/vcm reload） | op |
| [vcm](/commands/chat/vcm.md) | `vcm.use` | 允许使用扩音器 | op |
| [voicechat](/commands/chat/voicechat.md) | `voicechat.admin` | 允许测试语音聊天连接 | — |
| [voicechat](/commands/chat/voicechat.md) | `voicechat.groups` | 允许加入群组 | — |
| [voicechat](/commands/chat/voicechat.md) | `voicechat.listen` | 允许收听语音聊天 | — |
| [voicechat](/commands/chat/voicechat.md) | `voicechat.speak` | 允许语音聊天 | — |
| [YaoqingPlugin](/commands/chat/yaoqingplugin.md) | `yaoqing.admin` | 邀请系统管理（绑定明细/重置/重算） | op |
| [YaoqingPlugin](/commands/chat/yaoqingplugin.md) | `yaoqing.use` | 允许使用邀请功能 | True |

## 🧩 脚本与菜单

| 插件 | 节点 | 说明 | 默认 |
| --- | --- | --- | --- |
| [DeluxeMenus](/commands/config/deluxemenus.md) | `deluxemenus.admin` | 管理员指令 | op |
| [DeluxeMenus](/commands/config/deluxemenus.md) | `deluxemenus.menu.*` | 所有菜单的权限 | op |
| [DeluxeMenus](/commands/config/deluxemenus.md) | `deluxemenus.open` | 打开菜单，打开/dm &lt;menu&gt; | op |
| [DeluxeMenus](/commands/config/deluxemenus.md) | `deluxemenus.open.bypass` | 尝试为观众打开菜单，跳过播放器的观看要求检查 | op |
| [DeluxeMenus](/commands/config/deluxemenus.md) | `deluxemenus.open.others` | 打开菜单，打开/dm &lt;menu&gt; &lt;player&gt; | op |
| [DeluxeMenus](/commands/config/deluxemenus.md) | `deluxemenus.openrequirement.bypass.*` | 允许查看器绕过所有菜单打开要求 | op |
| [DeluxeMenus](/commands/config/deluxemenus.md) | `deluxemenus.placeholdersfor` | /dm open &lt;menu&gt; p解析菜单占位符的权限：&lt;player&gt; | op |
| [DeluxeMenus](/commands/config/deluxemenus.md) | `deluxemenus.placeholdersfor.exempt` | 当/dm为具有&lt;menu p:&lt;player&gt;此权限的玩家打开时，免于解析占位符 | op |
| [KaleidoscopeCookeryPlugin](/commands/config/kaleidoscopecookeryplugin.md) | `kaleidoscopecookery.recipe.browse` | 允许玩家用 /kcrecipe 浏览全部食谱 | op |
| [KaleidoscopeCookeryPlugin](/commands/config/kaleidoscopecookeryplugin.md) | `kaleidoscopecookery.recipe.edit` | 允许用 /kcrecipe edit 编辑食谱 | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.*` | 能够使用所有PAPI命令 | — |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.admin` | 能够使用所有PAPI命令 | — |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.ecloud` | 允许您访问PAPI eCloud | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.ecloud.*` | 能够使用所有PAPI ecloud命令 | — |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.ecloud.clear` | 允许您清除本地eCloud扩展缓存 | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.ecloud.download` | 允许您从eCloud下载扩展 | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.ecloud.info` | 允许您查看云扩展信息 | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.ecloud.list` | 允许您列出eCloud扩展 | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.ecloud.placeholders` | 允许您查看eCloud扩展的占位符 | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.ecloud.refresh` | 允许您刷新本地eCloud扩展缓存 | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.ecloud.status` | 允许您查看eCloud扩展的状态 | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.ecloud.update` | 允许您更新已注册的eCloud扩展 | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.help` | 允许您查看PAPI命令列表 | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.info` | 允许您查看扩展信息 | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.list` | 允许您列出活动扩展 | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.parse` | 允许您分析占位符 | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.register` | 允许您注册扩展 | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.reload` | 允许您重新加载PAPI及其配置 | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.unregister` | 允许您取消注册扩展 | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.updatenotify` | 当有PAPI更新时通知您 | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.version` | 允许您查看已安装的PAPI版本 | op |
| [Skript](/commands/config/skript.md) | `skript.*` | — | — |
| [Skript](/commands/config/skript.md) | `skript.admin` | 允许使用管理命令并接收新版本的通知。 | op |
| [Skript](/commands/config/skript.md) | `skript.effectcommands` | 允许将效果用作命令，例如“! set health to 10” | — |
| [Skript](/commands/config/skript.md) | `skript.reloadnotify` | 当其他人正在重新加载脚本文件时通知。 | — |
| [Skript](/commands/config/skript.md) | `skript.see_runtime_errors` | 发生运行时错误时在聊天中显示通知。 | op |

## 📊 记录与性能

| 插件 | 节点 | 说明 | 默认 |
| --- | --- | --- | --- |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.*` | 授予所有 CoreProtect 操作与命令的访问权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.co` | 拥有访问 CoreProtect /co 命令的权限 | True |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.consumer` | 拥有使用消费者命令的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.core` | 拥有访问 CoreProtect /core 命令的权限 | — |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.coreprotect` | 拥有访问 CoreProtect /coreprotect 命令的权限 | — |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.give` | 拥有使用 give 命令的权限 | — |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.help` | 拥有使用帮助命令的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.inspect` | 拥有使用检查模式的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.lookup` | 拥有使用查询命令的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.lookup.block` | 拥有查询方块数据的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.lookup.chat` | 拥有查询聊天消息的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.lookup.click` | 拥有查询玩家交互的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.lookup.command` | 拥有查询玩家命令的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.lookup.container` | 拥有查询容器交易的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.lookup.inventory` | 拥有查询背包交易的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.lookup.item` | 拥有查询物品交易的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.lookup.kill` | 拥有查询实体击杀的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.lookup.near` | 拥有使用 near 命令查询附近改动的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.lookup.session` | 拥有查询玩家会话的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.lookup.sign` | 拥有查询告示牌消息的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.lookup.spawn` | 拥有查询实体生成的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.lookup.username` | 拥有查询玩家改名记录的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.networking` | 拥有使用网络 API 的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.purge` | 拥有使用清理命令的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.reload` | 拥有使用重载命令的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.restore` | 拥有执行恢复的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.rollback` | 拥有执行回滚的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.status` | 拥有使用状态命令的权限 | op |
| [CoreProtect](/commands/audit/coreprotect.md) | `coreprotect.teleport` | 拥有使用传送命令的权限 | op |

## 🎲 小游戏与娱乐

| 插件 | 节点 | 说明 | 默认 |
| --- | --- | --- | --- |
| [Ah-Toy-1.0](/commands/minigame/ah-toy-1-0.md) | `ahtoy.command.give` | 允许使用 /toy give 获取玩具 | op |
| [Ah-Toy-1.0](/commands/minigame/ah-toy-1-0.md) | `ahtoy.command.reload` | 允许使用 /toy reload 重载玩具配置 | op |
| [Ah-WolfmanKill-1.0](/commands/minigame/ah-wolfmankill-1-0.md) | `wolfmankill.admin` | 管理员权限 | op |
| [Ah-WolfmanKill-1.0](/commands/minigame/ah-wolfmankill-1-0.md) | `wolfmankill.use` | 基础使用权限 | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.*` | GSit \|权限 | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.BellyFlop` | BellyFlop命令\|权限 | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.ByPass.*` | ByPass \|权限 | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.ByPass.Command` | ByPass命令\|权限 | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.ByPass.Region` | ByPass区域\|权限 | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.ByPass.World` | ByPass WORLD \|权限 | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.Crawl` | 爬网命令\|权限 | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.Crawl.*` | 爬网\|权限 | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.CrawlSneak` | 潜行\|权限 | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.CrawlToggle` | 切换爬网能力\|权限 | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.Kick.*` | 踢出\|权限 | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.Kick.Pose` | 踢腿姿势\|权限 | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.Kick.Sit` | Kick SIT \|权限 | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.Lay` | Lay命令\|权限 | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.LayBack` | LayBack命令\|权限 | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.PlayerSit` | PlayerSit单击\|权限 | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.PlayerSit.*` | PlayerSit \|权限 | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.PlayerSitToggle` | 切换PlayerSit能力\|权限 | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.Pose.*` | 姿势\|权限 | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.Reload` | 插件重新加载命令\|权限 | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.Sit` | SIT命令\|权限 | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.Sit.*` | SIT \|权限 | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.SitClick` | SIT单击\|权限 | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.SitToggle` | 切换坐姿能力\|权限 | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.Spin` | 旋转命令\|权限 | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.Update` | 更新通知\|权限 | op |
| [LeashPlayers](/commands/minigame/leashplayers.md) | `leashplayers.admin` | 允许管理所有人的栓绳 / 重载配置 | op |
| [LeashPlayers](/commands/minigame/leashplayers.md) | `leashplayers.use` | 允许使用栓绳栓玩家 | True |
| [LobbyGames](/commands/minigame/lobbygames.md) | `lobbygames.admin` | 访问/lg排行榜、/lg创建和/lg删除 | — |
| [LobbyGames](/commands/minigame/lobbygames.md) | `lobbygames.command` | 访问/lg列表，/lg tp | — |
| [LobbyGames](/commands/minigame/lobbygames.md) | `lobbygames.forcejoin` | 访问/lgjoinplayer | — |
| [LobbyGames](/commands/minigame/lobbygames.md) | `lobbygames.kickplayer` | 进入/lg kick | — |
| [MahjongPlay](/commands/minigame/mahjongplay.md) | `mahjongplay.command.action` | 允许执行麻将操作 | True |
| [MahjongPlay](/commands/minigame/mahjongplay.md) | `mahjongplay.command.bot` | 允许添加机器人 | — |
| [MahjongPlay](/commands/minigame/mahjongplay.md) | `mahjongplay.command.create` | 允许创建麻将桌 | — |
| [MahjongPlay](/commands/minigame/mahjongplay.md) | `mahjongplay.command.destroy` | 允许销毁麻将桌 | — |
| [MahjongPlay](/commands/minigame/mahjongplay.md) | `mahjongplay.command.info` | 允许查看麻将桌信息 | True |
| [MahjongPlay](/commands/minigame/mahjongplay.md) | `mahjongplay.command.join` | 允许加入麻将桌 | True |
| [MahjongPlay](/commands/minigame/mahjongplay.md) | `mahjongplay.command.kick` | 允许踢出玩家 | — |
| [MahjongPlay](/commands/minigame/mahjongplay.md) | `mahjongplay.command.leave` | 允许离开麻将桌 | True |
| [MahjongPlay](/commands/minigame/mahjongplay.md) | `mahjongplay.command.list` | 允许查看麻将桌列表 | True |
| [MahjongPlay](/commands/minigame/mahjongplay.md) | `mahjongplay.command.ready` | 允许准备 | True |
| [MahjongPlay](/commands/minigame/mahjongplay.md) | `mahjongplay.command.start` | 允许强制开始游戏 | — |
| [MahjongPlay](/commands/minigame/mahjongplay.md) | `mahjongplay.command.unready` | 允许取消准备 | True |
| [XingmianQuiz](/commands/minigame/xingmianquiz.md) | `xingmian.quiz.admin` | 星冕答题管理员 | op |

## 📦 其他

| 插件 | 节点 | 说明 | 默认 |
| --- | --- | --- | --- |
| [ArchitectPlugin](/commands/other/architectplugin.md) | `architect.admin` | 建筑师插件管理员 | op |
| [ArchitectPlugin](/commands/other/architectplugin.md) | `architect.shop` | 建材商店使用权（资深及以上默认可进，本权限用于单独开通） | op |
| [ArchitectPlugin](/commands/other/architectplugin.md) | `architect.use` | 使用建筑师插件 | True |
