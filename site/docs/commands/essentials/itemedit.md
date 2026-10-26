---
title: ItemEdit
createTime: 2026/10/24
---

# 物品编辑 · ItemEdit

> 分类 🧰 基础工具 · 版本 `3.7.10` · 指令 6 条 · api-version `1.13`

::: tip 手持物品的图形化编辑器，改名改 Lore 改属性
ItemEdit 让人不用碰命令方块和 NBT 数据，直接在界面里把手上这件物品改成想要的样子：名字、Lore、附魔、耐久、药水效果、盔甲纹饰都能调。它自带个人物品库 /itemstorage 和全服物品库 /serveritem，做好的物品可以存档、反复发放，也能配合经济插件对玩家出售或收购。适合服主做活动奖励、称号道具和商店商品，权限按功能拆得很细，可以只给管理员开放其中几项能力。
:::

## 什么时候会用到它

- 做活动奖励或礼包道具：改名、加 Lore、加发光，一次做成模板存起来反复发放。
- 临时救火：玩家物品卡住、耐久见底、数量不对，现场改数量、耐久或改成无法破坏。
- 搭建商店：先用 /serveritem 存好商品，再让玩家用经济插件买或卖。
- 配合资源包做自定义外观：给物品设置 custom model data 或 item model，替换成自己的贴图。
- 做药水、烟花、旗帜、头颅、盔甲纹饰这类特殊物品，点界面比记 NBT 快得多。

## 上手流程

