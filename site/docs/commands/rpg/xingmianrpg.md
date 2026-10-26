---
title: XingmianRPG
createTime: 2026/10/24
---

# 星冕RPG · XingmianRPG

> 分类 ⚔️ 战斗与 RPG · 版本 `1.1.49` · 指令 5 条 · api-version `1.21`

::: tip 星陨之地 RPG 世界的整套玩法管控插件
XingmianRPG 负责「星陨之地」这个 RPG 世界的全部规则：进出次数管控、星之秘钥（一次性进入道具）、世界内传送与命令封锁、鞘翅限滑翔、按距离触发的刷怪点、怪物掉落与摇点分配、boss 伤害战报，另外附带体力值与紫荆材料收购两个日常系统。命令分成三层：/rpg 给玩家用，/rpgadmin 给管理员配刷怪点和掉落，/stamina 与 /zjbuyer 管两条日常循环。绝大部分配置都在插件自身的 yml 里，改完用 /rpgadmin reload 生效。
:::

## 什么时候会用到它

- 让玩家进入「星陨之地」RPG 世界并限制每日进入次数
- 用星之秘钥道具让玩家额外进入一次，不占当天次数
- 在世界内封锁传送与部分命令，并限制鞘翅无限滑翔
- 配置按距离触发的刷怪点，按点位管理怪物与刷新冷却
- 给 boss 配掉落表：直接给击杀者或走摇点按点数分配
- 查看 boss 实时伤害排行与结算战报
- 管理玩家体力值，以及紫荆的每日材料收购换星点

## 上手流程

