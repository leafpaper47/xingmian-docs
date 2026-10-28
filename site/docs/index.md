---
title: 指令总览
createTime: 2026/10/24
---

# 星冕服务器 · 指令总览

共 **85** 个插件、**434** 条指令。每个插件页含「指令一览（指令/功能/用法/权限）」与「指令详解（语法、参数、示例）」。用右上角搜索（`Ctrl + K`）可直接搜指令名，例如 `co`、`lp`、`res`。

## 🛡️ 基础与权限

权限、插件加载、维护模式、Vault 经济桥等服务器底座。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [ConsoleSpamFixReborn](/commands/core/consolespamfixreborn.md) | 按规则屏蔽控制台重复报错刷屏 | `/csf` | 1 |
| [LuckPerms](/commands/core/luckperms.md) | 权限与组管理 | `/luckperms` | 1 |
| [MaintenanceMode](/commands/core/maintenancemode.md) | 开服维护期间的封服开关 | `/maintenance` | 1 |
| [PlugManX](/commands/core/plugmanx.md) | 插件热管理 | `/plugman` | 1 |
| [Vault](/commands/core/vault.md) | 经济与权限接口层 | `/vault-convert`、`/vault-info` | 2 |
| [WebBridge](/commands/core/webbridge.md) | 打通卫星地图网页聊天与游戏内聊天 | `/mapverify` | 1 |

## 🧰 基础工具

Essentials 系与各类物品/背包/生存辅助工具。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [ALCERecipeViewer](/commands/essentials/alcerecipeviewer.md) | 按分类浏览和搜索合成配方的合成表查看器 | `/alcerecipes` | 1 |
| [ArmoredElytra](/commands/essentials/armoredelytra.md) | 把胸甲和鞘翅合成一件带护甲的鞘翅 | `/armoredelytra` | 1 |
| [ArmorUnbreaking](/commands/essentials/armorunbreaking.md) | 让护甲耐久附魔按概率豁免耐久扣减 | `/armordura` | 1 |
| [BookEdit](/commands/essentials/bookedit.md) | 成书排版与作者信息编辑小工具 | `/book` | 1 |
| [CMILib](/commands/essentials/cmilib.md) | 库前置 | `/cmil` | 1 |
| [CraftBench](/commands/essentials/craftbench.md) | 随身 5×5 合成台与配方编辑工具 | `/craftbench`、`/craftbenchadmin` | 2 |
| [Essentials](/commands/essentials/essentials.md) | 基础指令总控 | `/afk`、`/antioch`、`/anvil`、`/back`… | 153 |
| [InBlock](/commands/essentials/inblock.md) | 自定义命令方块：右键方块执行指令 | `/inb` | 1 |
| [InfiniteFuel](/commands/essentials/infinitefuel.md) | 让熔炉烧不完的无限燃料小插件 | `/infinitefuel` | 1 |
| [InvSaver](/commands/essentials/invsaver.md) | 背包快照 | `/invSaver` | 6 |
| [ItemEdit](/commands/essentials/itemedit.md) | 物品编辑 | `/itemedit`、`/itemeditimport`、`/itemeditinfo`、`/itemeditreload`… | 6 |
| [LeafHat](/commands/essentials/leafhat.md) | 把手上物品戴到头上 | `/hat`、`/unhat` | 2 |
| [OpenInv](/commands/essentials/openinv.md) | 远程开箱 | `/anycontainer`、`/clearender`、`/clearinv`、`/openender`… | 10 |
| [PlayerSignIn](/commands/essentials/playersignin.md) | 玩家签到 | `/playerSignIn` | 1 |
| [PlayerTask](/commands/essentials/playertask.md) | 任务系统 | `/playerTask` | 1 |
| [StarAFK](/commands/essentials/starafk.md) | 自动与手动挂机状态管理 | `/afk` | 1 |

## 🌀 传送与出生点

随机传送、出生点、回家相关。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [BetterRTP](/commands/teleport/betterrtp.md) | 随机传送 | `/betterrtp` | 1 |
| [EssentialsSpawn](/commands/teleport/essentialsspawn.md) | 出生点传送 | `/setspawn`、`/spawn` | 2 |

## 🗺️ 世界与地图

