---
title: 指令总览
createTime: 2026/10/24
---

# 星冕服务器 · 指令总览

共 **80** 个插件、**318** 条指令。每个插件页含「指令一览（指令/功能/用法/权限）」与「指令详解（语法、参数、示例）」。用右上角搜索（`Ctrl + K`）可直接搜指令名，例如 `co`、`lp`、`res`。

## 🛡️ 基础与权限

权限、插件加载、维护模式、Vault 经济桥等服务器底座。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [ConsoleSpamFixReborn](/commands/core/consolespamfixreborn.md) | 按规则屏蔽控制台重复报错刷屏 | `/csf` | 1 |
| [LuckPerms](/commands/core/luckperms.md) | 全局权限系统：组 / 玩家 / 权限节点 | `/luckperms` | 1 |
| [MaintenanceMode](/commands/core/maintenancemode.md) | 开服维护期间的封服开关 | `/maintenance` | 1 |
| [PlugManX](/commands/core/plugmanx.md) | 插件热管，不关服就能装、卸、启停插件 | `/plugman` | 1 |
| [Vault](/commands/core/vault.md) | 经济与权限接口前置库，插件间的通用桥梁 | `/vault-convert`、`/vault-info` | 2 |
| [WebBridge](/commands/core/webbridge.md) | 打通卫星地图网页聊天与游戏内聊天 | `/mapverify` | 1 |

## 🧰 基础工具

Essentials 系与各类物品/背包/生存辅助工具。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [ALCERecipeViewer](/commands/essentials/alcerecipeviewer.md) | 按分类浏览和搜索合成配方的合成表查看器 | `/alcerecipes` | 1 |
| [ArmoredElytra](/commands/essentials/armoredelytra.md) | 把胸甲和鞘翅合成一件带护甲的鞘翅 | `/armoredelytra` | 1 |
| [ArmorUnbreaking](/commands/essentials/armorunbreaking.md) | 让护甲耐久附魔按概率豁免耐久扣减 | `/armordura` | 1 |
| [BookEdit](/commands/essentials/bookedit.md) | 成书排版与作者信息编辑小工具 | `/book` | 1 |
| [CMILib](/commands/essentials/cmilib.md) | CMI 等插件的前置依赖库，本身不提供玩法 | `/cmil` | 1 |
| [CraftBench](/commands/essentials/craftbench.md) | 随身 5×5 合成台与配方编辑工具 | `/craftbench`、`/craftbenchadmin` | 2 |
| [Essentials](/commands/essentials/essentials.md) | 服务器基础指令总控，管理、传送、经济全靠它 | `/afk`、`/antioch`、`/anvil`、`/back`… | 153 |
| [InBlock](/commands/essentials/inblock.md) | 自定义命令方块：右键方块执行指令 | `/inb` | 1 |
| [InfiniteFuel](/commands/essentials/infinitefuel.md) | 让熔炉烧不完的无限燃料小插件 | `/infinitefuel` | 1 |
| [InvSaver](/commands/essentials/invsaver.md) | 背包快照保存与回滚工具 | `/invSaver` | 1 |
| [ItemEdit](/commands/essentials/itemedit.md) | 手持物品的图形化编辑器，改名改 Lore 改属性 | `/itemedit`、`/itemeditimport`、`/itemeditinfo`、`/itemeditreload`… | 6 |
| [LeafHat](/commands/essentials/leafhat.md) | 把手上物品戴到头上，替代 Essentials 帽子功能 | `/hat`、`/unhat` | 2 |
| [OpenInv](/commands/essentials/openinv.md) | 宝箱式远程查看与编辑玩家背包、末影箱 | `/anycontainer`、`/clearender`、`/clearinv`、`/openender`… | 10 |
| [PlayerSignIn](/commands/essentials/playersignin.md) | 每日签到与补签卡管理插件 | `/playerSignIn` | 1 |
| [PlayerTask](/commands/essentials/playertask.md) | 每日任务、任务目标与任务币商城系统 | `/playerTask` | 1 |
| [StarAFK](/commands/essentials/starafk.md) | 自动与手动挂机状态管理 | `/afk` | 1 |

## 🌀 传送与出生点

随机传送、出生点、回家相关。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [BetterRTP](/commands/teleport/betterrtp.md) | 功能全面的随机传送插件，主世界野外探索标配 | `/betterrtp` | 1 |
| [EssentialsSpawn](/commands/teleport/essentialsspawn.md) | 管理服务器出生点的传送与设置 | `/setspawn`、`/spawn` | 2 |

## 🗺️ 世界与地图

地图渲染、坐标同步、天气与天象、镜像世界。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [ArtMap](/commands/world/artmap.md) | 把画架变成像素画板，作画、存作、发放作品 | `/art` | 1 |
| [MeteorShowers](/commands/world/meteorshowers.md) | 生存向随机流星雨事件：预警、陨石坑、战利品 | `/meteorshowers` | 1 |
| [Mirrora](/commands/world/mirrora.md) | 镜像方块插件，把一块区域的建筑按轴镜像复制 | `/mirror` | 1 |
| [WeatherCard](/commands/world/weathercard.md) | 四张扑克天气卡，手动切换家园与星陨之地的天气 | `/weathercard` | 1 |
| [XaeroTracker](/commands/world/xaerotracker.md) | 在小地图上显示与追踪玩家位置 | `/xaerotracker` | 1 |

