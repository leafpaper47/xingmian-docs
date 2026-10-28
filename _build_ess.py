# -*- coding: utf-8 -*-
"""生成 data/notes/essentials.json（153 条 Essentials 注册指令注解）。"""
import json, io, os

NAME = "Essentials"
ROLE = "基础指令总控"
SUMMARY = ("星冕服务器的基础指令插件：传送、家与地标、经济（自带 eco 给钱）、封禁禁言、"
           "物品与背包、运行状态查询都由它承接。管理员绝大多数后台操作从这里开始，"
           "权限用 LuckPerms 按 essentials.xxx 节点分发。")

WHATFOR = [
    "新手福利：地标、家、新手礼包、随机传送",
    "日常管人：封禁、限时封禁、禁言、监狱禁足",
    "配经济：给钱扣钱、定回收价、财富排行",
]

QUICK = [
    ("传送到玩家身边", "/tp 玩家名", "把自己送过去；/tphere 才是把人拉过来"),
    ("回家与设家", "/sethome 家名 → /home 家名", "带玩家名可替他人设家"),
    ("传送到地标", "/warp 主城", "地标先用 /setwarp 主城 建好"),
    ("给钱扣钱", "/eco give 玩家名 1000", "余额由它管，其它插件通过 Vault 读"),
    ("给物品", "/give 玩家名 diamond 64", "只给自己用 /item"),
    ("切游戏模式", "/gamemode creative 玩家名", "简写 /gmc /gms /gmsp，对他人要有权限"),
    ("禁言与踢人", "/mute 玩家名 1h 刷屏", "真封人用 /ban 或 /tempban"),
    ("看在线与负载", "/list 与 /gc", "/gc 别名 /tps 也能看 TPS 与内存"),
]

CAUTION = [
    "/ess reload 只重载 Essentials 自己的配置与语言文件，不动别的插件；Bukkit 的 /reload 会重载全部插件，"
    "容易留下内存泄漏和重复注册的任务。线上优先 /ess reload，动到别的插件就老实重启。",
    "Essentials 自带的经济只有装了 Vault 才会被商店、点券、任务类插件读到。服务器已有别的经济插件时，"
    "务必只留一个经济来源，否则余额对不上、排行榜会乱。",
    "/give 与 /eco 的数量、金额写错（多打一个 0）不能撤销，也不会进回收站。批量发放前先用小号试一条，"
    "重大操作前先 /backup。",
]

