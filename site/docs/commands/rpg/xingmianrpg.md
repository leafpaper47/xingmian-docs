---
title: XingmianRPG
createTime: 2026/10/24
---

# 星陨RPG · XingmianRPG

> 分类 ⚔️ 战斗与成长 · 版本 `1.1.53` · 指令 49 条 · api-version `1.21`

::: tip RPG 世界管控
管星陨之地的进出次数、传送与鞘翅限制、刷怪点、boss 掉落摇点，另带体力值与紫荆材料收购。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 进星陨之地 | /rpg enter | 每次进入扣一次当日次数 |
| 看今天还能进几次 | /rpg info | 用完了用 /rpg ticket buy 买秘钥 |
| 建刷怪点 | /rpg create K1 96 | 站到位置敲，96 是触发半径 |
| 往里加怪 | /rpg mob add K1 skeleton_melee | 加几种就同时出几种 |
| boss 改摇点 | /rpgadmin drop set rock_dragon mode roll | roll 摇点，direct 给击杀者 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/roll` | 打开 boss 掉落摇点界面，点数最高者得<br>别名 `/yaodian`、`/rollpoint`、`/yd` | `/roll` | — |
| `/rpg` | 打开 RPG 世界菜单<br>别名 `/rpgmenu`、`/rpgw` | `/rpg [enter\|leave\|info\|dmg\|ticket]` | — |
| `/rpg enter` | 进入星陨之地并扣一次当日次数 | — | — |
| `/rpg leave` | 离开星陨之地并送回返回点 | — | — |
| `/rpg info` | 查今日已用次数与收费档位 | — | — |
| `/rpg dmg` | 查身边那只 boss 的实时伤害排行 | — | — |
| `/rpg ticket` | 查看星之秘钥价格与用法 | — | — |
| `/rpg ticket buy` | 花星点购买星之秘钥 | — | — |
| `/rpg create` | 以当前位置建一个空刷怪点 | `/rpg create <名称> [触发半径]` | — |
| `/rpg copy` | 复制现有点位的怪与配置到你站的位置 | — | — |
| `/rpg mob add` | 往点位加一种怪 | `/rpg mob add <名称> <怪物ID>[:等级] [每种几只]` | — |
| `/rpgadmin` | RPG 世界管理总入口<br>别名 `/rgpa`、`/rpgadm`、`/xingmianrpg` | `/rpgadmin <子指令> [参数...]` | `xingmianrpg.admin` |
| `/rpgadmin reload` | 重载 config.yml | — | — |
| `/rpgadmin info` | 查玩家今日进入记录 | — | — |
| `/rpgadmin reset` | 把玩家今日次数清零 | — | — |
| `/rpgadmin set` | 直接设玩家今日已用次数 | — | — |
| `/rpgadmin return` | 以当前位置设置返回点 | — | — |
| `/rpgadmin entry` | 以当前位置设置进入落点 | — | — |
| `/rpgadmin tp` | 把玩家传进星陨之地，不扣次数 | — | — |
| `/rpgadmin killmobs` | 清掉本插件刷出来的怪 | — | — |
| `/rpgadmin ticket give` | 给玩家发星之秘钥 | — | — |
| `/rpgadmin sp create` | 以当前位置建空刷怪点 | — | — |
| `/rpgadmin sp copy` | 复制点位的怪与配置到当前位置 | — | — |
| `/rpgadmin sp mob add` | 往点位加怪，可带等级与每种只数 | — | — |
| `/rpgadmin sp mob remove` | 从点位删掉一种怪 | — | — |
| `/rpgadmin sp mob list` | 看点位配了哪些怪 | — | — |
| `/rpgadmin sp list` | 列全部点位与场上/目标怪数 | — | — |
| `/rpgadmin sp ids` | 列 MythicMobs 全部怪物 ID | — | — |
| `/rpgadmin sp set` | 改点位参数 | — | — |
| `/rpgadmin sp test` | 临时试刷点位 | — | — |
| `/rpgadmin sp cdreset` | 清补刷冷却，下一人进圈立刻刷整批 | — | — |
| `/rpgadmin sp remove` | 删除整个刷怪点 | — | — |
| `/rpgadmin drop add` | 给一只怪建掉落规则 | — | — |
| `/rpgadmin drop item add` | 往规则里加一条物品掉落 | `/rpgadmin drop item add <怪物ID> <条目名> <CE物品ID> [概率或…` | — |
| `/rpgadmin drop cmd add` | 往规则里加一条命令奖励 | — | — |
| `/rpgadmin drop set` | 改掉落规则字段 | `/rpgadmin drop set <怪物ID> <字段> <值>` | — |
| `/rpgadmin drop entry set` | 改某条掉落的概率、权重或数量区间 | `/rpgadmin drop entry set <怪物ID> <条目名> <字段> <值>` | — |
| `/rpgadmin drop entry remove` | 删掉某条掉落 | — | — |
| `/rpgadmin drop guarantee` | 设摇点保底条目，每次必出 | `/rpgadmin drop guarantee <怪物ID> <条目名｜none>` | — |
| `/rpgadmin drop list` | 看这只怪的规则与全部条目 | — | — |
| `/rpgadmin drop test` | 就地模拟抽一次掉落 | — | — |
| `/rpgadmin drop remove` | 删掉整条掉落规则 | — | — |
| `/stamina` | 查看玩家体力，不填参数看自己 | `/stamina [玩家] · /stamina add\|take\|set <玩家> <数值>` | — |
| `/stamina add` | 给玩家加体力，负数即扣 | — | — |
| `/zjbuyer` | 打开紫荆的今日材料收购界面<br>别名 `/zjb` | `/zjbuyer [info\|submit\|open\|reload] [玩家]` | — |
| `/zjbuyer info` | 在聊天里列今日收购清单 | — | — |
| `/zjbuyer submit` | 直接提交今日材料换星点 | — | — |
| `/zjbuyer open` | 为指定玩家打开收购界面 | — | — |
| `/zjbuyer reload` | 重载紫荆收购配置 zijing.yml | — | — |

## 指令详解

### `/roll` — 打开 boss 掉落摇点界面，点数最高者得

- **语法**：`/roll`

- **示例**：

```
/roll
```

- **别名**：`/yaodian`、`/rollpoint`、`/yd`
- **备注**：别名 yaodian、rollpoint、yd；只有 mode roll 的掉落要摇，摇中可放弃

### `/rpg` — 打开 RPG 世界菜单

- **语法**：`/rpg [enter|leave|info|dmg|ticket]`

- **示例**：

```
/rpg
```

- **别名**：`/rpgmenu`、`/rpgw`
- **备注**：别名 rpgmenu、rpgw

### `/rpg enter` — 进入星陨之地并扣一次当日次数


- **示例**：

```
/rpg enter
```

- **备注**：只在进入那一刻计次，死亡、离开都不多扣

### `/rpg leave` — 离开星陨之地并送回返回点


- **示例**：

```
/rpg leave
```

- **备注**：还原成进入前记录的游戏模式

### `/rpg info` — 查今日已用次数与收费档位


- **示例**：

```
/rpg info
```


### `/rpg dmg` — 查身边那只 boss 的实时伤害排行


- **示例**：

```
/rpg dmg
```

- **备注**：boss 死亡自动播报战报

### `/rpg ticket` — 查看星之秘钥价格与用法


- **示例**：

```
/rpg ticket
```

- **备注**：右键消耗 1 把进场，不占每日次数

### `/rpg ticket buy` — 花星点购买星之秘钥


- **示例**：

```
/rpg ticket buy 2
```

- **备注**：单次上限看 config 的 max-buy

### `/rpg create` — 以当前位置建一个空刷怪点

- **语法**：`/rpg create <名称> [触发半径]`

- **示例**：

```
/rpg create K1 96
```

- **备注**：建完还要 mob add 加怪才会刷

### `/rpg copy` — 复制现有点位的怪与配置到你站的位置


- **示例**：

```
/rpg copy K2 K1
```


### `/rpg mob add` — 往点位加一种怪

- **语法**：`/rpg mob add <名称> <怪物ID>[:等级] [每种几只]`

- **示例**：

```
/rpg mob add K1 skeleton_archer 2
```

- **备注**：加几种就同时出几种；ID 写错一只也不刷

### `/rpgadmin` — RPG 世界管理总入口

- **语法**：`/rpgadmin <子指令> [参数...]`

- **示例**：

```
/rpgadmin reload
```

- **别名**：`/rgpa`、`/rpgadm`、`/xingmianrpg`
- **权限**：`xingmianrpg.admin`
- **备注**：别名 rgpa、rpgadm；整条命令需 xingmianrpg.admin

### `/rpgadmin reload` — 重载 config.yml


- **示例**：

```
/rpgadmin reload
```

- **备注**：改点位、掉落表、次数价格后必跑

### `/rpgadmin info` — 查玩家今日进入记录


- **示例**：

```
/rpgadmin info Steve
```

- **备注**：标「进行中」多是死亡或掉线残留

### `/rpgadmin reset` — 把玩家今日次数清零


- **示例**：

```
/rpgadmin reset Steve
```


### `/rpgadmin set` — 直接设玩家今日已用次数


- **示例**：

```
/rpgadmin set Steve 0
```


### `/rpgadmin return` — 以当前位置设置返回点


- **示例**：

```
/rpgadmin return
```

- **备注**：必须站主世界敲，站 RPG 世界会被拒绝

### `/rpgadmin entry` — 以当前位置设置进入落点


- **示例**：

```
/rpgadmin entry
```

- **备注**：必须站 RPG 世界敲，设好立刻生效

### `/rpgadmin tp` — 把玩家传进星陨之地，不扣次数


- **示例**：

```
/rpgadmin tp Steve
```


### `/rpgadmin killmobs` — 清掉本插件刷出来的怪


- **示例**：

```
/rpgadmin killmobs K1
```

- **备注**：不点名则清全部

### `/rpgadmin ticket give` — 给玩家发星之秘钥


- **示例**：

```
/rpgadmin ticket give Steve 2
```

- **备注**：CE 不可用时退成自制纸片票

### `/rpgadmin sp create` — 以当前位置建空刷怪点


- **示例**：

```
/rpgadmin sp create K1 96
```

- **备注**：sp add 是老写法，等同 create

### `/rpgadmin sp copy` — 复制点位的怪与配置到当前位置


- **示例**：

```
/rpgadmin sp copy K2 K1
```


### `/rpgadmin sp mob add` — 往点位加怪，可带等级与每种只数


- **示例**：

```
/rpgadmin sp mob add K1 skeleton_melee
```


### `/rpgadmin sp mob remove` — 从点位删掉一种怪


- **示例**：

```
/rpgadmin sp mob remove K1 skeleton_archer
```

- **备注**：删光变空点位，不再刷

### `/rpgadmin sp mob list` — 看点位配了哪些怪


- **示例**：

```
/rpgadmin sp mob list K1
```


### `/rpgadmin sp list` — 列全部点位与场上/目标怪数


- **示例**：

```
/rpgadmin sp list
```


### `/rpgadmin sp ids` — 列 MythicMobs 全部怪物 ID


- **示例**：

```
/rpgadmin sp ids
```

- **备注**：拿不到说明 MM 没装或没加载完

### `/rpgadmin sp set` — 改点位参数


- **示例**：

```
/rpgadmin sp set K1 interval 300
```

- **备注**：字段 radius、spawn-radius、min、max、interval、level、y、despawn、enabled

### `/rpgadmin sp test` — 临时试刷点位


- **示例**：

```
/rpgadmin sp test K1
```

- **备注**：不入名单、不补刷、不影响正式冷却

### `/rpgadmin sp cdreset` — 清补刷冷却，下一人进圈立刻刷整批


- **示例**：

```
/rpgadmin sp cdreset all
```

- **备注**：只清冷却不动场上的怪

### `/rpgadmin sp remove` — 删除整个刷怪点


- **示例**：

```
/rpgadmin sp remove K2
```

- **备注**：删除后不可撤销

### `/rpgadmin drop add` — 给一只怪建掉落规则


- **示例**：

```
/rpgadmin drop add skeleton_melee
```

- **备注**：建了规则才由本插件发掉落，原版掉落被清

### `/rpgadmin drop item add` — 往规则里加一条物品掉落

- **语法**：`/rpgadmin drop item add <怪物ID> <条目名> <CE物品ID> [概率或权重] [最少] [最多]`

- **示例**：

```
/rpgadmin drop item add skeleton_melee tooth default:monster_tooth 1
```

- **备注**：CE物品ID 是 CraftEngine 物品 ID，不是原版物品名

### `/rpgadmin drop cmd add` — 往规则里加一条命令奖励


- **示例**：

```
/rpgadmin drop cmd add skeleton_melee 星点 10 5 eco give {player} {amount}
```

- **备注**：模板放最后可带空格，支持 {player} 与 {amount}

### `/rpgadmin drop set` — 改掉落规则字段

- **语法**：`/rpgadmin drop set <怪物ID> <字段> <值>`

- **示例**：

```
/rpgadmin drop set rock_dragon mode roll
```

- **备注**：字段 mode、pick、drops-min、drops-max、min-players、max-points、enabled

### `/rpgadmin drop entry set` — 改某条掉落的概率、权重或数量区间

- **语法**：`/rpgadmin drop entry set <怪物ID> <条目名> <字段> <值>`

- **示例**：

```
/rpgadmin drop entry set skeleton_melee tooth chance 1.5
```

- **备注**：字段 chance、weight、min-amount、max-amount、roll、display、type、value

### `/rpgadmin drop entry remove` — 删掉某条掉落


- **示例**：

```
/rpgadmin drop entry remove skeleton_melee tooth
```


### `/rpgadmin drop guarantee` — 设摇点保底条目，每次必出

- **语法**：`/rpgadmin drop guarantee <怪物ID> <条目名｜none>`

- **示例**：

```
/rpgadmin drop guarantee Stone_Golem core-3
```

- **备注**：不占 drops-min/max 件数；none 清空

### `/rpgadmin drop list` — 看这只怪的规则与全部条目


- **示例**：

```
/rpgadmin drop list rock_dragon
```

- **备注**：规则建了池子却空着等于白建

### `/rpgadmin drop test` — 就地模拟抽一次掉落


- **示例**：

```
/rpgadmin drop test skeleton_melee
```

- **备注**：抽到 roll 条目会发起摇点

### `/rpgadmin drop remove` — 删掉整条掉落规则


- **示例**：

```
/rpgadmin drop remove skeleton_melee
```

- **备注**：删后掉落交回原版或 MythicMobs，不可撤销

### `/stamina` — 查看玩家体力，不填参数看自己

- **语法**：`/stamina [玩家] · /stamina add|take|set <玩家> <数值>`

- **示例**：

```
/stamina Steve
```

- **备注**：每天满 100，boss 扣 30、小怪扣 0.1，0 点刷新

### `/stamina add` — 给玩家加体力，负数即扣


- **示例**：

```
/stamina add Steve 30
```

- **备注**：控制台可执行，离线玩家也生效

### `/zjbuyer` — 打开紫荆的今日材料收购界面

- **语法**：`/zjbuyer [info|submit|open|reload] [玩家]`

- **示例**：

```
/zjbuyer
```

- **别名**：`/zjb`
- **备注**：别名 zjb；每天 5 种材料，每样交 1 个换星点，每人每天一次

### `/zjbuyer info` — 在聊天里列今日收购清单


- **示例**：

```
/zjbuyer info
```


### `/zjbuyer submit` — 直接提交今日材料换星点


- **示例**：

```
/zjbuyer submit Steve
```

- **备注**：今日已交过会提示，不重复给星点

### `/zjbuyer open` — 为指定玩家打开收购界面


- **示例**：

```
/zjbuyer open Steve
```


### `/zjbuyer reload` — 重载紫荆收购配置 zijing.yml


- **示例**：

```
/zjbuyer reload
```

- **备注**：需 zjbuyer.admin；改完材料池与价格必跑

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/stamina take` | 扣玩家体力：take &lt;玩家&gt; &lt;数值&gt; | `/stamina take Steve 30` |
| `/stamina set` | 体力设成指定值，取值 0 到每日满值 | `/stamina set Steve 50` |
| `/stamina reset` | 体力重置为满值 | `/stamina reset Steve` |
| `/rpg sp` | 建点调参短写法：list、ids、set、test、tp、on、off、remove | `/rpg sp set K1 interval 300` |

## 注意事项

::: warning
- rpgadmin reset 与 set 直接改玩家今日次数，先 /rpgadmin info 核对再动。
- rpgadmin return 只能站主世界敲，entry 只能站 RPG 世界敲，站错会被拒绝。
- 权限：/rpg 与 /roll 用 xingmianrpg.use，rpgadmin 子指令用 xingmianrpg.admin，/zjbuyer 用 zjbuyer.use；bypass 一并放行传送、命令拦截与鞘翅限制。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `xingmianrpg.admin` | RPG 世界管理权限 | op |
| `xingmianrpg.bypass` | 无视 RPG 世界的传送封锁（进出都放行）、命令拦截与鞘翅限制（OP 已自动拥有） | op |
| `xingmianrpg.use` | 使用 RPG 菜单与进入 RPG 世界 | True |
| `zjbuyer.admin` | 重载紫荆收购配置 | op |
| `zjbuyer.use` | 使用紫荆的怪物材料收购 | True |
