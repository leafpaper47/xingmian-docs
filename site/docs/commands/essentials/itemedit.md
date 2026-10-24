---
title: ItemEdit
createTime: 2026/10/24
---

# ItemEdit

> 版本 `3.7.10` · 指令 6 条 · api-version `1.13` · 文件 `ItemEdit-3.7.10-zh.jar`

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/itemedit help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/itemedit` | 编辑手持物品 | — |
| `/itemeditimport` | 从其它插件导入配置 | — |
| `/itemeditinfo` | 查看 ItemEdit 的信息 | — |
| `/itemeditreload` | 重载配置 | — |
| `/itemstorage` | 保存与取回自己创建的物品 | — |
| `/serveritem` | 保存与取回物品，并可用控制台命令向玩家出售或购买 | — |

## 详细用法

### /itemedit

- **说明**：编辑手持物品
- **用法**：`/itemedit`
- **别名**：`/ie`

### /itemeditimport

- **说明**：从其它插件导入配置
- **用法**：`/itemeditimport`

### /itemeditinfo

- **说明**：查看 ItemEdit 的信息
- **用法**：`/itemeditinfo`

### /itemeditreload

- **说明**：重载配置
- **用法**：`/itemeditreload`

### /itemstorage

- **说明**：保存与取回自己创建的物品
- **用法**：`/itemstorage`
- **别名**：`/is`

### /serveritem

- **说明**：保存与取回物品，并可用控制台命令向玩家出售或购买
- **用法**：`/serveritem`
- **别名**：`/si`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `itemedit.admin` | Gives full access to the plugin | op |
| `itemedit.bypass.*` | Gives full access to the plugin | op |
| `itemedit.bypass.censure` | Bypass words restrictions when editing items | op |
| `itemedit.bypass.lore_length_limit` | Bypass restrictions on lore line max length set on config | op |
| `itemedit.bypass.lore_line_limit` | Bypass restrictions on lore line amount set on config | op |
| `itemedit.bypass.lore_type_restriction` | Bypass type restrictions when editing item lore | op |
| `itemedit.bypass.rename_length_limit` | Bypass restrictions on rename line max length set on config | op |
| `itemedit.bypass.rename_type_restriction` | Bypass type restrictions when renaming items | op |
| `itemedit.creativeuser` | Gives full access to the plugin | op |
| `itemedit.itemedit.*` | Gives full access to command /itemedit | op |
| `itemedit.itemedit.amount` | Allow editing item amount | op |
| `itemedit.itemedit.armortrim` | Allow setting trims on armor | op |
| `itemedit.itemedit.axolotlvariant` | Allow editing axolotl variant on axolotl buckets | op |
| `itemedit.itemedit.banner` | Allow editing banners | op |
| `itemedit.itemedit.bookauthor` | Allow editing book author | op |
| `itemedit.itemedit.bookenchant` | Allow editing book enchants | op |
| `itemedit.itemedit.bookenchant.bypass_max_level` | Allow editing book enchants above vanilla limits | op |
| `itemedit.itemedit.booktype` | Allow editing book type | op |
| `itemedit.itemedit.color` | Allow editing items colors | op |
| `itemedit.itemedit.color.firework_star` | Allow editing firework star color | op |
| `itemedit.itemedit.color.leather` | Allow editing leather color | op |
| `itemedit.itemedit.color.potion` | Allow editing potion color | op |
| `itemedit.itemedit.color.tipped_arrow` | Allow editing tipped arrow color | op |
| `itemedit.itemedit.compass` | Allow editing compass location | op |
| `itemedit.itemedit.custommodeldata` | Allow editing custom model data of items | op |
| `itemedit.itemedit.damage` | Allow editing item durability-damage | op |
| `itemedit.itemedit.enchant` | Allow editing item enchants | op |
| `itemedit.itemedit.enchant.bypass_max_level` | Allow editing item enchants above vanilla limits | op |
| `itemedit.itemedit.equipment` | Allow setting equipment properties | op |
| `itemedit.itemedit.fireresistent` | Allow setting fire resistance of this stack | op |
| `itemedit.itemedit.firework` | Allow editing fireworks with a gui | op |
| `itemedit.itemedit.fireworkpower` | Allow editing fireworks power | op |
| `itemedit.itemedit.food` | Allow editing potion effects | op |
| `itemedit.itemedit.food.bypass_limits` | Allow editing potion effects above level 2 | op |
| `itemedit.itemedit.glider` | Allow setting the item behavior | op |
| `itemedit.itemedit.glow` | Allow setting glow visual effect | op |
| `itemedit.itemedit.goathornsound` | Allow editing goat horn sound | op |
| `itemedit.itemedit.hide` | Allow editing item flags | op |
| `itemedit.itemedit.hideall` | Allow to hide all item flags at once | op |
| `itemedit.itemedit.hidetooltip` | Allow hiding tooltips | op |
| `itemedit.itemedit.itemmodel` | Allow setting item texture model | op |
| `itemedit.itemedit.listaliases` | Shows aliases | op |
| `itemedit.itemedit.lore` | Allow editing item lore | op |
| `itemedit.itemedit.lore.color.*` | Allow editing item lore and use all colors | op |
| `itemedit.itemedit.lore.color.aqua` | Allow editing item lore and use aqua color | op |
| `itemedit.itemedit.lore.color.black` | Allow editing item lore and use black color | op |
| `itemedit.itemedit.lore.color.blue` | Allow editing item lore and use blue color | op |
| `itemedit.itemedit.lore.color.dark_aqua` | Allow editing item lore and use dark_aqua color | op |
| `itemedit.itemedit.lore.color.dark_blue` | Allow editing item lore and use dark_blue color | op |
| `itemedit.itemedit.lore.color.dark_gray` | Allow editing item lore and use dark_gray color | op |
| `itemedit.itemedit.lore.color.dark_green` | Allow editing item lore and use dark_green color | op |
| `itemedit.itemedit.lore.color.dark_purple` | Allow editing item lore and use dark_purple color | op |
| `itemedit.itemedit.lore.color.dark_red` | Allow editing item lore and use dark_red color | op |
| `itemedit.itemedit.lore.color.gold` | Allow editing item lore and use gold color | op |
| `itemedit.itemedit.lore.color.gray` | Allow editing item lore and use gray color | op |
| `itemedit.itemedit.lore.color.green` | Allow editing item lore and use green color | op |
| `itemedit.itemedit.lore.color.hexa` | Allow editing item lore and use hexa colors | op |
| `itemedit.itemedit.lore.color.light_purple` | Allow editing item lore and use light_purple color | op |
| `itemedit.itemedit.lore.color.red` | Allow editing item lore and use red color | op |
| `itemedit.itemedit.lore.color.white` | Allow editing item lore and use white color | op |
| `itemedit.itemedit.lore.color.yellow` | Allow editing item lore and use yellow color | op |
| `itemedit.itemedit.lore.copy` | Allow to use lore sub commands copy, copybook and copyfile | op |
| `itemedit.itemedit.lore.format.*` | Allow editing item lore and use all formats | op |
| `itemedit.itemedit.lore.format.bold` | Allow editing item lore and use bold format | op |
| `itemedit.itemedit.lore.format.italic` | Allow editing item lore and use italic format | op |
| `itemedit.itemedit.lore.format.magic` | Allow editing item lore and use magic format | op |
| `itemedit.itemedit.lore.format.reset` | Allow editing item lore and use reset format | op |
| `itemedit.itemedit.lore.format.strikethrough` | Allow editing item lore and use strikethrough format | op |
| `itemedit.itemedit.lore.format.underline` | Allow editing item lore and use underline format | op |
| `itemedit.itemedit.lore.minimessage` | Allow editing item lore using minimessage placeholders | op |
| `itemedit.itemedit.maxstacksize` | Allow setting max stack size | op |
| `itemedit.itemedit.potioneffect` | Allow editing potion effects | op |
| `itemedit.itemedit.potioneffect.bypass_limits` | Allow editing potion effects above level 2 | op |
| `itemedit.itemedit.rarity` | Allow setting rarity of an item | op |
| `itemedit.itemedit.rename` | Allow editing item name | op |
| `itemedit.itemedit.rename.color.*` | Allow editing item name and use all colors | op |
| `itemedit.itemedit.rename.color.aqua` | Allow editing item name and use aqua color | op |
| `itemedit.itemedit.rename.color.black` | Allow editing item name and use black color | op |
| `itemedit.itemedit.rename.color.blue` | Allow editing item name and use blue color | op |
| `itemedit.itemedit.rename.color.dark_aqua` | Allow editing item name and use dark_aqua color | op |
| `itemedit.itemedit.rename.color.dark_blue` | Allow editing item name and use dark_blue color | op |
| `itemedit.itemedit.rename.color.dark_gray` | Allow editing item name and use dark_gray color | op |
| `itemedit.itemedit.rename.color.dark_green` | Allow editing item name and use dark_green color | op |
| `itemedit.itemedit.rename.color.dark_purple` | Allow editing item name and use dark_purple color | op |
| `itemedit.itemedit.rename.color.dark_red` | Allow editing item name and use dark_red color | op |
| `itemedit.itemedit.rename.color.gold` | Allow editing item name and use gold color | op |
| `itemedit.itemedit.rename.color.gray` | Allow editing item name and use gray color | op |
| `itemedit.itemedit.rename.color.green` | Allow editing item name and use green color | op |
| `itemedit.itemedit.rename.color.hexa` | Allow editing item name and use hexa colors | op |
| `itemedit.itemedit.rename.color.light_purple` | Allow editing item name and use light_purple color | op |
| `itemedit.itemedit.rename.color.red` | Allow editing item name and use red color | op |
| `itemedit.itemedit.rename.color.white` | Allow editing item name and use white color | op |
| `itemedit.itemedit.rename.color.yellow` | Allow editing item name and use yellow color | op |
| `itemedit.itemedit.rename.format.*` | Allow editing item name and use all formats | op |
| `itemedit.itemedit.rename.format.bold` | Allow editing item name and use bold format | op |
| `itemedit.itemedit.rename.format.italic` | Allow editing item name and use italic format | op |
| `itemedit.itemedit.rename.format.magic` | Allow editing item name and use magic format | op |
| `itemedit.itemedit.rename.format.reset` | Allow editing item name and use reset format | op |
| `itemedit.itemedit.rename.format.strikethrough` | Allow editing item name and use strikethrough format | op |
| `itemedit.itemedit.rename.format.underline` | Allow editing item name and use underline format | op |
| `itemedit.itemedit.rename.minimessage` | Allow editing item name using minimessage placeholders | op |
| `itemedit.itemedit.repaircost` | Allow editing repair costs | op |
| `itemedit.itemedit.repaircost.without_durability` | Allow to set a repair cost even on items which have no durability | op |
| `itemedit.itemedit.skullowner` | Allow editing skull skin owner | op |
| `itemedit.itemedit.spawnereggtype` | Allow editing monster's egg | op |
| `itemedit.itemedit.tropicalfish` | Allow editing tropical fish buckets | op |
| `itemedit.itemedit.type` | Allow editing item material | op |
| `itemedit.itemedit.unbreakable` | Allow editing item unbreakablity | op |
| `itemedit.itemeditimport` | Gives full access to command /itemeditimport | op |
| `itemedit.itemeditinfo` | Gives full access to command /itemeditinfo | op |
| `itemedit.itemeditreload` | Gives full access to command /itemeditreload | op |
| `itemedit.itemstorage.*` | Gives full access to command /itemstorage | op |
| `itemedit.itemstorage.delete` | Allow to delete stored items | op |
| `itemedit.itemstorage.get` | Allow to get stored items | op |
| `itemedit.itemstorage.save` | Allow to store items | op |
| `itemedit.itemstorage.show` | Allow to show stored items | op |
| `itemedit.itemstorage.update` | Allow to update stored items | op |
| `itemedit.serveritem.*` | Gives full access to command /serveritem | op |
| `itemedit.serveritem.buy` | Allow to buy fixed amount of stored items | op |
| `itemedit.serveritem.buymax` | Allow to buy stored items | op |
| `itemedit.serveritem.delete` | Allow to delete stored items | op |
| `itemedit.serveritem.drop` | Allow to drop stored items | op |
| `itemedit.serveritem.give` | Allow to give stored items | op |
| `itemedit.serveritem.save` | Allow to store items | op |
| `itemedit.serveritem.sell` | Allow to sell fixed amount of stored items | op |
| `itemedit.serveritem.sellmax` | Allow to sell stored items | op |
| `itemedit.serveritem.setnick` | Allow to set nicks for stored items | op |
| `itemedit.serveritem.show` | Allow to show stored items | op |
| `itemedit.serveritem.take` | Allow to take stored items | op |
| `itemedit.serveritem.update` | Allow to update stored items | op |
