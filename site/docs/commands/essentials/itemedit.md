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
| `itemedit.admin` | 拥有该插件的全部权限 | op |
| `itemedit.bypass.*` | 拥有该插件的全部权限 | op |
| `itemedit.bypass.censure` | 编辑项目时绕过单词限制 | op |
| `itemedit.bypass.lore_length_limit` | 在配置上设置的知识线最大长度的旁路限制 | op |
| `itemedit.bypass.lore_line_limit` | 绕过配置上设置的知识线数量的限制 | op |
| `itemedit.bypass.lore_type_restriction` | 编辑项目知识时绕过类型限制 | op |
| `itemedit.bypass.rename_length_limit` | 绕过配置上设置的重命名行最大长度的限制 | op |
| `itemedit.bypass.rename_type_restriction` | 重命名项目时绕过类型限制 | op |
| `itemedit.creativeuser` | 拥有该插件的全部权限 | op |
| `itemedit.itemedit.*` | 授予对command/itemedit的完全访问权限 | op |
| `itemedit.itemedit.amount` | 允许编辑项目金额 | op |
| `itemedit.itemedit.armortrim` | 允许在盔甲上设置修剪 | op |
| `itemedit.itemedit.axolotlvariant` | 允许在axolotl桶上编辑axolotl变体 | op |
| `itemedit.itemedit.banner` | 允许编辑横幅 | op |
| `itemedit.itemedit.bookauthor` | 允许编辑图书作者 | op |
| `itemedit.itemedit.bookenchant` | 允许编辑书籍附魔剂 | op |
| `itemedit.itemedit.bookenchant.bypass_max_level` | 允许编辑高于香草限制的书籍附魔剂 | op |
| `itemedit.itemedit.booktype` | 允许编辑图书类型 | op |
| `itemedit.itemedit.color` | 允许编辑项目颜色 | op |
| `itemedit.itemedit.color.firework_star` | 允许编辑烟花星星颜色 | op |
| `itemedit.itemedit.color.leather` | 允许编辑皮革颜色 | op |
| `itemedit.itemedit.color.potion` | 允许编辑药水颜色 | op |
| `itemedit.itemedit.color.tipped_arrow` | 允许编辑提示箭头颜色 | op |
| `itemedit.itemedit.compass` | 允许编辑罗盘位置 | op |
| `itemedit.itemedit.custommodeldata` | 允许编辑项目的自定义模型数据 | op |
| `itemedit.itemedit.damage` | 允许编辑项目耐久度-伤害 | op |
| `itemedit.itemedit.enchant` | 允许编辑物品附魔 | op |
| `itemedit.itemedit.enchant.bypass_max_level` | 允许编辑高于香草限制的物品附魔剂 | op |
| `itemedit.itemedit.equipment` | 允许设置设备属性 | op |
| `itemedit.itemedit.fireresistent` | 允许设置此堆栈的耐火性 | op |
| `itemedit.itemedit.firework` | 允许使用GUI编辑烟花 | op |
| `itemedit.itemedit.fireworkpower` | 允许编辑烟花动力 | op |
| `itemedit.itemedit.food` | 允许编辑药水效果 | op |
| `itemedit.itemedit.food.bypass_limits` | 允许编辑2级以上的药水效果 | op |
| `itemedit.itemedit.glider` | 允许设置项目行为 | op |
| `itemedit.itemedit.glow` | 允许设置发光视觉效果 | op |
| `itemedit.itemedit.goathornsound` | 允许编辑山羊喇叭声 | op |
| `itemedit.itemedit.hide` | 允许编辑项目标记 | op |
| `itemedit.itemedit.hideall` | 允许一次隐藏所有项目标志 | op |
| `itemedit.itemedit.hidetooltip` | 允许隐藏工具提示 | op |
| `itemedit.itemedit.itemmodel` | 允许设置项目纹理模型 | op |
| `itemedit.itemedit.listaliases` | 显示别名 | op |
| `itemedit.itemedit.lore` | 允许编辑物品的说明文本 | op |
| `itemedit.itemedit.lore.color.*` | 允许编辑项目知识并使用所有颜色 | op |
| `itemedit.itemedit.lore.color.aqua` | 允许编辑项目知识并使用水蓝色 | op |
| `itemedit.itemedit.lore.color.black` | 允许编辑项目知识并使用黑色 | op |
| `itemedit.itemedit.lore.color.blue` | 允许编辑项目知识并使用蓝色 | op |
| `itemedit.itemedit.lore.color.dark_aqua` | 允许编辑项目知识并使用dark_aqua颜色 | op |
| `itemedit.itemedit.lore.color.dark_blue` | 允许编辑项目知识并使用DARK_BLUE颜色 | op |
| `itemedit.itemedit.lore.color.dark_gray` | 允许编辑项目知识并使用DARK_GREY颜色 | op |
| `itemedit.itemedit.lore.color.dark_green` | 允许编辑项目知识并使用DARK_GREEN颜色 | op |
| `itemedit.itemedit.lore.color.dark_purple` | 允许编辑项目知识并使用DARK_PURPLE颜色 | op |
| `itemedit.itemedit.lore.color.dark_red` | 允许编辑项目知识并使用DARK_RED颜色 | op |
| `itemedit.itemedit.lore.color.gold` | 允许编辑项目知识并使用金色 | op |
| `itemedit.itemedit.lore.color.gray` | 允许编辑项目知识并使用灰色 | op |
| `itemedit.itemedit.lore.color.green` | 允许编辑项目知识并使用绿色 | op |
| `itemedit.itemedit.lore.color.hexa` | 允许编辑项目知识并使用十六进制颜色 | op |
| `itemedit.itemedit.lore.color.light_purple` | 允许编辑项目知识并使用LIGHT_PURPLE颜色 | op |
| `itemedit.itemedit.lore.color.red` | 允许编辑项目知识并使用红色 | op |
| `itemedit.itemedit.lore.color.white` | 允许编辑项目知识并使用白色 | op |
| `itemedit.itemedit.lore.color.yellow` | 允许编辑项目知识并使用黄色 | op |
| `itemedit.itemedit.lore.copy` | 允许使用lore子命令copy, copybook和copyfile | op |
| `itemedit.itemedit.lore.format.*` | 允许编辑项目知识并使用所有格式 | op |
| `itemedit.itemedit.lore.format.bold` | 允许编辑项目知识并使用粗体格式 | op |
| `itemedit.itemedit.lore.format.italic` | 允许编辑项目知识并使用斜体格式 | op |
| `itemedit.itemedit.lore.format.magic` | 允许编辑项目知识并使用魔法格式 | op |
| `itemedit.itemedit.lore.format.reset` | 允许编辑项目知识并使用重置格式 | op |
| `itemedit.itemedit.lore.format.strikethrough` | 允许编辑项目知识并使用删除线格式 | op |
| `itemedit.itemedit.lore.format.underline` | 允许编辑项目知识并使用下划线格式 | op |
| `itemedit.itemedit.lore.minimessage` | 允许使用最小消息占位符编辑项目知识 | op |
| `itemedit.itemedit.maxstacksize` | 允许设置最大堆栈大小 | op |
| `itemedit.itemedit.potioneffect` | 允许编辑药水效果 | op |
| `itemedit.itemedit.potioneffect.bypass_limits` | 允许编辑2级以上的药水效果 | op |
| `itemedit.itemedit.rarity` | 允许设置项目的稀有度 | op |
| `itemedit.itemedit.rename` | 允许编辑项目名称 | op |
| `itemedit.itemedit.rename.color.*` | 允许编辑项目名称并使用所有颜色 | op |
| `itemedit.itemedit.rename.color.aqua` | 允许编辑项目名称并使用水蓝色 | op |
| `itemedit.itemedit.rename.color.black` | 允许编辑项目名称并使用黑色 | op |
| `itemedit.itemedit.rename.color.blue` | 允许编辑项目名称并使用蓝色 | op |
| `itemedit.itemedit.rename.color.dark_aqua` | 允许编辑项目名称并使用dark_aqua颜色 | op |
| `itemedit.itemedit.rename.color.dark_blue` | 允许编辑项目名称并使用DARK_BLUE颜色 | op |
| `itemedit.itemedit.rename.color.dark_gray` | 允许编辑项目名称并使用DARK_GREY颜色 | op |
| `itemedit.itemedit.rename.color.dark_green` | 允许编辑项目名称并使用DARK_GREEN颜色 | op |
| `itemedit.itemedit.rename.color.dark_purple` | 允许编辑项目名称并使用DARK_PURPLE颜色 | op |
| `itemedit.itemedit.rename.color.dark_red` | 允许编辑项目名称并使用DARK_RED颜色 | op |
| `itemedit.itemedit.rename.color.gold` | 允许编辑项目名称并使用金色 | op |
| `itemedit.itemedit.rename.color.gray` | 允许编辑项目名称并使用灰色 | op |
| `itemedit.itemedit.rename.color.green` | 允许编辑项目名称并使用绿色 | op |
| `itemedit.itemedit.rename.color.hexa` | 允许编辑项目名称并使用十六进制颜色 | op |
| `itemedit.itemedit.rename.color.light_purple` | 允许编辑项目名称并使用LIGHT_PURPLE颜色 | op |
| `itemedit.itemedit.rename.color.red` | 允许编辑项目名称并使用红色 | op |
| `itemedit.itemedit.rename.color.white` | 允许编辑项目名称并使用白色 | op |
| `itemedit.itemedit.rename.color.yellow` | 允许编辑项目名称并使用黄色 | op |
| `itemedit.itemedit.rename.format.*` | 允许编辑项目名称并使用所有格式 | op |
| `itemedit.itemedit.rename.format.bold` | 允许编辑项目名称并使用粗体格式 | op |
| `itemedit.itemedit.rename.format.italic` | 允许编辑项目名称并使用斜体格式 | op |
| `itemedit.itemedit.rename.format.magic` | 允许编辑项目名称并使用魔术格式 | op |
| `itemedit.itemedit.rename.format.reset` | 允许编辑项目名称并使用重置格式 | op |
| `itemedit.itemedit.rename.format.strikethrough` | 允许编辑项目名称并使用删除线格式 | op |
| `itemedit.itemedit.rename.format.underline` | 允许编辑项目名称并使用下划线格式 | op |
| `itemedit.itemedit.rename.minimessage` | 允许使用最小消息占位符编辑项目名称 | op |
| `itemedit.itemedit.repaircost` | 允许编辑维修费用 | op |
| `itemedit.itemedit.repaircost.without_durability` | 即使在没有耐久性的物品上也允许设置维修成本 | op |
| `itemedit.itemedit.skullowner` | 允许编辑颅骨皮肤所有者 | op |
| `itemedit.itemedit.spawnereggtype` | 允许编辑怪物的蛋 | op |
| `itemedit.itemedit.tropicalfish` | 允许编辑热带鱼桶 | op |
| `itemedit.itemedit.type` | 允许编辑物料材料 | op |
| `itemedit.itemedit.unbreakable` | 允许编辑项目不可破解 | op |
| `itemedit.itemeditimport` | 授予对命令/itemeditimport的完全访问权限 | op |
| `itemedit.itemeditinfo` | 授予对command/itemeditinfo的完全访问权限 | op |
| `itemedit.itemeditreload` | 授予对命令/itemeditreload的完全访问权限 | op |
| `itemedit.itemstorage.*` | 提供对命令/itemstorage | op |
| `itemedit.itemstorage.delete` | 允许删除已存储的物品 | op |
| `itemedit.itemstorage.get` | 允许获取存储的物料 | op |
| `itemedit.itemstorage.save` | 允许存储物品 | op |
| `itemedit.itemstorage.show` | 允许查看已存储的物品 | op |
| `itemedit.itemstorage.update` | 允许更新已存储的物品 | op |
| `itemedit.serveritem.*` | 授予对命令/serveritem | op |
| `itemedit.serveritem.buy` | 允许购买固定数量的存储项目 | op |
| `itemedit.serveritem.buymax` | 允许购买已存储的物品 | op |
| `itemedit.serveritem.delete` | 允许删除已存储的物品 | op |
| `itemedit.serveritem.drop` | 允许删除存储的项目 | op |
| `itemedit.serveritem.give` | 允许提供存储的物料 | op |
| `itemedit.serveritem.save` | 允许存储物品 | op |
| `itemedit.serveritem.sell` | 允许销售固定数量的存储项目 | op |
| `itemedit.serveritem.sellmax` | 允许出售存储的物品 | op |
| `itemedit.serveritem.setnick` | 允许为存储的项目设置昵称 | op |
| `itemedit.serveritem.show` | 允许查看已存储的物品 | op |
| `itemedit.serveritem.take` | 允许取用存储的物料 | op |
| `itemedit.serveritem.update` | 允许更新已存储的物品 | op |
