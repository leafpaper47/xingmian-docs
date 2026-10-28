---
title: MythicMobs
createTime: 2026/10/24
---

# 自定义怪物 · MythicMobs

> 分类 ⚔️ 战斗与 RPG · 版本 `5.13.0-SNAPSHOT-850a23db` · 指令 39 条 · api-version `1.13`

::: tip 自定义怪物
用 YAML 写怪物、物品、技能和刷怪点，再用 /mm 的子指令在游戏里生成、调试和批量管理。子指令很多，先记 mobs、items、spawners 三组。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 刷一只怪 | /mm mobs spawn SkeletalKnight:3 2 | ID 后接 :等级 |
| 给自己发物品 | /mm items get SkeletonSword | ID 用 list 查 |
| 测技能 | /mm test cast Fireball | 对着实体释放 |
| 改完重载 | /mm reload | 活着的怪不换配置 |
| 查准星实体 | /mm utility gettargetinfo | 看血量等级归属 |
| 看周围刷怪点 | /mm spawners find 50 | 输出可点击 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/addpin` | 快速添加PIN码 | — | — |
| `/mythicmobs` | MythicMobs基础命令<br>别名 `/mm` | — | — |
| `/mythicmobsmenu` | 打开图形化管理菜单<br>别名 `/mmmenu`、`/mmm` | `/mythicmobsmenu` | — |
| `/pins` | 更简单的引脚命令<br>别名 `/pin` | — | — |
| `/spawnmob` | 在身前生成怪物<br>别名 `/spawnmythicmob`、`/mspawn`、`/msummon` | `/spawnmob <怪物[:等级]> [数量]` | — |
| `/mm reload` | 重载全部配置文件 | `/mm reload` | `mythicmobs.reload` |
| `/mm save` | 立刻把运行时数据写盘 | `/mm save` | — |
| `/mm version` | 查看版本号和是否有更新 | `/mm version` | — |
| `/mm debug` | 调控制台调试输出等级 | `/mm debug [0-4] ｜ /mm debug mode <true｜false>` | — |
| `/mm debug timings` | 统计技能和刷怪点耗时 | `/mm debug timings [on｜off｜skills｜spawners]` | — |
| `/mm signal` | 向技能系统广播命名信号 | `/mm signal <信号名>` | `mythicmobs.signal` |
| `/mm mobs spawn` | 在指定位置生成 MythicMobs 生物 | `/mm mobs spawn <怪物[:等级]> [数量] [-t] [-p 玩家]` | — |
| `/mm mobs kill` | 清掉指定类型的活跃生物 | `/mm mobs kill <怪物> [半径]` | — |
| `/mm mobs killall` | 清掉所有活跃的 MythicMobs 生物 | `/mm mobs killall [半径] [LITERALLY]` | — |
| `/mm mobs list` | 列出已加载的怪物 ID | `/mm mobs list [筛选词]` | — |
| `/mm mobs info` | 查某个怪物类型的配置概要 | `/mm mobs info <怪物>` | — |
| `/mm mobs stats` | 统计当前活跃生物数量 | `/mm mobs stats` | — |
| `/mm mobs listactive` | 列表活跃生物并带传送/删除按钮 | `/mm mobs listactive` | — |
| `/mm items get` | 给自己取自定义物品 | `/mm items get <物品ID> [数量]` | — |
| `/mm items give` | 把自定义物品发给指定玩家 | `/mm items give <玩家> <物品ID> [数量] [-s]` | — |
| `/mm items list` | 列出已加载的物品 ID | `/mm items list [筛选词]` | — |
| `/mm items import` | 把手上的物品导出成物品配置 | `/mm items import <物品ID> [文件名]` | — |
| `/mm items enchant` | 给手上物品加一段 MythicMobs 附魔 | `/mm items enchant <附魔名> [等级]` | — |
| `/mm skills info` | 查某个技能的配置来源与路径 | `/mm skills info <技能名>` | — |
| `/mm test cast` | 让目标实体立刻释放一次技能 | `/mm test cast <技能> [威力] [-s]` | — |
| `/mm test mechanic` | 直接执行一行技能机制 | `/mm test mechanic <机制行>` | — |
| `/mm test taunt` | 让准星所指怪物把仇恨锁到你身上 | `/mm test taunt` | — |
| `/mm spawners create` | 在瞄准的方块上创建刷怪点 | `/mm spawners create <名称> <怪物[:等级｜区间]>` | — |
| `/mm spawners remove` | 删除一个刷怪点 | `/mm spawners remove <名称>` | — |
| `/mm spawners find` | 列出附近的刷怪点 | `/mm spawners find [半径]` | — |
| `/mm spawners info` | 看刷怪点的位置、条件和关联生物 | `/mm spawners info <名称>` | — |
| `/mm spawners set` | 改刷怪点的运行属性 | `/mm spawners set <名称> <属性> <值>` | — |
| `/mm spawners activate` | 强制刷怪点立刻跑一次判定 | `/mm spawners activate <名称>` | — |
| `/mm spawners copy` | 把瞄准的方块复制成刷怪点副本 | `/mm spawners copy <源名称> <新名称>` | — |
| `/mm egg get` | 拿一只自定义怪物的刷怪蛋 | `/mm egg get <怪物> [数量]` | — |
| `/mm egg give` | 把刷怪蛋发给玩家 | `/mm egg give <玩家> <怪物> [数量]` | — |
| `/mm utility getiteminfo` | 看手上物品的材料、组件和 NBT | `/mm utility getiteminfo` | — |
| `/mm utility gettargetinfo` | 看准星所指实体的 MythicMobs 信息 | `/mm utility gettargetinfo` | — |
| `/mm pins list` | 列出已登记的 pin | `/mm pins list` | — |

## 指令详解

### `/addpin` — 快速添加PIN码


### `/mythicmobs` — MythicMobs基础命令

- **别名**：`/mm`

### `/mythicmobsmenu` — 打开图形化管理菜单

- **语法**：`/mythicmobsmenu`

- **示例**：

```
/mythicmobsmenu
```

- **别名**：`/mmmenu`、`/mmm`
- **备注**：别名 mmmenu、mmm；浏览器是 Premium 功能。

### `/pins` — 更简单的引脚命令

- **别名**：`/pin`

### `/spawnmob` — 在身前生成怪物

- **语法**：`/spawnmob <怪物[:等级]> [数量]`

- **示例**：

```
/spawnmob SkeletalKnight:5 2
```

- **别名**：`/spawnmythicmob`、`/mspawn`、`/msummon`
- **备注**：别名 mspawn、msummon，等价 mm mobs spawn。

### `/mm reload` — 重载全部配置文件

- **语法**：`/mm reload`

- **示例**：

```
/mm reload
```

- **权限**：`mythicmobs.reload`
- **备注**：写错只在控制台报错，改前备份。

### `/mm save` — 立刻把运行时数据写盘

- **语法**：`/mm save`

- **示例**：

```
/mm save
```

- **备注**：改完刷怪点兜底用。

### `/mm version` — 查看版本号和是否有更新

- **语法**：`/mm version`

- **示例**：

```
/mm version
```

- **备注**：别名 ver、v。

### `/mm debug` — 调控制台调试输出等级

- **语法**：`/mm debug [0-4] ｜ /mm debug mode <true｜false>`

- **示例**：

```
/mm debug 1
```

- **备注**：技能不触发时开；查完必须关，会拖慢控制台。

### `/mm debug timings` — 统计技能和刷怪点耗时

- **语法**：`/mm debug timings [on｜off｜skills｜spawners]`

- **示例**：

```
/mm debug timings on
```

- **备注**：找卡顿来源专用。

### `/mm signal` — 向技能系统广播命名信号

- **语法**：`/mm signal <信号名>`

- **示例**：

```
/mm signal boss_start
```

- **权限**：`mythicmobs.signal`
- **备注**：技能里用 signal 触发器接住。

### `/mm mobs spawn` — 在指定位置生成 MythicMobs 生物

- **语法**：`/mm mobs spawn <怪物[:等级]> [数量] [-t] [-p 玩家]`

- **示例**：

```
/mm mobs spawn SkeletalKnight:5 3 -t
```

- **备注**：-t 刷在准星方块；failed 且控制台无报错＝该区域禁止刷怪。ID 区分大小写。

### `/mm mobs kill` — 清掉指定类型的活跃生物

- **语法**：`/mm mobs kill <怪物> [半径]`

- **示例**：

```
/mm mobs kill SkeletalKnight 50
```

- **备注**：类型是子串匹配，Knight 会命中所有含它的 ID；-f 改按阵营。

### `/mm mobs killall` — 清掉所有活跃的 MythicMobs 生物

- **语法**：`/mm mobs killall [半径] [LITERALLY]`

- **示例**：

```
/mm mobs killall 30
```

- **备注**：不带半径＝全服所有世界；不响应 kill 的生物要加 LITERALLY。

### `/mm mobs list` — 列出已加载的怪物 ID

- **语法**：`/mm mobs list [筛选词]`

- **示例**：

```
/mm mobs list skeleton
```

- **备注**：确认配置到底加载了没有。

### `/mm mobs info` — 查某个怪物类型的配置概要

- **语法**：`/mm mobs info <怪物>`

- **示例**：

```
/mm mobs info SkeletalKnight
```


### `/mm mobs stats` — 统计当前活跃生物数量

- **语法**：`/mm mobs stats`

- **示例**：

```
/mm mobs stats
```

- **备注**：怪越刷越多、TPS 掉时先看它。

### `/mm mobs listactive` — 列表活跃生物并带传送/删除按钮

- **语法**：`/mm mobs listactive`

- **示例**：

```
/mm mobs listactive
```

- **备注**：别名 la；找卡坐标的怪最有效。

### `/mm items get` — 给自己取自定义物品

- **语法**：`/mm items get <物品ID> [数量]`

- **示例**：

```
/mm items get SkeletonSword 3
```

- **备注**：取不到多是 items.yml 配错了，控制台有 stacktrace。

### `/mm items give` — 把自定义物品发给指定玩家

- **语法**：`/mm items give <玩家> <物品ID> [数量] [-s]`

- **示例**：

```
/mm items give Steve SkeletonSword 2
```

- **备注**：玩家须在线；-s 不回显，写命令方块用。

### `/mm items list` — 列出已加载的物品 ID

- **语法**：`/mm items list [筛选词]`

- **示例**：

```
/mm items list sword
```


### `/mm items import` — 把手上的物品导出成物品配置

- **语法**：`/mm items import <物品ID> [文件名]`

- **示例**：

```
/mm items import MySword
```

- **备注**：写进 items/ 下的 yml，导完要 reload；items export 是空实现。

### `/mm items enchant` — 给手上物品加一段 MythicMobs 附魔

- **语法**：`/mm items enchant <附魔名> [等级]`

- **示例**：

```
/mm items enchant Lifesteal 3
```

- **备注**：只改手上这件，不动配置。

### `/mm skills info` — 查某个技能的配置来源与路径

- **语法**：`/mm skills info <技能名>`

- **示例**：

```
/mm skills info Fireball
```

- **备注**：skills 下只有 info，测技能用 test cast。

### `/mm test cast` — 让目标实体立刻释放一次技能

- **语法**：`/mm test cast <技能> [威力] [-s]`

- **示例**：

```
/mm test cast Fireball 5
```

- **备注**：要先瞄准或选中实体。

### `/mm test mechanic` — 直接执行一行技能机制

- **语法**：`/mm test mechanic <机制行>`

- **示例**：

```
/mm test mechanic ignite{ticks=60}
```

- **备注**：调单个 mechanism 最快，不用重载。

### `/mm test taunt` — 让准星所指怪物把仇恨锁到你身上

- **语法**：`/mm test taunt`

- **示例**：

```
/mm test taunt
```

- **备注**：测仇恨和目标选择技能用。

### `/mm spawners create` — 在瞄准的方块上创建刷怪点

- **语法**：`/mm spawners create <名称> <怪物[:等级｜区间]>`

- **示例**：

```
/mm spawners create DarkCave SkeletalKnight:1-5
```

- **备注**：名称要唯一；必须准星对着方块，否则提示 target a valid block。

### `/mm spawners remove` — 删除一个刷怪点

- **语法**：`/mm spawners remove <名称>`

- **示例**：

```
/mm spawners remove DarkCave
```

- **备注**：别名 delete、r；删点不清已刷出来的怪。

### `/mm spawners find` — 列出附近的刷怪点

- **语法**：`/mm spawners find [半径]`

- **示例**：

```
/mm spawners find 50
```

- **备注**：别名 listnear、ln；没有 list 子指令。

### `/mm spawners info` — 看刷怪点的位置、条件和关联生物

- **语法**：`/mm spawners info <名称>`

- **示例**：

```
/mm spawners info DarkCave
```

- **备注**：不刷怪先看条件是否满足、maxmobs 是否顶满。

### `/mm spawners set` — 改刷怪点的运行属性

- **语法**：`/mm spawners set <名称> <属性> <值>`

- **示例**：

```
/mm spawners set DarkCave cooldown 30
```

- **备注**：属性名对应 spawner 配置字段，改完 /mm save。

### `/mm spawners activate` — 强制刷怪点立刻跑一次判定

- **语法**：`/mm spawners activate <名称>`

- **示例**：

```
/mm spawners activate DarkCave
```

- **备注**：别名 a；不用等人靠近就能验证。

### `/mm spawners copy` — 把瞄准的方块复制成刷怪点副本

- **语法**：`/mm spawners copy <源名称> <新名称>`

- **示例**：

```
/mm spawners copy DarkCave DarkCave2
```

- **备注**：位置取准星方块，适合铺一片同款。

### `/mm egg get` — 拿一只自定义怪物的刷怪蛋

- **语法**：`/mm egg get <怪物> [数量]`

- **示例**：

```
/mm egg get SkeletalKnight
```

- **备注**：能塞进原版刷怪笼做固定点刷怪。

### `/mm egg give` — 把刷怪蛋发给玩家

- **语法**：`/mm egg give <玩家> <怪物> [数量]`

- **示例**：

```
/mm egg give Steve SkeletalKnight 3
```


### `/mm utility getiteminfo` — 看手上物品的材料、组件和 NBT

- **语法**：`/mm utility getiteminfo`

- **示例**：

```
/mm utility getiteminfo
```

- **备注**：别名 gii；查装备来自哪个插件先跑它。

### `/mm utility gettargetinfo` — 看准星所指实体的 MythicMobs 信息

- **语法**：`/mm utility gettargetinfo`

- **示例**：

```
/mm utility gettargetinfo
```

- **备注**：别名 gti；显示等级、血量、所属刷怪点。

### `/mm pins list` — 列出已登记的 pin

- **语法**：`/mm pins list`

- **示例**：

```
/mm pins list
```

- **备注**：pin 是技能用的世界锚点，别和刷怪点混淆。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/mm info` | 版本与已加载内容概要 | `/mm info` |
| `/mm items info <ID>` | 看物品定义详情 | `/mm items info SkeletonSword` |
| `/mm items edit <ID>` | 游戏内改物品，子项 enchants/lore/stats（Premium） | `/mm items edit SkeletonSword` |
| `/mm mobs clean` | 清掉失效的活跃生物记录 | `/mm mobs clean` |
| `/mm mobs browse` | 图形界面浏览编辑怪物（Premium） | `/mm mobs browse` |
| `/mm spawners move <名称>` | 挪到瞄准的方块 | `/mm spawners move DarkCave` |
| `/mm spawners cut <匹配式>` | 剪进剪贴板，配 paste、undo | `/mm spawners cut Dark*` |
| `/mm spawners addcondition <名称> <条件>` | 加触发条件，删除用 rc | `/mm spawners addcondition DarkCave daylight{}` |
| `/mm spawners addspawncondition <名称> <条件>` | 加刷怪条件，删除用 rsc | `/mm spawners addspawncondition DarkCave height{h=60}` |
| `/mm spawners resettimers <名称>` | 重置冷却计时 | `/mm spawners resettimers DarkCave` |
| `/mm debug toggleclock` | 开关技能时钟 | `/mm debug toggleclock` |
| `/mm test addthreat <数值>` | 加仇恨，reducethreat 减 | `/mm test addthreat 50` |
| `/mm utility listallentities` | 列出全服实体，带传送/删除按钮 | `/mm utility listallentities` |
| `/mm utility getblockcoordinates` | 复制准星方块坐标 | `/mm utility getblockcoordinates` |
| `/mm utility getstats` | 看目标生物属性修饰明细 | `/mm utility getstats` |
| `/mm dialogs show <dialog> [玩家]` | 弹出 dialog 预览（Premium） | `/mm dialogs show shop Steve` |
| `/mm camera` | 相机关键帧编辑 | `/mm camera` |
| `/pins` | pin 系统独立入口（/addpin 快捷建点）：createpin、createregion、wand、warp | `/pins list` |

## 注意事项

::: warning
- 改完 yml 都要 /mm reload，但已在世界里的生物不会换新配置：要么 killall 重刷，要么等它自然消失。
- /mm mobs killall 不带半径会清全服所有世界的生物，Boss、副本、刷怪点正在打的都算，只在维护窗口用。
- 刷怪点跟着创建时的世界走：换地图或直接复制世界文件夹搬服，刷怪点全部失效，得重新落点。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `mythicmobs.admin` | 方便您使用所有设施！ | op |
| `mythicmobs.reload` | 允许访问/mm重新加载！ | op |
| `mythicmobs.signal` | 提供接入/mm信号！ | op |
