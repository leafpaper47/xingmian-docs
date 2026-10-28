# -*- coding: utf-8 -*-
"""最终版：生成 data/notes/essentials.json，并自动收敛到 18KB 以内。"""
import importlib.util, json, io, os

HERE = os.path.dirname(os.path.abspath(__file__))
LIMIT = 18432

spec = importlib.util.spec_from_file_location("b2", os.path.join(HERE, "_b2.py"))
b2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b2)          # 先生成 4 空格版本，稍后覆盖
m = b2.m

SYN = {
"mail": "/mail [send|read|clear] [对象] [内容]",
"settpr": "/settpr <center|minrange|maxrange> [值]",
"tppos": "/tppos <x> <y> <z> [世界]",
"exp": "/exp <show|give|set> [玩家名] [数量]",
"editsign": "/editsign <set|clear|copy|paste> [文本]",
"ptime": "/ptime [day|night|reset] [玩家名]",
"unlimited": "/unlimited <list|item|clear>",
"pweather": "/pweather [sun|storm|reset] [玩家名]",
"potion": "/potion <clear|apply|effect:名>",
"clearinventory": "/clearinventory [玩家名] [物品]",
}
WHAT = {
"essentials": "查看插件版本与加载状态",
"customtext": "输出 bukkit.yml 定义的自定义文本",
"gc": "查看内存、TPS 与实体数",
"antioch": "在脚下引爆一片 TNT",
"afk": "标记自己为暂离并自动回复",
"itemdb": "查询物品 ID 与耐久",
"clearinventoryconfirmtoggle": "切换清空背包的二次确认",
"beezooka": "向准星射出一只爆炸蜜蜂",
"kittycannon": "发射一只爆炸猫",
"nuke": "引爆大范围炸弹",
"tpaall": "让全服玩家向你发传送请求",
}

# 高频指令例子里要留两条的
TWO_EX = {"tp": 2, "eco": 2, "pay": 1, "home": 2, "kit": 2, "give": 1, "msg": 1,
          "mute": 2, "clearinventory": 1, "sethome": 2, "warp": 2, "time": 2}

# 追加示例（用户点名的高频项）
ADD_EX = {
"ignore": ["/ignore 小明"],
"feed": ["/feed 小明"],
"workbench": ["/workbench"],
"hat": ["/hat"],
"enderchest": ["/enderchest 小明"],
"list": ["/list"],
}

m.C = [(c, WHAT.get(c, w), SYN.get(c, s)) for c, w, s in m.C]
note = m.build()

KEEP_PARAMS = {"tp", "pay", "eco", "give", "mute", "togglejail", "mail", "kit",
               "gamemode", "warp", "time", "clearinventory", "tempban", "exp"}
for c in note["commands"]:
    if c["cmd"] not in KEEP_PARAMS:
        c.pop("params", None)
    # 无参数指令的 syntax 与 cmd 完全重复，交给 gen_docs 从 plugin.yml 推导（页面显示一致）
    if c.get("syntax") == "/" + c["cmd"]:
        c.pop("syntax", None)
    if c["cmd"] in ADD_EX:
        c["examples"] = ADD_EX[c["cmd"]]
    if c.get("examples") and c["cmd"] in TWO_EX:
        c["examples"] = c["examples"][:TWO_EX[c["cmd"]]]
    elif c.get("examples"):
        c["examples"] = c["examples"][:1]

m.SUMMARY = ("星冕服务器的基础指令插件：传送、家与地标、经济（自带 eco 给钱）、封禁禁言、"
             "物品与背包、状态查询都由它承接，权限用 LuckPerms 按 essentials.xxx 分发。")
m.WHATFOR = ["新手福利：地标、家、礼包、随机传送",
             "日常管人：封禁、禁言、监狱",
             "配经济：给钱扣钱、定回收价"]