地图渲染、坐标同步、天气与天象、镜像世界。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [ArtMap](/commands/world/artmap.md) | 把画架变成像素画板 | `/art` | 1 |
| [MeteorShowers](/commands/world/meteorshowers.md) | 随机流星雨事件与预警 | `/meteorshowers` | 1 |
| [Mirrora](/commands/world/mirrora.md) | 镜像方块插件 | `/mirror` | 1 |
| [WeatherCard](/commands/world/weathercard.md) | 四张扑克天气卡 | `/weathercard` | 1 |
| [XaeroTracker](/commands/world/xaerotracker.md) | 在小地图上显示与追踪玩家位置 | `/xaerotracker` | 1 |

## 🔒 领地与保护

领地、容器锁、WorldGuard 图形界面。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [BlockLocker](/commands/protect/blocklocker.md) | 用告示牌给箱子门做私有上锁 | `/blocklocker` | 1 |
| [Residence](/commands/protect/residence.md) | 领地保护 | `/rc`、`/res`、`/resadmin`、`/resload`… | 35 |
| [TownPlugin](/commands/protect/townplugin.md) | 城镇系统 | `/town`、`/townadmin`、`/townui`、`/townwarp`… | 5 |
| [WorldGuardGUI](/commands/protect/worldguardgui.md) | WorldGuard 区域 | `/wggui` | 1 |

## 🪙 经济与商店

点券、商店、玩家交易、赞助充值。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [AfDianPay](/commands/economy/afdianpay.md) | 爱发电对接 | `/afDianPay` | 1 |
| [DummyPool](/commands/economy/dummypool.md) | 服务器里的台球玩法插件 | `/dummypool`、`/dump` | 2 |
| [MagicPointsLog](/commands/economy/magicpointslog.md) | PlayerPoints 点数变动记录 | `/mpl` | 1 |
| [SenluoBuyer](/commands/economy/senluobuyer.md) | 森罗厨房每日随机收购回收面板 | `/senluobuyer` | 1 |
| [Shopkeepers](/commands/economy/shopkeepers.md) | NPC 商店 | `/shopkeeper` | 1 |
| [WineSuite](/commands/economy/winesuite.md) | 酿酒图鉴 | `/winebook`、`/winebuyer` | 2 |

## ⚔️ 战斗与 RPG

MythicMobs 系、附魔、Boss、属性、自定义战斗。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | 自定义附魔 | `/ecoenchants`、`/enchant`、`/enchantinfo` | 3 |
| [EliteMobs](/commands/rpg/elitemobs.md) | 精英怪物 | `/elitemobs` | 1 |
| [EnchantInfuser](/commands/rpg/enchantinfuser.md) | 铁匠铺式附魔强化 | `/enin` | 1 |
| [FoMiningComp](/commands/rpg/fominingcomp.md) | 挖矿竞赛活动插件 | `/fominingcomp` | 1 |
| [KaoguGuide](/commands/rpg/kaoguguide.md) | 考古图鉴 | `/kaoguguide` | 1 |
| [KaoguPlugin](/commands/rpg/kaoguplugin.md) | 考古玩法 | `/kaogu` | 1 |
| [MythicMobs](/commands/rpg/mythicmobs.md) | 自定义怪物 | `/addpin`、`/mythicmobs`、`/mythicmobsmenu`、`/pins`… | 5 |
| [MythicTools](/commands/rpg/mythictools.md) | MythicMobs 掉落与 Boss 工具 | `/mythictools` | 1 |
| [PVPPlugin](/commands/rpg/pvpplugin.md) | 玩家间决斗与公平排位的可视化管理插件 | `/pvp` | 1 |
| [StarPact](/commands/rpg/starpact.md) | 关系契约社交 | `/gender`、`/xzqy`、`/xzqyxb` | 16 |
| [XingmianElement](/commands/rpg/xingmianelement.md) | 元素职业 | `/element`、`/xmbe` | 2 |
| [XingmianRPG](/commands/rpg/xingmianrpg.md) | RPG 世界管控 | `/roll`、`/rpg`、`/rpgadmin`、`/stamina`… | 49 |

## 🧟 生物与展示

伪装、模型、NPC、实体编辑。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [BossBarHealth](/commands/entity/bossbarhealth.md) | 用BOSS栏实时显示玩家与敌人血量 | `/bossbarhealth` | 1 |
| [EditableStands](/commands/entity/editablestands.md) | 拿物品右键盔甲架 | `/editablestands` | 1 |
| [FancyNpcsGUI](/commands/entity/fancynpcsgui.md) | FancyNpcs 图形化 NPC 编辑 | `/npcgui` | 1 |
| [LibsDisguises](/commands/entity/libsdisguises.md) | 伪装系统 | `/copydisguise`、`/disguise`、`/disguiseanimation`、`/disguiseclone`… | 28 |
| [ModelEngine](/commands/entity/modelengine.md) | 自定义模型 | `/meg` | 1 |
| [YiyunCEskin](/commands/entity/yiyunceskin.md) | 给 CraftEngine 物品套用皮肤 | `/yiyunceskin` | 1 |

