---
title: Essentials
createTime: 2026/10/24
---

# 基础指令 · Essentials

> 分类 🧰 基础工具 · 版本 `2.22.1-dev+12-776f709` · 指令 153 条 · api-version `1.13`

::: tip 服务器基础指令总控，管理、传送、经济全靠它
Essentials 是 Minecraft 服务端最常见的基础指令插件，把传送、家与地标、经济、封禁禁言、物品与背包管理、运行状态查询这些日常操作打包成一套指令。它自己就能管钱（用 eco 给钱），也可以通过 Vault 把余额共享给商店、点券、任务类插件。管理员绝大部分后台操作都从它开始，配合 LuckPerms 管权限、EssentialsSpawn 管多世界出生点最顺手。
:::

## 什么时候会用到它

- 新玩家进服要用地标、家、新手礼包这类基础福利指令
- 日常管人：封禁、限时封禁、禁言、踢人、查坐标、看背包
- 搭主城：设地标、设出生点附近的家、配随机传送的中心和半径
- 配经济：给钱扣钱、给物品定回收价、做财富排行榜
- 自己排查问题：看 TPS、内存、在线名单、某人最后一次上线时间

## 上手流程

1. 先在控制台执行 /essentials 确认插件加载正常、版本正确
2. 用 LuckPerms 把 essentials.* 或按需的 essentials.xxx 发给管理组，普通玩家只给传送、家、私信这类
3. 用 /setwarp 把主城、副本、商店等重要地点标出来，玩家用 /warp 名单里的地标传送
4. 用 /eco、/setworth、/createkit 配好启动资金、回收价和新手礼包
5. 最后按需调 config.yml 里的冷却、传送等待秒数、以及是否开启 tpa 需要对方同意

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/afk` | 把自己或指定玩家标记为暂离，可附自定义留言<br>别名 `/eafk`、`/away`、`/eaway` | `/afk [玩家名或留言]` | — |
| `/antioch` | OP 恶搞指令，在原地炸出一发大范围 TNT<br>别名 `/eantioch`、`/grenade`、`/egrenade`、`/tnt`、`/etnt` | `/antioch [留言]` | — |
| `/anvil` | 原地打开铁砧界面，修装备、改名字不用回家<br>别名 `/eanvil` | `/anvil` | — |
| `/back` | 回到上一次传送或死亡之前的位置<br>别名 `/eback`、`/return`、`/ereturn` | `/back [玩家名]` | — |
| `/backup` | 按配置立刻触发一次服务器备份<br>别名 `/ebackup` | `/backup` | — |
| `/balance` | 查看自己或他人的金币余额<br>别名 `/bal`、`/ebal`、`/ebalance`、`/money`、`/emoney` | `/balance [玩家名]` | — |
| `/balancetop` | 查看服务器财富排行榜<br>别名 `/ebalancetop`、`/baltop`、`/ebaltop` | `/balancetop [页码]` | — |
| `/ban` | 封禁玩家，可以附上原因<br>别名 `/eban` | `/ban 玩家名 [原因]` | — |
| `/banip` | 封禁某个 IP 地址<br>别名 `/ebanip` | `/banip IP地址 [原因]` | — |
| `/beezooka` | 娱乐指令，向准心方向射出一只爆炸蜜蜂<br>别名 `/ebeezooka`、`/beecannon`、`/ebeecannon` | `/beezooka` | — |
| `/bigtree` | 在准心处生成一棵大树，可指定树种<br>别名 `/ebigtree`、`/largetree`、`/elargetree` | `/bigtree 树种` | — |
| `/book` | 重新打开手里的成书继续编辑<br>别名 `/ebook` | `/book [title 或 author 参数：新名字]` | — |
| `/bottom` | 传送到当前位置最低的一层可站立方块<br>别名 `/ebottom` | `/bottom` | — |
| `/break` | 直接破坏准心对着的那个方块<br>别名 `/ebreak` | `/break` | — |
| `/broadcast` | 向全服玩家发一条公告<br>别名 `/bc`、`/ebc`、`/bcast`、`/ebcast`、`/ebroadcast`、`/shout`、`/eshout` | `/broadcast 消息内容` | — |
| `/broadcastworld` | 只向指定世界发公告<br>别名 `/bcw`、`/ebcw`、`/bcastw`、`/ebcastw`、`/ebroadcastworld`、`/shoutworld`、`/eshoutworld` | `/broadcastworld 世界名 消息内容` | — |
| `/burn` | 点燃指定玩家若干秒<br>别名 `/eburn` | `/burn 玩家名 秒数` | — |
| `/cartographytable` | 原地打开制图台<br>别名 `/ecartographytable`、`/carttable`、`/ecarttable` | `/cartographytable` | — |
| `/clearinventory` | 清空自己或他人背包，可按物品筛选<br>别名 `/ci`、`/eci`、`/clean`、`/eclean`、`/clear`、`/eclear`、`/clearinvent`、`/eclearinvent`、`/eclearinventory` | `/clearinventory [玩家名或星号] [物品或星号] [数量]` | — |
| `/clearinventoryconfirmtoggle` | 开关清背包前的二次确认提示<br>别名 `/eclearinventoryconfirmtoggle`、`/clearinventoryconfirmoff`、`/eclearinventoryconfirmoff`、`/clearconfirmoff`、`/eclearconfirmoff`、`/clearconfirmon`、`/eclearconfirmon`、`/clearconfirm`、`/eclearconfirm` | `/clearinventoryconfirmtoggle` | — |
| `/compass` | 报告自己当前的朝向和方位<br>别名 `/ecompass`、`/direction`、`/edirection` | `/compass` | — |
| `/condense` | 把背包里的散装物品压成块，如铁锭转铁块<br>别名 `/econdense`、`/compact`、`/ecompact`、`/blocks`、`/eblocks`、`/toblocks`、`/etoblocks` | `/condense [物品名]` | — |
| `/createkit` | 把自己当前背包内容存成一个礼包<br>别名 `/kitcreate`、`/createk`、`/kc`、`/ck` | `/createkit 礼包名 冷却秒数` | — |
| `/customtext` | 配合 bukkit.yml 的自定义指令，输出一段纯文本 | `/自定义文本指令名` | — |
| `/delhome` | 删除自己的某个家<br>别名 `/edelhome`、`/remhome`、`/eremhome`、`/rmhome`、`/ermhome` | `/delhome [玩家名:]家名` | — |
| `/deljail` | 删除指定监狱点<br>别名 `/edeljail`、`/remjail`、`/eremjail`、`/rmjail`、`/ermjail` | `/deljail 监狱名` | — |
| `/delkit` | 删除指定礼包<br>别名 `/edelkit`、`/remkit`、`/eremkit`、`/rmkit`、`/ermkit`、`/deletekit`、`/edeletekit` | `/delkit 礼包名` | — |
| `/delwarp` | 删除指定地标<br>别名 `/edelwarp`、`/remwarp`、`/eremwarp`、`/rmwarp`、`/ermwarp` | `/delwarp 地标名` | — |
| `/depth` | 报告当前高度相对海平面的深度<br>别名 `/edepth`、`/height`、`/eheight` | `/depth` | — |
| `/disposal` | 打开随身垃圾桶，随手丢东西<br>别名 `/edisposal`、`/trash`、`/etrash` | `/disposal` | — |
| `/eco` | 管理经济：给钱、扣钱、设置、清零<br>别名 `/eeco`、`/economy`、`/eeconomy` | `/eco 增减方式 玩家名 金额` | — |
| `/editsign` | 直接改写地上告示牌的文字<br>别名 `/sign`、`/esign`、`/eeditsign` | `/editsign set或clear或copy或paste [行号] [文字]` | — |
| `/enchant` | 给手上的物品附魔并指定等级<br>别名 `/eenchant`、`/enchantment`、`/eenchantment` | `/enchant 附魔名 [等级]` | — |
| `/enderchest` | 打开自己或他人的末影箱<br>别名 `/echest`、`/eechest`、`/eenderchest`、`/endersee`、`/eendersee`、`/ec`、`/eec` | `/enderchest [玩家名]` | — |
| `/essentials` | 查看 Essentials 的版本与加载状态<br>别名 `/eessentials`、`/ess`、`/eess`、`/essversion` | `/essentials` | — |
| `/exp` | 给经验、设经验、清零或查看经验<br>别名 `/eexp`、`/xp` | `/exp 操作 玩家名 [数值]` | — |
| `/ext` | 熄灭自己或他人身上的火<br>别名 `/eext`、`/extinguish`、`/eextinguish` | `/ext [玩家名]` | — |
| `/feed` | 回满自己或他人的饥饿值<br>别名 `/eat`、`/eeat`、`/efeed` | `/feed [玩家名]` | — |
| `/fireball` | 朝准心发射火球等各种投掷物<br>别名 `/efireball`、`/fireentity`、`/efireentity`、`/fireskull`、`/efireskull` | `/fireball [投掷物类型] [速度]` | — |
| `/firework` | 编辑手上烟花的参数并燃放<br>别名 `/efirework` | `/firework 参数或power或clear或fire [数值]` | — |
| `/fly` | 开关自己或他人的飞行<br>别名 `/efly` | `/fly [玩家名] [on或off]` | — |
| `/gamemode` | 切换自己或他人的游戏模式<br>别名 `/adventure`、`/eadventure`、`/adventuremode`、`/eadventuremode`、`/creative`、`/ecreative`、`/eecreative`、`/creativemode`、`/ecreativemode`、`/egamemode`、`/gm`、`/egm`、`/gma`、`/egma`、`/gmc`、`/egmc`、`/gms`、`/egms`、`/gmt`、`/egmt`、`/survival`、`/esurvival`、`/survivalmode`、`/esurvivalmode`、`/gmsp`、`/sp`、`/egmsp`、`/spec`、`/spectator` | `/gamemode 模式 [玩家名]` | — |
| `/gc` | 查看内存、在线数、TPS 等运行状态<br>别名 `/lag`、`/elag`、`/egc`、`/mem`、`/emem`、`/memory`、`/ememory`、`/uptime`、`/euptime`、`/tps`、`/etps`、`/entities`、`/eentities` | `/gc` | — |
| `/getpos` | 查看自己或他人的坐标<br>别名 `/coords`、`/egetpos`、`/position`、`/eposition`、`/whereami`、`/ewhereami`、`/getlocation`、`/egetlocation`、`/getloc`、`/egetloc` | `/getpos [玩家名]` | — |
| `/give` | 给玩家发放物品并指定数量<br>别名 `/egive` | `/give 玩家名 物品名 [数量]` | — |
| `/god` | 开关无敌模式<br>别名 `/egod`、`/godmode`、`/egodmode`、`/tgm`、`/etgm` | `/god [玩家名] [on或off]` | — |
| `/grindstone` | 原地打开砂轮，附魔随意装卸<br>别名 `/egrindstone` | `/grindstone` | — |
| `/hat` | 把手上的方块或物品戴到头上<br>别名 `/ehat`、`/head`、`/ehead` | `/hat [remove]` | — |
| `/heal` | 回满自己或他人的血量<br>别名 `/eheal` | `/heal [玩家名]` | — |
| `/help` | 列出可用指令，支持关键词搜索<br>别名 `/ehelp` | `/help [关键词] [页码]` | — |
| `/helpop` | 向在线管理员发一条求助消息<br>别名 `/ac`、`/eac`、`/amsg`、`/eamsg`、`/ehelpop` | `/helpop 消息内容` | — |
| `/home` | 回家，可以指定家名<br>别名 `/ehome`、`/homes`、`/ehomes` | `/home [玩家名:]家名` | — |
| `/ice` | 把玩家冻住，限制其移动<br>别名 `/eice`、`/efreeze` | `/ice [玩家名]` | — |
| `/ignore` | 屏蔽某个玩家的发言<br>别名 `/eignore`、`/unignore`、`/eunignore`、`/delignore`、`/edelignore`、`/remignore`、`/eremignore`、`/rmignore`、`/ermignore` | `/ignore 玩家名` | — |
| `/info` | 查看服主预先写好的服务器介绍<br>别名 `/about`、`/eabout`、`/ifo`、`/eifo`、`/einfo`、`/inform`、`/einform`、`/news`、`/enews` | `/info [章节] [页码]` | — |
| `/invsee` | 查看他人背包的内容<br>别名 `/einvsee` | `/invsee 玩家名` | — |
| `/item` | 直接给自己刷一个物品<br>别名 `/i`、`/eitem`、`/ei` | `/item 物品名 [数量]` | — |
| `/itemdb` | 查物品的 ID、耐久等信息<br>别名 `/dura`、`/edura`、`/durability`、`/edurability`、`/eitemdb`、`/itemno`、`/eitemno` | `/itemdb 物品` | — |
| `/itemlore` | 给手上物品加、改、清说明文字<br>别名 `/lore`、`/elore`、`/ilore`、`/eilore`、`/eitemlore` | `/itemlore add或set或clear [文字或行号] [文字]` | — |
| `/itemname` | 给手上的物品改名<br>别名 `/iname`、`/einame`、`/eitemname`、`/itemrename`、`/irename`、`/eitemrename`、`/eirename` | `/itemname [新名字]` | — |
| `/jailedplayers` | 列出当前所有在押玩家<br>别名 `/ejailedplayers`、`/ejailed`、`/ejp` | `/jailedplayers` | — |
| `/jails` | 列出所有已设置的监狱<br>别名 `/ejails` | `/jails` | — |
| `/jump` | 瞬移到准心指向的那个方块上<br>别名 `/j`、`/ej`、`/ejump`、`/jumpto`、`/ejumpto` | `/jump` | — |
| `/kick` | 把玩家踢下线，可附原因<br>别名 `/ekick` | `/kick 玩家名 [原因]` | — |
| `/kickall` | 把除自己以外的玩家全部踢下线<br>别名 `/ekickall` | `/kickall [原因]` | — |
| `/kill` | 直接击杀指定玩家<br>别名 `/ekill` | `/kill 玩家名` | — |
| `/kit` | 领取礼包，或查看自己能领哪些礼包<br>别名 `/ekit`、`/kits`、`/ekits` | `/kit [礼包名] [玩家名]` | — |
| `/kitreset` | 重置某个礼包的领取冷却<br>别名 `/ekitreset`、`/kitr`、`/ekitr`、`/resetkit`、`/eresetkit` | `/kitreset 礼包名 [玩家名]` | — |
| `/kittycannon` | 娱乐指令，向准心方向扔一只爆炸小猫<br>别名 `/ekittycannon` | `/kittycannon` | — |
| `/lightning` | 在准心或指定玩家身上劈下闪电<br>别名 `/elightning`、`/shock`、`/eshock`、`/smite`、`/esmite`、`/strike`、`/estrike`、`/thor`、`/ethor` | `/lightning [玩家名] [强度]` | — |
| `/list` | 查看当前在线玩家名单<br>别名 `/elist`、`/online`、`/eonline`、`/playerlist`、`/eplayerlist`、`/plist`、`/eplist`、`/who`、`/ewho` | `/list [分组]` | — |
| `/loom` | 原地打开织布机<br>别名 `/eloom` | `/loom` | — |
| `/mail` | 收发站内离线邮件<br>别名 `/email`、`/eemail`、`/memo`、`/ememo` | `/mail read或clear或send [收件人] [内容]` | — |
| `/me` | 以第三人称描述自己做的一个动作<br>别名 `/action`、`/eaction`、`/describe`、`/edescribe`、`/eme` | `/me 动作描述` | — |
| `/more` | 把手上的物品补满一整组<br>别名 `/emore` | `/more [数量]` | — |
| `/motd` | 查看服务器每日公告<br>别名 `/emotd` | `/motd [章节] [页码]` | — |
| `/msg` | 给某个玩家发一条私信<br>别名 `/w`、`/m`、`/t`、`/pm`、`/emsg`、`/epm`、`/tell`、`/etell`、`/whisper`、`/ewhisper` | `/msg 玩家名 消息内容` | — |
| `/msgtoggle` | 开关是否接收别人的私信<br>别名 `/emsgtoggle` | `/msgtoggle [玩家名] [on或off]` | — |
| `/mute` | 禁言或解禁玩家，可限时<br>别名 `/emute`、`/silence`、`/esilence`、`/unmute`、`/eunmute` | `/mute 玩家名 [时长] [原因]` | — |
| `/near` | 列出自己或某人身边一定范围内的玩家<br>别名 `/enear`、`/nearby`、`/enearby` | `/near [玩家名] [半径]` | — |
| `/nick` | 改自己或他人的昵称<br>别名 `/enick`、`/nickname`、`/enickname` | `/nick [玩家名] 昵称或off` | — |
| `/nuke` | 娱乐指令，让目标玩家原地爆炸<br>别名 `/enuke` | `/nuke [玩家名]` | — |
| `/pay` | 把余额里的钱转给其他玩家<br>别名 `/epay` | `/pay 玩家名 金额` | — |
| `/payconfirmtoggle` | 开关转账前的大额确认提示<br>别名 `/epayconfirmtoggle`、`/payconfirmoff`、`/epayconfirmoff`、`/payconfirmon`、`/epayconfirmon`、`/payconfirm`、`/epayconfirm` | `/payconfirmtoggle` | — |
| `/paytoggle` | 开关是否接受别人转账<br>别名 `/epaytoggle`、`/payoff`、`/epayoff`、`/payon`、`/epayon` | `/paytoggle [玩家名]` | — |
| `/ping` | 测一下当前自己到服务器的延迟<br>别名 `/echo`、`/eecho`、`/eping`、`/pong`、`/epong` | `/ping` | — |
| `/playtime` | 查看自己或他人的累计游戏时长<br>别名 `/eplaytime` | `/playtime [玩家名]` | — |
| `/potion` | 给手上的药水写入自定义药水效果<br>别名 `/epotion`、`/elixer`、`/eelixer` | `/potion clear或apply或效果参数` | — |
| `/powertool` | 把手上的物品绑定一条指令，左键即执行<br>别名 `/epowertool`、`/pt`、`/ept` | `/powertool [前缀] 指令` | — |
| `/powertoollist` | 列出当前已绑定的动力工具<br>别名 `/epowertoollist`、`/ptlist`、`/eptlist` | `/powertoollist` | — |
| `/powertooltoggle` | 一键启用或禁用所有动力工具<br>别名 `/epowertooltoggle`、`/ptt`、`/eptt`、`/pttoggle`、`/epttoggle` | `/powertooltoggle` | — |
| `/ptime` | 只改某个玩家的客户端时间，不影响全服<br>别名 `/playertime`、`/eplayertime`、`/eptime` | `/ptime 时间 [玩家名或星号]` | — |
| `/pweather` | 只改某个玩家的客户端天气<br>别名 `/playerweather`、`/eplayerweather`、`/epweather` | `/pweather 天气 [玩家名或星号]` | — |
| `/r` | 快速回复上一条收到的私信<br>别名 `/er`、`/reply`、`/ereply` | `/r 消息内容` | — |
| `/realname` | 用昵称反查玩家的真实 ID<br>别名 `/erealname` | `/realname 昵称` | — |
| `/recipe` | 查看某个物品的合成配方<br>别名 `/formula`、`/eformula`、`/method`、`/emethod`、`/erecipe`、`/recipes`、`/erecipes` | `/recipe 物品名 [数量]` | — |
| `/remove` | 批量清理世界里的实体，如掉落物、动物<br>别名 `/eremove`、`/butcher`、`/ebutcher`、`/killall`、`/ekillall`、`/mobkill`、`/emobkill` | `/remove 类型 [半径或世界]` | — |
| `/renamehome` | 给已有的家改个名字<br>别名 `/erenamehome` | `/renamehome 旧家名 新家名` | — |
| `/repair` | 修满手上或全部装备的耐久<br>别名 `/fix`、`/efix`、`/erepair` | `/repair [hand或all]` | — |
| `/rest` | 重置自己或他人的睡眠计时，防幻翼刷出<br>别名 `/erest` | `/rest [玩家名]` | — |
| `/rtoggle` | 设置 /r 回复的是最后发信人还是最后收信人<br>别名 `/ertoggle`、`/replytoggle`、`/ereplytoggle` | `/rtoggle [玩家名] [on或off]` | — |
| `/rules` | 查看服务器规则<br>别名 `/erules` | `/rules [章节] [页码]` | — |
| `/seen` | 查看玩家最后一次下线的时间<br>别名 `/eseen`、`/ealts`、`/alts` | `/seen 玩家名` | — |
| `/sell` | 把手上的物品卖给系统换钱<br>别名 `/esell` | `/sell 物品名或hand或inventory [数量]` | — |
| `/sethome` | 把当前位置设为家，可自定义家名<br>别名 `/esethome`、`/createhome`、`/ecreatehome` | `/sethome [玩家名:]家名` | — |
| `/setjail` | 以当前位置创建一间监狱<br>别名 `/esetjail`、`/createjail`、`/ecreatejail` | `/setjail 监狱名` | — |
| `/settpr` | 设置随机传送的中心点和远近范围<br>别名 `/esettpr`、`/settprandom`、`/esettprandom` | `/settpr center或minrange或maxrange [数值]` | — |
| `/setwarp` | 以当前位置创建一个地标<br>别名 `/createwarp`、`/ecreatewarp`、`/esetwarp` | `/setwarp 地标名` | — |
| `/setworth` | 设置某个物品的回收价格<br>别名 `/esetworth` | `/setworth 物品名 价格` | — |
| `/showkit` | 预览某个礼包里都有什么<br>别名 `/kitpreview`、`/preview`、`/kitshow` | `/showkit 礼包名` | — |
| `/skull` | 设置手上头颅属于哪个玩家<br>别名 `/eskull`、`/playerskull`、`/eplayerskull`、`/head`、`/ehead` | `/skull [头颅主人] [玩家名]` | — |
| `/smithingtable` | 原地打开锻造台<br>别名 `/esmithingtable`、`/smithtable`、`/esmithtable` | `/smithingtable` | — |
| `/socialspy` | 开关偷看他人私信和邮件的模式<br>别名 `/esocialspy` | `/socialspy [玩家名] [on或off]` | — |
| `/spawner` | 改刷怪笼生成什么生物，可设间隔<br>别名 `/changems`、`/echangems`、`/espawner`、`/mobspawner`、`/emobspawner` | `/spawner 生物名 [间隔秒数]` | — |
| `/spawnmob` | 生成指定生物，可带数量与骑乘关系<br>别名 `/mob`、`/emob`、`/spawnentity`、`/espawnentity`、`/espawnmob` | `/spawnmob 生物名 [数量] [玩家名]` | — |
| `/speed` | 改自己或他人的行走、飞行速度<br>别名 `/flyspeed`、`/eflyspeed`、`/fspeed`、`/efspeed`、`/espeed`、`/walkspeed`、`/ewalkspeed`、`/wspeed`、`/ewspeed` | `/speed [类型] 速度值 [玩家名]` | — |
| `/stonecutter` | 原地打开切石机<br>别名 `/estonecutter` | `/stonecutter` | — |
| `/sudo` | 让某个玩家替你执行一条指令<br>别名 `/esudo` | `/sudo 玩家名 指令` | — |
| `/suicide` | 让自己立刻死亡<br>别名 `/esuicide` | `/suicide` | — |
| `/tempban` | 限时封禁玩家<br>别名 `/etempban` | `/tempban 玩家名 时长 [原因]` | — |
| `/tempbanip` | 限时封禁某个 IP 地址<br>别名 `/etempbanip` | `/tempbanip IP地址 时长 [原因]` | — |
| `/thunder` | 开关雷雨天，可指定持续时长<br>别名 `/ethunder` | `/thunder true或false [时长]` | — |
| `/time` | 查看或修改世界时间<br>别名 `/day`、`/eday`、`/night`、`/enight`、`/etime` | `/time [set或add] 时间 [世界名或all]` | — |
| `/togglejail` | 把玩家关进监狱，或把在押玩家放出来<br>别名 `/jail`、`/ejail`、`/tjail`、`/etjail`、`/etogglejail`、`/unjail`、`/eunjail` | `/togglejail 玩家名 监狱名 [时长]` | — |
| `/top` | 传送到当前位置最高的方块上方<br>别名 `/etop` | `/top` | — |
| `/tp` | 把自己或某人传送到目标玩家<br>别名 `/tele`、`/etele`、`/teleport`、`/eteleport`、`/etp`、`/tp2p`、`/etp2p` | `/tp 目标玩家 [被传送者]` | — |
| `/tpa` | 申请传送到某个玩家身边<br>别名 `/call`、`/ecall`、`/etpa`、`/tpask`、`/etpask` | `/tpa 玩家名` | — |
| `/tpaall` | 让所有在线玩家申请传送到某人身边<br>别名 `/etpaall` | `/tpaall 玩家名` | — |
| `/tpacancel` | 撤回自己发出的所有传送申请<br>别名 `/etpacancel` | `/tpacancel [玩家名]` | — |
| `/tpaccept` | 同意别人的传送申请<br>别名 `/etpaccept`、`/tpyes`、`/etpyes` | `/tpaccept [玩家名或星号]` | — |
| `/tpahere` | 申请把某个玩家拉到自己身边<br>别名 `/etpahere` | `/tpahere 玩家名` | — |
| `/tpall` | 把所有在线玩家传送到某个玩家那里<br>别名 `/etpall` | `/tpall [玩家名]` | — |
| `/tpauto` | 开关自动同意收到的传送申请<br>别名 `/etpauto` | `/tpauto [玩家名]` | — |
| `/tpdeny` | 拒绝别人的传送申请<br>别名 `/etpdeny`、`/tpno`、`/etpno` | `/tpdeny [玩家名或星号]` | — |
| `/tphere` | 直接把某个玩家拉到自己身边<br>别名 `/s`、`/etphere` | `/tphere 玩家名` | — |
| `/tpo` | 无视对方关闭传送的限制，强行传送过去<br>别名 `/etpo` | `/tpo 目标玩家 [被传送者]` | — |
| `/tpoffline` | 传送到离线玩家最后下线的位置<br>别名 `/otp`、`/offlinetp`、`/tpoff`、`/tpoffline`、`/etpoffline` | `/tpoffline 玩家名` | — |
| `/tpohere` | 无视限制，强行把玩家拉到自己身边<br>别名 `/etpohere` | `/tpohere 玩家名` | — |
| `/tppos` | 按指定坐标传送自己<br>别名 `/etppos` | `/tppos X坐标 Y坐标 Z坐标 [朝向] [俯仰] [世界名]` | — |
| `/tpr` | 随机传送到世界某处<br>别名 `/etpr`、`/tprandom`、`/etprandom` | `/tpr` | — |
| `/tptoggle` | 开关自己是否允许被别人传送<br>别名 `/etptoggle` | `/tptoggle [玩家名] [on或off]` | — |
| `/tree` | 在准心处生成一棵树，可指定树种<br>别名 `/etree` | `/tree 树种` | — |
| `/unban` | 解除对某个玩家的封禁<br>别名 `/pardon`、`/eunban`、`/epardon` | `/unban 玩家名` | — |
| `/unbanip` | 解除对某个 IP 地址的封禁<br>别名 `/eunbanip`、`/pardonip`、`/epardonip` | `/unbanip IP地址` | — |
| `/unlimited` | 让指定物品可以无限放置<br>别名 `/eunlimited`、`/ul`、`/unl`、`/eul`、`/eunl` | `/unlimited list或item或clear [玩家名]` | — |
| `/vanish` | 隐身，从其他玩家视野里消失<br>别名 `/v`、`/ev`、`/evanish` | `/vanish [玩家名] [on或off]` | — |
| `/warp` | 列出所有地标，或传送到某个地标<br>别名 `/ewarp`、`/warps`、`/ewarps` | `/warp [页码或地标名] [玩家名]` | — |
| `/warpinfo` | 查看某个地标所在的坐标和世界<br>别名 `/ewarpinfo` | `/warpinfo 地标名` | — |
| `/weather` | 把世界天气切成晴天或雷雨<br>别名 `/rain`、`/erain`、`/sky`、`/esky`、`/storm`、`/estorm`、`/sun`、`/esun`、`/eweather` | `/weather storm或sun [持续时长]` | — |
| `/whois` | 查看某个玩家的基础资料<br>别名 `/ewhois` | `/whois 昵称或玩家名` | — |
| `/workbench` | 原地打开工作台<br>别名 `/craft`、`/ecraft`、`/wb`、`/ewb`、`/wbench`、`/ewbench`、`/eworkbench` | `/workbench` | — |
| `/world` | 切换或传送到另一个世界<br>别名 `/eworld` | `/world [世界名]` | — |
| `/worth` | 估算手上或背包物品的卖价<br>别名 `/eprice`、`/price`、`/eworth` | `/worth 物品名或hand或inventory [数量]` | — |

## 指令详解

### `/afk` — 把自己或指定玩家标记为暂离，可附自定义留言

- **语法**：`/afk [玩家名或留言]`

- **示例**：

```
/afk 去吃饭了
```

- **别名**：`/eafk`、`/away`、`/eaway`

### `/antioch` — OP 恶搞指令，在原地炸出一发大范围 TNT

- **语法**：`/antioch [留言]`

- **示例**：

```
/antioch
```

- **别名**：`/eantioch`、`/grenade`、`/egrenade`、`/tnt`、`/etnt`

### `/anvil` — 原地打开铁砧界面，修装备、改名字不用回家

- **语法**：`/anvil`

- **示例**：

```
/anvil
```

- **别名**：`/eanvil`

### `/back` — 回到上一次传送或死亡之前的位置

- **语法**：`/back [玩家名]`

- **示例**：

```
/back
```

- **别名**：`/eback`、`/return`、`/ereturn`

### `/backup` — 按配置立刻触发一次服务器备份

- **语法**：`/backup`

- **示例**：

```
/backup
```

- **别名**：`/ebackup`

### `/balance` — 查看自己或他人的金币余额

- **语法**：`/balance [玩家名]`

- **示例**：

```
/balance Steve
```

- **别名**：`/bal`、`/ebal`、`/ebalance`、`/money`、`/emoney`

### `/balancetop` — 查看服务器财富排行榜

- **语法**：`/balancetop [页码]`

- **示例**：

```
/balancetop 1
```

- **别名**：`/ebalancetop`、`/baltop`、`/ebaltop`

### `/ban` — 封禁玩家，可以附上原因

- **语法**：`/ban 玩家名 [原因]`

- **示例**：

```
/ban Steve 使用作弊客户端
```

- **别名**：`/eban`

### `/banip` — 封禁某个 IP 地址

- **语法**：`/banip IP地址 [原因]`

- **示例**：

```
/banip 203.0.113.7 恶意刷屏
```

- **别名**：`/ebanip`

### `/beezooka` — 娱乐指令，向准心方向射出一只爆炸蜜蜂

- **语法**：`/beezooka`

- **示例**：

```
/beezooka
```

- **别名**：`/ebeezooka`、`/beecannon`、`/ebeecannon`

### `/bigtree` — 在准心处生成一棵大树，可指定树种

- **语法**：`/bigtree 树种`

- **示例**：

```
/bigtree redwood
```

- **别名**：`/ebigtree`、`/largetree`、`/elargetree`

### `/book` — 重新打开手里的成书继续编辑

- **语法**：`/book [title 或 author 参数：新名字]`

- **示例**：

```
/book
```

- **别名**：`/ebook`

### `/bottom` — 传送到当前位置最低的一层可站立方块

- **语法**：`/bottom`

- **示例**：

```
/bottom
```

- **别名**：`/ebottom`

### `/break` — 直接破坏准心对着的那个方块

- **语法**：`/break`

- **示例**：

```
/break
```

- **别名**：`/ebreak`

### `/broadcast` — 向全服玩家发一条公告

- **语法**：`/broadcast 消息内容`

- **示例**：

```
/broadcast 服务器十分钟后重启，请先下线保存
```

- **别名**：`/bc`、`/ebc`、`/bcast`、`/ebcast`、`/ebroadcast`、`/shout`、`/eshout`

### `/broadcastworld` — 只向指定世界发公告

- **语法**：`/broadcastworld 世界名 消息内容`

- **示例**：

```
/broadcastworld world 主城今晚八点活动
```

- **别名**：`/bcw`、`/ebcw`、`/bcastw`、`/ebcastw`、`/ebroadcastworld`、`/shoutworld`、`/eshoutworld`

### `/burn` — 点燃指定玩家若干秒

- **语法**：`/burn 玩家名 秒数`

- **示例**：

```
/burn Steve 5
```

- **别名**：`/eburn`

### `/cartographytable` — 原地打开制图台

- **语法**：`/cartographytable`

- **示例**：

```
/cartographytable
```

- **别名**：`/ecartographytable`、`/carttable`、`/ecarttable`

### `/clearinventory` — 清空自己或他人背包，可按物品筛选

- **语法**：`/clearinventory [玩家名或星号] [物品或星号] [数量]`

- **示例**：

```
/clearinventory Steve
```

- **别名**：`/ci`、`/eci`、`/clean`、`/eclean`、`/clear`、`/eclear`、`/clearinvent`、`/eclearinvent`、`/eclearinventory`

### `/clearinventoryconfirmtoggle` — 开关清背包前的二次确认提示

- **语法**：`/clearinventoryconfirmtoggle`

- **示例**：

```
/clearinventoryconfirmtoggle
```

- **别名**：`/eclearinventoryconfirmtoggle`、`/clearinventoryconfirmoff`、`/eclearinventoryconfirmoff`、`/clearconfirmoff`、`/eclearconfirmoff`、`/clearconfirmon`、`/eclearconfirmon`、`/clearconfirm`、`/eclearconfirm`

### `/compass` — 报告自己当前的朝向和方位

- **语法**：`/compass`

- **示例**：

```
/compass
```

- **别名**：`/ecompass`、`/direction`、`/edirection`

### `/condense` — 把背包里的散装物品压成块，如铁锭转铁块

- **语法**：`/condense [物品名]`

- **示例**：

```
/condense iron_ingot
```

- **别名**：`/econdense`、`/compact`、`/ecompact`、`/blocks`、`/eblocks`、`/toblocks`、`/etoblocks`

### `/createkit` — 把自己当前背包内容存成一个礼包

- **语法**：`/createkit 礼包名 冷却秒数`

- **示例**：

```
/createkit newbie 86400
```

- **别名**：`/kitcreate`、`/createk`、`/kc`、`/ck`

### `/customtext` — 配合 bukkit.yml 的自定义指令，输出一段纯文本

- **语法**：`/自定义文本指令名`

- **示例**：

```
/自定义文本指令名
```


### `/delhome` — 删除自己的某个家

- **语法**：`/delhome [玩家名:]家名`

- **示例**：

```
/delhome home2
```

- **别名**：`/edelhome`、`/remhome`、`/eremhome`、`/rmhome`、`/ermhome`

### `/deljail` — 删除指定监狱点

- **语法**：`/deljail 监狱名`

- **示例**：

```
/deljail jail1
```

- **别名**：`/edeljail`、`/remjail`、`/eremjail`、`/rmjail`、`/ermjail`

### `/delkit` — 删除指定礼包

- **语法**：`/delkit 礼包名`

- **示例**：

```
/delkit newbie
```

- **别名**：`/edelkit`、`/remkit`、`/eremkit`、`/rmkit`、`/ermkit`、`/deletekit`、`/edeletekit`

### `/delwarp` — 删除指定地标

- **语法**：`/delwarp 地标名`

- **示例**：

```
/delwarp shop
```

- **别名**：`/edelwarp`、`/remwarp`、`/eremwarp`、`/rmwarp`、`/ermwarp`

### `/depth` — 报告当前高度相对海平面的深度

- **语法**：`/depth`

- **示例**：

```
/depth
```

- **别名**：`/edepth`、`/height`、`/eheight`

### `/disposal` — 打开随身垃圾桶，随手丢东西

- **语法**：`/disposal`

- **示例**：

```
/disposal
```

- **别名**：`/edisposal`、`/trash`、`/etrash`

### `/eco` — 管理经济：给钱、扣钱、设置、清零

- **语法**：`/eco 增减方式 玩家名 金额`

- **示例**：

```
/eco give Steve 1000
```

- **别名**：`/eeco`、`/economy`、`/eeconomy`

### `/editsign` — 直接改写地上告示牌的文字

- **语法**：`/editsign set或clear或copy或paste [行号] [文字]`

- **示例**：

```
/editsign set 1 欢迎来到星冕服务器
```

- **别名**：`/sign`、`/esign`、`/eeditsign`

### `/enchant` — 给手上的物品附魔并指定等级

- **语法**：`/enchant 附魔名 [等级]`

- **示例**：

```
/enchant sharpness 5
```

- **别名**：`/eenchant`、`/enchantment`、`/eenchantment`

### `/enderchest` — 打开自己或他人的末影箱

- **语法**：`/enderchest [玩家名]`

- **示例**：

```
/enderchest Steve
```

- **别名**：`/echest`、`/eechest`、`/eenderchest`、`/endersee`、`/eendersee`、`/ec`、`/eec`

### `/essentials` — 查看 Essentials 的版本与加载状态

- **语法**：`/essentials`

- **示例**：

```
/essentials
```

- **别名**：`/eessentials`、`/ess`、`/eess`、`/essversion`

### `/exp` — 给经验、设经验、清零或查看经验

- **语法**：`/exp 操作 玩家名 [数值]`

- **示例**：

```
/exp give Steve 30
```

- **别名**：`/eexp`、`/xp`

### `/ext` — 熄灭自己或他人身上的火

- **语法**：`/ext [玩家名]`

- **示例**：

```
/ext Steve
```

- **别名**：`/eext`、`/extinguish`、`/eextinguish`

### `/feed` — 回满自己或他人的饥饿值

- **语法**：`/feed [玩家名]`

- **示例**：

```
/feed Steve
```

- **别名**：`/eat`、`/eeat`、`/efeed`

### `/fireball` — 朝准心发射火球等各种投掷物

- **语法**：`/fireball [投掷物类型] [速度]`

- **示例**：

```
/fireball small 2
```

- **别名**：`/efireball`、`/fireentity`、`/efireentity`、`/fireskull`、`/efireskull`

### `/firework` — 编辑手上烟花的参数并燃放

- **语法**：`/firework 参数或power或clear或fire [数值]`

- **示例**：

```
/firework fire 1
```

- **别名**：`/efirework`

### `/fly` — 开关自己或他人的飞行

- **语法**：`/fly [玩家名] [on或off]`

- **示例**：

```
/fly on
```

- **别名**：`/efly`

### `/gamemode` — 切换自己或他人的游戏模式

- **语法**：`/gamemode 模式 [玩家名]`

- **示例**：

```
/gamemode creative Steve
```

- **别名**：`/adventure`、`/eadventure`、`/adventuremode`、`/eadventuremode`、`/creative`、`/ecreative`、`/eecreative`、`/creativemode`、`/ecreativemode`、`/egamemode`、`/gm`、`/egm`、`/gma`、`/egma`、`/gmc`、`/egmc`、`/gms`、`/egms`、`/gmt`、`/egmt`、`/survival`、`/esurvival`、`/survivalmode`、`/esurvivalmode`、`/gmsp`、`/sp`、`/egmsp`、`/spec`、`/spectator`

### `/gc` — 查看内存、在线数、TPS 等运行状态

- **语法**：`/gc`

- **示例**：

```
/gc
```

- **别名**：`/lag`、`/elag`、`/egc`、`/mem`、`/emem`、`/memory`、`/ememory`、`/uptime`、`/euptime`、`/tps`、`/etps`、`/entities`、`/eentities`

### `/getpos` — 查看自己或他人的坐标

- **语法**：`/getpos [玩家名]`

- **示例**：

```
/getpos Steve
```

- **别名**：`/coords`、`/egetpos`、`/position`、`/eposition`、`/whereami`、`/ewhereami`、`/getlocation`、`/egetlocation`、`/getloc`、`/egetloc`

### `/give` — 给玩家发放物品并指定数量

- **语法**：`/give 玩家名 物品名 [数量]`

- **示例**：

```
/give Steve diamond 8
```

- **别名**：`/egive`

### `/god` — 开关无敌模式

- **语法**：`/god [玩家名] [on或off]`

- **示例**：

```
/god Steve on
```

- **别名**：`/egod`、`/godmode`、`/egodmode`、`/tgm`、`/etgm`

### `/grindstone` — 原地打开砂轮，附魔随意装卸

- **语法**：`/grindstone`

- **示例**：

```
/grindstone
```

- **别名**：`/egrindstone`

### `/hat` — 把手上的方块或物品戴到头上

- **语法**：`/hat [remove]`

- **示例**：

```
/hat
```

- **别名**：`/ehat`、`/head`、`/ehead`

### `/heal` — 回满自己或他人的血量

- **语法**：`/heal [玩家名]`

- **示例**：

```
/heal Steve
```

- **别名**：`/eheal`

### `/help` — 列出可用指令，支持关键词搜索

- **语法**：`/help [关键词] [页码]`

- **示例**：

```
/help warp
```

- **别名**：`/ehelp`

### `/helpop` — 向在线管理员发一条求助消息

- **语法**：`/helpop 消息内容`

- **示例**：

```
/helpop 我在主城卡住了
```

- **别名**：`/ac`、`/eac`、`/amsg`、`/eamsg`、`/ehelpop`

### `/home` — 回家，可以指定家名

- **语法**：`/home [玩家名:]家名`

- **示例**：

```
/home
```

- **别名**：`/ehome`、`/homes`、`/ehomes`

### `/ice` — 把玩家冻住，限制其移动

- **语法**：`/ice [玩家名]`

- **示例**：

```
/ice Steve
```

- **别名**：`/eice`、`/efreeze`

### `/ignore` — 屏蔽某个玩家的发言

- **语法**：`/ignore 玩家名`

- **示例**：

```
/ignore Steve
```

- **别名**：`/eignore`、`/unignore`、`/eunignore`、`/delignore`、`/edelignore`、`/remignore`、`/eremignore`、`/rmignore`、`/ermignore`

### `/info` — 查看服主预先写好的服务器介绍

- **语法**：`/info [章节] [页码]`

- **示例**：

```
/info
```

- **别名**：`/about`、`/eabout`、`/ifo`、`/eifo`、`/einfo`、`/inform`、`/einform`、`/news`、`/enews`

### `/invsee` — 查看他人背包的内容

- **语法**：`/invsee 玩家名`

- **示例**：

```
/invsee Steve
```

- **别名**：`/einvsee`

### `/item` — 直接给自己刷一个物品

- **语法**：`/item 物品名 [数量]`

- **示例**：

```
/item diamond 64
```

- **别名**：`/i`、`/eitem`、`/ei`

### `/itemdb` — 查物品的 ID、耐久等信息

- **语法**：`/itemdb 物品`

- **示例**：

```
/itemdb diamond_sword
```

- **别名**：`/dura`、`/edura`、`/durability`、`/edurability`、`/eitemdb`、`/itemno`、`/eitemno`

### `/itemlore` — 给手上物品加、改、清说明文字

- **语法**：`/itemlore add或set或clear [文字或行号] [文字]`

- **示例**：

```
/itemlore add 星冕专属装备
```

- **别名**：`/lore`、`/elore`、`/ilore`、`/eilore`、`/eitemlore`

### `/itemname` — 给手上的物品改名

- **语法**：`/itemname [新名字]`

- **示例**：

```
/itemname 星冕之剑
```

- **别名**：`/iname`、`/einame`、`/eitemname`、`/itemrename`、`/irename`、`/eitemrename`、`/eirename`

### `/jailedplayers` — 列出当前所有在押玩家

- **语法**：`/jailedplayers`

- **示例**：

```
/jailedplayers
```

- **别名**：`/ejailedplayers`、`/ejailed`、`/ejp`

### `/jails` — 列出所有已设置的监狱

- **语法**：`/jails`

- **示例**：

```
/jails
```

- **别名**：`/ejails`

### `/jump` — 瞬移到准心指向的那个方块上

- **语法**：`/jump`

- **示例**：

```
/jump
```

- **别名**：`/j`、`/ej`、`/ejump`、`/jumpto`、`/ejumpto`

### `/kick` — 把玩家踢下线，可附原因

- **语法**：`/kick 玩家名 [原因]`

- **示例**：

```
/kick Steve 请勿刷屏
```

- **别名**：`/ekick`

### `/kickall` — 把除自己以外的玩家全部踢下线

- **语法**：`/kickall [原因]`

- **示例**：

```
/kickall 服务器即将重启
```

- **别名**：`/ekickall`

### `/kill` — 直接击杀指定玩家

- **语法**：`/kill 玩家名`

- **示例**：

```
/kill Steve
```

- **别名**：`/ekill`

### `/kit` — 领取礼包，或查看自己能领哪些礼包

- **语法**：`/kit [礼包名] [玩家名]`

- **示例**：

```
/kit newbie
```

- **别名**：`/ekit`、`/kits`、`/ekits`

### `/kitreset` — 重置某个礼包的领取冷却

- **语法**：`/kitreset 礼包名 [玩家名]`

- **示例**：

```
/kitreset newbie Steve
```

- **别名**：`/ekitreset`、`/kitr`、`/ekitr`、`/resetkit`、`/eresetkit`

### `/kittycannon` — 娱乐指令，向准心方向扔一只爆炸小猫

- **语法**：`/kittycannon`

- **示例**：

```
/kittycannon
```

- **别名**：`/ekittycannon`

### `/lightning` — 在准心或指定玩家身上劈下闪电

- **语法**：`/lightning [玩家名] [强度]`

- **示例**：

```
/lightning Steve
```

- **别名**：`/elightning`、`/shock`、`/eshock`、`/smite`、`/esmite`、`/strike`、`/estrike`、`/thor`、`/ethor`

### `/list` — 查看当前在线玩家名单

- **语法**：`/list [分组]`

- **示例**：

```
/list
```

- **别名**：`/elist`、`/online`、`/eonline`、`/playerlist`、`/eplayerlist`、`/plist`、`/eplist`、`/who`、`/ewho`

### `/loom` — 原地打开织布机

- **语法**：`/loom`

- **示例**：

```
/loom
```

- **别名**：`/eloom`

### `/mail` — 收发站内离线邮件

- **语法**：`/mail read或clear或send [收件人] [内容]`

- **示例**：

```
/mail send Steve 晚上八点集合
```

- **别名**：`/email`、`/eemail`、`/memo`、`/ememo`

### `/me` — 以第三人称描述自己做的一个动作

- **语法**：`/me 动作描述`

- **示例**：

```
/me 整理了一下背包
```

- **别名**：`/action`、`/eaction`、`/describe`、`/edescribe`、`/eme`

### `/more` — 把手上的物品补满一整组

- **语法**：`/more [数量]`

- **示例**：

```
/more
```

- **别名**：`/emore`

### `/motd` — 查看服务器每日公告

- **语法**：`/motd [章节] [页码]`

- **示例**：

```
/motd
```

- **别名**：`/emotd`

### `/msg` — 给某个玩家发一条私信

- **语法**：`/msg 玩家名 消息内容`

- **示例**：

```
/msg Steve 到主城找我
```

- **别名**：`/w`、`/m`、`/t`、`/pm`、`/emsg`、`/epm`、`/tell`、`/etell`、`/whisper`、`/ewhisper`

### `/msgtoggle` — 开关是否接收别人的私信

- **语法**：`/msgtoggle [玩家名] [on或off]`

- **示例**：

```
/msgtoggle on
```

- **别名**：`/emsgtoggle`

### `/mute` — 禁言或解禁玩家，可限时

- **语法**：`/mute 玩家名 [时长] [原因]`

- **示例**：

```
/mute Steve 1h 刷屏
```

- **别名**：`/emute`、`/silence`、`/esilence`、`/unmute`、`/eunmute`

### `/near` — 列出自己或某人身边一定范围内的玩家

- **语法**：`/near [玩家名] [半径]`

- **示例**：

```
/near Steve 100
```

- **别名**：`/enear`、`/nearby`、`/enearby`

### `/nick` — 改自己或他人的昵称

- **语法**：`/nick [玩家名] 昵称或off`

- **示例**：

```
/nick Steve 小史
```

- **别名**：`/enick`、`/nickname`、`/enickname`

### `/nuke` — 娱乐指令，让目标玩家原地爆炸

- **语法**：`/nuke [玩家名]`

- **示例**：

```
/nuke Steve
```

- **别名**：`/enuke`

### `/pay` — 把余额里的钱转给其他玩家

- **语法**：`/pay 玩家名 金额`

- **示例**：

```
/pay Steve 100
```

- **别名**：`/epay`

### `/payconfirmtoggle` — 开关转账前的大额确认提示

- **语法**：`/payconfirmtoggle`

- **示例**：

```
/payconfirmtoggle
```

- **别名**：`/epayconfirmtoggle`、`/payconfirmoff`、`/epayconfirmoff`、`/payconfirmon`、`/epayconfirmon`、`/payconfirm`、`/epayconfirm`

### `/paytoggle` — 开关是否接受别人转账

- **语法**：`/paytoggle [玩家名]`

- **示例**：

```
/paytoggle
```

- **别名**：`/epaytoggle`、`/payoff`、`/epayoff`、`/payon`、`/epayon`

### `/ping` — 测一下当前自己到服务器的延迟

- **语法**：`/ping`

- **示例**：

```
/ping
```

- **别名**：`/echo`、`/eecho`、`/eping`、`/pong`、`/epong`

### `/playtime` — 查看自己或他人的累计游戏时长

- **语法**：`/playtime [玩家名]`

- **示例**：

```
/playtime Steve
```

- **别名**：`/eplaytime`

### `/potion` — 给手上的药水写入自定义药水效果

- **语法**：`/potion clear或apply或效果参数`

- **示例**：

```
/potion clear
```

- **别名**：`/epotion`、`/elixer`、`/eelixer`

### `/powertool` — 把手上的物品绑定一条指令，左键即执行

- **语法**：`/powertool [前缀] 指令`

- **示例**：

```
/powertool /spawn
```

- **别名**：`/epowertool`、`/pt`、`/ept`

### `/powertoollist` — 列出当前已绑定的动力工具

- **语法**：`/powertoollist`

- **示例**：

```
/powertoollist
```

- **别名**：`/epowertoollist`、`/ptlist`、`/eptlist`

### `/powertooltoggle` — 一键启用或禁用所有动力工具

- **语法**：`/powertooltoggle`

- **示例**：

```
/powertooltoggle
```

- **别名**：`/epowertooltoggle`、`/ptt`、`/eptt`、`/pttoggle`、`/epttoggle`

### `/ptime` — 只改某个玩家的客户端时间，不影响全服

- **语法**：`/ptime 时间 [玩家名或星号]`

- **示例**：

```
/ptime night
```

- **别名**：`/playertime`、`/eplayertime`、`/eptime`

### `/pweather` — 只改某个玩家的客户端天气

- **语法**：`/pweather 天气 [玩家名或星号]`

- **示例**：

```
/pweather sun
```

- **别名**：`/playerweather`、`/eplayerweather`、`/epweather`

### `/r` — 快速回复上一条收到的私信

- **语法**：`/r 消息内容`

- **示例**：

```
/r 马上到
```

- **别名**：`/er`、`/reply`、`/ereply`

### `/realname` — 用昵称反查玩家的真实 ID

- **语法**：`/realname 昵称`

- **示例**：

```
/realname 小史
```

- **别名**：`/erealname`

### `/recipe` — 查看某个物品的合成配方

- **语法**：`/recipe 物品名 [数量]`

- **示例**：

```
/recipe diamond_pickaxe
```

- **别名**：`/formula`、`/eformula`、`/method`、`/emethod`、`/erecipe`、`/recipes`、`/erecipes`

### `/remove` — 批量清理世界里的实体，如掉落物、动物

- **语法**：`/remove 类型 [半径或世界]`

- **示例**：

```
/remove drops 100
```

- **别名**：`/eremove`、`/butcher`、`/ebutcher`、`/killall`、`/ekillall`、`/mobkill`、`/emobkill`

### `/renamehome` — 给已有的家改个名字

- **语法**：`/renamehome 旧家名 新家名`

- **示例**：

```
/renamehome home2 农场
```

- **别名**：`/erenamehome`

### `/repair` — 修满手上或全部装备的耐久

- **语法**：`/repair [hand或all]`

- **示例**：

```
/repair hand
```

- **别名**：`/fix`、`/efix`、`/erepair`

### `/rest` — 重置自己或他人的睡眠计时，防幻翼刷出

- **语法**：`/rest [玩家名]`

- **示例**：

```
/rest Steve
```

- **别名**：`/erest`

### `/rtoggle` — 设置 /r 回复的是最后发信人还是最后收信人

- **语法**：`/rtoggle [玩家名] [on或off]`

- **示例**：

```
/rtoggle
```

- **别名**：`/ertoggle`、`/replytoggle`、`/ereplytoggle`

### `/rules` — 查看服务器规则

- **语法**：`/rules [章节] [页码]`

- **示例**：

```
/rules
```

- **别名**：`/erules`

### `/seen` — 查看玩家最后一次下线的时间

- **语法**：`/seen 玩家名`

- **示例**：

```
/seen Steve
```

- **别名**：`/eseen`、`/ealts`、`/alts`

### `/sell` — 把手上的物品卖给系统换钱

- **语法**：`/sell 物品名或hand或inventory [数量]`

- **示例**：

```
/sell hand
```

- **别名**：`/esell`

### `/sethome` — 把当前位置设为家，可自定义家名

- **语法**：`/sethome [玩家名:]家名`

- **示例**：

```
/sethome home1
```

- **别名**：`/esethome`、`/createhome`、`/ecreatehome`

### `/setjail` — 以当前位置创建一间监狱

- **语法**：`/setjail 监狱名`

- **示例**：

```
/setjail jail1
```

- **别名**：`/esetjail`、`/createjail`、`/ecreatejail`

### `/settpr` — 设置随机传送的中心点和远近范围

- **语法**：`/settpr center或minrange或maxrange [数值]`

- **示例**：

```
/settpr minrange 200
```

- **别名**：`/esettpr`、`/settprandom`、`/esettprandom`

### `/setwarp` — 以当前位置创建一个地标

- **语法**：`/setwarp 地标名`

- **示例**：

```
/setwarp shop
```

- **别名**：`/createwarp`、`/ecreatewarp`、`/esetwarp`

### `/setworth` — 设置某个物品的回收价格

- **语法**：`/setworth 物品名 价格`

- **示例**：

```
/setworth diamond 100
```

- **别名**：`/esetworth`

### `/showkit` — 预览某个礼包里都有什么

- **语法**：`/showkit 礼包名`

- **示例**：

```
/showkit newbie
```

- **别名**：`/kitpreview`、`/preview`、`/kitshow`

### `/skull` — 设置手上头颅属于哪个玩家

- **语法**：`/skull [头颅主人] [玩家名]`

- **示例**：

```
/skull Steve
```

- **别名**：`/eskull`、`/playerskull`、`/eplayerskull`、`/head`、`/ehead`

### `/smithingtable` — 原地打开锻造台

- **语法**：`/smithingtable`

- **示例**：

```
/smithingtable
```

- **别名**：`/esmithingtable`、`/smithtable`、`/esmithtable`

### `/socialspy` — 开关偷看他人私信和邮件的模式

- **语法**：`/socialspy [玩家名] [on或off]`

- **示例**：

```
/socialspy on
```

- **别名**：`/esocialspy`

### `/spawner` — 改刷怪笼生成什么生物，可设间隔

- **语法**：`/spawner 生物名 [间隔秒数]`

- **示例**：

```
/spawner zombie 20
```

- **别名**：`/changems`、`/echangems`、`/espawner`、`/mobspawner`、`/emobspawner`

### `/spawnmob` — 生成指定生物，可带数量与骑乘关系

- **语法**：`/spawnmob 生物名 [数量] [玩家名]`

- **示例**：

```
/spawnmob zombie 5
```

- **别名**：`/mob`、`/emob`、`/spawnentity`、`/espawnentity`、`/espawnmob`

### `/speed` — 改自己或他人的行走、飞行速度

- **语法**：`/speed [类型] 速度值 [玩家名]`

- **示例**：

```
/speed walk 2
```

- **别名**：`/flyspeed`、`/eflyspeed`、`/fspeed`、`/efspeed`、`/espeed`、`/walkspeed`、`/ewalkspeed`、`/wspeed`、`/ewspeed`

### `/stonecutter` — 原地打开切石机

- **语法**：`/stonecutter`

- **示例**：

```
/stonecutter
```

- **别名**：`/estonecutter`

### `/sudo` — 让某个玩家替你执行一条指令

- **语法**：`/sudo 玩家名 指令`

- **示例**：

```
/sudo Steve spawn
```

- **别名**：`/esudo`

### `/suicide` — 让自己立刻死亡

- **语法**：`/suicide`

- **示例**：

```
/suicide
```

- **别名**：`/esuicide`

### `/tempban` — 限时封禁玩家

- **语法**：`/tempban 玩家名 时长 [原因]`

- **示例**：

```
/tempban Steve 3d 恶意破坏
```

- **别名**：`/etempban`

### `/tempbanip` — 限时封禁某个 IP 地址

- **语法**：`/tempbanip IP地址 时长 [原因]`

- **示例**：

```
/tempbanip 203.0.113.7 1d 刷屏
```

- **别名**：`/etempbanip`

### `/thunder` — 开关雷雨天，可指定持续时长

- **语法**：`/thunder true或false [时长]`

- **示例**：

```
/thunder true 300
```

- **别名**：`/ethunder`

### `/time` — 查看或修改世界时间

- **语法**：`/time [set或add] 时间 [世界名或all]`

- **示例**：

```
/time set day
```

- **别名**：`/day`、`/eday`、`/night`、`/enight`、`/etime`

### `/togglejail` — 把玩家关进监狱，或把在押玩家放出来

- **语法**：`/togglejail 玩家名 监狱名 [时长]`

- **示例**：

```
/togglejail Steve jail1 1d
```

- **别名**：`/jail`、`/ejail`、`/tjail`、`/etjail`、`/etogglejail`、`/unjail`、`/eunjail`

### `/top` — 传送到当前位置最高的方块上方

- **语法**：`/top`

- **示例**：

```
/top
```

- **别名**：`/etop`

### `/tp` — 把自己或某人传送到目标玩家

- **语法**：`/tp 目标玩家 [被传送者]`

- **示例**：

```
/tp Steve
```

- **别名**：`/tele`、`/etele`、`/teleport`、`/eteleport`、`/etp`、`/tp2p`、`/etp2p`

### `/tpa` — 申请传送到某个玩家身边

- **语法**：`/tpa 玩家名`

- **示例**：

```
/tpa Steve
```

- **别名**：`/call`、`/ecall`、`/etpa`、`/tpask`、`/etpask`

### `/tpaall` — 让所有在线玩家申请传送到某人身边

- **语法**：`/tpaall 玩家名`

- **示例**：

```
/tpaall Steve
```

- **别名**：`/etpaall`

### `/tpacancel` — 撤回自己发出的所有传送申请

- **语法**：`/tpacancel [玩家名]`

- **示例**：

```
/tpacancel
```

- **别名**：`/etpacancel`

### `/tpaccept` — 同意别人的传送申请

- **语法**：`/tpaccept [玩家名或星号]`

- **示例**：

```
/tpaccept Steve
```

- **别名**：`/etpaccept`、`/tpyes`、`/etpyes`

### `/tpahere` — 申请把某个玩家拉到自己身边

- **语法**：`/tpahere 玩家名`

- **示例**：

```
/tpahere Steve
```

- **别名**：`/etpahere`

### `/tpall` — 把所有在线玩家传送到某个玩家那里

- **语法**：`/tpall [玩家名]`

- **示例**：

```
/tpall Steve
```

- **别名**：`/etpall`

### `/tpauto` — 开关自动同意收到的传送申请

- **语法**：`/tpauto [玩家名]`

- **示例**：

```
/tpauto
```

- **别名**：`/etpauto`

### `/tpdeny` — 拒绝别人的传送申请

- **语法**：`/tpdeny [玩家名或星号]`

- **示例**：

```
/tpdeny Steve
```

- **别名**：`/etpdeny`、`/tpno`、`/etpno`

### `/tphere` — 直接把某个玩家拉到自己身边

- **语法**：`/tphere 玩家名`

- **示例**：

```
/tphere Steve
```

- **别名**：`/s`、`/etphere`

### `/tpo` — 无视对方关闭传送的限制，强行传送过去

- **语法**：`/tpo 目标玩家 [被传送者]`

- **示例**：

```
/tpo Steve
```

- **别名**：`/etpo`

### `/tpoffline` — 传送到离线玩家最后下线的位置

- **语法**：`/tpoffline 玩家名`

- **示例**：

```
/tpoffline Steve
```

- **别名**：`/otp`、`/offlinetp`、`/tpoff`、`/tpoffline`、`/etpoffline`

### `/tpohere` — 无视限制，强行把玩家拉到自己身边

- **语法**：`/tpohere 玩家名`

- **示例**：

```
/tpohere Steve
```

- **别名**：`/etpohere`

### `/tppos` — 按指定坐标传送自己

- **语法**：`/tppos X坐标 Y坐标 Z坐标 [朝向] [俯仰] [世界名]`

- **示例**：

```
/tppos 100 70 -200
```

- **别名**：`/etppos`

### `/tpr` — 随机传送到世界某处

- **语法**：`/tpr`

- **示例**：

```
/tpr
```

- **别名**：`/etpr`、`/tprandom`、`/etprandom`

### `/tptoggle` — 开关自己是否允许被别人传送

- **语法**：`/tptoggle [玩家名] [on或off]`

- **示例**：

```
/tptoggle off
```

- **别名**：`/etptoggle`

### `/tree` — 在准心处生成一棵树，可指定树种

- **语法**：`/tree 树种`

- **示例**：

```
/tree oak
```

- **别名**：`/etree`

### `/unban` — 解除对某个玩家的封禁

- **语法**：`/unban 玩家名`

- **示例**：

```
/unban Steve
```

- **别名**：`/pardon`、`/eunban`、`/epardon`

### `/unbanip` — 解除对某个 IP 地址的封禁

- **语法**：`/unbanip IP地址`

- **示例**：

```
/unbanip 203.0.113.7
```

- **别名**：`/eunbanip`、`/pardonip`、`/epardonip`

### `/unlimited` — 让指定物品可以无限放置

- **语法**：`/unlimited list或item或clear [玩家名]`

- **示例**：

```
/unlimited item stone
```

- **别名**：`/eunlimited`、`/ul`、`/unl`、`/eul`、`/eunl`

### `/vanish` — 隐身，从其他玩家视野里消失

- **语法**：`/vanish [玩家名] [on或off]`

- **示例**：

```
/vanish on
```

- **别名**：`/v`、`/ev`、`/evanish`

### `/warp` — 列出所有地标，或传送到某个地标

- **语法**：`/warp [页码或地标名] [玩家名]`

- **示例**：

```
/warp shop
```

- **别名**：`/ewarp`、`/warps`、`/ewarps`

### `/warpinfo` — 查看某个地标所在的坐标和世界

- **语法**：`/warpinfo 地标名`

- **示例**：

```
/warpinfo shop
```

- **别名**：`/ewarpinfo`

### `/weather` — 把世界天气切成晴天或雷雨

- **语法**：`/weather storm或sun [持续时长]`

- **示例**：

```
/weather sun
```

- **别名**：`/rain`、`/erain`、`/sky`、`/esky`、`/storm`、`/estorm`、`/sun`、`/esun`、`/eweather`

### `/whois` — 查看某个玩家的基础资料

- **语法**：`/whois 昵称或玩家名`

- **示例**：

```
/whois Steve
```

- **别名**：`/ewhois`

### `/workbench` — 原地打开工作台

- **语法**：`/workbench`

- **示例**：

```
/workbench
```

- **别名**：`/craft`、`/ecraft`、`/wb`、`/ewb`、`/wbench`、`/ewbench`、`/eworkbench`

### `/world` — 切换或传送到另一个世界

- **语法**：`/world [世界名]`

- **示例**：

```
/world world
```

- **别名**：`/eworld`

### `/worth` — 估算手上或背包物品的卖价

- **语法**：`/worth 物品名或hand或inventory [数量]`

- **示例**：

```
/worth hand
```

- **别名**：`/eprice`、`/price`、`/eworth`

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `eco give 玩家名 金额` | 给玩家加钱 | `/eco give Steve 1000` |
| `eco take 玩家名 金额` | 扣掉玩家一部分钱 | `/eco take Steve 500` |
| `eco set 玩家名 金额` | 把余额直接设成指定数 | `/eco set Steve 1000` |
| `eco reset 玩家名` | 把余额清零 | `/eco reset Steve` |
| `exp give 玩家名 数量` | 给玩家经验点 | `/exp give Steve 30` |
| `exp set 玩家名 数量` | 把玩家经验设成指定等级 | `/exp set Steve 30` |
| `exp show 玩家名` | 查看玩家当前经验 | `/exp show Steve` |
| `exp reset 玩家名` | 把玩家经验清零 | `/exp reset Steve` |
| `itemlore add 文字` | 给手上物品加一行说明 | `/itemlore add 星冕专属装备` |
| `itemlore set 行号 文字` | 改写指定行的说明 | `/itemlore set 1 攻击力加十` |
| `itemlore clear` | 清空物品的全部说明 | `/itemlore clear` |
| `editsign set 行号 文字` | 改写告示牌某一行的内容 | `/editsign set 1 欢迎来到星冕服务器` |
| `editsign clear 行号` | 清空告示牌某一行 | `/editsign clear 2` |
| `editsign copy` | 复制当前告示牌的文字 | `/editsign copy` |
| `editsign paste` | 把复制到的文字贴到另一块告示牌 | `/editsign paste` |
| `time set day` | 把时间调到白天 | `/time set day` |
| `time add 数值` | 在当前时间上追加 tick | `/time add 1000` |
| `unlimited list` | 看当前无限放置列表 | `/unlimited list` |
| `unlimited item 物品名` | 把某物品加入无限放置 | `/unlimited item stone` |
| `unlimited clear` | 清空无限放置列表 | `/unlimited clear` |
| `remove all` | 清掉附近所有可清理实体 | `/remove all 100` |
| `remove drops` | 只清掉落物，留着生物和建筑 | `/remove drops 200` |
| `mail read` | 读自己的站内邮件 | `/mail read` |
| `mail send 玩家名 内容` | 给某个玩家发离线邮件 | `/mail send Steve 晚上八点集合` |
| `mail clear` | 清空自己的邮件 | `/mail clear` |
| `ptime day` | 只把自己看到的天空改成白天 | `/ptime day` |
| `pweather sun` | 只把自己看到的天气改成晴天 | `/pweather sun` |
| `powertool 指令` | 把手上的物品绑定成执行该指令的按键工具 | `/powertool /spawn` |
| `potion clear` | 清掉手上药水的自定义效果 | `/potion clear` |

## 注意事项

::: warning
- 给钱、清背包、发物品这些操作没有撤销按钮，尤其是 clearinventory 和 kickall，执行前先核对对象。
- 封禁、禁言、雷雨的时长要写成 1d2h30m 这种格式，写成中文或纯数字容易当场报语法错误。
- 绝大多数指令靠 essentials.xxx 权限节点放行，玩家提示无权限先去 LuckPerms 查组权限，不要反复改配置。
- tpa、warp、home 这类指令名容易和其他传送插件撞车，装两个前先确认哪个插件接管，否则指令会互相覆盖。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `essentials.*` | 默认让 OP 玩家拥有全部权限 | op |
| `essentials.afk` | 允许访问/afk命令 | — |
| `essentials.afk.auto` | 拥有此权限的玩家在配置文件中定义的无操作时间段后将被设置为afk | — |
| `essentials.afk.kickexempt` | 拥有此权限的玩家不会因为是AFK而被踢出 | — |
| `essentials.afk.message` | 允许玩家设置自定义AFK消息 | — |
| `essentials.afk.others` | 允许玩家设置其他玩家的AFK状态 | — |
| `essentials.antioch` | 允许访问/antioch命令 | — |
| `essentials.anvil` | 允许访问/anvil命令 | — |
| `essentials.back` | 允许访问/back命令 | — |
| `essentials.back.into.<world>` | 允许玩家使用/back命令前往特定世界 | — |
| `essentials.back.ondeath` | 拥有此权限的玩家将在死亡期间存储返回位置 | — |
| `essentials.back.onteleport` | 拥有此权限的玩家将在任何传送过程中存储返回位置 | True |
| `essentials.back.others` | 允许其他玩家访问/back命令 | — |
| `essentials.backup` | 允许访问/backup命令 | — |
| `essentials.balance` | 允许访问/balance命令 | — |
| `essentials.balance.others` | 允许使用/balance命令查看其他玩家的余额 | — |
| `essentials.balancetop` | 允许访问/balancetop命令 | — |
| `essentials.balancetop.exclude` | 拥有此权限的玩家将被排除在平衡台之外 | — |
| `essentials.balancetop.force` | 允许访问强制刷新平衡顶列表 | — |
| `essentials.ban` | 允许访问/ban命令 | — |
| `essentials.ban.exempt` | 防止指定的群组或玩家被封禁 | — |
| `essentials.ban.notify` | 允许在玩家被禁用时通知持有人 | — |
| `essentials.ban.offline` | 允许离线玩家访问/ban命令，这可能反过来用于禁止离线的豁免玩家 | — |
| `essentials.banip` | 允许访问/banip命令 | — |
| `essentials.banip.notify` | 允许在玩家被禁用时通知持有人 | — |
| `essentials.beezooka` | 允许访问/beezooka命令 | — |
| `essentials.bigtree` | 允许访问/bigtree命令 | — |
| `essentials.book` | 允许访问/book命令 | — |
| `essentials.book.author` | 允许使用/book命令访问编辑图书作者 | — |
| `essentials.book.others` | 允许使用/book命令编辑其他玩家的书籍 | — |
| `essentials.book.title` | 允许使用/book命令编辑图书标题 | — |
| `essentials.bottom` | 允许访问/bottom命令 | — |
| `essentials.break` | 允许访问/break命令 | — |
| `essentials.break.bedrock` | 允许访问基岩的/break命令 | — |
| `essentials.broadcast` | 允许访问/broadcast命令 | — |
| `essentials.broadcastworld` | 允许访问/broadcastworld命令 | — |
| `essentials.burn` | 允许访问/burn命令 | — |
| `essentials.cartographytable` | 允许访问/cartographytable命令 | — |
| `essentials.chat.ignoreexempt` | 拥有此权限的人员将不会被忽略，即使他们在其他人员忽略列表中 | — |
| `essentials.chat.spy` | 允许承载者查看所有本地聊天消息，无论其是否靠近发件人 | — |
| `essentials.chat.spy.exempt` | 允许承载免除本地聊天间谍权限 | — |
| `essentials.clearinventory` | 允许访问/clearinventory命令 | — |
| `essentials.clearinventory.all` | 允许使用/clearinventory命令清除所有玩家的库存 | — |
| `essentials.clearinventory.others` | 允许使用/clearinventory命令清除其他玩家的库存 | — |
| `essentials.clearinventoryconfirmtoggle` | 允许访问/clearinventoryconfirmtoggle命令 | — |
| `essentials.commandcooldowns.bypass` | 允许绕过所有命令冷却时间 | — |
| `essentials.commandcooldowns.bypass.<commandname>` | 允许绕过特定命令的冷却时间 | — |
| `essentials.compass` | 允许访问/compass命令 | — |
| `essentials.condense` | 允许访问/condense命令 | — |
| `essentials.createkit` | 允许访问/createkit命令 | — |
| `essentials.customtext` | 允许访问/customtext命令和所有别名 | — |
| `essentials.delhome` | 允许访问/delhome命令 | — |
| `essentials.delhome.others` | 允许使用/delhome命令删除其他玩家主页 | — |
| `essentials.deljail` | 允许访问/deljail命令 | — |
| `essentials.delkit` | 允许访问/delkit命令 | — |
| `essentials.delwarp` | 允许访问/delwarp命令 | — |
| `essentials.depth` | 允许访问/depth命令 | — |
| `essentials.disposal` | 允许访问/disposal命令 | — |
| `essentials.eco` | 允许访问/eco命令 | — |
| `essentials.eco.loan` | 允许持有人拥有负余额 | — |
| `essentials.editsign` | 允许访问/editsign命令 | — |
| `essentials.editsign.color` | 允许持有人在标志上使用颜色代码 | — |
| `essentials.editsign.format` | 允许持有人在标志上使用格式代码 | — |
| `essentials.editsign.magic` | 允许持有人在标志上使用魔法代码 | — |
| `essentials.editsign.rgb` | 允许持有人在标志上使用RGB代码 | — |
| `essentials.editsign.unlimited` | 允许持有人超过标志上的15个字符限制 | — |
| `essentials.editsign.waxed.exempt` | 允许持有人编辑打蜡标志 | — |
| `essentials.enchant` | 允许访问/enchant命令 | — |
| `essentials.enchantments.<enchantment>` | 允许持有人使用/enchant命令使用特定的魔法 | — |
| `essentials.enchantments.allowunsafe` | 允许携带者使用不安全的附魔物品 | — |
| `essentials.enderchest` | 允许访问/enderchest命令 | — |
| `essentials.enderchest.modify` | 允许持有人修改其他玩家的义务 | — |
| `essentials.enderchest.others` | 允许其他玩家访问/enderchest命令 | — |
| `essentials.essentials` | 允许访问/essentials命令 | — |
| `essentials.exempt` | 豁免许多版主操作的父级权限 | — |
| `essentials.exp` | 允许使用 /exp 指令 | — |
| `essentials.exp.give` | 允许持有人为自己提供经验 | — |
| `essentials.exp.give.others` | 允许持有人为其他玩家提供经验 | — |
| `essentials.exp.others` | 允许持有人查看其他玩家的体验 | — |
| `essentials.exp.set` | 允许持有人为自己设置体验 | — |
| `essentials.exp.set.others` | 允许持有人为其他玩家设置经验 | — |
| `essentials.ext` | 允许访问/ext命令 | — |
| `essentials.ext.others` | 允许其他玩家访问/ext命令 | — |
| `essentials.feed` | 允许访问/feed命令 | — |
| `essentials.feed.others` | 允许其他玩家访问/feed命令 | — |
| `essentials.fireball` | 允许访问/fireball命令。每种类型的火球都需要额外的权限。 | — |
| `essentials.fireball.arrow` | 允许访问/fireball命令中的箭头 | — |
| `essentials.fireball.dragon` | 允许在/fireball命令中使用龙 | — |
| `essentials.fireball.egg` | 允许访问/fireball命令中的egg | — |
| `essentials.fireball.fireball` | 允许访问/fireball命令中的fireball | — |
| `essentials.fireball.large` | 允许访问/fireball命令中的大火球 | — |
| `essentials.fireball.lingeringpotion` | 允许在/fireball命令中使用挥之不去的药水 | — |
| `essentials.fireball.skull` | 允许在/fireball命令中使用头骨 | — |
| `essentials.fireball.small` | 允许访问/fireball命令中的小火球 | — |
| `essentials.fireball.snowball` | 允许访问/fireball命令中的雪球 | — |
| `essentials.fireball.splashpotion` | 允许访问/fireball命令中的飞溅药水 | — |
| `essentials.fireball.trident` | 允许访问/fireball命令中的三叉戟 | — |
| `essentials.firework` | 允许访问/firework命令 | — |
| `essentials.firework.fire` | 允许携带者使用烟花命令启动手中的烟花副本 | — |
| `essentials.firework.multiple` | 允许携带者使用烟花指令发射多支烟花 | — |
| `essentials.fly` | 允许访问/fly命令 | — |
| `essentials.fly.others` | 允许其他玩家访问/fly命令 | — |
| `essentials.fly.safelogin` | 如果此权限的持有者在空中登录，他们将被置于飞行模式 | — |
| `essentials.gamemode` | 允许访问/gamemode命令 | — |
| `essentials.gamemode.*` | 允许使用/gamemode命令访问所有游戏模式 | op |
| `essentials.gamemode.adventure` | 允许使用/gamemode命令访问冒险游戏模式 | — |
| `essentials.gamemode.all` | 允许使用/gamemode命令访问所有游戏模式 | — |
| `essentials.gamemode.creative` | 允许使用/gamemode命令访问创意游戏模式 | — |
| `essentials.gamemode.others` | 允许其他玩家访问/gamemode命令 | — |
| `essentials.gamemode.spectator` | 允许使用/gamemode命令访问旁观者游戏模式 | — |
| `essentials.gamemode.survival` | 允许使用/gamemode命令访问生存游戏模式 | — |
| `essentials.gc` | 允许访问/gc命令 | — |
| `essentials.getpos` | 允许访问/getpos命令 | — |
| `essentials.getpos.others` | 允许其他玩家访问/getpos命令 | — |
| `essentials.give` | 允许访问/give命令 | — |
| `essentials.give.item-<item-name>` | 允许在启用基于权限的项目生成时访问特定项目的/give命令 | — |
| `essentials.give.item-all` | 允许在启用基于权限的项目生成时访问所有项目的/give命令 | — |
| `essentials.god` | 允许访问/god命令 | — |
| `essentials.god.others` | 允许其他玩家访问/god命令 | — |
| `essentials.god.pvp` | 允许持有者在上帝模式下攻击玩家 | — |
| `essentials.grindstone` | 允许访问/grindstone命令 | — |
| `essentials.hat` | 允许访问/hat命令 | — |
| `essentials.hat.ignore-binding` | 允许持有者在为物品配备了绑定诅咒时使用/hat命令 | — |
| `essentials.hat.prevent-type.<item-name>` | 防止玩家对指定项目使用/hat命令 | — |
| `essentials.heal` | 允许访问/heal命令 | — |
| `essentials.heal.others` | 允许其他玩家访问/heal命令 | — |
| `essentials.help` | 允许访问/help命令 | — |
| `essentials.help.<plugin-name>` | 允许访问特定插件的/help命令 | — |
| `essentials.helpop` | 允许访问/helpop命令 | — |
| `essentials.helpop.receive` | 允许持有人接收帮助消息 | — |
| `essentials.home` | 允许访问/home命令 | — |
| `essentials.home.bed` | 允许访问床的/home命令 | — |
| `essentials.home.compass` | 将玩家的指南针指向他们的第一个主页。需要在配置中启用compass-towards-home-perm。 | — |
| `essentials.home.others` | 允许使用/home命令传送到其他玩家家园 | — |
| `essentials.ice` | 允许使用 /ice 指令 | — |
| `essentials.ice.others` | 允许对其他玩家使用 /ice 指令 | — |
| `essentials.ignore` | 允许访问/ignore命令 | — |
| `essentials.info` | 允许访问/info命令 | — |
| `essentials.invsee` | 允许访问/invsee命令 | — |
| `essentials.invsee.equip` | 允许使用/invsee命令查看盔甲槽中的项目 | — |
| `essentials.invsee.modify` | 允许使用/invsee命令访问修改其他玩家库存中的项目 | — |
| `essentials.invsee.preventmodify` | 防止其他玩家修改玩家库存。 | — |
| `essentials.item` | 允许访问/item命令 | — |
| `essentials.itemdb` | 允许访问/itemdb命令 | — |
| `essentials.itemlore` | 允许访问/itemlore命令 | — |
| `essentials.itemname` | 允许访问/itemname命令 | — |
| `essentials.itemname.color` | 允许使用彩色文本访问/itemname命令 | — |
| `essentials.itemname.format` | 允许访问带有格式文本的/itemname命令 | — |
| `essentials.itemname.magic` | 允许使用魔术文本访问/itemname命令 | — |
| `essentials.itemname.prevent-type.<item-name>` | 防止玩家对指定项目使用/itemname命令 | — |
| `essentials.itemname.rgb` | 允许访问带有RGB文本的/itemname命令 | — |
| `essentials.itemspawn.exempt` | 允许持有人生成项目黑名单中的项目 | — |
| `essentials.itemspawn.meta-author` | 允许承载使用作者元数据生成项目 | — |
| `essentials.itemspawn.meta-book` | 允许承载从book.txt中生成具有预填充内容的项目 | — |
| `essentials.itemspawn.meta-chapter-<chapter>` | 仅允许持有人使用/give命令从book.txt.中生成特定的书籍。 | — |
| `essentials.itemspawn.meta-firework` | 允许持有者使用烟花元数据生成项目 | — |
| `essentials.itemspawn.meta-head` | 允许持有人生成具有头部元数据的项目 | — |
| `essentials.itemspawn.meta-lore` | 允许持有人生成具有知识元数据的项目 | — |
| `essentials.itemspawn.meta-title` | 允许持有人生成具有标题元数据的项目 | — |
| `essentials.jail.allow-block-damage` | 允许持有人在入狱期间损坏格挡 | — |
| `essentials.jail.allow-break` | 允许持票人在入狱时打破障碍 | — |
| `essentials.jail.allow-interact` | 允许持有人在入狱时与区块进行交互 | — |
| `essentials.jail.allow-place` | 允许持有人在入狱时放置区块 | — |
| `essentials.jail.allow.<command>` | 允许持有人在被监禁时使用指定的命令 | — |
| `essentials.jail.exempt` | 防止指定的组或玩家被监禁 | — |
| `essentials.jail.notify` | 允许在其他玩家被监禁时通知持有人 | — |
| `essentials.jailedplayers` | 允许访问/jailedplayers命令 | — |
| `essentials.jails` | 允许访问/jails命令 | — |
| `essentials.joinfullserver` | 允许加入服务器，即使服务器已满 | — |
| `essentials.jump` | 允许访问/jump命令 | — |
| `essentials.jump.lock` | 允许访问/jump lock命令 | — |
| `essentials.keepinv` | 控制玩家是否在死亡时保留库存。 | — |
| `essentials.keepxp` | 允许用户在死亡时保留经验值，而不是将其丢弃。 | — |
| `essentials.kick` | 允许访问/kick命令 | — |
| `essentials.kick.exempt` | 防止玩家被踢出。 | — |
| `essentials.kick.notify` | 允许在其他玩家被踢出时通知持有人 | — |
| `essentials.kickall` | 允许访问/kickall命令 | — |
| `essentials.kickall.exempt` | 防止玩家被/kickall踢出 | — |
| `essentials.kill` | 允许访问/kill命令 | — |
| `essentials.kill.exempt` | 防止玩家被击杀/击杀 | — |
| `essentials.kill.force` | 允许持票人被杀/杀死，即使他们的死亡被取消 | — |
| `essentials.kit` | 允许访问/kit命令 | — |
| `essentials.kit.exemptdelay` | 免除您的套件延迟功能，这会影响标志和命令。 | — |
| `essentials.kit.others` | 允许其他玩家访问/kit命令 | — |
| `essentials.kitreset` | 允许访问/kitreset命令 | — |
| `essentials.kitreset.others` | 允许使用/kitreset命令重置其他玩家套件 | — |
| `essentials.kits.*` | 允许访问所有套件 | — |
| `essentials.kits.<kit-name>` | 允许访问特定套件 | — |
| `essentials.kittycannon` | 允许访问/kittycannon命令 | — |
| `essentials.lightning` | 允许访问/lightning命令 | — |
| `essentials.lightning.others` | 允许其他玩家访问/lightning命令 | — |
| `essentials.list` | 允许访问/list命令 | — |
| `essentials.list.hidden` | 允许在/list命令中查看隐藏的玩家 | — |
| `essentials.loom` | 允许访问/loom命令 | — |
| `essentials.mail` | 允许访问/mail命令 | — |
| `essentials.mail.clear.others` | 允许使用/mail命令清除其他玩家的邮件 | — |
| `essentials.mail.clearall` | 允许使用/mail命令清除所有邮件 | — |
| `essentials.mail.send` | 允许使用/mail命令访问发送邮件 | — |
| `essentials.mail.sendall` | 允许使用/mail命令向所有玩家发送邮件 | — |
| `essentials.mail.sendtemp` | 允许使用/mail命令访问发送临时邮件 | — |
| `essentials.me` | 允许访问/me命令 | — |
| `essentials.more` | 允许访问/more命令 | — |
| `essentials.motd` | 允许访问/motd命令 | — |
| `essentials.msg` | 允许访问/msg命令 | — |
| `essentials.msg.color` | 允许使用彩色文本访问/msg命令 | — |
| `essentials.msg.format` | 允许访问带有格式文本的/msg命令 | — |
| `essentials.msg.magic` | 允许使用魔术文本访问/msg命令 | — |
| `essentials.msg.multiple` | 允许使用/msg命令向多个玩家发送消息 | — |
| `essentials.msg.rgb` | 允许使用RGB文本访问/msg命令 | — |
| `essentials.msg.url` | 允许访问/msg命令中的发送URL | — |
| `essentials.msgtoggle` | 允许访问/msgtoggle命令 | — |
| `essentials.msgtoggle.bypass` | 允许持有人绕过其他玩家的msgtoggle设置 | — |
| `essentials.msgtoggle.others` | 允许其他玩家访问/msgtoggle命令 | — |
| `essentials.mute` | 允许访问/mute命令 | — |
| `essentials.mute.exempt` | 防止指定的组或玩家被静音 | — |
| `essentials.mute.notify` | 允许在其他玩家被静音时通知持有人 | — |
| `essentials.mute.offline` | 允许访问静音离线播放器 | — |
| `essentials.mute.unlimited` | 允许持有人覆盖最大静音时间设置 | — |
| `essentials.near` | 允许访问/near命令 | — |
| `essentials.near.exclude` | 如果玩家应被排除在近距离查找之外。 | — |
| `essentials.near.maxexempt` | 允许承载绕过/near命令的半径限制 | — |
| `essentials.near.others` | 允许其他玩家访问/near命令 | — |
| `essentials.nick` | 允许访问/nick命令 | — |
| `essentials.nick.allowunsafe` | 如果玩家有这个，他们可以将其用户名设置为任何值。请谨慎使用，因为这有可能破坏用户数据文件。 | — |
| `essentials.nick.blacklist.bypass` | 允许持有人绕过昵称黑名单 | — |
| `essentials.nick.changecolors` | 允许持有人* *仅* *更改其昵称的颜色 | — |
| `essentials.nick.color` | 允许使用彩色文本访问/nick命令 | — |
| `essentials.nick.format` | 允许访问带有格式文本的/nick命令 | — |
| `essentials.nick.hideprefix` | 拥有此权限的玩家将不会应用昵称前缀 | — |
| `essentials.nick.magic` | 允许使用魔术文本访问/nick命令 | — |
| `essentials.nick.others` | 允许其他玩家访问/nick命令 | — |
| `essentials.nick.rgb` | 允许访问带有RGB文本的/nick命令 | — |
| `essentials.nocommandcost.<command>` | 允许持有人免费使用指定的命令 | — |
| `essentials.nocommandcost.all` | 允许持有人免费使用所有命令 | — |
| `essentials.nuke` | 允许访问/nuke命令 | — |
| `essentials.oversizedstacks` | 允许承载生成超大堆栈 | — |
| `essentials.pay` | 允许访问/pay命令 | — |
| `essentials.pay.multiple` | 允许使用/pay命令向多个玩家付款 | — |
| `essentials.pay.offline` | 允许使用/pay命令向离线玩家付款 | — |
| `essentials.payconfirmtoggle` | 允许访问/payconfirmtoggle命令 | — |
| `essentials.paytoggle` | 允许访问/paytoggle命令 | — |
| `essentials.ping` | 允许访问/ping命令 | — |
| `essentials.playtime` | 允许访问/playtime命令 | — |
| `essentials.playtime.others` | 允许其他玩家访问/playtime命令 | — |
| `essentials.potion` | 允许访问/potion命令 | — |
| `essentials.potion.<potion-type>` | 允许访问特定药剂类型的/potion命令 | — |
| `essentials.potion.apply` | 允许访问/potion apply命令 | — |
| `essentials.powertool` | 允许访问/powertool命令 | — |
| `essentials.powertool.append` | 允许访问将多个命令添加到动力工具 | — |
| `essentials.powertoollist` | 允许访问/powertoollist命令 | — |
| `essentials.powertooltoggle` | 允许访问/powertooltoggle命令 | — |
| `essentials.ptime` | 允许访问/ptime命令 | — |
| `essentials.ptime.others` | 允许其他玩家访问/ptime命令 | — |
| `essentials.pvpdelay.exempt` | 允许承载绕过pvp延迟设置 | — |
| `essentials.pweather` | 允许访问/pweather命令 | — |
| `essentials.pweather.others` | 允许其他玩家访问/pweather命令 | — |
| `essentials.realname` | 允许访问/realname命令 | — |
| `essentials.recipe` | 允许访问/recipe命令 | — |
| `essentials.remove` | 允许访问/remove命令 | — |
| `essentials.renamehome` | 允许访问/renamehome命令 | — |
| `essentials.renamehome.others` | 允许使用/renamehome命令重命名其他玩家主页 | — |
| `essentials.repair` | 允许访问/repair命令 | — |
| `essentials.repair.all` | 允许访问/repair all命令 | — |
| `essentials.repair.armor` | 允许访问/repair armor命令 | — |
| `essentials.repair.enchanted` | 允许访问对附魔物品使用/repair命令 | — |
| `essentials.rest` | 允许访问/rest命令 | — |
| `essentials.rest.others` | 允许其他玩家访问/rest命令 | — |
| `essentials.rtoggle` | 允许访问/rtoggle命令 | — |
| `essentials.rules` | 允许访问/rules命令 | — |
| `essentials.seen` | 允许访问/seen命令 | — |
| `essentials.seen.alts` | 允许使用alts访问/seen命令 | — |
| `essentials.seen.banreason` | 允许使用禁止原因访问/seen命令 | — |
| `essentials.seen.extra` | 允许访问带有额外信息的/seen命令 | — |
| `essentials.seen.firstlogin` | 允许在首次登录时访问/seen命令 | — |
| `essentials.seen.ip` | 允许使用IP地址访问/seen命令 | — |
| `essentials.seen.ipsearch` | 允许使用/seen命令访问IP地址 | — |
| `essentials.seen.location` | 允许通过位置访问/seen命令 | — |
| `essentials.seen.uuid` | 允许使用UUID访问/seen命令 | — |
| `essentials.seen.whitelist` | 允许以白名单状态访问/seen命令 | — |
| `essentials.sell` | 允许访问/sell命令 | — |
| `essentials.sell.bulk` | 允许使用/sell命令访问批量销售项目 | — |
| `essentials.sell.hand` | 允许使用/sell命令出售手头的商品 | — |
| `essentials.sethome` | 允许访问/sethome命令 | — |
| `essentials.sethome.bed` | 允许玩家在白天右键单击床以更新其“床”主页。 | — |
| `essentials.sethome.multiple` | 允许使用/sethome命令设置多个房源 | — |
| `essentials.sethome.multiple.<set name>` | 将房源数量限制提高到配置中定义的特定数量 | — |
| `essentials.sethome.multiple.unlimited` | 允许使用/sethome命令设置无限个房源 | — |
| `essentials.sethome.others` | 允许使用/sethome命令设置其他玩家主页 | — |
| `essentials.setjail` | 允许访问/setjail命令 | — |
| `essentials.settpr` | 允许访问/settpr命令 | — |
| `essentials.setwarp` | 允许访问/setwarp命令 | — |
| `essentials.setworth` | 允许访问/setworth命令 | — |
| `essentials.showkit` | 允许访问/showkit命令 | — |
| `essentials.signs.break.balance` | 允许持票人打破平衡标志 | — |
| `essentials.signs.break.buy` | 允许持票人打破买入标志 | — |
| `essentials.signs.break.disposal` | 允许持有人打破处置标志 | — |
| `essentials.signs.break.enchant` | 允许持有人打破附魔标志 | — |
| `essentials.signs.break.free` | 允许持票人打破自由标志 | — |
| `essentials.signs.break.gamemode` | 允许持有人打破游戏模式标志 | — |
| `essentials.signs.break.heal` | 允许持有人打破治疗标志 | — |
| `essentials.signs.break.info` | 允许持有人破坏信息标志 | — |
| `essentials.signs.break.kit` | 允许持有人打破试剂盒标志 | — |
| `essentials.signs.break.mail` | 允许持票人打破邮件标志 | — |
| `essentials.signs.break.protection` | 允许承载者打破保护标志 | — |
| `essentials.signs.break.repair` | 允许持票人打破维修标志 | — |
| `essentials.signs.break.sell` | 允许持票人打破卖出标志 | — |
| `essentials.signs.break.spawnmob` | 允许持有人打破产卵怪迹象 | — |
| `essentials.signs.break.time` | 允许持有人打破时间标志 | — |
| `essentials.signs.break.trade` | 允许持票人打破贸易标志 | — |
| `essentials.signs.break.warp` | 允许持有人打破曲速标志 | — |
| `essentials.signs.break.weather` | 允许持票人打破天气标志 | — |
| `essentials.signs.color` | 允许持有人创建和使用彩色标志 | — |
| `essentials.signs.create.balance` | 允许持有人创建平衡标志 | — |
| `essentials.signs.create.buy` | 允许持票人创建购买标志 | — |
| `essentials.signs.create.disposal` | 允许持有人创建处置标志 | — |
| `essentials.signs.create.enchant` | 允许持有人创建附魔标志 | — |
| `essentials.signs.create.free` | 允许持有人创建免费标志 | — |
| `essentials.signs.create.gamemode` | 允许持有人创建游戏模式标志 | — |
| `essentials.signs.create.heal` | 允许持有人创建治疗标志 | — |
| `essentials.signs.create.info` | 允许持有人创建信息标志 | — |
| `essentials.signs.create.kit` | 允许持有人创建试剂盒标志 | — |
| `essentials.signs.create.mail` | 允许持票人创建邮件标志 | — |
| `essentials.signs.create.protection` | 允许持有人创建保护标志 | — |
| `essentials.signs.create.repair` | 允许持有人创建维修标志 | — |
| `essentials.signs.create.sell` | 允许持有人创建卖出标志 | — |
| `essentials.signs.create.spawnmob` | 允许持有人创建spawnmob标志 | — |
| `essentials.signs.create.time` | 允许持有人创建时间标志 | — |
| `essentials.signs.create.trade` | 允许持票人创建商标 | — |
| `essentials.signs.create.warp` | 允许持有人创建经纱标志 | — |
| `essentials.signs.create.weather` | 允许持有人创建天气标志 | — |
| `essentials.signs.enchant.allowunsafe` | 允许持有人创建和使用不安全的附魔标志 | — |
| `essentials.signs.format` | 允许持有人创建和使用格式标志 | — |
| `essentials.signs.magic` | 允许持有人创建和使用魔法标志 | — |
| `essentials.signs.protection.override` | 允许持有人打破其他玩家创建的标志 | — |
| `essentials.signs.rgb` | 允许持有人创建和使用RGB标志 | — |
| `essentials.signs.trade.override` | 允许持票人打破其他玩家创建的商标 | — |
| `essentials.signs.trade.override.collect` | 允许持票人从其他玩家创建的商标中收集道具 | — |
| `essentials.signs.use.balance` | 允许持票人使用平衡标志 | — |
| `essentials.signs.use.buy` | 允许持票人使用购买标志 | — |
| `essentials.signs.use.disposal` | 允许持有人使用处置标志 | — |
| `essentials.signs.use.enchant` | 允许持有人使用附魔标志 | — |
| `essentials.signs.use.free` | 允许持有人使用自由标志 | — |
| `essentials.signs.use.gamemode` | 允许持有人使用游戏模式标志 | — |
| `essentials.signs.use.heal` | 允许持有者使用治疗告示牌 | — |
| `essentials.signs.use.info` | 允许持有人使用信息标志 | — |
| `essentials.signs.use.kit` | 允许持有人使用套件标志 | — |
| `essentials.signs.use.mail` | 允许持票人使用邮件标志 | — |
| `essentials.signs.use.protection` | 允许持有人使用保护标志 | — |
| `essentials.signs.use.repair` | 允许持票人使用维修标志 | — |
| `essentials.signs.use.sell` | 允许持有人使用卖出标志 | — |
| `essentials.signs.use.spawnmob` | 允许持有人使用spawnmob标志 | — |
| `essentials.signs.use.time` | 允许持有人使用时间标志 | — |
| `essentials.signs.use.trade` | 允许持票人使用商标 | — |
| `essentials.signs.use.warp` | 允许持有人使用经纱标志 | — |
| `essentials.signs.use.weather` | 允许持有人使用天气标志 | — |
| `essentials.silentjoin` | 允许静默加入 | — |
| `essentials.silentjoin.vanish` | 允许静默加入，并进入消失模式 | — |
| `essentials.silentquit` | 禁止具有此权限的用户离开/退出消息。 | — |
| `essentials.skull` | 允许访问/skull命令 | — |
| `essentials.skull.modify` | 允许使用/skull命令修改其他玩家的头骨 | — |
| `essentials.skull.others` | 允许使用/skull命令创建其他玩家的头骨 | — |
| `essentials.skull.spawn` | 允许使用/skull命令生成头骨 | — |
| `essentials.sleepingignored` | 允许持票人无需睡觉即可度过夜晚 | — |
| `essentials.smithingtable` | 允许访问/smithingtable命令 | — |
| `essentials.socialspy` | 允许访问/socialspy命令 | — |
| `essentials.socialspy.others` | 允许其他玩家访问/socialspy命令 | — |
| `essentials.spawner` | 允许访问/spawner命令 | — |
| `essentials.spawner.*` | 允许访问使用/spawner命令将spawner的类型设置为所有类型 | — |
| `essentials.spawner.<mob-type>` | 允许访问使用/spawner命令将spawner的类型设置为特定类型 | — |
| `essentials.spawner.delay` | 允许使用/spawner命令访问以设置生成器的延迟 | — |
| `essentials.spawnerconvert.*` | 允许承载者放置任何类型的产卵器 | — |
| `essentials.spawnerconvert.<mob-type>` | 允许持有人放置特定类型的产卵器 | — |
| `essentials.spawnmob` | 允许访问/spawnmob命令 | — |
| `essentials.spawnmob.*` | 允许使用/spawnmob命令生成所有mob | — |
| `essentials.spawnmob.<mob-type>` | 允许使用/spawnmob命令生成特定的mob | — |
| `essentials.spawnmob.stack` | 允许使用/spawnmob命令访问堆栈中的生成mob | — |
| `essentials.speed` | 允许访问/speed命令 | — |
| `essentials.speed.bypass` | 允许承载绕过配置中设置的速度限制 | — |
| `essentials.speed.fly` | 允许访问飞行速度的/speed命令 | — |
| `essentials.speed.others` | 允许其他玩家访问/speed命令 | — |
| `essentials.speed.walk` | 允许访问步行速度的/speed命令 | — |
| `essentials.stonecutter` | 允许访问/stonecutter命令 | — |
| `essentials.sudo` | 允许访问/sudo命令 | — |
| `essentials.sudo.exempt` | 防止玩家被其他用户使用 | — |
| `essentials.sudo.multiple` | 允许多个玩家访问/sudo命令 | — |
| `essentials.suicide` | 允许多个玩家访问/suicide命令 | — |
| `essentials.teleport.cooldown.bypass.back` | 如果玩家没有此权限，/back将具有冷却时间，即使使用父旁路烫印 | True |
| `essentials.teleport.cooldown.bypass.tpa` | 如果玩家没有此权限，/tpa将具有冷却时间，即使有父旁路perm | True |
| `essentials.teleport.timer.bypass` | 允许承载绕过传送延迟 | — |
| `essentials.teleport.timer.move` | 允许携带者在等待传送时移动 | — |
| `essentials.tempban` | 允许访问/tempban命令 | — |
| `essentials.tempban.exempt` | 防止指定的组或玩家被临时禁用 | — |
| `essentials.tempban.offline` | 允许访问临时禁用离线玩家 | — |
| `essentials.tempban.unlimited` | 允许持有人覆盖max-tempban-time设置 | — |
| `essentials.tempbanip` | 允许访问/tempbanip命令 | — |
| `essentials.thunder` | 允许访问/thunder命令 | — |
| `essentials.time` | 允许访问/time命令 | — |
| `essentials.time.set` | 允许访问使用/time命令设置时间 | — |
| `essentials.time.world.all` | 允许访问使用/time命令设置所有世界的时间 | — |
| `essentials.togglejail` | 允许访问/togglejail命令 | — |
| `essentials.togglejail.offline` | 允许离线玩家访问/togglejail命令 | — |
| `essentials.top` | 允许访问/top命令 | — |
| `essentials.tp` | 允许访问/tp命令 | — |
| `essentials.tp.others` | 允许使用/tp命令远程传送给其他用户 | — |
| `essentials.tp.position` | 允许使用/tp命令传送到某个位置 | — |
| `essentials.tpa` | 允许访问/tpa命令 | — |
| `essentials.tpaall` | 允许访问/tpaall命令 | — |
| `essentials.tpacancel` | 允许访问/tpaccept命令 | — |
| `essentials.tpaccept` | 允许访问/tpaccept命令 | — |
| `essentials.tpahere` | 允许访问/tpahere命令 | — |
| `essentials.tpall` | 允许访问/tpall命令 | — |
| `essentials.tpauto` | 允许访问/tpauto命令 | — |
| `essentials.tpauto.others` | 允许其他玩家访问/tpauto命令 | — |
| `essentials.tpdeny` | 允许访问/tpdeny命令 | — |
| `essentials.tphere` | 允许访问/tphere命令 | — |
| `essentials.tpo` | 允许访问/tpo命令 | — |
| `essentials.tpoffline` | 允许访问/tpoffline命令 | — |
| `essentials.tpohere` | 允许访问/tpohere命令 | — |
| `essentials.tppos` | 允许访问/tppos命令 | — |
| `essentials.tpr` | 允许访问/tpr命令 | — |
| `essentials.tptoggle` | 允许访问/tptoggle命令 | — |
| `essentials.tptoggle.others` | 允许其他玩家访问/tptoggle命令 | — |
| `essentials.tree` | 允许访问/tree命令 | — |
| `essentials.unban` | 允许访问/unban命令 | — |
| `essentials.unbanip` | 允许访问/unbanip命令 | — |
| `essentials.unlimited` | 允许访问/unlimited命令 | — |
| `essentials.unlimited.item-<item-name>` | 允许在启用基于权限的项目生成时访问特定项目的/unlimited命令 | — |
| `essentials.unlimited.item-all` | 允许在启用基于权限的项目生成时访问所有项目的/unlimited命令 | — |
| `essentials.unlimited.item-bucket` | 允许访问水桶和熔岩的/unlimited命令 | — |
| `essentials.unlimited.others` | 允许其他玩家访问/unlimited命令 | — |
| `essentials.updatecheck` | 持有人将收到EssentialsX更新的通知 | — |
| `essentials.vanish` | 允许访问/vanish命令 | — |
| `essentials.vanish.effect` | 在消失模式下对玩家应用隐身效果 | — |
| `essentials.vanish.interact` | 允许持有人在消失模式下与玩家互动 | — |
| `essentials.vanish.others` | 允许其他玩家访问/vanish命令 | — |
| `essentials.vanish.pickup` | 允许持票人在消失模式下领取物品 | — |
| `essentials.vanish.pvp` | 允许持有者在消失模式下攻击玩家 | — |
| `essentials.vanish.see` | 允许持有人在消失模式下看到其他玩家 | — |
| `essentials.version` | 允许访问/version命令 | — |
| `essentials.warp` | 允许访问/warp命令 | — |
| `essentials.warp.list` | 允许访问/warp list命令 | — |
| `essentials.warp.others` | 允许其他玩家访问/warp命令 | — |
| `essentials.warp.overwrite.*` | 允许承载覆盖所有翘曲 | — |
| `essentials.warp.overwrite.<warp-name>` | 允许承载覆盖特定曲线 | — |
| `essentials.warpinfo` | 允许访问/warpinfo命令 | — |
| `essentials.weather` | 允许访问/weather命令 | — |
| `essentials.whitelist.bypass` | 允许玩家加入服务器，即使他们没有列入白名单。 | — |
| `essentials.whois` | 允许访问/whois命令 | — |
| `essentials.whois.ip` | 允许使用IP地址访问/whois命令 | — |
| `essentials.workbench` | 允许访问/workbench命令 | — |
| `essentials.world` | 允许访问/world命令 | — |
| `essentials.worlds.<world-name>` | 允许使用各种命令访问特定世界 | — |
| `essentials.worth` | 允许访问/worth命令 | — |

## 相关插件

[EssentialsSpawn](/commands/teleport/essentialsspawn.md)、[Vault](/commands/core/vault.md)、[LuckPerms](/commands/core/luckperms.md)、[PlaceholderAPI](/commands/config/placeholderapi.md)