# (cmd, what, syntax)
C = [
("afk", "把自己标记为暂离并自动回复私聊", "/afk [玩家名或留言]"),
("antioch", "在脚下引爆一片 TNT（恶搞）", "/antioch [留言]"),
("anvil", "原地打开铁砧界面改装备", "/anvil"),
("back", "回到上次传送或死亡前的位置", "/back [玩家名]"),
("backup", "立即触发一次服务端备份", "/backup"),
("balance", "查看自己或他人的金币余额", "/balance [玩家名]"),
("balancetop", "查看服务器财富排行榜", "/balancetop [页码]"),
("ban", "封禁玩家并立即踢下线", "/ban <玩家名> [原因]"),
("banip", "按 IP 地址封禁", "/banip <IP> [原因]"),
("beezooka", "向准星方向射出一只爆炸蜜蜂", "/beezooka"),
("book", "改写手里成书的标题或作者", "/book [title|author 值]"),
("bottom", "传送到当前位置最底可站立层", "/bottom"),
("break", "直接破坏准星所指的方块", "/break"),
("broadcast", "向全服广播一条公告", "/broadcast <内容>"),
("broadcastworld", "只向指定世界广播公告", "/broadcastworld <世界> <内容>"),
("bigtree", "在准星处生成一棵大树", "/bigtree <树种>"),
("burn", "点燃指定玩家若干秒", "/burn <玩家名> <秒>"),
("cartographytable", "原地打开制图台", "/cartographytable"),
("clearinventory", "清空背包，可指定物品与数量", "/clearinventory [玩家名|*] [物品|*] [数量]"),
("clearinventoryconfirmtoggle", "切换清空背包时的二次确认", "/clearinventoryconfirmtoggle"),
("condense", "把背包散装材料压成块", "/condense [物品名]"),
("compass", "显示当前朝向", "/compass"),
("createkit", "用自己背包创建礼包", "/createkit <礼包名> <冷却>"),
("customtext", "输出 bukkit.yml 里定义的自定义文本", "自定义别名（bukkit.yml 定义）"),
("delhome", "删除一个家", "/delhome [玩家名:]<家名>"),
("deljail", "删除一座监狱", "/deljail <监狱名>"),
("delkit", "删除一个礼包", "/delkit <礼包名>"),
("delwarp", "删除一个地标", "/delwarp <地标名>"),
("depth", "显示当前所在高度", "/depth"),
("disposal", "打开垃圾桶界面丢东西", "/disposal"),
("eco", "给钱、扣钱、设余额或清零", "/eco <give|take|set|reset> <玩家名> <数额>"),
("enchant", "给手持物品附魔", "/enchant <附魔名> [等级]"),
("enderchest", "打开自己或他人的末影箱", "/enderchest [玩家名]"),
("essentials", "查看 Essentials 版本与加载状态", "/essentials"),
("exp", "查询、设置、给予经验", "/exp [reset|show|set|give] [玩家名] [数量]"),
("ext", "扑灭玩家身上的火", "/ext [玩家名]"),
("feed", "回满饱食度", "/feed [玩家名]"),
("fly", "开关飞行", "/fly [玩家名] [on|off]"),
("fireball", "发射指定类型的火球", "/fireball [类型] [速度]"),
("firework", "生成、发射或清除烟花", "/firework <参数|power|clear|fire> [数量]"),
("gamemode", "切换自己或他人的游戏模式", "/gamemode <survival|creative|adventure|spectator> [玩家名]"),
("gc", "查看内存、TPS、实体与在线时长", "/gc"),
("getpos", "显示坐标与朝向", "/getpos [玩家名]"),
("give", "给指定玩家物品", "/give <玩家名> <物品> [数量]"),
("god", "开关无敌", "/god [玩家名] [on|off]"),
("grindstone", "原地打开砂轮", "/grindstone"),
("hat", "把手持物品戴到头上", "/hat [remove]"),
("heal", "回满血量", "/heal [玩家名]"),
("help", "检索可用于你的指令帮助", "/help [关键词] [页码]"),
("helpop", "向在线管理员求助", "/helpop <内容>"),
("home", "传送到自己的家", "/home [玩家名:][家名]"),
("ice", "冻结或解冻玩家的移动", "/ice [玩家名]"),
("ignore", "屏蔽某玩家的消息", "/ignore <玩家名>"),
("info", "分章查看服务器信息", "/info [章节] [页码]"),
("invsee", "查看在线玩家的背包", "/invsee <玩家名>"),
("item", "给自己发物品", "/item <物品> [数量]"),
("itemdb", "查询物品 ID、数据值与耐久", "/itemdb <物品>"),
("itemlore", "改写手持物品的说明文字", "/itemlore <add|set|clear> [行号] [文本]"),
("itemname", "改写手持物品的显示名", "/itemname [新名字]"),
("jailedplayers", "列出所有在押玩家", "/jailedplayers"),
("jails", "列出所有监狱", "/jails"),
("jump", "传送到准星落点", "/jump"),
("kick", "踢出指定玩家", "/kick <玩家名> [原因]"),
("kickall", "踢出除自己外的所有人", "/kickall [原因]"),
("kill", "杀死指定玩家", "/kill <玩家名>"),
("kit", "领取礼包", "/kit [礼包名] [玩家名]"),
("kitreset", "重置礼包冷却", "/kitreset <礼包名> [玩家名]"),
("kittycannon", "发射一只爆炸猫（恶搞）", "/kittycannon"),
("lightning", "在目标处打一道雷", "/lightning [玩家名] [强度]"),
("list", "列出在线玩家或某权限组", "/list [群组]"),
("loom", "原地打开织布机", "/loom"),
("mail", "读写离线留言", "/mail [read|send|sendall|clear|sendtemp …]"),
("me", "以第三人称发一条动作", "/me <内容>"),
("more", "把手持物品补到满堆", "/more [数量]"),
("motd", "查看每日公告分章", "/motd [章节] [页码]"),
("msg", "私聊指定玩家", "/msg <玩家名> <内容>"),
("msgtoggle", "开关接收私聊", "/msgtoggle [玩家名] [on|off]"),
("mute", "禁言或解除禁言", "/mute <玩家名> [时长] [原因]"),
("near", "列出附近的玩家", "/near [玩家名] [半径]"),
("nick", "设置或清除昵称", "/nick [玩家名] <昵称|off>"),
("nuke", "引爆大范围炸弹（恶搞）", "/nuke [玩家名]"),
("tpoffline", "传送到离线玩家的下线点", "/tpoffline <玩家名>"),
("pay", "转账给其他玩家", "/pay <玩家名> <数额>"),
("paytoggle", "开关接收转账", "/paytoggle [玩家名] [on|off]"),
("payconfirmtoggle", "切换转账时的二次确认", "/payconfirmtoggle"),
("ping", "显示自己的当前延迟", "/ping"),
("playtime", "查看累计在线时长", "/playtime [玩家名]"),
("potion", "清除或施加药水效果", "/potion <clear|apply|effect:…> [玩家名]"),
("powertool", "给手持物品绑定一条指令", "/powertool <指令…>"),
("powertoollist", "列出已绑定的物品指令", "/powertoollist"),
("powertooltoggle", "开关物品指令绑定", "/powertooltoggle"),
("ptime", "单独设置玩家的客户端时间", "/ptime [list|reset|day|night|17:30] [玩家名|*]"),
("pweather", "单独设置玩家的客户端天气", "/pweather [list|reset|sun|storm] [玩家名|*]"),
("r", "回复上一条私聊", "/r <内容>"),
("rtoggle", "开关快速回复", "/rtoggle [玩家名] [on|off]"),
("realname", "由昵称反查真实玩家名", "/realname <昵称>"),
("recipe", "查询物品的合成配方", "/recipe <物品> [页码]"),
("remove", "按类型批量清除实体", "/remove <类型> [半径|世界]"),
("renamehome", "重命名一个家", "/renamehome <[玩家名:]家名> <新名>"),
("repair", "修满手持或全部装备耐久", "/repair [hand|all]"),
("rest", "让玩家躺下进入休息状态", "/rest [玩家名]"),
("rules", "分章查看服务器规则", "/rules [章节] [页码]"),
("seen", "查玩家最后在线时间", "/seen <玩家名>"),
("sell", "按回收价出售物品", "/sell <物品|hand|inventory|blocks> [数量]"),
("sethome", "把当前位置设为家", "/sethome [[玩家名:]家名]"),
("setjail", "把当前位置创建为监狱", "/setjail <监狱名>"),
("settpr", "设置随机传送的中心与范围", "/settpr [center|minrange|maxrange] [值]"),
("setwarp", "把当前位置设为地标", "/setwarp <地标名>"),
("setworth", "设定物品的回收单价", "/setworth [物品名] <单价>"),
("showkit", "预览礼包内容", "/showkit <礼包名>"),
("editsign", "改写准星告示牌的文字", "/editsign <set|clear|copy|paste> [行] [文本]"),
("skull", "获取指定玩家的头颅", "/skull [owner] [玩家名]"),
("smithingtable", "原地打开锻造台", "/smithingtable"),
("socialspy", "旁观全服私聊", "/socialspy [玩家名] [on|off]"),
("spawner", "把准星刷怪笼改成指定生物", "/spawner <生物> [延迟]"),
("spawnmob", "生成生物，可带坐骑", "/spawnmob <生物>[:数据] [数量]"),
("speed", "设置行走或飞行速度", "/speed [walk|fly] <速度> [玩家名]"),
("stonecutter", "原地打开切石机", "/stonecutter"),
("sudo", "以他人身份执行一条指令", "/sudo <玩家名> <指令>"),
("suicide", "让自己自杀", "/suicide"),
("tempban", "限时封禁玩家", "/tempban <玩家名> <时长> [原因]"),
("tempbanip", "限时封禁一个 IP", "/tempbanip <IP> <时长> [原因]"),
("thunder", "开关雷雨并设定时长", "/thunder <true|false> [时长]"),
("time", "设置或推进世界时间", "/time [set|add] <时间> [世界|all]"),
("togglejail", "把玩家押入或放出监狱", "/togglejail <玩家名> <监狱名> [时长]"),
("top", "传送到当前位置最高可站立点", "/top"),
("tp", "传送到玩家身边或把人传过去", "/tp <玩家名> [目标玩家]"),
("tpa", "请求传送到对方身边", "/tpa <玩家名>"),
("tpaall", "让全服玩家向你发起传送请求", "/tpaall <玩家名>"),
("tpaccept", "同意传送请求", "/tpaccept [玩家名|*]"),
("tpahere", "请求对方传送到你身边", "/tpahere <玩家名>"),
("tpall", "把所有在线玩家传送到你身边", "/tpall [玩家名]"),
("tpauto", "开关自动同意传送请求", "/tpauto [玩家名]"),
("tpacancel", "撤回自己发出的传送请求", "/tpacancel [玩家名]"),
("tpdeny", "拒绝传送请求", "/tpdeny [玩家名|*]"),
("tphere", "把指定玩家传送到你身边", "/tphere <玩家名>"),
("tpo", "绕过权限把玩家传过去", "/tpo <玩家名> [目标玩家]"),
("tpohere", "强制把玩家拉到你身边", "/tpohere <玩家名>"),
("tppos", "传送到精确坐标", "/tppos <x> <y> <z> [yaw] [pitch] [世界]"),
("tpr", "随机传送", "/tpr"),
("tptoggle", "开关接收传送请求", "/tptoggle [玩家名] [on|off]"),
("tree", "在准星处种一棵指定树", "/tree <树种>"),
("unban", "解除玩家封禁", "/unban <玩家名>"),
("unbanip", "解除 IP 封禁", "/unbanip <IP>"),
("unlimited", "设置物品无限或装备不减耐久", "/unlimited <list|item|clear> [玩家名]"),
("vanish", "隐身，对普通玩家不可见", "/vanish [玩家名] [on|off]"),
("warp", "传送到指定地标", "/warp <地标名> [玩家名]"),
("warpinfo", "查看地标的坐标与创建者", "/warpinfo <地标名>"),
("weather", "设置世界天气", "/weather <sun|storm> [时长]"),
("whois", "用昵称查玩家信息", "/whois <昵称>"),
("workbench", "原地打开工作台", "/workbench"),
("world", "传送到指定世界或查看世界列表", "/world [世界名]"),
("worth", "查询物品的回收价", "/worth <物品|hand|inventory> [-数量]"),
]

