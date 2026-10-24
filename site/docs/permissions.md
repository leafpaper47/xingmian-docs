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
| [ConsoleSpamFixReborn](/commands/core/consolespamfixreborn.md) | `csf.admin` | Admin commands access. | op |
| [MaintenanceMode](/commands/core/maintenancemode.md) | `maintenance.bypass` | 免除维护模式限制（不被踢、可进服） | op |
| [MaintenanceMode](/commands/core/maintenancemode.md) | `maintenance.use` | 允许使用维护模式指令 | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.admin` | Allows use of all PlugMan commands. | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.check` | Allows use of the check command. | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.check.all` | Allows use of the check all command. | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.deps` | Allows use of the deps command. | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.disable` | Allows use of the disable command. | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.disable.all` | Allows use of the disable all command. | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.dump` | Allows use of the dump command. | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.enable` | Allows use of the enable command. | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.enable.all` | Allows use of the enable all command. | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.help` | Allows use of the help command. | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.info` | Allows use of the info command. | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.list` | Allows use of the list command. | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.load` | Allows use of the load command. | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.lookup` | Allows use of the lookup command. | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.reload` | Allows use of the reload command. | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.reloadconfig` | Allows use of the reload config command. | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.reloadmode` | Allows use of the reload mode command. | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.restart` | Allows use of the restart command. | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.restart.all` | Allows use of the restart all command. | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.unload` | Allows use of the unload command. | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.update` | Allows the player to see the update alerts. | op |
| [PlugManX](/commands/core/plugmanx.md) | `plugman.usage` | Allows use of the usage command. | op |
| [Vault](/commands/core/vault.md) | `vault.admin` | Grants access to the administrative tools. | op |
| [Vault](/commands/core/vault.md) | `vault.update` | Notifies the player when Vault is in need of an up | op |

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
| [Essentials](/commands/essentials/essentials.md) | `essentials.*` | Give players with op everything by default | op |
| [Essentials](/commands/essentials/essentials.md) | `essentials.afk` | Allows access to the /afk command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.afk.auto` | Players with this permission will be set to afk af | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.afk.kickexempt` | Players with this permission will not be kicked fo | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.afk.message` | Allows the player to set a custom AFK message | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.afk.others` | Allows the player to set another player's AFK stat | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.antioch` | Allows access to the /antioch command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.anvil` | Allows access to the /anvil command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.back` | Allows access to the /back command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.back.into.<world>` | Allows the player to use the /back command to trav | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.back.ondeath` | Players with this permission will have back locati | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.back.onteleport` | Players with this permission will have back locati | True |
| [Essentials](/commands/essentials/essentials.md) | `essentials.back.others` | Allows access to the /back command for other playe | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.backup` | Allows access to the /backup command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.balance` | Allows access to the /balance command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.balance.others` | Allows view other players balance with the /balanc | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.balancetop` | Allows access to the /balancetop command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.balancetop.exclude` | Players with this permission are excluded from the | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.balancetop.force` | Allows access to force refresh the balancetop list | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ban` | Allows access to the /ban command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ban.exempt` | Prevent a specified group or player from being ban | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ban.notify` | Allows the bearer to be notified when a player is  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ban.offline` | Allows access to the /ban command for offline play | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.banip` | Allows access to the /banip command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.banip.notify` | Allows the bearer to be notified when a player is  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.beezooka` | Allows access to the /beezooka command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.bigtree` | Allows access to the /bigtree command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.book` | Allows access to the /book command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.book.author` | Allows access to edit book authors with the /book  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.book.others` | Allows access to edit other players books with the | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.book.title` | Allows access to edit book titles with the /book c | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.bottom` | Allows access to the /bottom command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.break` | Allows access to the /break command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.break.bedrock` | Allows access to the /break command for bedrock | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.broadcast` | Allows access to the /broadcast command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.broadcastworld` | Allows access to the /broadcastworld command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.burn` | Allows access to the /burn command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.cartographytable` | Allows access to the /cartographytable command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.chat.ignoreexempt` | Someone with this permission will not be ignored,  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.chat.spy` | Allows the bearers to see all local chat messages, | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.chat.spy.exempt` | Allows the bearer to be exempt from the local chat | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.clearinventory` | Allows access to the /clearinventory command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.clearinventory.all` | Allows access to clear the inventory of all player | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.clearinventory.others` | Allows access to clear the inventory of other play | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.clearinventoryconfirmtoggle` | Allows access to the /clearinventoryconfirmtoggle  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.commandcooldowns.bypass` | Allows the bypassing of all command cooldowns | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.commandcooldowns.bypass.<commandname>` | Allows the bypassing of the cooldown for a specifi | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.compass` | Allows access to the /compass command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.condense` | Allows access to the /condense command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.createkit` | Allows access to the /createkit command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.customtext` | Allows access to the /customtext command and all a | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.delhome` | Allows access to the /delhome command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.delhome.others` | Allows access to delete other players homes with t | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.deljail` | Allows access to the /deljail command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.delkit` | Allows access to the /delkit command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.delwarp` | Allows access to the /delwarp command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.depth` | Allows access to the /depth command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.disposal` | Allows access to the /disposal command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.eco` | Allows access to the /eco command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.eco.loan` | Allows the bearer to possess a negative balance | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.editsign` | Allows access to the /editsign command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.editsign.color` | Allows the bearer to use color codes on signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.editsign.format` | Allows the bearer to use formatting codes on signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.editsign.magic` | Allows the bearer to use magic codes on signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.editsign.rgb` | Allows the bearer to use RGB codes on signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.editsign.unlimited` | Allows the bearer to exceed the 15 character limit | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.editsign.waxed.exempt` | Allows the bearer to edit waxed signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.enchant` | Allows access to the /enchant command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.enchantments.<enchantment>` | Allows the bearer to use a specific enchantment wi | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.enchantments.allowunsafe` | Allows the bearer to enchant items with unsafe enc | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.enderchest` | Allows access to the /enderchest command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.enderchest.modify` | Allows the bearer to modify other players enderche | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.enderchest.others` | Allows access to the /enderchest command for other | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.essentials` | Allows access to the /essentials command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.exempt` | Parent permission to be exempt from many moderator | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.exp` | Allows access to the /exp command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.exp.give` | Allows the bearer to give experience to themselves | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.exp.give.others` | Allows the bearer to give experience to other play | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.exp.others` | Allows the bearer to view other players experience | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.exp.set` | Allows the bearer to set experience for themselves | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.exp.set.others` | Allows the bearer to set experience for other play | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ext` | Allows access to the /ext command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ext.others` | Allows access to the /ext command for other player | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.feed` | Allows access to the /feed command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.feed.others` | Allows access to the /feed command for other playe | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball` | Allows access to the /fireball command. Additional | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.arrow` | Allows access to use the arrows in the /fireball c | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.dragon` | Allows access to use the dragon in the /fireball c | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.egg` | Allows access to use the egg in the /fireball comm | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.fireball` | Allows access to use the fireball in the /fireball | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.large` | Allows access to use the large fireball in the /fi | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.lingeringpotion` | Allows access to use the lingering potion in the / | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.skull` | Allows access to use the skull in the /fireball co | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.small` | Allows access to use the small fireball in the /fi | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.snowball` | Allows access to use the snowball in the /fireball | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.splashpotion` | Allows access to use the splash potion in the /fir | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fireball.trident` | Allows access to use the trident in the /fireball  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.firework` | Allows access to the /firework command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.firework.fire` | Allows the bearer to use the firework command to l | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.firework.multiple` | Allows the bearer to use the firework command to l | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fly` | Allows access to the /fly command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fly.others` | Allows access to the /fly command for other player | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.fly.safelogin` | Bearers of this permission will be put into fly mo | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.gamemode` | Allows access to the /gamemode command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.gamemode.*` | Allows access to all gamemodes with the /gamemode  | op |
| [Essentials](/commands/essentials/essentials.md) | `essentials.gamemode.adventure` | Allows access to the adventure gamemode with the / | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.gamemode.all` | Allows access to all gamemodes with the /gamemode  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.gamemode.creative` | Allows access to the creative gamemode with the /g | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.gamemode.others` | Allows access to the /gamemode command for other p | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.gamemode.spectator` | Allows access to the spectator gamemode with the / | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.gamemode.survival` | Allows access to the survival gamemode with the /g | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.gc` | Allows access to the /gc command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.getpos` | Allows access to the /getpos command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.getpos.others` | Allows access to the /getpos command for other pla | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.give` | Allows access to the /give command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.give.item-<item-name>` | Allows access to the /give command for a specific  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.give.item-all` | Allows access to the /give command for all items w | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.god` | Allows access to the /god command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.god.others` | Allows access to the /god command for other player | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.god.pvp` | Allows the bearer to attack players while in god m | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.grindstone` | Allows access to the /grindstone command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.hat` | Allows access to the /hat command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.hat.ignore-binding` | Allows the bearer to use the /hat command when the | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.hat.prevent-type.<item-name>` | Prevents the player from using the /hat command wi | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.heal` | Allows access to the /heal command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.heal.others` | Allows access to the /heal command for other playe | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.help` | Allows access to the /help command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.help.<plugin-name>` | Allows access to the /help command for a specific  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.helpop` | Allows access to the /helpop command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.helpop.receive` | Allows the bearer to receive helpop messages | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.home` | Allows access to the /home command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.home.bed` | Allows access to the /home command for beds | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.home.compass` | Point the player's compass at their first home. co | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.home.others` | Allows access to teleport to other players homes w | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ice` | Allows access to the /ice command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ice.others` | Allows access to the /ice command for other player | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ignore` | Allows access to the /ignore command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.info` | Allows access to the /info command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.invsee` | Allows access to the /invsee command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.invsee.equip` | Allows access to view items in armor slots with th | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.invsee.modify` | Allows access to modify items in other players inv | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.invsee.preventmodify` | Prevents other players from modifying the players  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.item` | Allows access to the /item command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemdb` | Allows access to the /itemdb command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemlore` | Allows access to the /itemlore command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemname` | Allows access to the /itemname command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemname.color` | Allows access to the /itemname command with color  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemname.format` | Allows access to the /itemname command with format | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemname.magic` | Allows access to the /itemname command with magic  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemname.prevent-type.<item-name>` | Prevents the player from using the /itemname comma | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemname.rgb` | Allows access to the /itemname command with RGB te | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemspawn.exempt` | Allows the bearer to spawn items in the item black | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemspawn.meta-author` | Allows the bearer to spawn items with author metad | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemspawn.meta-book` | Allows the bearer to spawn items with pre-filled c | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemspawn.meta-chapter-<chapter>` | Allows the bearer to spawn specific books only, fr | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemspawn.meta-firework` | Allows the bearer to spawn items with firework met | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemspawn.meta-head` | Allows the bearer to spawn items with head metadat | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemspawn.meta-lore` | Allows the bearer to spawn items with lore metadat | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.itemspawn.meta-title` | Allows the bearer to spawn items with title metada | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jail.allow-block-damage` | Allows the bearer to damage blocks while jailed | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jail.allow-break` | Allows the bearer to break blocks while jailed | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jail.allow-interact` | Allows the bearer to interact with blocks while ja | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jail.allow-place` | Allows the bearer to place blocks while jailed | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jail.allow.<command>` | Allows the bearer to use the specified command whi | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jail.exempt` | Prevent a specified group or player from being jai | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jail.notify` | Allows the bearer to be notified when other player | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jailedplayers` | Allows access to the /jailedplayers command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jails` | Allows access to the /jails command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.joinfullserver` | Allows the to join the server even if it is full | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jump` | Allows access to the /jump command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.jump.lock` | Allows access to the /jump lock command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.keepinv` | Controls whether players keep their inventory on d | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.keepxp` | Allows the user to keep their exp on death, instea | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kick` | Allows access to the /kick command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kick.exempt` | Prevents the player from being kicked. | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kick.notify` | Allows the bearer to be notified when other player | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kickall` | Allows access to the /kickall command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kickall.exempt` | Prevents the player from being kicked by /kickall | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kill` | Allows access to the /kill command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kill.exempt` | Prevents the player from being killed by /kill | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kill.force` | Allows the bearer to be killed by /kill even if th | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kit` | Allows access to the /kit command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kit.exemptdelay` | Exempts you from the kit delay feature, this affec | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kit.others` | Allows access to the /kit command for other player | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kitreset` | Allows access to the /kitreset command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kitreset.others` | Allows access to reset other players kits with the | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kits.*` | Allows access to all kits | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kits.<kit-name>` | Allows access to a specific kit | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.kittycannon` | Allows access to the /kittycannon command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.lightning` | Allows access to the /lightning command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.lightning.others` | Allows access to the /lightning command for other  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.list` | Allows access to the /list command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.list.hidden` | Allow access to view hidden players in the /list c | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.loom` | Allows access to the /loom command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mail` | Allows access to the /mail command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mail.clear.others` | Allows access to clear other players mail with the | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mail.clearall` | Allows access to clear all mail with the /mail com | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mail.send` | Allows access to send mail with the /mail command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mail.sendall` | Allows access to send mail to all players with the | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mail.sendtemp` | Allows access to send temporary mail with the /mai | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.me` | Allows access to the /me command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.more` | Allows access to the /more command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.motd` | Allows access to the /motd command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.msg` | Allows access to the /msg command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.msg.color` | Allows access to the /msg command with color text | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.msg.format` | Allows access to the /msg command with formatting  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.msg.magic` | Allows access to the /msg command with magic text | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.msg.multiple` | Allows access to send messages to multiple players | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.msg.rgb` | Allows access to the /msg command with RGB text | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.msg.url` | Allows access to send URLs in the /msg command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.msgtoggle` | Allows access to the /msgtoggle command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.msgtoggle.bypass` | Allows the bearer to bypass the msgtoggle setting  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.msgtoggle.others` | Allows access to the /msgtoggle command for other  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mute` | Allows access to the /mute command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mute.exempt` | Prevent a specified group or player from being mut | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mute.notify` | Allows the bearer to be notified when other player | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mute.offline` | Allows access to mute offline players | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.mute.unlimited` | Allows the bearer to override the max-mute-time se | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.near` | Allows access to the /near command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.near.exclude` | If the player should be excluded from near lookups | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.near.maxexempt` | Allows the bearer to bypass the radius limit for t | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.near.others` | Allows access to the /near command for other playe | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nick` | Allows access to the /nick command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nick.allowunsafe` | If a player has this, they can set their username  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nick.blacklist.bypass` | Allows the bearer to bypass the nickname blacklist | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nick.changecolors` | Allows the bearer to change **only** the color of  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nick.color` | Allows access to the /nick command with color text | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nick.format` | Allows access to the /nick command with formatting | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nick.hideprefix` | Players with this permission will not have the nic | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nick.magic` | Allows access to the /nick command with magic text | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nick.others` | Allows access to the /nick command for other playe | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nick.rgb` | Allows access to the /nick command with RGB text | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nocommandcost.<command>` | Allows the bearer to use the specified command wit | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nocommandcost.all` | Allows the bearer to use all commands without cost | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.nuke` | Allows access to the /nuke command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.oversizedstacks` | Allows the bearer to spawn oversized stacks | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.pay` | Allows access to the /pay command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.pay.multiple` | Allows access to pay multiple players with the /pa | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.pay.offline` | Allows access to pay offline players with the /pay | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.payconfirmtoggle` | Allows access to the /payconfirmtoggle command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.paytoggle` | Allows access to the /paytoggle command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ping` | Allows access to the /ping command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.playtime` | Allows access to the /playtime command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.playtime.others` | Allows access to the /playtime command for other p | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.potion` | Allows access to the /potion command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.potion.<potion-type>` | Allows access to the /potion command for a specifi | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.potion.apply` | Allows access to the /potion apply command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.powertool` | Allows access to the /powertool command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.powertool.append` | Allows access to add multiple commands to a powert | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.powertoollist` | Allows access to the /powertoollist command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.powertooltoggle` | Allows access to the /powertooltoggle command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ptime` | Allows access to the /ptime command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.ptime.others` | Allows access to the /ptime command for other play | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.pvpdelay.exempt` | Allows the bearer to bypass the pvp delay setting | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.pweather` | Allows access to the /pweather command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.pweather.others` | Allows access to the /pweather command for other p | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.realname` | Allows access to the /realname command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.recipe` | Allows access to the /recipe command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.remove` | Allows access to the /remove command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.renamehome` | Allows access to the /renamehome command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.renamehome.others` | Allows access to rename other players homes with t | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.repair` | Allows access to the /repair command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.repair.all` | Allows access to the /repair all command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.repair.armor` | Allows access to the /repair armor command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.repair.enchanted` | Allows access to use the /repair command on enchan | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.rest` | Allows access to the /rest command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.rest.others` | Allows access to the /rest command for other playe | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.rtoggle` | Allows access to the /rtoggle command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.rules` | Allows access to the /rules command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.seen` | Allows access to the /seen command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.seen.alts` | Allows access to the /seen command with alts | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.seen.banreason` | Allows access to the /seen command with ban reason | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.seen.extra` | Allows access to the /seen command with extra info | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.seen.firstlogin` | Allows access to the /seen command with first logi | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.seen.ip` | Allows access to the /seen command with IP address | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.seen.ipsearch` | Allows access to use IP addresses with the /seen c | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.seen.location` | Allows access to the /seen command with location | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.seen.uuid` | Allows access to the /seen command with UUID | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.seen.whitelist` | Allows access to the /seen command with whitelist  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sell` | Allows access to the /sell command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sell.bulk` | Allows access to bulk sell items with the /sell co | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sell.hand` | Allows access to sell the item in hand with the /s | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sethome` | Allows access to the /sethome command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sethome.bed` | Allows the player to right click a bed during dayt | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sethome.multiple` | Allows access to set multiple homes with the /seth | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sethome.multiple.<set name>` | Raises the limit of homes to a specific number def | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sethome.multiple.unlimited` | Allows access to set unlimited homes with the /set | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sethome.others` | Allows access to set other players homes with the  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.setjail` | Allows access to the /setjail command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.settpr` | Allows access to the /settpr command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.setwarp` | Allows access to the /setwarp command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.setworth` | Allows access to the /setworth command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.showkit` | Allows access to the /showkit command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.balance` | Allows the bearer to break balance signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.buy` | Allows the bearer to break buy signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.disposal` | Allows the bearer to break disposal signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.enchant` | Allows the bearer to break enchant signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.free` | Allows the bearer to break free signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.gamemode` | Allows the bearer to break gamemode signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.heal` | Allows the bearer to break heal signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.info` | Allows the bearer to break info signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.kit` | Allows the bearer to break kit signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.mail` | Allows the bearer to break mail signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.protection` | Allows the bearer to break protection signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.repair` | Allows the bearer to break repair signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.sell` | Allows the bearer to break sell signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.spawnmob` | Allows the bearer to break spawnmob signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.time` | Allows the bearer to break time signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.trade` | Allows the bearer to break trade signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.warp` | Allows the bearer to break warp signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.break.weather` | Allows the bearer to break weather signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.color` | Allows the bearer to create and use color signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.balance` | Allows the bearer to create balance signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.buy` | Allows the bearer to create buy signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.disposal` | Allows the bearer to create disposal signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.enchant` | Allows the bearer to create enchant signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.free` | Allows the bearer to create free signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.gamemode` | Allows the bearer to create gamemode signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.heal` | Allows the bearer to create heal signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.info` | Allows the bearer to create info signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.kit` | Allows the bearer to create kit signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.mail` | Allows the bearer to create mail signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.protection` | Allows the bearer to create protection signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.repair` | Allows the bearer to create repair signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.sell` | Allows the bearer to create sell signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.spawnmob` | Allows the bearer to create spawnmob signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.time` | Allows the bearer to create time signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.trade` | Allows the bearer to create trade signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.warp` | Allows the bearer to create warp signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.create.weather` | Allows the bearer to create weather signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.enchant.allowunsafe` | Allows the bearer to create and use unsafe enchant | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.format` | Allows the bearer to create and use format signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.magic` | Allows the bearer to create and use magic signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.protection.override` | Allows the bearer to break signs created by other  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.rgb` | Allows the bearer to create and use RGB signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.trade.override` | Allows the bearer to break trade signs created by  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.trade.override.collect` | Allows the bearer to collect items from trade sign | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.balance` | Allows the bearer to use balance signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.buy` | Allows the bearer to use buy signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.disposal` | Allows the bearer to use disposal signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.enchant` | Allows the bearer to use enchant signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.free` | Allows the bearer to use free signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.gamemode` | Allows the bearer to use gamemode signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.heal` | Allows the bearer to use heal signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.info` | Allows the bearer to use info signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.kit` | Allows the bearer to use kit signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.mail` | Allows the bearer to use mail signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.protection` | Allows the bearer to use protection signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.repair` | Allows the bearer to use repair signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.sell` | Allows the bearer to use sell signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.spawnmob` | Allows the bearer to use spawnmob signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.time` | Allows the bearer to use time signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.trade` | Allows the bearer to use trade signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.warp` | Allows the bearer to use warp signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.signs.use.weather` | Allows the bearer to use weather signs | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.silentjoin` | Allow to join silently | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.silentjoin.vanish` | Allow to join silently, and get put in vanish mode | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.silentquit` | Suppress leave/quit messages for users with this p | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.skull` | Allows access to the /skull command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.skull.modify` | Allows access to modify other players skulls with  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.skull.others` | Allows access to creating other players skulls wit | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.skull.spawn` | Allows access to spawn a skull with the /skull com | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sleepingignored` | Allows the bearer to not be required to sleep to s | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.smithingtable` | Allows access to the /smithingtable command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.socialspy` | Allows access to the /socialspy command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.socialspy.others` | Allows access to the /socialspy command for other  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.spawner` | Allows access to the /spawner command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.spawner.*` | Allows access to set the type of a spawner with th | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.spawner.<mob-type>` | Allows access to set the type of a spawner with th | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.spawner.delay` | Allows access to set the delay of a spawner with t | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.spawnerconvert.*` | Allows the bearer to place spawners of any type | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.spawnerconvert.<mob-type>` | Allows the bearer to place spawners of a specific  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.spawnmob` | Allows access to the /spawnmob command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.spawnmob.*` | Allows access to spawn all mobs with the /spawnmob | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.spawnmob.<mob-type>` | Allows access to spawn a specific mob with the /sp | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.spawnmob.stack` | Allows access to spawn mobs in stacks with the /sp | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.speed` | Allows access to the /speed command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.speed.bypass` | Allows the bearer to bypass the speed limit set in | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.speed.fly` | Allows access to the /speed command for fly speed | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.speed.others` | Allows access to the /speed command for other play | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.speed.walk` | Allows access to the /speed command for walk speed | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.stonecutter` | Allows access to the /stonecutter command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sudo` | Allows access to the /sudo command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sudo.exempt` | Prevents the player from being sudo'ed by another  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.sudo.multiple` | Allows access to the /sudo command for multiple pl | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.suicide` | Allows access to the /suicide command for multiple | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.teleport.cooldown.bypass.back` | If the player does not have this permission, /back | True |
| [Essentials](/commands/essentials/essentials.md) | `essentials.teleport.cooldown.bypass.tpa` | If the player does not have this permission, /tpa  | True |
| [Essentials](/commands/essentials/essentials.md) | `essentials.teleport.timer.bypass` | Allows the bearer to bypass the teleport delay | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.teleport.timer.move` | Allows the bearer to move while waiting for a tele | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tempban` | Allows access to the /tempban command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tempban.exempt` | Prevent a specified group or player from being tem | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tempban.offline` | Allows access to tempban offline players | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tempban.unlimited` | Allows the bearer to override the max-tempban-time | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tempbanip` | Allows access to the /tempbanip command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.thunder` | Allows access to the /thunder command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.time` | Allows access to the /time command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.time.set` | Allows access to set the time with the /time comma | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.time.world.all` | Allows access to set the time for all worlds with  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.togglejail` | Allows access to the /togglejail command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.togglejail.offline` | Allows access to the /togglejail command for offli | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.top` | Allows access to the /top command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tp` | Allows access to the /tp command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tp.others` | Allows access to teleporting to other users with t | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tp.position` | Allows access to teleporting to a position with th | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpa` | Allows access to the /tpa command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpaall` | Allows access to the /tpaall command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpacancel` | Allows access to the /tpaccept command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpaccept` | Allows access to the /tpaccept command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpahere` | Allows access to the /tpahere command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpall` | Allows access to the /tpall command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpauto` | Allows access to the /tpauto command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpauto.others` | Allows access to the /tpauto command for other pla | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpdeny` | Allows access to the /tpdeny command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tphere` | Allows access to the /tphere command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpo` | Allows access to the /tpo command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpoffline` | Allows access to the /tpoffline command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpohere` | Allows access to the /tpohere command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tppos` | Allows access to the /tppos command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tpr` | Allows access to the /tpr command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tptoggle` | Allows access to the /tptoggle command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tptoggle.others` | Allows access to the /tptoggle command for other p | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.tree` | Allows access to the /tree command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.unban` | Allows access to the /unban command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.unbanip` | Allows access to the /unbanip command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.unlimited` | Allows access to the /unlimited command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.unlimited.item-<item-name>` | Allows access to the /unlimited command for a spec | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.unlimited.item-all` | Allows access to the /unlimited command for all it | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.unlimited.item-bucket` | Allows access to the /unlimited command for bucket | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.unlimited.others` | Allows access to the /unlimited command for other  | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.updatecheck` | The bearer will be notified of updates to Essentia | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.vanish` | Allows access to the /vanish command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.vanish.effect` | Applies invisibility effects to the player when th | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.vanish.interact` | Allows the bearer to interact with players in vani | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.vanish.others` | Allows access to the /vanish command for other pla | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.vanish.pickup` | Allows the bearer to pick up items while in vanish | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.vanish.pvp` | Allows the bearer to attack players while in vanis | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.vanish.see` | Allows the bearer to see other players in vanish m | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.version` | Allows access to the /version command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.warp` | Allows access to the /warp command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.warp.list` | Allows access to the /warp list command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.warp.others` | Allows access to the /warp command for other playe | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.warp.overwrite.*` | Allows the bearer to overwrite all warps | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.warp.overwrite.<warp-name>` | Allows the bearer to overwrite a specific warp | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.warpinfo` | Allows access to the /warpinfo command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.weather` | Allows access to the /weather command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.whitelist.bypass` | Allows a player to join the server even if they ar | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.whois` | Allows access to the /whois command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.whois.ip` | Allows access to the /whois command with IP addres | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.workbench` | Allows access to the /workbench command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.world` | Allows access to the /world command | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.worlds.<world-name>` | Allows access to the specific world with various c | — |
| [Essentials](/commands/essentials/essentials.md) | `essentials.worth` | Allows access to the /worth command | — |
| [InBlock](/commands/essentials/inblock.md) | `Inblock.give` | 允许给予自定义方块物品 | op |
| [InBlock](/commands/essentials/inblock.md) | `Inblock.open` | 允许打开仓库界面 | op |
| [InBlock](/commands/essentials/inblock.md) | `Inblock.reload` | 允许重载配置 | op |
| [InfiniteFuel](/commands/essentials/infinitefuel.md) | `infinitefuel.admin` | — | op |
| [InvSaver](/commands/essentials/invsaver.md) | `invSaver.list` | — | op |
| [InvSaver](/commands/essentials/invsaver.md) | `invSaver.preview` | — | op |
| [InvSaver](/commands/essentials/invsaver.md) | `invSaver.reload` | — | op |
| [InvSaver](/commands/essentials/invsaver.md) | `invSaver.restore` | — | op |
| [InvSaver](/commands/essentials/invsaver.md) | `invSaver.save` | — | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.admin` | Gives full access to the plugin | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.bypass.*` | Gives full access to the plugin | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.bypass.censure` | Bypass words restrictions when editing items | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.bypass.lore_length_limit` | Bypass restrictions on lore line max length set on | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.bypass.lore_line_limit` | Bypass restrictions on lore line amount set on con | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.bypass.lore_type_restriction` | Bypass type restrictions when editing item lore | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.bypass.rename_length_limit` | Bypass restrictions on rename line max length set  | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.bypass.rename_type_restriction` | Bypass type restrictions when renaming items | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.creativeuser` | Gives full access to the plugin | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.*` | Gives full access to command /itemedit | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.amount` | Allow editing item amount | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.armortrim` | Allow setting trims on armor | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.axolotlvariant` | Allow editing axolotl variant on axolotl buckets | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.banner` | Allow editing banners | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.bookauthor` | Allow editing book author | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.bookenchant` | Allow editing book enchants | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.bookenchant.bypass_max_level` | Allow editing book enchants above vanilla limits | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.booktype` | Allow editing book type | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.color` | Allow editing items colors | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.color.firework_star` | Allow editing firework star color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.color.leather` | Allow editing leather color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.color.potion` | Allow editing potion color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.color.tipped_arrow` | Allow editing tipped arrow color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.compass` | Allow editing compass location | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.custommodeldata` | Allow editing custom model data of items | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.damage` | Allow editing item durability-damage | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.enchant` | Allow editing item enchants | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.enchant.bypass_max_level` | Allow editing item enchants above vanilla limits | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.equipment` | Allow setting equipment properties | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.fireresistent` | Allow setting fire resistance of this stack | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.firework` | Allow editing fireworks with a gui | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.fireworkpower` | Allow editing fireworks power | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.food` | Allow editing potion effects | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.food.bypass_limits` | Allow editing potion effects above level 2 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.glider` | Allow setting the item behavior | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.glow` | Allow setting glow visual effect | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.goathornsound` | Allow editing goat horn sound | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.hide` | Allow editing item flags | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.hideall` | Allow to hide all item flags at once | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.hidetooltip` | Allow hiding tooltips | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.itemmodel` | Allow setting item texture model | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.listaliases` | Shows aliases | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore` | Allow editing item lore | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.*` | Allow editing item lore and use all colors | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.aqua` | Allow editing item lore and use aqua color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.black` | Allow editing item lore and use black color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.blue` | Allow editing item lore and use blue color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.dark_aqua` | Allow editing item lore and use dark_aqua color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.dark_blue` | Allow editing item lore and use dark_blue color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.dark_gray` | Allow editing item lore and use dark_gray color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.dark_green` | Allow editing item lore and use dark_green color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.dark_purple` | Allow editing item lore and use dark_purple color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.dark_red` | Allow editing item lore and use dark_red color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.gold` | Allow editing item lore and use gold color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.gray` | Allow editing item lore and use gray color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.green` | Allow editing item lore and use green color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.hexa` | Allow editing item lore and use hexa colors | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.light_purple` | Allow editing item lore and use light_purple color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.red` | Allow editing item lore and use red color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.white` | Allow editing item lore and use white color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.color.yellow` | Allow editing item lore and use yellow color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.copy` | Allow to use lore sub commands copy, copybook and  | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.format.*` | Allow editing item lore and use all formats | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.format.bold` | Allow editing item lore and use bold format | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.format.italic` | Allow editing item lore and use italic format | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.format.magic` | Allow editing item lore and use magic format | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.format.reset` | Allow editing item lore and use reset format | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.format.strikethrough` | Allow editing item lore and use strikethrough form | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.format.underline` | Allow editing item lore and use underline format | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.lore.minimessage` | Allow editing item lore using minimessage placehol | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.maxstacksize` | Allow setting max stack size | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.potioneffect` | Allow editing potion effects | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.potioneffect.bypass_limits` | Allow editing potion effects above level 2 | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rarity` | Allow setting rarity of an item | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename` | Allow editing item name | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.*` | Allow editing item name and use all colors | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.aqua` | Allow editing item name and use aqua color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.black` | Allow editing item name and use black color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.blue` | Allow editing item name and use blue color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.dark_aqua` | Allow editing item name and use dark_aqua color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.dark_blue` | Allow editing item name and use dark_blue color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.dark_gray` | Allow editing item name and use dark_gray color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.dark_green` | Allow editing item name and use dark_green color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.dark_purple` | Allow editing item name and use dark_purple color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.dark_red` | Allow editing item name and use dark_red color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.gold` | Allow editing item name and use gold color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.gray` | Allow editing item name and use gray color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.green` | Allow editing item name and use green color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.hexa` | Allow editing item name and use hexa colors | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.light_purple` | Allow editing item name and use light_purple color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.red` | Allow editing item name and use red color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.white` | Allow editing item name and use white color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.color.yellow` | Allow editing item name and use yellow color | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.format.*` | Allow editing item name and use all formats | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.format.bold` | Allow editing item name and use bold format | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.format.italic` | Allow editing item name and use italic format | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.format.magic` | Allow editing item name and use magic format | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.format.reset` | Allow editing item name and use reset format | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.format.strikethrough` | Allow editing item name and use strikethrough form | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.format.underline` | Allow editing item name and use underline format | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.rename.minimessage` | Allow editing item name using minimessage placehol | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.repaircost` | Allow editing repair costs | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.repaircost.without_durability` | Allow to set a repair cost even on items which hav | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.skullowner` | Allow editing skull skin owner | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.spawnereggtype` | Allow editing monster's egg | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.tropicalfish` | Allow editing tropical fish buckets | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.type` | Allow editing item material | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemedit.unbreakable` | Allow editing item unbreakablity | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemeditimport` | Gives full access to command /itemeditimport | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemeditinfo` | Gives full access to command /itemeditinfo | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemeditreload` | Gives full access to command /itemeditreload | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemstorage.*` | Gives full access to command /itemstorage | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemstorage.delete` | Allow to delete stored items | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemstorage.get` | Allow to get stored items | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemstorage.save` | Allow to store items | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemstorage.show` | Allow to show stored items | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.itemstorage.update` | Allow to update stored items | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.*` | Gives full access to command /serveritem | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.buy` | Allow to buy fixed amount of stored items | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.buymax` | Allow to buy stored items | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.delete` | Allow to delete stored items | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.drop` | Allow to drop stored items | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.give` | Allow to give stored items | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.save` | Allow to store items | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.sell` | Allow to sell fixed amount of stored items | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.sellmax` | Allow to sell stored items | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.setnick` | Allow to set nicks for stored items | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.show` | Allow to show stored items | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.take` | Allow to take stored items | op |
| [ItemEdit](/commands/essentials/itemedit.md) | `itemedit.serveritem.update` | Allow to update stored items | op |
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
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.biome` | RTP to specific biomes | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.bypass.*` | — | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.bypass.cooldown` | Bypass cooldowns | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.bypass.delay` | Bypass delays | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.bypass.economy` | Bypass economy | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.bypass.hunger` | Bypass hunger | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.edit` | Edit a custom/default world rtp center/radius | op |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.group.*` | Use a permission group to rtp with different restr | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.info` | View info about all worlds rtp will work in | op |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.location` | RTP using a specific location | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.player` | RTP another player | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.reload` | Reload the config | op |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.sign` | Ability to create an RTP sign | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.test` | While debugger enabled, be able to test particles, | op |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.updater` | Get notification on new updates | op |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.use` | Use RTP command | True |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.version` | See which version is running | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.world` | Use world command | — |
| [BetterRTP](/commands/teleport/betterrtp.md) | `betterrtp.world.*` | RTP in all enabled worlds | — |
| [EssentialsSpawn](/commands/teleport/essentialsspawn.md) | `essentials.setspawn` | Allows access to the /setspawn command | — |
| [EssentialsSpawn](/commands/teleport/essentialsspawn.md) | `essentials.spawn` | Allows access to the /spawn command | — |
| [EssentialsSpawn](/commands/teleport/essentialsspawn.md) | `essentials.spawn-on-join.exempt` | Bypass spawn teleportation on join when spawn-on-j | — |
| [EssentialsSpawn](/commands/teleport/essentialsspawn.md) | `essentials.spawn.others` | Allows access to the /spawn command for other play | — |

## 🗺️ 世界与地图

| 插件 | 节点 | 说明 | 默认 |
| --- | --- | --- | --- |
| [ArtMap](/commands/world/artmap.md) | `artmap.admin` | Allows administrative commands | op |
| [ArtMap](/commands/world/artmap.md) | `artmap.artist` | Allows players to paint, and place/break easels in | op |
| [ArtMap](/commands/world/artmap.md) | `artmap.artkit` | Gives players a kit of art supplies while they use | op |
| [ArtMap](/commands/world/artmap.md) | `artmap.menu` | Allows players to open the ArtMap menu | True |
| [ArtMap](/commands/world/artmap.md) | `artmap.prevent.afk` | Player will not be kicked for being AFK at easel.  | — |
| [ArtMap](/commands/world/artmap.md) | `artmap.region.member` | Allows players to place/break easels in regions th | op |
| [MeteorShowers](/commands/world/meteorshowers.md) | `meteorshowers.admin` | Access to all MeteorShowers admin commands | op |
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
| [BlockLocker](/commands/protect/blocklocker.md) | `blocklocker.admin` | Edit someone's protection signs, or remove the pro | op |
| [BlockLocker](/commands/protect/blocklocker.md) | `blocklocker.bypass` | Bypass someone else's protection, but don't allow  | op |
| [BlockLocker](/commands/protect/blocklocker.md) | `blocklocker.protect` | Protect containers and doors. | True |
| [BlockLocker](/commands/protect/blocklocker.md) | `blocklocker.reload` | Reload the plugin using /blocklocker reload. | op |
| [BlockLocker](/commands/protect/blocklocker.md) | `blocklocker.wilderness` | Place chests in the wilderness (outside of Towny c | True |
| [Residence](/commands/protect/residence.md) | `residence.admin` | Gives you access to /resadmin | op |
| [Residence](/commands/protect/residence.md) | `residence.admin.move` | Allows to override move flag | op |
| [Residence](/commands/protect/residence.md) | `residence.admin.tp` | Allows to override tp flag | op |
| [Residence](/commands/protect/residence.md) | `residence.bypass.command` | Bypasses command flag in residence | op |
| [Residence](/commands/protect/residence.md) | `residence.bypass.nofly` | Bypasses nofly flag in residence | op |
| [Residence](/commands/protect/residence.md) | `residence.chatcolor` | Allows to change residence chat color | True |
| [Residence](/commands/protect/residence.md) | `residence.chatkick` | Allows to kick players from residence chat | True |
| [Residence](/commands/protect/residence.md) | `residence.chatprefix` | Allows to change residence chat prefix | op |
| [Residence](/commands/protect/residence.md) | `residence.command.area` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.auto` | Allows to create max residence | True |
| [Residence](/commands/protect/residence.md) | `residence.command.bank` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.check` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.clearflags` | Allows to access particular command | op |
| [Residence](/commands/protect/residence.md) | `residence.command.command` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.compass` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.confirm` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.contract` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.create` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.current` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.expand` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.flags` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.give` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.gset` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.gui` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.info` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.kick` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.lease` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.limits` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.list` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.list.others` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.listall` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.listallhidden` | Allows to access particular command | op |
| [Residence](/commands/protect/residence.md) | `residence.command.listhidden` | Allows to access particular command | op |
| [Residence](/commands/protect/residence.md) | `residence.command.lists` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.lset` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.market` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.material` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.message` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.message.enter` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.message.enter.remove` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.message.leave` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.message.leave.remove` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.mirror` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.padd` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.pdel` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.pset` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.rc` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.reload` | Allows to access particular command | op |
| [Residence](/commands/protect/residence.md) | `residence.command.remove` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.removeall` | Allows to access particular command | op |
| [Residence](/commands/protect/residence.md) | `residence.command.removeworld` | Allows to access particular command | op |
| [Residence](/commands/protect/residence.md) | `residence.command.rename` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.renamearea` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.resadmin` | Allows to access particular command | op |
| [Residence](/commands/protect/residence.md) | `residence.command.resbank` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.reset` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.rt` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.select` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.server` | Allows to access particular command | op |
| [Residence](/commands/protect/residence.md) | `residence.command.set` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.setdefaultflags` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.setmain` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.setowner` | Allows to access particular command | op |
| [Residence](/commands/protect/residence.md) | `residence.command.shop` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.show` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.siege` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.signconvert` | Allows to access particular command | op |
| [Residence](/commands/protect/residence.md) | `residence.command.signupdate` | Allows to access particular command | op |
| [Residence](/commands/protect/residence.md) | `residence.command.sublist` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.subzone` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.tool` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.tp` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.tpconfirm` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.tpset` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.unstuck` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.command.version` | Allows to access particular command | True |
| [Residence](/commands/protect/residence.md) | `residence.compass` | Allows to set compass pointer to residence | True |
| [Residence](/commands/protect/residence.md) | `residence.contract` | Allows you to contract residence | True |
| [Residence](/commands/protect/residence.md) | `residence.contract.subzone` | Allows you to contract residences subzone | True |
| [Residence](/commands/protect/residence.md) | `residence.create` | Allows you to create residences | True |
| [Residence](/commands/protect/residence.md) | `residence.create.subzone` | Allows you to create residences subzone | True |
| [Residence](/commands/protect/residence.md) | `residence.delete` | Allows you to delete residences | True |
| [Residence](/commands/protect/residence.md) | `residence.delete.subzone` | Allows you to delete residences subzone | True |
| [Residence](/commands/protect/residence.md) | `residence.expand` | Allows you to expand residence | True |
| [Residence](/commands/protect/residence.md) | `residence.expand.subzone` | Allows you to expand residences subzone | True |
| [Residence](/commands/protect/residence.md) | `residence.newguyresidence` | Allows for auto residence creation on chest place | True |
| [Residence](/commands/protect/residence.md) | `residence.randomtp` | Allows to use /res rt command | True |
| [Residence](/commands/protect/residence.md) | `residence.rename` | Allows you to rename residences | True |
| [Residence](/commands/protect/residence.md) | `residence.resize` | Allows you to resize an area | True |
| [Residence](/commands/protect/residence.md) | `residence.select` | Allows you to select an area to make residences | True |
| [Residence](/commands/protect/residence.md) | `residence.select.auto.others` | Allows to turn on auto selection for other players | op |
| [Residence](/commands/protect/residence.md) | `residence.topadmin` | Gives you access to /resreload and /resload comman | op |
| [Residence](/commands/protect/residence.md) | `residence.versioncheck` | Notice to new version after connect | op |
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
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.*` | Access to everything | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.admin` | Create and modify admin shopkeepers | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.bypass` | Bypass player shop restrictions (access player sho | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.citizen` | Create Citizens NPC shopkeepers | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.cleanup-citizen-shopkeepers` | Delete invalid Citizen shopkeepers via command | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.create` | Allows the creation of shopkeepers via command | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.debug` | Toggle debug mode and access debugging commands | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.delete-unspawnable-shopkeepers` | Delete unspawnable shopkeepers via command | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.edit-villagers` | Edit regular villagers | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.edit-wandering-traders` | Edit regular wandering traders | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.entity.*` | Create shopkeepers of any mob type | True |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.give` | Give shop creation items via command | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.givecurrency` | Give currency items via command | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.hanging-sign` | Create hanging sign shopkeepers | True |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.help` | Display the command help | True |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.hire` | Allows hiring of shopkeepers | True |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.history.admin` | View the trading history of others and admin shops | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.history.own` | View your own trading history | True |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.list.admin` | List the admin shops | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.list.others` | List the player shops of other players | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.list.own` | List your own player shops | True |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.maxshops.unlimited` | Allows the creation of an unlimited number of shop | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.notify.trades` | Allows turning trade notifications for you on or o | True |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.player` | Create any type of player shopkeeper | True |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.player.book` | Create books selling player shopkeepers | — |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.player.buy` | Create buying player shopkeepers | — |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.player.sell` | Create selling player shopkeepers | — |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.player.trade` | Create trading player shopkeepers | — |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.reload` | Reload the plugin | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.remote` | Remotely open shops via command | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.remote.otherplayers` | Remotely open shops for other players | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.remoteedit` | Remotely edit shops via command | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.remove-all.admin` | Remove all admin shops via command | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.remove-all.others` | Remove all the shops of another player via command | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.remove-all.own` | Remove all of your own shops via command | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.remove-all.player` | Remove the player shops of all players via command | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.remove.admin` | Remove admin shops via command | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.remove.others` | Remove the shops of other players via command | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.remove.own` | Remove your own shops via command | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.setcurrency` | Set the currency items via command | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.setforhire` | Set a shopkeeper to be for hire | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.settradedcommand` | Set the traded command for the held item | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.settradeperm` | Set the trade permissions for admin shops | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.sign` | Create sign shopkeepers | True |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.snapshot` | Access shopkeeper snapshot commands | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.teleport` | Teleport to shopkeepers via command | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.teleport.others` | Teleport other players to shopkeepers | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.trade` | Allows trading with shopkeepers | True |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.trade-notifications.admin` | Receive trade notifications for admin shops | — |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.trade-notifications.player` | Receive trade notifications for player shops | — |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.transfer` | Transfer ownership of player shops | op |
| [Shopkeepers](/commands/economy/shopkeepers.md) | `shopkeeper.updateitems` | Update third-party items | op |
| [WineSuite](/commands/economy/winesuite.md) | `winebook.admin` | 允许管理图鉴 | op |
| [WineSuite](/commands/economy/winesuite.md) | `winebook.use` | 允许使用酿酒图鉴 | True |
| [WineSuite](/commands/economy/winesuite.md) | `winebuyer.admin` | 允许重载/重置收购配置 | op |
| [WineSuite](/commands/economy/winesuite.md) | `winebuyer.use` | 允许使用酒水收购 | True |

## ⚔️ 战斗与 RPG

| 插件 | 节点 | 说明 | 默认 |
| --- | --- | --- | --- |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.*` | All ecoenchants permissions | op |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.anvil.*` | All anvil perks | op |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.anvil.color` | Allows using color codes in anvils | op |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.command.*` | All commands | op |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.command.ecoenchants` | Allows the use of /ecoenchants. | True |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.command.enchant` | Allows the use of /enchant. | op |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.command.enchantinfo` | Allows the use of /enchantinfo. | True |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.command.giverandombook` | Allows giving random books | op |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.command.gui` | Allows the use of /ecoenchants gui. | True |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.command.reload` | Allows reloading the config | op |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | `ecoenchants.command.toggledescriptions` | Allows the use of /ecoenchants toggledescriptions. | True |
| [EliteMobs](/commands/rpg/elitemobs.md) | `elitemobs.admin` | 管理 EliteMobs（开关/重载/刷怪） | op |
| [EnchantInfuser](/commands/rpg/enchantinfuser.md) | `infuser.use` | 允许使用铁匠铺 | True |
| [FoMiningComp](/commands/rpg/fominingcomp.md) | `fominingcomp.admin` | Access to all FoMiningComp admin commands | op |
| [KaoguGuide](/commands/rpg/kaoguguide.md) | `kaoguguide.admin` | 允许重载图鉴数据 | op |
| [KaoguGuide](/commands/rpg/kaoguguide.md) | `kaoguguide.use` | 允许使用考古图鉴 | True |
| [KaoguPlugin](/commands/rpg/kaoguplugin.md) | `kaogu.admin` | 考古插件管理权限 | op |
| [KaoguPlugin](/commands/rpg/kaoguplugin.md) | `kaogu.use` | 使用考古插件基础功能 | True |
| [MythicMobs](/commands/rpg/mythicmobs.md) | `mythicmobs.admin` | Gives access to everything! | op |
| [MythicMobs](/commands/rpg/mythicmobs.md) | `mythicmobs.reload` | Gives access /mm reload! | op |
| [MythicMobs](/commands/rpg/mythicmobs.md) | `mythicmobs.signal` | Gives access /mm signal! | op |
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
| [BossBarHealth](/commands/entity/bossbarhealth.md) | `BossBarHealth.Admin` | Give access to all commands | op |
| [BossBarHealth](/commands/entity/bossbarhealth.md) | `BossBarHealth.Hide` | Give access to /bbh hide | True |
| [BossBarHealth](/commands/entity/bossbarhealth.md) | `BossBarHealth.Show` | Give access to /bbh show | True |
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
| [FancyNpcsGUI](/commands/entity/fancynpcsgui.md) | `fancynpcsgui.admin` | Grants all NPC GUI permissions | op |
| [FancyNpcsGUI](/commands/entity/fancynpcsgui.md) | `fancynpcsgui.create` | — | op |
| [FancyNpcsGUI](/commands/entity/fancynpcsgui.md) | `fancynpcsgui.delete` | — | op |
| [FancyNpcsGUI](/commands/entity/fancynpcsgui.md) | `fancynpcsgui.edit` | — | op |
| [FancyNpcsGUI](/commands/entity/fancynpcsgui.md) | `fancynpcsgui.use` | — | op |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.config` | Allows player to check Lib's Disguises config for  | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.count` | Allows the user to see how many disguises are acti | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.debug` | Allows a server admin to test a player disguise fo | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.disguiseanimation` | Play a supported animation on your own disguise | op |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.disguiseentityanimation` | Play a supported animation on a right clicked enti | op |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.disguiseplayeranimation` | Play a supported animation on a player/uuid's disg | op |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.disguiseradiusanimation` | Play a supported animation on all supported disgui | op |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.disguiseselectoranimation` | Play a supported animation on all supported disgui | op |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.grabhead` | Allows the command user to use /grabhead | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.hidename` | Allows player to ignore name being forced above di | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.json` | Allows player to parse held item to json | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.metainfo` | Allows player to get meta info | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.mods` | Allows the user to see mods in use. | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.multiname` | Allows the command user to set names on different  | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.noactionbar` | Hides the action bar even if enabled in config | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.permtest` | Allows player to test permissions | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.pve` | Allows player to ignore pve restrictions. | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.pvp` | Allows player to ignore pvp restrictions. | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.ratelimitbypass` | Allows a living player to bypass the 500ms rate li | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.reload` | Allows the user to reload LibsDisguises. | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.scoreboardtest` | Test if the scoreboard is valid, this is a simple  | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd` | See all commands in tab-completion | True |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.copydisguise` | See the /copydisguise command in tab-completion | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguise` | See the /disguise command in tab-completion | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseanimation` | See the /disguiseanimation command in tab-completi | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseclone` | See the /disguiseclone command in tab-completion | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseentity` | See the /disguiseentity command in tab-completion | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseentityanimation` | See the /disguiseentityanimation command in tab-co | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguisehelp` | See the /disguisehelp command in tab-completion | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguisemodify` | See the /disguisemodify command in tab-completion | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguisemodifyentity` | See the /disguisemodifyentity command in tab-compl | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguisemodifyplayer` | See the /disguisemodifyplayer command in tab-compl | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguisemodifyradius` | See the /disguisemodifyradius command in tab-compl | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguisemodifyselector` | See the /disguisemodifyselector command in tab-com | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseplayer` | See the /disguiseplayer command in tab-completion | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseplayeranimation` | See the /disguiseplayeranimation command in tab-co | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseradius` | See the /disguiseradius command in tab-completion | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseradiusanimation` | See the /disguiseradiusanimation command in tab-co | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseselector` | See the /disguiseselector command in tab-completio | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseselectoranimation` | See the /disguiseselectoranimation command in tab- | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseviewbar` | See the /disguiseviewbar command in tab-completion | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.disguiseviewself` | See the /disguiseviewself command in tab-completio | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.grabhead` | See the /grabhead command in tab-completion | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.grabskin` | See the /grabskin command in tab-completion | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.savedisguise` | See the /savedisguise command in tab-completion | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.undisguise` | See the /undisguise command in tab-completion | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.undisguiseentity` | See the /undisguiseentity command in tab-completio | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.undisguiseplayer` | See the /undisguiseplayer command in tab-completio | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.undisguiseradius` | See the /undisguiseradius command in tab-completio | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seecmd.undisguiseselector` | See the /undisguiseselector command in tab-complet | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.seethrough` | Allows player to see through disguises. | — |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.selfdisguises` | Controls if the player can view a self disguise, d | True |
| [LibsDisguises](/commands/entity/libsdisguises.md) | `libsdisguises.update` | Allows the user to update Libs Disguises | — |
| [ModelEngine](/commands/entity/modelengine.md) | `modelengine.command` | Access to all Model Engine commands. | op |
| [YiyunCEskin](/commands/entity/yiyunceskin.md) | `yiyunceskin.admin` | Admin permission for YiyunCEskin | op |
| [YiyunCEskin](/commands/entity/yiyunceskin.md) | `yiyunceskin.use` | Basic skin usage permission | true |

