# -*- coding: utf-8 -*-
"""最终收敛：按体积预算裁 params/examples、压缩缩进，写回 data/notes/essentials.json。"""
import importlib.util, json, io, os

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("b2", os.path.join(HERE, "_b2.py"))
b2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b2)   # 会先生成 4 空格版本，稍后覆盖
m = b2.m                     # _build_ess 模块本体

note = m.build()

# 只给「光看 syntax 猜不出含义」的高频指令保留 params
KEEP_PARAMS = {"tp", "pay", "eco", "give", "mute", "togglejail", "mail", "kit",
               "gamemode", "warp", "time", "clearinventory", "tempban", "exp"}
KEEP_EX = {"tp", "tphere", "tpa", "tpaccept", "back", "tppos", "tpoffline", "tpall",
           "home", "sethome", "warp", "setwarp", "delhome",
           "pay", "balance", "balancetop", "eco", "worth",
           "give", "item", "enchant", "exp", "kit", "invsee", "clearinventory", "repair",
           "heal", "fly", "god", "gamemode", "vanish", "lightning",
           "msg", "r", "mail", "socialspy", "afk", "seen", "near",
           "ban", "tempban", "kick", "mute", "togglejail",
           "time", "weather", "gc", "essentials", "help"}
TWO_EX = {"tp", "eco", "give", "home", "sethome", "warp", "kit", "fly", "god",
          "gamemode", "clearinventory", "mute", "time", "afk", "repair", "msg", "exp", "mail"}

FIX_EX = {
"clearinventory": ["/clearinventory 小明", "/clearinventory 小明 diamond"],
"item": ["/item apple 16"],
}

for c in note["commands"]:
    if c["cmd"] not in KEEP_PARAMS:
        c.pop("params", None)
    if c["cmd"] not in KEEP_EX:
        c.pop("examples", None)
    elif c.get("examples"):
        c["examples"] = FIX_EX.get(c["cmd"]) or (c["examples"] if c["cmd"] in TWO_EX else c["examples"][:1])


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
        out.append('  %s%s' % (j(c), "," if i < k - 1 else ""))
    out.append('  ],')
    out.append('  "caution": [')
    for i, x in enumerate(n["caution"]):
        out.append('    %s%s' % (j(x), "," if i < len(n["caution"]) - 1 else ""))
    out.append('  ]')
    out.append('}')
    return "\n".join(out) + "\n"


txt = dump(note)
with io.open(os.path.join(HERE, "data", "notes", "essentials.json"), "w", encoding="utf-8", newline="\n") as f:
    f.write(txt)
print("bytes=%d commands=%d what=%d examples=%d params=%d"
      % (len(txt.encode("utf-8")), len(note["commands"]),
         sum(1 for c in note["commands"] if c.get("what")),
         sum(len(c.get("examples") or []) for c in note["commands"]),
         sum(len(c.get("params") or []) for c in note["commands"])))