P = lambda n, r, note="": {"name": n, "required": r, **({"note": note} if note else {})}

EX = {
"afk": {"params": [P("玩家名或留言", False, "留空=只是暂离")], "examples": ["/afk", "/afk 吃饭去"]},
"back": {"params": [P("玩家名", False, "留空=自己")], "examples": ["/back"]},
"balance": {"params": [P("玩家名", False, "留空=自己")], "examples": ["/balance", "/balance 小明"]},
"balancetop": {"params": [P("页码", False)], "examples": ["/balancetop"]},
"ban": {"params": [P("玩家名", True), P("原因", False)], "examples": ["/ban 小明 使用外挂"]},
"tempban": {"params": [P("玩家名", True), P("时长", True, "如 7d"), P("原因", False)],
            "examples": ["/tempban 小明 7d 使用外挂"]},
"kick": {"params": [P("玩家名", True), P("原因", False)], "examples": ["/kick 小明 刷屏"]},
"mute": {"params": [P("玩家名", True), P("时长", False, "如 1h"), P("原因", False)],
         "examples": ["/mute 小明 1h 刷屏", "/mute 小明"]},
"togglejail": {"params": [P("玩家名", True), P("监狱名", True), P("时长", False, "留空=永久")],
               "examples": ["/togglejail 小明 监狱 1d", "/togglejail 小明 监狱"]},
"socialspy": {"params": [P("玩家名", False, "留空=自己"), P("on|off", False)],
              "examples": ["/socialspy", "/socialspy 小明 on"]},
"vanish": {"params": [P("玩家名", False, "留空=自己"), P("on|off", False)],
           "examples": ["/vanish", "/vanish 小明 off"]},
"msg": {"params": [P("玩家名", True), P("内容", True)], "examples": ["/msg 小明 来主城一趟"]},
"r": {"params": [P("内容", True)], "examples": ["/r 在路上，马上到"]},
"mail": {"params": [P("子命令", False, "send/read/clear/sendall"), P("对象", False), P("内容", False)],
         "examples": ["/mail send 小明 回来领钱", "/mail read"]},
"ignore": {"params": [P("玩家名", True)], "examples": ["/ignore 小明"]},
"seen": {"params": [P("玩家名", True)], "examples": ["/seen 小明"]},
"near": {"params": [P("玩家名", False), P("半径", False, "默认 200")], "examples": ["/near", "/near 小明 100"]},
"list": {"examples": ["/list"]},
"help": {"params": [P("关键词", False), P("页码", False)], "examples": ["/help 传送", "/help"]},
"pay": {"params": [P("玩家名", True, "收钱的一方"), P("数额", True, "正整数")],
        "examples": ["/pay 小明 500"]},
"eco": {"params": [P("子命令", True, "give/take/set/reset"), P("玩家名", True), P("数额", True)],
        "examples": ["/eco give 小明 1000", "/eco take 小明 500"]},
"kit": {"params": [P("礼包名", False), P("玩家名", False, "留空=自己")],
        "examples": ["/kit 新手", "/kit 新手 小明"]},
"createkit": {"params": [P("礼包名", True), P("冷却", True, "如 24h")], "examples": ["/createkit 新手 24h"]},
"give": {"params": [P("玩家名", True), P("物品", True, "ID 或英文名"), P("数量", False)],
         "examples": ["/give 小明 diamond 64"]},
"item": {"params": [P("物品", True), P("数量", False)], "examples": ["/item apple 16"]},
"enchant": {"params": [P("附魔名", True, "如 sharpness"), P("等级", False)],
            "examples": ["/enchant sharpness 5"]},
"exp": {"params": [P("子命令", False, "show/set/give/reset"), P("玩家名", False), P("数量", False)],
        "examples": ["/exp give 小明 30", "/exp show 小明"]},
"heal": {"params": [P("玩家名", False, "留空=自己")], "examples": ["/heal", "/heal 小明"]},
"feed": {"params": [P("玩家名", False, "留空=自己")], "examples": ["/feed 小明"]},
"fly": {"params": [P("玩家名", False), P("on|off", False)], "examples": ["/fly", "/fly 小明 off"]},
"god": {"params": [P("玩家名", False), P("on|off", False)], "examples": ["/god", "/god 小明 on"]},
"gamemode": {"params": [P("模式", True, "survival/gmc 等"), P("玩家名", False)],
             "examples": ["/gamemode creative", "/gmc 小明"]},
"tp": {"params": [P("玩家名", True, "要去的人"), P("目标玩家", False, "留空=自己过去")],
       "examples": ["/tp 小明", "/tp 小明 小红"]},
"tphere": {"params": [P("玩家名", True)], "examples": ["/tphere 小明"]},
"tpa": {"params": [P("玩家名", True)], "examples": ["/tpa 小明"]},
"tpahere": {"params": [P("玩家名", True)], "examples": ["/tpahere 小明"]},
"tpaccept": {"params": [P("玩家名", False, "留空=全部同意")], "examples": ["/tpaccept", "/tpaccept 小明"]},
"tpdeny": {"params": [P("玩家名", False, "留空=全部拒绝")], "examples": ["/tpdeny"]},
"tpacancel": {"examples": ["/tpacancel"]},
"tpall": {"examples": ["/tpall"]},
"tppos": {"params": [P("x", True), P("y", True), P("z", True), P("世界", False)],
          "examples": ["/tppos 100 64 -200", "/tppos 0 70 0 world_nether"]},
"home": {"params": [P("家名", False, "留空=默认家")], "examples": ["/home", "/home 矿场"]},
"sethome": {"params": [P("家名", False, "留空=sethome")], "examples": ["/sethome", "/sethome 矿场"]},
"delhome": {"params": [P("家名", True)], "examples": ["/delhome 矿场"]},
"warp": {"params": [P("地标名", True), P("玩家名", False, "留空=自己")],
         "examples": ["/warp 主城", "/warp 主城 小明"]},
"setwarp": {"params": [P("地标名", True)], "examples": ["/setwarp 主城"]},
"clearinventory": {"params": [P("玩家名", False), P("物品", False, "* 全部")],
                   "examples": ["/clearinventory 小明", "/ci 小明 diamond"]},
"invsee": {"params": [P("玩家名", True)], "examples": ["/invsee 小明"]},
"enderchest": {"params": [P("玩家名", False)], "examples": ["/enderchest 小明"]},
"repair": {"params": [P("hand|all", False, "留空=手持")], "examples": ["/repair hand", "/repair all"]},
"hat": {"examples": ["/hat", "/hat remove"]},
"workbench": {"examples": ["/workbench"]},
"lightning": {"params": [P("玩家名", False), P("强度", False)], "examples": ["/lightning 小明"]},
"time": {"params": [P("子命令", False, "set/add"), P("时间", True, "day/12000"), P("世界", False, "all=全部")],
         "examples": ["/time set day", "/time set night world"]},
"weather": {"params": [P("sun|storm", True), P("时长", False, "秒")],
            "examples": ["/weather sun", "/weather storm 600"]},
"gc": {"notes": "别名 /tps、/lag、/mem、/uptime 都能看 TPS 与内存", "examples": ["/gc"]},
"essentials": {"notes": "/ess reload 只重载 Essentials 自身配置，不影响其它插件", "examples": ["/essentials"]},
"worth": {"params": [P("物品", True)], "examples": ["/worth diamond"]},
"speed": {"params": [P("walk|fly", False), P("速度", True, "0.2 左右为原速")],
          "examples": ["/speed 2", "/speed fly 1 小明"]},
"ptime": {"examples": ["/ptime night", "/ptime reset 小明"]},
"pweather": {"examples": ["/pweather sun"]},
"spawnmob": {"params": [P("生物", True), P("数量", False)], "examples": ["/spawnmob zombie 3"]},
}