1. 手上拿着要改的物品，输入 /ie 打开编辑界面；也可以直接用 /itemedit 的子指令改单项属性。
2. 按需点选修改：改名、加 Lore、调附魔等级、改数量或耐久，改动立刻作用在当前手持物品上。
3. 改满意后，用 /itemstorage 存进自己的物品库；需要全服通用就用 /serveritem 存进服务器物品库当模板。
4. 要发给玩家或上架时，从 /serveritem 取用、发放，或配合经济插件做买卖。
5. 改过插件配置后执行 /itemeditreload 让设置生效。

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/itemedit` | 打开手持物品的编辑界面，或用子指令直接改某项属性<br>别名 `/ie` | `/itemedit 子指令 [参数值]` | — |
| `/itemeditimport` | 从其它插件或旧数据导入物品配置 | `/itemeditimport` | — |
| `/itemeditinfo` | 查看 ItemEdit 的版本与运行信息 | `/itemeditinfo` | — |
| `/itemeditreload` | 重载 ItemEdit 的配置文件 | `/itemeditreload` | — |
| `/itemstorage` | 打开个人物品库，保存与取回自己做过的物品<br>别名 `/is` | `/itemstorage` | — |
| `/serveritem` | 服务器物品库，保存取回物品，并可向玩家出售或收购<br>别名 `/si` | `/serveritem` | — |

## 指令详解

### `/itemedit` — 打开手持物品的编辑界面，或用子指令直接改某项属性

- **语法**：`/itemedit 子指令 [参数值]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子指令` | 可选 | 如 rename、lore、amount、enchant 等；不写则打开编辑界面 |
| `参数值` | 可选 | 子指令需要的值，如新名称、数量、附魔等级 |


- **示例**：

```
/itemedit
/itemedit rename 星冕之剑
/itemedit amount 16
```

- **别名**：`/ie`
- **备注**：别名 /ie。主指令本身是界面入口，具体能改哪些项取决于执行者拿到的权限节点，没权限的项会直接不生效；颜色、粗体斜体等格式也要单独授权。

### `/itemeditimport` — 从其它插件或旧数据导入物品配置

- **语法**：`/itemeditimport`

- **示例**：

```
/itemeditimport
```

- **备注**：换服、换插件版本时用来把已有物品数据搬进来。导入前先备份插件数据目录，导入后抽查几件物品的名称、Lore 和附魔有没有丢掉。

### `/itemeditinfo` — 查看 ItemEdit 的版本与运行信息

- **语法**：`/itemeditinfo`

- **示例**：

```
/itemeditinfo
```

- **备注**：报 bug 或求助时先跑这条，把输出的版本号一起发出去。

### `/itemeditreload` — 重载 ItemEdit 的配置文件

- **语法**：`/itemeditreload`

- **示例**：

```
/itemeditreload
```

- **备注**：只重载配置，不会补装新权限节点。改完权限还是要靠 LuckPerms 之类重新给，重载后建议拿测试号实际试一次界面是否正常。

### `/itemstorage` — 打开个人物品库，保存与取回自己做过的物品

- **语法**：`/itemstorage`

- **示例**：

```
/itemstorage
/is
```

- **别名**：`/is`
- **备注**：别名 /is。库是跟着账号走的，适合给自己攒模板；要发给别人或给全服当商品，用 /serveritem。保存、删除、更新、查看、取出分属不同权限节点。

### `/serveritem` — 服务器物品库，保存取回物品，并可向玩家出售或收购

- **语法**：`/serveritem`

- **示例**：

```
/serveritem
/si
```

- **别名**：`/si`
- **备注**：别名 /si。这是全服共享的库，存进去的物品可以给玩家发放、让玩家取用，也能配合经济插件做定量出售/收购（对应 sell、buy、sellmax、buymax 等权限）。上架前务必确认价格和数量，控制台也能发起这类发布操作。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `rename 新名称` | 重命名手持物品，颜色与格式受授权限制 | `/itemedit rename 星冕之剑` |
| `lore` | 编辑手持物品的 Lore 说明文本 | `/itemedit lore` |
| `lore copy` | 把物品的 Lore 复制到另一件物品上 | `/itemedit lore copy` |
| `amount 数量` | 修改这一堆物品的数量 | `/itemedit amount 16` |
| `damage 数值` | 修改物品的耐久损耗值 | `/itemedit damage 100` |
| `enchant 附魔名 等级` | 给物品加附魔并设置等级 | `/itemedit enchant sharpness 5` |
| `unbreakable` | 把物品设置为无法破坏 | `/itemedit unbreakable` |
| `hideall` | 一次性隐藏物品上的全部属性标签 | `/itemedit hideall` |
| `type 材料名` | 更换物品的材质类型 | `/itemedit type diamond_sword` |
| `skullowner 玩家名` | 设置玩家头颅使用哪个玩家的皮肤 | `/itemedit skullowner Notch` |
| `potioneffect 效果名` | 给药水类物品添加或修改效果 | `/itemedit potioneffect speed` |
| `color 颜色值` | 设置皮革、药水、烟花星等物品的颜色 | `/itemedit color ff0000` |
| `custommodeldata 数值` | 设置物品的自定义模型数据，配合资源包换外观 | `/itemedit custommodeldata 1001` |
| `repaircost 数值` | 设置铁砧修理所需等级成本 | `/itemedit repaircost 10` |
| `maxstacksize 数值` | 设置这堆物品的最大堆叠数量 | `/itemedit maxstacksize 64` |
| `rarity 稀有度` | 设置物品名称的稀有度配色 | `/itemedit rarity epic` |
| `glow` | 给物品加发光效果 | `/itemedit glow` |
| `listaliases` | 显示可用的别名列表 | `/itemedit listaliases` |

## 注意事项

::: warning
- 权限拆得很细：只给 itemedit.itemedit.rename 只能写纯文本名字，要上颜色和粗体斜体还得给 itemedit.itemedit.rename.color.* 和 rename.format.* 这类子节点，Lore 同理。
- 超出原版上限的附魔等级、2 级以上的药水效果、自定义食物属性需要单独的 bypass 节点（enchant.bypass_max_level、potioneffect.bypass_limits、food.bypass_limits），不给就只能写原版范围内。
- 编辑后的物品带自定义数据和 NBT，跨版本升级、转手给其它插件前先在测试服验证能正常识别，不要直接把改过的物品批量回滚给玩家。
- 子指令与参数的完整清单以游戏内执行 /itemedit 时的提示和插件配置文件为准，命令前先在工作服试一遍再上正服。
:::

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

## 相关插件

[Vault](/commands/core/vault.md)、[LuckPerms](/commands/core/luckperms.md)、[PlaceholderAPI](/commands/config/placeholderapi.md)