## 💬 聊天与社交

| 插件 | 节点 | 说明 | 默认 |
| --- | --- | --- | --- |
| [BroadcastPlusPlus](/commands/chat/broadcastplusplus.md) | `broadcastplusplus.admin` | Full control — send, studio, reload. | op |
| [BroadcastPlusPlus](/commands/chat/broadcastplusplus.md) | `broadcastplusplus.send` | Send broadcasts and preview presets. | op |
| [BroadcastPlusPlus](/commands/chat/broadcastplusplus.md) | `broadcastplusplus.studio` | Open the Broadcast Studio GUI. | op |
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
| [TAB](/commands/chat/tab.md) | `tab.admin` | Grants all TAB permissions | op |
| [TAB](/commands/chat/tab.md) | `tab.announce.bar` | Allows player to run /tab bossbar announce | op |
| [TAB](/commands/chat/tab.md) | `tab.announce.scoreboard` | Allows player to run /tab scoreboard announce | op |
| [TAB](/commands/chat/tab.md) | `tab.bossbar.toggle` | Allows player to run /tab bossbar | op |
| [TAB](/commands/chat/tab.md) | `tab.bypass` | Makes player bypass per world playerlist if bypass | op |
| [TAB](/commands/chat/tab.md) | `tab.change.*` | Allows player to change property using command | op |
| [TAB](/commands/chat/tab.md) | `tab.cpu` | Allows player to run /tab cpu | op |
| [TAB](/commands/chat/tab.md) | `tab.dump` | Allows player to run /tab dump &lt;player&gt; | op |
| [TAB](/commands/chat/tab.md) | `tab.group.*` | Considers player in group if assigning by permissi | op |
| [TAB](/commands/chat/tab.md) | `tab.groupinfo` | Allows player to run /tab group &lt;group&gt; | op |
| [TAB](/commands/chat/tab.md) | `tab.grouplist` | Allows player to run /tab groups | op |
| [TAB](/commands/chat/tab.md) | `tab.mysql.download` | Allows player to run /tab mysql download | op |
| [TAB](/commands/chat/tab.md) | `tab.mysql.upload` | Allows player to run /tab mysql upload | op |
| [TAB](/commands/chat/tab.md) | `tab.nametag.toggle` | Allows player to run /tab nametag toggle | op |
| [TAB](/commands/chat/tab.md) | `tab.nametag.toggle.other` | Allows player to run /tab nametag toggle [other pl | op |
| [TAB](/commands/chat/tab.md) | `tab.parse` | Allows player to run /tab parse &lt;player&gt; &lt | op |
| [TAB](/commands/chat/tab.md) | `tab.reload` | Allows player to run /tab reload | op |
| [TAB](/commands/chat/tab.md) | `tab.remove` | Allows player to remove group/user using commands | op |
| [TAB](/commands/chat/tab.md) | `tab.scoreboard.show` | Allows player to run /tab scoreboard show | op |
| [TAB](/commands/chat/tab.md) | `tab.scoreboard.show.other` | Allows player to run /tab scoreboard show for othe | op |
| [TAB](/commands/chat/tab.md) | `tab.scoreboard.toggle` | Allows player to run /tab scoreboard | op |
| [TAB](/commands/chat/tab.md) | `tab.scoreboard.toggle.other` | Allows player to run /tab scoreboard for other pla | op |
| [TAB](/commands/chat/tab.md) | `tab.seevanished` | Marks player as able to see vanished players for f | op |
| [TAB](/commands/chat/tab.md) | `tab.send.bar` | Allows player to run /tab bossbar send | op |
| [TAB](/commands/chat/tab.md) | `tab.setcollision` | Allows player to run /tab setcollision &lt;player& | op |
| [TAB](/commands/chat/tab.md) | `tab.spectatorbypass` | Makes player bypass spectator fix | op |
| [TAB](/commands/chat/tab.md) | `tab.staff` | Makes player counted in %staffonline% placeholder | op |
| [TAB](/commands/chat/tab.md) | `tab.tabcomplete` | Allows player to complete all TAB commands | op |
| [vcm](/commands/chat/vcm.md) | `vcm.admin` | 允许使用管理命令（/vcm give、/vcm reload） | op |
| [vcm](/commands/chat/vcm.md) | `vcm.use` | 允许使用扩音器 | op |
| [voicechat](/commands/chat/voicechat.md) | `voicechat.admin` | Allows to test voice chat connections | — |
| [voicechat](/commands/chat/voicechat.md) | `voicechat.groups` | Allows to join groups | — |
| [voicechat](/commands/chat/voicechat.md) | `voicechat.listen` | Allows to listen to voice chat | — |
| [voicechat](/commands/chat/voicechat.md) | `voicechat.speak` | Allows to speak in voice chat | — |
| [YaoqingPlugin](/commands/chat/yaoqingplugin.md) | `yaoqing.admin` | 邀请系统管理（绑定明细/重置/重算） | op |
| [YaoqingPlugin](/commands/chat/yaoqingplugin.md) | `yaoqing.use` | 允许使用邀请功能 | True |

## 🧩 脚本与菜单

| 插件 | 节点 | 说明 | 默认 |
| --- | --- | --- | --- |
| [DeluxeMenus](/commands/config/deluxemenus.md) | `deluxemenus.admin` | admin commands | op |
| [DeluxeMenus](/commands/config/deluxemenus.md) | `deluxemenus.menu.*` | permission for all menus | op |
| [DeluxeMenus](/commands/config/deluxemenus.md) | `deluxemenus.open` | open a menu with /dm open &lt;menu&gt; | op |
| [DeluxeMenus](/commands/config/deluxemenus.md) | `deluxemenus.open.bypass` | attempt to open a menu for a viewer skipping view  | op |
| [DeluxeMenus](/commands/config/deluxemenus.md) | `deluxemenus.open.others` | open a menu with /dm open &lt;menu&gt; &lt;player& | op |
| [DeluxeMenus](/commands/config/deluxemenus.md) | `deluxemenus.openrequirement.bypass.*` | Allows the viewer to bypass all menu open requirem | op |
| [DeluxeMenus](/commands/config/deluxemenus.md) | `deluxemenus.placeholdersfor` | permission to parse menu placeholders with /dm ope | op |
| [DeluxeMenus](/commands/config/deluxemenus.md) | `deluxemenus.placeholdersfor.exempt` | exempt from placeholders being parsed when targete | op |
| [KaleidoscopeCookeryPlugin](/commands/config/kaleidoscopecookeryplugin.md) | `kaleidoscopecookery.recipe.browse` | 允许玩家用 /kcrecipe 浏览全部食谱 | op |
| [KaleidoscopeCookeryPlugin](/commands/config/kaleidoscopecookeryplugin.md) | `kaleidoscopecookery.recipe.edit` | 允许用 /kcrecipe edit 编辑食谱 | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.*` | Ability to use all PAPI commands | — |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.admin` | Ability to use all PAPI commands | — |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.ecloud` | Allows you to access PAPI eCloud | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.ecloud.*` | Ability to use all PAPI ecloud commands | — |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.ecloud.clear` | Allows you to clear the local eCloud expansion cac | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.ecloud.download` | Allows you to download an expansion from the eClou | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.ecloud.info` | Allows you to view cloud expansion information | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.ecloud.list` | Allows you to list eCloud expansions | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.ecloud.placeholders` | Allows you to view the placeholders of a eCloud ex | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.ecloud.refresh` | Allows you to refresh the local eCloud expansion c | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.ecloud.status` | Allows you to view the status of eCloud expansions | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.ecloud.update` | Allows you to update registered eCloud expansions | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.help` | Allows you to view the list of PAPI commands | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.info` | Allows you to view expansion information | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.list` | Allows you to list active expansions | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.parse` | Allows you to parse placeholders | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.register` | Allows you to register expansions | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.reload` | Allows you to reload PAPI and its configuration | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.unregister` | Allows you to unregister expansions | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.updatenotify` | Notifies you when there is a PAPI update | op |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | `placeholderapi.version` | Allows you to view the version of PAPI installed | op |
| [Skript](/commands/config/skript.md) | `skript.*` | — | — |
| [Skript](/commands/config/skript.md) | `skript.admin` | Allows use of administrative commands and receivin | op |
| [Skript](/commands/config/skript.md) | `skript.effectcommands` | Allows to use effects as commands, e.g. '!set heal | — |
| [Skript](/commands/config/skript.md) | `skript.reloadnotify` | Notifies when others are reloading script files. | — |
| [Skript](/commands/config/skript.md) | `skript.see_runtime_errors` | Shows notifications in chat when runtime errors oc | op |

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
| [GSit](/commands/minigame/gsit.md) | `GSit.*` | GSit \| Permissions | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.BellyFlop` | BellyFlop command \| Permission | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.ByPass.*` | ByPass \| Permissions | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.ByPass.Command` | ByPass command \| Permission | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.ByPass.Region` | ByPass region \| Permission | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.ByPass.World` | ByPass world \| Permission | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.Crawl` | Crawl command \| Permission | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.Crawl.*` | Crawl \| Permissions | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.CrawlSneak` | Crawl sneak \| Permission | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.CrawlToggle` | Toggle crawl ability \| Permission | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.Kick.*` | Kick \| Permissions | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.Kick.Pose` | Kick pose \| Permission | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.Kick.Sit` | Kick sit \| Permission | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.Lay` | Lay command \| Permission | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.LayBack` | LayBack command \| Permission | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.PlayerSit` | PlayerSit click \| Permission | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.PlayerSit.*` | PlayerSit \| Permissions | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.PlayerSitToggle` | Toggle PlayerSit ability \| Permission | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.Pose.*` | Pose \| Permissions | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.Reload` | Plugin reload command \| Permission | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.Sit` | Sit command \| Permission | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.Sit.*` | Sit \| Permissions | op |
| [GSit](/commands/minigame/gsit.md) | `GSit.SitClick` | Sit click \| Permission | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.SitToggle` | Toggle sit ability \| Permission | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.Spin` | Spin command \| Permission | True |
| [GSit](/commands/minigame/gsit.md) | `GSit.Update` | Update notification \| Permission | op |
| [LeashPlayers](/commands/minigame/leashplayers.md) | `leashplayers.admin` | 允许管理所有人的栓绳 / 重载配置 | op |
| [LeashPlayers](/commands/minigame/leashplayers.md) | `leashplayers.use` | 允许使用栓绳栓玩家 | True |
| [LobbyGames](/commands/minigame/lobbygames.md) | `lobbygames.admin` | Access to /lg leaderboard, /lg create, and /lg del | — |
| [LobbyGames](/commands/minigame/lobbygames.md) | `lobbygames.command` | Access to /lg list, /lg tp | — |
| [LobbyGames](/commands/minigame/lobbygames.md) | `lobbygames.forcejoin` | Access to /lgjoinplayer | — |
| [LobbyGames](/commands/minigame/lobbygames.md) | `lobbygames.kickplayer` | Access to /lg kick | — |
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