def build():
    cmds = []
    for cmd, what, syn in C:
        d = {"cmd": cmd, "what": what, "syntax": syn}
        extra = EX.get(cmd)
        if extra:
            if extra.get("params"):
                d["params"] = extra["params"]
            if extra.get("examples"):
                d["examples"] = extra["examples"]
            if extra.get("notes"):
                d["notes"] = extra["notes"]
        cmds.append(d)
    return {
        "name": NAME, "role": ROLE, "summary": SUMMARY,
        "whatFor": WHATFOR,
        "quick": [{"scene": a, "cmd": b, "note": c} for a, b, c in QUICK],
        "commands": cmds,
        "caution": CAUTION,
    }


def j(o):
    return json.dumps(o, ensure_ascii=False, separators=(",", ":"))


def dump(note):
    out = ["{"]
    out.append('  "name": %s,' % j(note["name"]))
    out.append('  "role": %s,' % j(note["role"]))
    out.append('  "summary": %s,' % j(note["summary"]))
    out.append('  "whatFor": [')
    wf = note["whatFor"]
    for i, x in enumerate(wf):
        out.append('    %s%s' % (j(x), "," if i < len(wf) - 1 else ""))
    out.append('  ],')
    out.append('  "quick": [')
    for i, q in enumerate(note["quick"]):
        out.append('    %s%s' % (j(q), "," if i < len(note["quick"]) - 1 else ""))
    out.append('  ],')
    out.append('  "commands": [')
    n = len(note["commands"])
    for i, c in enumerate(note["commands"]):
        out.append('    %s%s' % (j(c), "," if i < n - 1 else ""))
    out.append('  ],')
    out.append('  "caution": [')
    for i, x in enumerate(note["caution"]):
        out.append('    %s%s' % (j(x), "," if i < len(note["caution"]) - 1 else ""))
    out.append('  ]')
    out.append('}')
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    note = build()
    txt = dump(note)
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "notes", "essentials.json")
    with io.open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(txt)
    b = len(txt.encode("utf-8"))
    w = sum(1 for c in note["commands"] if c.get("what"))
    ex = sum(1 for c in note["commands"] if c.get("examples"))
    pa = sum(1 for c in note["commands"] if c.get("params"))
    print("bytes=%d commands=%d what=%d examples=%d params=%d" % (b, len(note["commands"]), w, ex, pa))