## 🔒 领地与保护

领地、容器锁、WorldGuard 图形界面。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [BlockLocker](/commands/protect/blocklocker.md) | 用告示牌给箱子门做私有上锁 | `/blocklocker` | 1 |
| [Residence](/commands/protect/residence.md) | 方块领地保护与经济租赁一体化管理 | `/rc`、`/res`、`/resadmin`、`/resload`… | 5 |
| [TownPlugin](/commands/protect/townplugin.md) | 星冕服自研城镇系统，聚落建城与城镇管理 | `/town`、`/townadmin`、`/townui`、`/townwarp`… | 5 |
| [WorldGuardGUI](/commands/protect/worldguardgui.md) | WorldGuard 区域的图形化管理界面 | `/wggui` | 1 |

## 🪙 经济与商店

点券、商店、玩家交易、赞助充值。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [AfDianPay](/commands/economy/afdianpay.md) | 把爱发电赞助自动换成游戏内奖励 | `/afDianPay` | 1 |
| [DummyPool](/commands/economy/dummypool.md) | 服务器里的台球玩法插件，负责球台与对局 | `/dummypool`、`/dump` | 2 |
| [MagicPointsLog](/commands/economy/magicpointslog.md) | 记录并查询 PlayerPoints 点券的收支流水 | `/mpl` | 1 |
| [SenluoBuyer](/commands/economy/senluobuyer.md) | 森罗厨房每日随机收购回收面板 | `/senluobuyer` | 1 |
| [Shopkeepers](/commands/economy/shopkeepers.md) | 用村民或实体当店主的玩家商店与系统商店系统 | `/shopkeeper` | 1 |
| [WineSuite](/commands/economy/winesuite.md) | 自研酒水套装：酿酒图鉴加酒水收购 | `/winebook`、`/winebuyer` | 2 |

## ⚔️ 战斗与 RPG

MythicMobs 系、附魔、Boss、属性、自定义战斗。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [EcoEnchants](/commands/rpg/ecoenchants.md) | 自定义附魔系统，给物品加全新附魔 | `/ecoenchants`、`/enchant`、`/enchantinfo` | 3 |
| [EliteMobs](/commands/rpg/elitemobs.md) | 精英怪物的生成与运维管理 | `/elitemobs` | 1 |
| [EnchantInfuser](/commands/rpg/enchantinfuser.md) | 铁匠铺式附魔强化，用强化石给装备锻打附魔 | `/enin` | 1 |
| [FoMiningComp](/commands/rpg/fominingcomp.md) | 挖矿竞赛活动插件，按挖矿量排名发奖 | `/fominingcomp` | 1 |
| [KaoguGuide](/commands/rpg/kaoguguide.md) | 用图鉴界面查看玩家已修复过的古物 | `/kaoguguide` | 1 |
| [KaoguPlugin](/commands/rpg/kaoguplugin.md) | 考古玩法主插件：化石获取、鉴定、修复与回收 | `/kaogu` | 1 |
| [MythicMobs](/commands/rpg/mythicmobs.md) | 用配置定义怪物、技能与掉落的自定义怪物引擎 | `/addpin`、`/mythicmobs`、`/mythicmobsmenu`、`/pins`… | 5 |
| [MythicTools](/commands/rpg/mythictools.md) | MythicMobs 掉落/Boss/刷怪的辅助管理工具 | `/mythictools` | 1 |
| [PVPPlugin](/commands/rpg/pvpplugin.md) | 玩家间决斗与公平排位的可视化管理插件 | `/pvp` | 1 |
| [StarPact](/commands/rpg/starpact.md) | 星契：玩家人际羁绊与亲密度系统，全界面操作 | `/gender`、`/xzqy`、`/xzqyxb` | 3 |
| [XingmianElement](/commands/rpg/xingmianelement.md) | 星冕自研的元素等级与法杖技能系统 | `/element`、`/xmbe` | 2 |
| [XingmianRPG](/commands/rpg/xingmianrpg.md) | 星陨之地 RPG 世界的整套玩法管控插件 | `/roll`、`/rpg`、`/rpgadmin`、`/stamina`… | 5 |

## 🧟 生物与展示

