# -*- coding: utf-8 -*-
"""在 _build_ess.py 基础上做体积收敛：精简 syntax、params、examples 与 quick 标注。"""
import importlib.util, json, io, os

spec = importlib.util.spec_from_file_location("b", os.path.join(os.path.dirname(os.path.abspath(__file__)), "_build_ess.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

SYN = {
"clearinventory": "/clearinventory [玩家名] [物品] [数量]",
"editsign": "/editsign <set|clear|copy|paste> [文本]",
"exp": "/exp <show|set|give|reset> [玩家名] [数量]",
"firework": "/firework <power|clear|fire> [数量]",
"gamemode": "/gamemode <模式> [玩家名]",
"itemlore": "/itemlore <add|set|clear> [文本]",
"mail": "/mail [read|send|clear|sendall] [对象] [内容]",
"potion": "/potion <clear|apply|effect:名>",
"powertool": "/powertool <指令>",
"ptime": "/ptime [reset|day|night|17:30] [玩家名]",
"pweather": "/pweather [reset|sun|storm] [玩家名]",
"remove": "/remove <类型> [半径]",
"settpr": "/settpr <center|minrange|maxrange> [值]",
"spawnmob": "/spawnmob <生物> [数量]",
"time": "/time <set|add> <时间> [世界|all]",
"unlimited": "/unlimited <list|item|clear> [玩家名]",
"thunder": "/thunder <true|false> [时长]",
"customtext": "bukkit.yml 自定义别名",
"world": "/world [世界名]",
}

WHAT = {
"firework": "生成、发射或清除烟花",
"clearinventory": "清空背包，可指定物品与数量",
"essentials": "查看 Essentials 版本与状态",
"gc": "查看内存、TPS、实体与在线时长",
"world": "传送到指定世界或查看列表",
"gamemode": "切换游戏模式",
"unlimited": "设置无限物品或不掉耐久",
"settpr": "设置随机传送中心与范围",
"spawnmob": "生成生物，可带坐骑",
"spawner": "把准星刷怪笼改成指定生物",
"spawnmob ": "",
}

def P(n, r=False, note=""):
    d = {"name": n}
    if r:
        d["required"] = True
    if note:
        d["note"] = note
    return d


EX = {
# —— 传送 ——
"tp":     {"params": [P("玩家名", True, "要去的人"), P("目标玩家", False, "留空=自己过去")],
           "examples": ["/tp 小明", "/tp 小明 小红"]},
"tphere": {"params": [P("玩家名", True)], "examples": ["/tphere 小明"]},
"tpa":    {"params": [P("玩家名", True)], "examples": ["/tpa 小明"]},
"tpaccept": {"params": [P("玩家名", False, "留空=全部同意")], "examples": ["/tpaccept", "/tpaccept 小明"]},
"back":   {"examples": ["/back"]},
"tppos":  {"params": [P("x", True), P("y", True), P("z", True), P("世界", False)],
           "examples": ["/tppos 100 64 -200"]},
"tpoffline": {"examples": ["/tpoffline 小明"]},
"tpall":  {"examples": ["/tpall"]},
# —— 家与地标 ——
"home":   {"examples": ["/home", "/home 矿场"]},
"sethome": {"examples": ["/sethome", "/sethome 矿场"]},
"delhome": {"examples": ["/delhome 矿场"]},
"warp":   {"params": [P("地标名", True), P("玩家名", False, "留空=自己")],
           "examples": ["/warp 主城", "/warp 主城 小明"]},
"setwarp": {"params": [P("地标名", True)], "examples": ["/setwarp 主城"]},
# —— 经济 ——
"pay":    {"params": [P("玩家名", True, "收钱的人"), P("数额", True, "正整数")],
           "examples": ["/pay 小明 500"]},
"balance": {"examples": ["/balance", "/balance 小明"]},
"balancetop": {"examples": ["/balancetop"]},
"eco":    {"params": [P("子命令", True, "give/take/set/reset"), P("玩家名", True), P("数额", True)],
           "examples": ["/eco give 小明 1000", "/eco take 小明 500"]},
"worth":  {"params": [P("物品", True)], "examples": ["/worth diamond"]},
# —— 物品与经验 ——
"give":   {"params": [P("玩家名", True), P("物品", True, "ID 或英文名"), P("数量", False)],
           "examples": ["/give 小明 diamond 64"]},
"item":   {"params": [P("物品", True), P("数量", False)], "examples": ["/item apple 16"]},
"enchant": {"params": [P("附魔名", True, "如 sharpness"), P("等级", False)],
            "examples": ["/enchant sharpness 5"]},
"exp":    {"params": [P("子命令", False, "show/give/set"), P("玩家名", False), P("数量", False)],
           "examples": ["/exp give 小明 30", "/exp show 小明"]},
"kit":    {"params": [P("礼包名", False), P("玩家名", False, "留空=自己")],
           "examples": ["/kit 新手", "/kit 新手 小明"]},
"invsee": {"params": [P("玩家名", True)], "examples": ["/invsee 小明"]},
"enderchest": {"examples": ["/enderchest 小明"]},
"clearinventory": {"params": [P("玩家名", False), P("物品", False, "* = 全部")],
                   "examples": ["/clearinventory 小明", "/ci 小明 diamond"]},
"repair": {"examples": ["/repair hand", "/repair all"]},
"more":   {"examples": ["/more"]},
# —— 状态 ——
"heal":   {"examples": ["/heal 小明"]},
"feed":   {"examples": ["/feed 小明"]},
"fly":    {"params": [P("玩家名", False), P("on|off", False)], "examples": ["/fly", "/fly 小明 off"]},
"god":    {"params": [P("玩家名", False), P("on|off", False)], "examples": ["/god", "/god 小明 on"]},
"gamemode": {"params": [P("模式", True, "survival/gmc 等"), P("玩家名", False)],
             "examples": ["/gamemode creative", "/gmc 小明"]},
"vanish": {"params": [P("玩家名", False), P("on|off", False)], "examples": ["/vanish"]},
"lightning": {"params": [P("玩家名", False), P("强度", False)], "examples": ["/lightning 小明"]},
# —— 聊天与社交 ——
"msg":    {"params": [P("玩家名", True), P("内容", True)], "examples": ["/msg 小明 来主城一趟"]},
"r":      {"params": [P("内容", True)], "examples": ["/r 在路上，马上到"]},
"mail":   {"params": [P("子命令", False, "send/read/sendall"), P("对象", False), P("内容", False)],
           "examples": ["/mail send 小明 回来领钱", "/mail read"]},
"socialspy": {"params": [P("玩家名", False), P("on|off", False)],
              "examples": ["/socialspy", "/socialspy 小明 on"]},
"ignore": {"examples": ["/ignore 小明"]},
"afk":    {"examples": ["/afk", "/afk 吃饭去"]},
"seen":   {"params": [P("玩家名", True)], "examples": ["/seen 小明"]},
"near":   {"examples": ["/near 小明 100"]},
# —— 管理处罚 ——
"ban":    {"params": [P("玩家名", True), P("原因", False)], "examples": ["/ban 小明 使用外挂"]},
"tempban": {"params": [P("玩家名", True), P("时长", True, "如 7d"), P("原因", False)],
            "examples": ["/tempban 小明 7d 使用外挂"]},
"kick":   {"params": [P("玩家名", True), P("原因", False)], "examples": ["/kick 小明 刷屏"]},
"mute":   {"params": [P("玩家名", True), P("时长", False, "如 1h"), P("原因", False)],
           "examples": ["/mute 小明 1h 刷屏", "/mute 小明"]},
"togglejail": {"params": [P("玩家名", True), P("监狱名", True), P("时长", False, "留空=永久")],
               "examples": ["/togglejail 小明 监狱 1d"]},
"unban":  {"examples": ["/unban 小明"]},
# —— 运维 ——
"time":   {"params": [P("子命令", False, "set/add"), P("时间", True, "day/12000"), P("世界", False, "all=全部")],
           "examples": ["/time set day", "/time set night world"]},
"weather": {"params": [P("sun|storm", True), P("时长", False, "秒")],
            "examples": ["/weather sun", "/weather storm 600"]},
"gc":     {"notes": "别名 /tps、/lag、/mem 也能看 TPS 与内存", "examples": ["/gc"]},
"essentials": {"notes": "/ess reload 只重载 Essentials 自身配置，不动其它插件", "examples": ["/essentials"]},
"help":   {"examples": ["/help 传送", "/help"]},
"list":   {"examples": ["/list"]},
"workbench": {"examples": ["/workbench"]},
"hat":    {"examples": ["/hat"]},
"speed":  {"params": [P("walk|fly", False), P("速度", True, "0.2 为原速")],
           "examples": ["/speed 2"]},
}

m.EX = EX
m.C = [(c, WHAT.get(c, w), SYN.get(c, s)) for c, w, s in m.C]
m.WHATFOR = [
    "新手福利：地标、家、礼包、随机传送",
    "日常管人：封禁、限时封禁、禁言、监狱",
    "配经济：给钱扣钱、定回收价、财富排行",
]
m.QUICK = [
    ("传送到玩家身边", "/tp 玩家名", "自己过去"),
    ("拉人过来", "/tphere 玩家名", "反向传送"),
    ("回家与设家", "/sethome 家名 → /home 家名", "可加玩家名替人设"),
    ("传送到地标", "/warp 主城", "先 /setwarp 主城"),
    ("给钱扣钱", "/eco give 玩家名 1000", "余额由 Vault 共享"),
    ("给物品", "/give 玩家名 diamond 64", "只给自己用 /item"),
    ("切游戏模式", "/gamemode creative 玩家名", "简写 /gmc /gms"),
    ("禁言与踢人", "/mute 玩家名 1h 刷屏", "封人用 /ban /tempban"),
]

note = m.build()
txt = m.dump(note)
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "notes", "essentials.json")
with io.open(p, "w", encoding="utf-8", newline="\n") as f:
    f.write(txt)
print("bytes=%d commands=%d examples=%d params=%d"
      % (len(txt.encode("utf-8")), len(note["commands"]),
         sum(len(c.get("examples") or []) for c in note["commands"]),
         sum(len(c.get("params") or []) for c in note["commands"])))