## 💬 聊天与社交

聊天格式、公告、邮件、称号、语音、计分板。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [BroadcastPlusPlus](/commands/chat/broadcastplusplus.md) | 公告广播 | `/broadcast` | 1 |
| [LeafChat](/commands/chat/leafchat.md) | 统一管理聊天格式 | `/chatcolor`、`/leafchat`、`/leafchatview`、`/msg`… | 8 |
| [PlayerTitle](/commands/chat/playertitle.md) | 称号系统 | `/playerTitle` | 1 |
| [SweetMail](/commands/chat/sweetmail.md) | 站内邮件 | `/sweetmail` | 1 |
| [TAB](/commands/chat/tab.md) | TAB 列表 | `/tab` | 1 |
| [vcm](/commands/chat/vcm.md) | 语音喇叭 | `/vcm` | 1 |
| [voicechat](/commands/chat/voicechat.md) | 近距离语音聊天与临时语音群组 | `/voicechat` | 1 |
| [YaoqingPlugin](/commands/chat/yaoqingplugin.md) | 老玩家拉新与邀请码绑定奖励系统 | `/yaoqing` | 1 |

## 🧩 脚本与菜单

Skript、DeluxeMenus、PlaceholderAPI 等二次开发底座。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [DeluxeMenus](/commands/config/deluxemenus.md) | GUI 菜单 | `/deluxemenus` | 1 |
| [KaleidoscopeCookeryPlugin](/commands/config/kaleidoscopecookeryplugin.md) | 森罗厨房菜谱系统 | `/kcrecipe` | 1 |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | 变量占位符 | `/placeholderapi` | 1 |
| [Skript](/commands/config/skript.md) | 脚本引擎 | `/skript` | 1 |

## 📊 记录与性能

方块回滚、性能采样、审计。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [CoreProtect](/commands/audit/coreprotect.md) | 方块日志与回滚 | `/co` | 17 |
| [spark](/commands/audit/spark.md) | 性能剖析 | `/spark` | 1 |

## 🎲 小游戏与娱乐

服务器自研玩法与休闲小游戏。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [Ah-Toy-1.0](/commands/minigame/ah-toy-1-0.md) | 趣味小玩具发放与配置管理插件 | `/toy` | 1 |
| [Ah-WolfmanKill-1.0](/commands/minigame/ah-wolfmankill-1-0.md) | 狼人杀小游戏的开局与场地管理插件 | `/wk` | 1 |
| [allmusic](/commands/minigame/allmusic.md) | 点歌/音乐 | `/music` | 1 |
| [GSit](/commands/minigame/gsit.md) | 坐姿动作 | `/gbellyflop`、`/gcrawl`、`/glay`、`/glayback`… | 7 |
| [LeashPlayers](/commands/minigame/leashplayers.md) | 用栓绳把玩家当动物一样牵走的小游戏插件 | `/leash` | 1 |
| [LobbyGames](/commands/minigame/lobbygames.md) | 小游戏汇总 | `/lgjoin`、`/lgjoinplayer`、`/lobbygames` | 3 |
| [MahjongPlay](/commands/minigame/mahjongplay.md) | 麻将小游戏 | `/mahjong` | 1 |
| [XingmianQuiz](/commands/minigame/xingmianquiz.md) | 定时全服答题 | `/quiz` | 4 |

## 📦 其他

未归类的插件。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [AntiBoom](/commands/other/antiboom.md) | 爆炸伤害防护与区域豁免 | `/antiboom` | 1 |
| [ArchitectPlugin](/commands/other/architectplugin.md) | 星冕服务器的建筑师认证与接单系统 | `/arch`、`/archadmin`、`/archshop`、`/task` | 4 |
| [Images](/commands/other/images.md) | 自定义图片 | `/image` | 1 |
| [PatPatPlugin](/commands/other/patpatplugin.md) | 拍拍互动 | `/patpat` | 1 |
| [SenluoCookbook](/commands/other/senluocookbook.md) | 森罗厨房图鉴 | `/cookbook` | 1 |
| [YccHongBao](/commands/other/ycchongbao.md) | 红包发放与领取记录查询 | `/ycch` | 1 |
