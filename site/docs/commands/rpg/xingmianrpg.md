---
title: XingmianRPG
createTime: 2026/10/24
---

# XingmianRPG

> 版本 `1.1.49` · 指令 5 条 · api-version `1.21` · 文件 `XingmianRPG-1.1.49.jar`

星陨之地 RPG 世界功能插件 —— 进入次数管控 / 星之秘钥（一次性进入道具）/ 传送封锁 / 鞘翅限滑翔 / 距离触发刷怪点 / 掉落与摇点 / boss 伤害战报

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/roll help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/roll` | 打开 boss 掉落摇点界面（大型 boss 掉落归点数最高者） | — |
| `/rpg` | 打开 RPG 世界菜单 / 进入 / 离开 / 查看状态（管理员还有刷怪点短命令） | — |
| `/rpgadmin` | RPG 世界管理命令 | `xingmianrpg.admin` |
| `/stamina` | 查看 / 增减星陨之地的体力（每天 100 点，boss -30，小怪 -0.1，0 点刷新） | — |
| `/zjbuyer` | 紫荆的怪物材料收购（每天 5 种，每样交 1 个换星点，每人每天一次） | — |

## 详细用法

### /roll

- **说明**：打开 boss 掉落摇点界面（大型 boss 掉落归点数最高者）
- **用法**：`/roll - 打开摇点界面（奖励列表 / 摇点 / 放弃摇点）`
- **别名**：`/yaodian`、`/rollpoint`、`/yd`

### /rpg

- **说明**：打开 RPG 世界菜单 / 进入 / 离开 / 查看状态（管理员还有刷怪点短命令）
- **用法**：`/rpg - 打开菜单`<br>`/rpg enter - 立即进入`<br>`/rpg leave - 离开 RPG 世界`<br>`/rpg info - 查看今日次数`<br>`/rpg dmg - 查看身边那只 boss 的实时伤害排行（boss 死时会自动播报一次战报）`<br>`/rpg ticket - 星之秘钥说明（价格 / 用法）`<br>`/rpg ticket buy [数量] - 花星点购买星之秘钥（一次性进入道具，不占每日次数）`<br>`---- 以下需要管理权限 ----`<br>`/rpg create &lt;名称&gt; [触发半径] - 建空刷怪点`<br>`/rpg create &lt;新名称&gt; copy &lt;源点位&gt; - 复制一个点位（怪物+配置照搬，位置用你站的地方）`<br>`/rpg copy &lt;新名称&gt; &lt;源点位&gt; [触发半径] - 同上`<br>`/rpg mob add &lt;名称&gt; &lt;怪物ID&gt; [每种几只] - 往点位里加怪（加几种就同时出现几种）`<br>`/rpg mob list|remove &lt;名称&gt; [怪物ID]`<br>`/rpg sp list|ids|tp|on|off|test|set|remove`
- **别名**：`/rpgmenu`、`/rpgw`

### /rpgadmin

- **说明**：RPG 世界管理命令
- **用法**：`/rpgadmin reload - 重载配置`<br>`/rpgadmin info [玩家] - 查看进入记录`<br>`/rpgadmin reset &lt;玩家&gt; - 重置今日次数`<br>`/rpgadmin set &lt;玩家&gt; &lt;已用次数&gt; - 直接设置今日已用次数`<br>`/rpgadmin return - 以当前位置设置返回点`<br>`/rpgadmin entry - 以当前位置设置 RPG 进入落点`<br>`/rpgadmin tp [玩家] - 传送到 RPG 世界（不扣次数）`<br>`/rpgadmin killmobs [点位] - 清除本插件刷出的怪`<br>`/rpgadmin ticket give &lt;玩家&gt; [数量] - 发放星之秘钥（一次性进入道具）`<br>`/rpgadmin sp create &lt;名称&gt; [触发半径] - 以当前位置建一个空刷怪点`<br>`/rpgadmin sp create &lt;新名称&gt; copy &lt;源点位&gt; - 复制点位：怪物与配置照搬，位置用当前位置`<br>`/rpgadmin sp copy &lt;新名称&gt; &lt;源点位&gt; [触发半径] - 同上`<br>`/rpgadmin sp add &lt;名称&gt; [触发半径] - 同 sp create（老写法也支持 sp add &lt;名称&gt; &lt;怪物ID&gt;）`<br>`/rpgadmin sp mob add &lt;名称&gt; &lt;怪物ID&gt;[:等级] [每种几只] - 往点位里加怪`<br>`/rpgadmin sp mob &lt;remove|list|clear&gt; &lt;名称&gt; [怪物ID]`<br>`/rpgadmin sp remove|list|tp|on|off|test|set|ids &lt;名称&gt;`<br>`/rpgadmin sp cdreset &lt;all|名称&gt; - 刷新补刷冷却（立刻可再刷，不动场上的怪）`<br>`/rpgadmin drop add &lt;怪物ID&gt; - 给这只怪建掉落规则（mode direct 直接给击杀者）`<br>`/rpgadmin drop set &lt;怪物ID&gt; mode roll - 改成摇点分配（大型 boss）`<br>`/rpgadmin drop set &lt;怪物ID&gt; pick chance|weight - 逐条独立概率 / 按权重抽件`<br>`/rpgadmin drop item add &lt;怪物ID&gt; &lt;条目名&gt; &lt;CE物品ID&gt; [概率或权重] [最少] [最多]`<br>`/rpgadmin drop cmd add &lt;怪物ID&gt; &lt;条目名&gt; [概率或权重] [最少] [最多] &lt;命令模板&gt;`<br>`/rpgadmin drop entry &lt;list|remove|set&gt; &lt;怪物ID&gt; ...`<br>`/rpgadmin drop guarantee &lt;怪物ID&gt; &lt;条目id|none&gt; - roll 摇点保底（每次必出，不占件数）`<br>`/rpgadmin drop list | test &lt;怪物ID&gt;`<br>`/rpgadmin drop ... - 与 roll 完全等价（旧名字，保留兼容）`
- **别名**：`/rgpa`、`/rpgadm`、`/xingmianrpg`
- **权限**：`xingmianrpg.admin`

### /stamina

- **说明**：查看 / 增减星陨之地的体力（每天 100 点，boss -30，小怪 -0.1，0 点刷新）
- **用法**：`/stamina - 看自己的体力`<br>`/stamina &lt;玩家&gt; - 看指定玩家的体力`<br>`/stamina add|give &lt;玩家&gt; &lt;数值&gt; - 加体力（负数即扣）`<br>`/stamina take &lt;玩家&gt; &lt;数值&gt; - 扣体力`<br>`/stamina set &lt;玩家&gt; &lt;数值&gt; - 设为指定值（0 ~ 每日满值）`<br>`/stamina reset &lt;玩家&gt; - 重置为满值`<br>`---- 均可由控制台执行，玩家可离线 ----`

### /zjbuyer

- **说明**：紫荆的怪物材料收购（每天 5 种，每样交 1 个换星点，每人每天一次）
- **用法**：`/zjbuyer - 打开收购清单`<br>`/zjbuyer info [玩家] - 聊天里列今日清单`<br>`/zjbuyer submit [玩家] - 直接提交今日材料`<br>`/zjbuyer open [玩家] - 为指定玩家打开收购界面`<br>`/zjbuyer reload - 重载 zijing.yml`
- **别名**：`/zjb`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `xingmianrpg.admin` | RPG 世界管理权限 | op |
| `xingmianrpg.bypass` | 无视 RPG 世界的传送封锁（进出都放行）、命令拦截与鞘翅限制（OP 已自动拥有） | op |
| `xingmianrpg.use` | 使用 RPG 菜单与进入 RPG 世界 | True |
| `zjbuyer.admin` | 重载紫荆收购配置 | op |
| `zjbuyer.use` | 使用紫荆的怪物材料收购 | True |