1. 用 /rpgadmin entry 与 /rpgadmin return 先把进入落点和返回点定好
2. 用 /rpgadmin sp create 建刷怪点，再用 /rpgadmin sp mob add 往里加怪物
3. 用 /rpgadmin drop add 给 boss 建掉落规则，必要时改成 roll 摇点并设保底
4. 玩家用 /rpg 进世界，打完 boss 用 /roll 摇点分装备
5. 改完配置文件执行 /rpgadmin reload，再用 /rpgadmin info 与 /stamina 核对状态

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/roll` | 打开 boss 掉落摇点界面，按点数最高者得奖励<br>别名 `/yaodian`、`/rollpoint`、`/yd` | `/roll` | — |
| `/rpg` | 打开 RPG 世界菜单，可进入、离开、查次数与伤害排行<br>别名 `/rpgmenu`、`/rpgw` | `/rpg [enter｜leave｜info｜dmg｜ticket]` | — |
| `/rpgadmin` | 管理 RPG 世界：点位、刷怪、掉落、次数与钥匙<br>别名 `/rgpa`、`/rpgadm`、`/xingmianrpg` | `/rpgadmin [reload｜info｜reset｜set｜return｜entry｜tp｜k…` | `xingmianrpg.admin` |
| `/stamina` | 查看或增减玩家体力，每天满 100 点 | `/stamina [玩家] 或 /stamina add｜give｜take｜set｜reset 玩…` | — |
| `/zjbuyer` | 紫荆的每日怪物材料收购，交材料换星点<br>别名 `/zjb` | `/zjbuyer [info｜submit｜open｜reload] [玩家]` | — |

## 指令详解

### `/roll` — 打开 boss 掉落摇点界面，按点数最高者得奖励

- **语法**：`/roll`

- **示例**：

```
/roll
```

- **别名**：`/yaodian`、`/rollpoint`、`/yd`
- **备注**：别名 yaodian、rollpoint、yd。只对配置成 roll 模式的大型 boss 掉落生效，普通怪默认直接给击杀者；摇中后可以点放弃摇点。

### `/rpg` — 打开 RPG 世界菜单，可进入、离开、查次数与伤害排行

- **语法**：`/rpg [enter｜leave｜info｜dmg｜ticket]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子指令` | 可选 | 不带参数打开菜单；enter 立即进入；leave 离开世界；info 查看今日次数；dmg 查看身边那只 boss 的实时伤害排行；ticket 看星之秘钥说明，ticket buy [数量] 花星点购买 |
| `数量` | 可选 | 仅 ticket buy 使用，指购买几把星之秘钥，省略时按 1 把处理 |


- **示例**：

```
/rpg
/rpg enter
/rpg info
/rpg dmg
/rpg ticket buy 2
```

- **别名**：`/rpgmenu`、`/rpgw`
- **备注**：别名 rpgmenu、rpgw。建点、加怪、copy 等管理子指令也挂在这个命令下，但需要 xingmianrpg.admin。boss 死亡时插件会自动播报一次战报，不用手动敲 dmg。

### `/rpgadmin` — 管理 RPG 世界：点位、刷怪、掉落、次数与钥匙

- **语法**：`/rpgadmin [reload｜info｜reset｜set｜return｜entry｜tp｜killmobs｜ticket｜sp｜drop]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子指令` | 必填 | reload 重载配置；info [玩家] 查进入记录；reset 重置今日次数；set 玩家 次数 直接设已用次数；return 与 entry 用当前位置设返回点与进入落点；tp [玩家] 传进世界且不扣次数；killmobs [点位] 清除本插件刷出的怪；ticket give 玩家 [数量] 发星之秘钥 |
| `sp 系列` | 可选 | sp create 建空点位；sp create 新名称 copy 源点位 或 sp copy 复制点位；sp mob add 加怪；sp mob remove｜list｜clear 管怪；sp remove｜list｜tp｜on｜off｜test｜set｜ids 管点位；sp cdreset all 或 点位 刷新补刷冷却 |
| `drop 系列` | 可选 | drop add 怪物ID 建掉落规则；drop set 怪物ID mode roll 改摇点；pick chance｜weight 切换独立概率或按权重抽件；drop item add 加物品条目；drop cmd add 加命令条目；drop entry list｜remove｜set 管条目；drop guarantee 设摇点保底；drop list 与 drop test 预览测试 |
| `怪物ID` | 可选 | 对应怪物插件里的怪物标识，sp mob add 还支持写成 怪物ID:等级 的写法 |


- **示例**：

```
/rpgadmin reload
/rpgadmin sp create 荒漠祭坛 16
/rpgadmin sp mob add 荒漠祭坛 zombie 3
/rpgadmin drop set boss_sand mode roll
/rpgadmin ticket give Steve 2
```

- **别名**：`/rgpa`、`/rpgadm`、`/xingmianrpg`
- **权限**：`xingmianrpg.admin`
- **备注**：别名 rgpa、rpgadm、xingmianrpg，需要 xingmianrpg.admin。drop 系列和 /roll 的旧名字完全等价；drop item add 的 CE物品ID 指服务端自定义物品插件里的物品 ID，不是原版物品名。

### `/stamina` — 查看或增减玩家体力，每天满 100 点

- **语法**：`/stamina [玩家] 或 /stamina add｜give｜take｜set｜reset 玩家 数值`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `玩家` | 可选 | 目标玩家名，可离线；省略时查自己 |
| `数值` | 可选 | add 与 give 为加值（负数即扣），take 为扣除量，set 则设为该值，范围 0 到每日满值 |


- **示例**：

```
/stamina
/stamina Steve
/stamina add Steve -30
/stamina set Steve 50
/stamina reset Steve
```

- **备注**：体力每天 100 点，boss 扣 30、小怪扣 0.1，降到 0 后需要刷新恢复。所有子指令都能由控制台执行，玩家离线也能改。

### `/zjbuyer` — 紫荆的每日怪物材料收购，交材料换星点

- **语法**：`/zjbuyer [info｜submit｜open｜reload] [玩家]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子指令` | 可选 | 不带参数打开收购清单界面；info [玩家] 在聊天里列今日清单；submit [玩家] 直接提交今日材料；open [玩家] 为指定玩家打开界面；reload 重载 zijing.yml |
| `玩家` | 可选 | 代操作的目标玩家，省略时默认自己 |


- **示例**：

```
/zjbuyer
/zjbuyer info
/zjbuyer submit
/zjbuyer open Steve
```

- **别名**：`/zjb`
- **备注**：别名 zjb。每天刷 5 种材料，每样交 1 个换星点，每人每天一次；reload 需要 zjbuyer.admin，普通使用要 zjbuyer.use。

## 注意事项

::: warning
- 这是星冕服务器自研插件，具体参数与可用子指令以游戏内 help 和在服上实测为准，别照抄网上的通用教程。
- 大部分子指令需要 xingmianrpg.admin（默认 op），/rpg 与 /roll 走 xingmianrpg.use，/zjbuyer 走 zjbuyer.use；权限收回后玩家连菜单都打不开。
- xingmianrpg.bypass 会同时放行传送封锁、命令拦截和鞘翅限制，OP 默认自带，排查「为什么他能飞/能传送」先看这条。
- 改完 yml 一定要 /rpgadmin reload（收购配置用 /zjbuyer reload），否则刷怪点与掉落表还是旧数据。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `xingmianrpg.admin` | RPG 世界管理权限 | op |
| `xingmianrpg.bypass` | 无视 RPG 世界的传送封锁（进出都放行）、命令拦截与鞘翅限制（OP 已自动拥有） | op |
| `xingmianrpg.use` | 使用 RPG 菜单与进入 RPG 世界 | True |
| `zjbuyer.admin` | 重载紫荆收购配置 | op |
| `zjbuyer.use` | 使用紫荆的怪物材料收购 | True |

## 相关插件

[MythicMobs](/commands/rpg/mythicmobs.md)、CraftEngine