伪装、模型、NPC、实体编辑。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [BossBarHealth](/commands/entity/bossbarhealth.md) | 用BOSS栏实时显示玩家与敌人血量的HUD插件 | `/bossbarhealth` | 1 |
| [EditableStands](/commands/entity/editablestands.md) | 拿物品右键盔甲架，直接改形态的轻量工具 | `/editablestands` | 1 |
| [FancyNpcsGUI](/commands/entity/fancynpcsgui.md) | FancyNpcs 的图形化 NPC 编辑器 | `/npcgui` | 1 |
| [LibsDisguises](/commands/entity/libsdisguises.md) | 把玩家和实体伪装成其他生物、玩家或物品 | `/copydisguise`、`/disguise`、`/disguiseanimation`、`/disguiseclone`… | 28 |
| [ModelEngine](/commands/entity/modelengine.md) | 让服务器用自定义 3D 模型替换生物外观并播放动画 | `/meg` | 1 |
| [YiyunCEskin](/commands/entity/yiyunceskin.md) | 给 CraftEngine 物品条目套用云皮肤的配套插件 | `/yiyunceskin` | 1 |

## 💬 聊天与社交

聊天格式、公告、邮件、称号、语音、计分板。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [BroadcastPlusPlus](/commands/chat/broadcastplusplus.md) | 统一管理全服公告广播与多种显示通道 | `/broadcast` | 1 |
| [LeafChat](/commands/chat/leafchat.md) | 统一管理聊天格式、私聊、禁言与物品展示 | `/chatcolor`、`/leafchat`、`/leafchatview`、`/msg`… | 8 |
| [PlayerTitle](/commands/chat/playertitle.md) | 称号系统：发放、展示、商城与收藏 | `/playerTitle` | 1 |
| [SweetMail](/commands/chat/sweetmail.md) | 玩家之间离线寄信与寄物品的邮件系统 | `/sweetmail` | 1 |
| [TAB](/commands/chat/tab.md) | 统一管理 TAB 列表、计分板、侧边栏与名称标签 | `/tab` | 1 |
| [vcm](/commands/chat/vcm.md) | 语音扩音器：用喇叭向全场广播语音 | `/vcm` | 1 |
| [voicechat](/commands/chat/voicechat.md) | 近距离语音聊天与临时语音群组 | `/voicechat` | 1 |
| [YaoqingPlugin](/commands/chat/yaoqingplugin.md) | 老玩家拉新与邀请码绑定奖励系统 | `/yaoqing` | 1 |

## 🧩 脚本与菜单

Skript、DeluxeMenus、PlaceholderAPI 等二次开发底座。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [DeluxeMenus](/commands/config/deluxemenus.md) | 用 YAML 配置箱子菜单的界面插件 | `/deluxemenus` | 1 |
| [KaleidoscopeCookeryPlugin](/commands/config/kaleidoscopecookeryplugin.md) | 森罗厨房菜谱系统，查看与编辑自定义食物配方 | `/kcrecipe` | 1 |
| [PlaceholderAPI](/commands/config/placeholderapi.md) | 全服统一的变量占位符引擎，供各插件取值 | `/placeholderapi` | 1 |
| [Skript](/commands/config/skript.md) | 脚本引擎，用接近英语的语句改写服务器机制 | `/skript` | 1 |

## 📊 记录与性能

方块回滚、性能采样、审计。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [CoreProtect](/commands/audit/coreprotect.md) | 方块日志：查谁动过箱子、回滚破坏 | `/co` | 1 |
| [spark](/commands/audit/spark.md) | 服务器卡顿排查与性能采样工具 | `/spark` | 1 |

## 🎲 小游戏与娱乐

服务器自研玩法与休闲小游戏。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [Ah-Toy-1.0](/commands/minigame/ah-toy-1-0.md) | 趣味小玩具发放与配置管理插件 | `/toy` | 1 |
| [Ah-WolfmanKill-1.0](/commands/minigame/ah-wolfmankill-1-0.md) | 狼人杀小游戏的开局与场地管理插件 | `/wk` | 1 |
| [allmusic](/commands/minigame/allmusic.md) | 全服音乐播放与广播的点歌类插件 | `/music` | 1 |
| [GSit](/commands/minigame/gsit.md) | 让玩家坐下、躺下、爬行与旋转的姿势插件 | `/gbellyflop`、`/gcrawl`、`/glay`、`/glayback`… | 7 |
| [LeashPlayers](/commands/minigame/leashplayers.md) | 用栓绳把玩家当动物一样牵走的小游戏插件 | `/leash` | 1 |
| [LobbyGames](/commands/minigame/lobbygames.md) | 在大厅里开小游戏对局，玩家随进随玩 | `/lgjoin`、`/lgjoinplayer`、`/lobbygames` | 3 |
| [MahjongPlay](/commands/minigame/mahjongplay.md) | 在服务器里打日本立直麻将的小游戏 | `/mahjong` | 1 |
| [XingmianQuiz](/commands/minigame/xingmianquiz.md) | 定时自动百科答题，首个答对者得星点 | `/quiz` | 1 |

## 📦 其他

未归类的插件。

| 插件 | 定位 | 主要指令 | 指令数 |
| --- | --- | --- | --- |
| [ArchitectPlugin](/commands/other/architectplugin.md) | 星冕服务器的建筑师认证与接单系统 | `/arch`、`/archadmin`、`/archshop`、`/task` | 4 |