m.QUICK = [
    ("传送到玩家身边", "/tp 玩家名", "自己过去"),
    ("拉人过来", "/tphere 玩家名", "反向传送"),
    ("回家与设家", "/sethome 家名 → /home 家名", "可替人设"),
    ("去地标", "/warp 主城", "先 /setwarp 主城"),
    ("给钱扣钱", "/eco give 玩家名 1000", "走 Vault 共享"),
    ("给物品", "/give 玩家名 diamond 64", "给自己用 /item"),
    ("切游戏模式", "/gamemode creative 玩家名", "简写 /gmc"),
    ("禁言与踢人", "/mute 玩家名 1h 刷屏", "封人用 /ban"),
]
m.CAUTION = [
    "/ess reload 只重载 Essentials 自己的配置，不动别的插件；Bukkit 的 /reload 重载全部插件，"
    "容易内存泄漏和重复注册任务，线上优先 /ess reload，动到别的插件就老实重启。",
    "Essentials 自带经济要装了 Vault 才会被商店、点券、任务类插件读到。服务器已有别的经济插件时只留一个来源，"
    "否则余额对不上、排行榜会乱。",
    "/give 和 /eco 的数额写错（多打一个 0）不能撤销。批量发放先拿小号试一条，大动作前先 /backup。",
]
note.update({"summary": m.SUMMARY, "whatFor": m.WHATFOR, "quick": [
    {"scene": a, "cmd": b, "note": c} for a, b, c in m.QUICK], "caution": m.CAUTION})


def j(o):
    return json.dumps(o, ensure_ascii=False, separators=(",", ":"))


def dump(n):
    out = ["{"]
    out.append('  "name": %s,' % j(n["name"]))
    out.append('  "role": %s,' % j(n["role"]))
    out.append('  "summary": %s,' % j(n["summary"]))
    out.append('  "whatFor": [')
    for i, x in enumerate(n["whatFor"]):
        out.append('    %s%s' % (j(x), "," if i < len(n["whatFor"]) - 1 else ""))
    out.append('  ],')
    out.append('  "quick": [')
    for i, q in enumerate(n["quick"]):
        out.append('    %s%s' % (j(q), "," if i < len(n["quick"]) - 1 else ""))
    out.append('  ],')
    out.append('  "commands": [')
    k = len(n["commands"])
    for i, c in enumerate(n["commands"]):
        out.append(' %s%s' % (j(c), "," if i < k - 1 else ""))
    out.append('  ],')
    out.append('  "caution": [')
    for i, x in enumerate(n["caution"]):
        out.append('    %s%s' % (j(x), "," if i < len(n["caution"]) - 1 else ""))
    out.append('  ]')
    out.append('}')
    return "\n".join(out) + "\n"


txt = dump(note)
# 自动收敛：优先砍低价值示例，再砍参数说明
TRIM_ORDER = ["worth", "tpoffline", "tpall", "tppos", "tpaaccept", "enderchest", "list",
              "near", "lightning", "help", "seen", "workbench", "hat", "ignore", "feed",
              "afk", "socialspy", "repair", "vanish", "item", "enchant", "exp", "invsee"]
dropped = []
while len(txt.encode("utf-8")) > LIMIT:
    done = False
    for name in TRIM_ORDER:
        for c in note["commands"]:
            if c["cmd"] == name and c.get("examples"):
                c.pop("examples")
                dropped.append(name)
                done = True
                break
        if done:
            break
    if not done:
        for c in note["commands"]:
            if c.get("params"):
                ps = [p for p in c["params"] if p.get("note")]
                if ps:
                    ps[-1].pop("note", None)
                    done = True
                    break
    if not done:
        for c in note["commands"]:
            if c.get("params"):
                c["params"] = c["params"][:-1]
                if not c["params"]:
                    c.pop("params")
                done = True
                break
    if not done:
        break
    txt = dump(note)

with io.open(os.path.join(HERE, "data", "notes", "essentials.json"), "w", encoding="utf-8", newline="\n") as f:
    f.write(txt)
print("bytes=%d commands=%d what=%d examples=%d params=%d dropped=%s"
      % (len(txt.encode("utf-8")), len(note["commands"]),
         sum(1 for c in note["commands"] if c.get("what")),
         sum(len(c.get("examples") or []) for c in note["commands"]),
         sum(len(c.get("params") or []) for c in note["commands"]), ",".join(dropped) or "-"))
