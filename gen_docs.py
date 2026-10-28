# -*- coding: utf-8 -*-
"""根据服务器插件 jar 中 plugin.yml 的解析结果（wcdoc/data/plugin_commands.json）
+ 人工注解库（wcdoc/data/notes/*.json）
生成 VuePress + theme-plume 的管理员指令文档站内容。

页面结构：
  /                    指令总览（站点入口，不再有「首页」）
  /commands/<cat>/     分类索引
  /commands/<cat>/<slug>.md   单插件页（有注解 → 完整版；无注解 → plugin.yml 极简版）
"""
import json, os, re, hashlib

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data", "plugin_commands.json")
NOTES = os.path.join(ROOT, "data", "notes")
SITE = os.path.join(ROOT, "site")
DOCS = os.path.join(SITE, "docs")
TODAY = "2026/10/24"

# ---------------- 分类定义 ----------------
CATS = [
    ("core", "基础与权限", "🛡️", "权限、插件加载、维护模式、Vault 经济桥等服务器底座。"),
    ("essentials", "基础工具", "🧰", "Essentials 系与各类物品/背包/生存辅助工具。"),
    ("teleport", "传送与出生点", "🌀", "随机传送、出生点、回家相关。"),
    ("world", "世界与地图", "🗺️", "地图渲染、坐标同步、天气与天象、镜像世界。"),
    ("protect", "领地与保护", "🔒", "领地、容器锁、WorldGuard 图形界面。"),
    ("economy", "经济与商店", "🪙", "点券、商店、玩家交易、赞助充值。"),
    ("rpg", "战斗与 RPG", "⚔️", "MythicMobs 系、附魔、Boss、属性、自定义战斗。"),
    ("entity", "生物与展示", "🧟", "伪装、模型、NPC、实体编辑。"),
    ("chat", "聊天与社交", "💬", "聊天格式、公告、邮件、称号、语音、计分板。"),
    ("config", "脚本与菜单", "🧩", "Skript、DeluxeMenus、PlaceholderAPI 等二次开发底座。"),
    ("audit", "记录与性能", "📊", "方块回滚、性能采样、审计。"),
    ("minigame", "小游戏与娱乐", "🎲", "服务器自研玩法与休闲小游戏。"),
    ("other", "其他", "📦", "未归类的插件。"),
]
CAT_ORDER = [c[0] for c in CATS]
CAT_META = {c[0]: {"title": c[1], "icon": c[2], "desc": c[3]} for c in CATS}

ASSIGN = {
    "AfDianPay": "economy", "Ah-Toy-1.0": "minigame", "Ah-WolfmanKill-1.0": "minigame",
    "ALCERecipeViewer": "essentials", "allmusic": "minigame", "ArchitectPlugin": "other",
    "ArmoredElytra": "essentials", "ArmorUnbreaking": "essentials", "ArtMap": "world",
    "BetterRTP": "teleport", "BlockLocker": "protect", "BookEdit": "essentials",
    "BossBarHealth": "entity", "BroadcastPlusPlus": "chat", "CMILib": "essentials",
    "ConsoleSpamFixReborn": "core", "CoreProtect": "audit", "CraftBench": "essentials",
    "DeluxeMenus": "config", "DummyPool": "economy", "EcoEnchants": "rpg",
    "EditableStands": "entity", "EliteMobs": "rpg", "EnchantInfuser": "rpg",
    "Essentials": "essentials", "EssentialsSpawn": "teleport", "FancyNpcsGUI": "entity",
    "FoMiningComp": "rpg", "GSit": "minigame", "InBlock": "essentials",
    "InfiniteFuel": "essentials", "InvSaver": "essentials", "ItemEdit": "essentials",
    "KaleidoscopeCookeryPlugin": "config", "KaoguGuide": "rpg", "KaoguPlugin": "rpg",
    "LeafChat": "chat", "LeafHat": "essentials", "LeashPlayers": "minigame",
    "LibsDisguises": "entity", "LobbyGames": "minigame", "LuckPerms": "core",
    "MagicPointsLog": "economy", "MahjongPlay": "minigame", "MaintenanceMode": "core",
    "MeteorShowers": "world", "Mirrora": "world", "ModelEngine": "entity",
    "MythicMobs": "rpg", "MythicTools": "rpg", "OpenInv": "essentials",
    "PlaceholderAPI": "config", "PlayerSignIn": "essentials", "PlayerTask": "essentials",
    "PlayerTitle": "chat", "PlugManX": "core", "PVPPlugin": "rpg", "Residence": "protect",
    "SenluoBuyer": "economy", "Shopkeepers": "economy", "Skript": "config", "spark": "audit",
    "StarAFK": "essentials", "StarPact": "rpg", "SweetMail": "chat", "TAB": "chat",
    "TownPlugin": "protect", "Vault": "core", "vcm": "chat", "voicechat": "chat",
    "WeatherCard": "world", "WebBridge": "core", "WineSuite": "economy",
    "WorldGuardGUI": "protect", "XaeroTracker": "world", "XingmianElement": "rpg",
    "XingmianQuiz": "minigame", "XingmianRPG": "rpg", "YaoqingPlugin": "chat",
    "YiyunCEskin": "entity",
}

# 侧边栏 / 标题用的功能简称
FUNC_CN = {
    "ALCERecipeViewer": "配方查询", "AfDianPay": "爱发电支付", "Ah-Toy-1.0": "小玩具",
    "Ah-WolfmanKill-1.0": "狼人杀", "ArchitectPlugin": "建筑师认证", "ArmorUnbreaking": "盔甲免损耗",
    "ArmoredElytra": "装甲鞘翅", "ArtMap": "像素画板", "BetterRTP": "随机传送",
    "BlockLocker": "告示牌锁", "BookEdit": "成书编辑", "BossBarHealth": "BOSS血条",
    "BroadcastPlusPlus": "公告广播", "CMILib": "CMI前置库", "ConsoleSpamFixReborn": "控制台屏蔽",
    "CoreProtect": "日志回滚", "CraftBench": "随身工作台", "DeluxeMenus": "GUI菜单",
    "DummyPool": "台球", "EcoEnchants": "自定义附魔", "EditableStands": "盔甲架编辑",
    "EliteMobs": "精英怪物", "EnchantInfuser": "附魔注入", "Essentials": "基础指令",
    "EssentialsSpawn": "出生点", "FancyNpcsGUI": "图形化NPC", "FoMiningComp": "挖矿竞赛",
    "GSit": "坐下趴下", "InBlock": "指令方块", "InfiniteFuel": "无限燃料",
    "InvSaver": "背包快照", "ItemEdit": "物品编辑", "KaleidoscopeCookeryPlugin": "森罗厨房",
    "KaoguGuide": "考古图鉴", "KaoguPlugin": "考古系统", "LeafChat": "聊天管理",
    "LeafHat": "头顶帽子", "LeashPlayers": "玩家拴绳", "LibsDisguises": "伪装",
    "LobbyGames": "大厅小游戏", "LuckPerms": "权限组", "MagicPointsLog": "点券流水",
    "MahjongPlay": "麻将", "MaintenanceMode": "维护模式", "MeteorShowers": "流星雨",
    "Mirrora": "镜像方块", "ModelEngine": "模型引擎", "MythicMobs": "自定义怪物",
    "MythicTools": "神话工具包", "OpenInv": "远程背包", "PlaceholderAPI": "变量占位符",
    "PlayerSignIn": "每日签到", "PlayerTask": "玩家任务", "PlayerTitle": "称号",
    "PlugManX": "插件管理", "PVPPlugin": "决斗排位", "Residence": "领地",
    "SenluoBuyer": "菜品收购", "Shopkeepers": "商店NPC", "Skript": "脚本引擎",
    "spark": "性能分析", "StarAFK": "挂机检测", "StarPact": "星契",
    "SweetMail": "邮件", "TAB": "列表计分板", "TownPlugin": "城镇",
    "Vault": "经济前置", "vcm": "语音喇叭", "voicechat": "语音聊天",
    "WeatherCard": "天气卡", "WebBridge": "网页桥接", "WineSuite": "酿酒图鉴",
    "WorldGuardGUI": "区域管理", "XaeroTracker": "小地图追踪", "XingmianElement": "元素系统",
    "XingmianQuiz": "知识问答", "XingmianRPG": "星陨RPG", "YaoqingPlugin": "玩家邀请",
    "YiyunCEskin": "云皮肤", "allmusic": "全服音乐",
}

COLOR = re.compile(r"[§&](?![a-zA-Z]+;)[0-9a-fk-orxA-FK-ORX]")


def decolor(s):
    """只去颜色码、不转义（用于把人工注解读进来后再统一转义一次）"""
    if s is None:
        return ""
    s = COLOR.sub("", str(s)).replace("\r", "")
    s = s.replace("|", "\uff5c")  # 全角竖线：笔记里的 <true|false> 之类在表格里不必转义
    return s.strip()


def clean(s):
    """去颜色码 + HTML/模板转义（页面会被当作 Vue 模板编译，裸 < > {{ }} 会导致构建失败）"""
    if s is None:
        return ""
    s = str(s)
    s = COLOR.sub("", s)
    s = s.replace("\r", "")
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = s.replace("{{", "&#123;&#123;").replace("}}", "&#125;&#125;")
    return s.strip()


def slug(name):
    s = name.lower()
    s = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", s).strip("-")
    return s or hashlib.md5(name.encode()).hexdigest()[:8]


CODE_SPAN = re.compile(r"`[^`\n]*`")


def txt(s):
    """正文段落转义：注解里的裸 < > 会被 Vue 当标签解析导致构建失败（如 <newline>）"""
    if s is None:
        return ""
    s = str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return s.replace("{{", "&#123;&#123;").replace("}}", "&#125;&#125;")


def fix_code_spans(text):
    """反引号代码段里不该预先 HTML 转义：markdown-it 会自己转义，预先转义会显示成 &lt;x&gt;"""
    def _one(m):
        t = m.group(0)
        return t.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    return CODE_SPAN.sub(_one, text)


def cell(s):
    """表格单元格转义"""
    s = clean(s).replace("|", "\\|").replace("\n", "<br>")
    return s if s else "—"


# 英文说明的中文对照表（由 translate_ui.py 生成，可人工修订后重跑生成器）
ZH_CACHE = {}
_ZH_FILE = os.path.join(os.path.dirname(DATA), "zh_cache.json")
if os.path.isfile(_ZH_FILE):
    with open(_ZH_FILE, encoding="utf-8") as _f:
        ZH_CACHE = json.load(_f)


def zh(s):
    """英文说明查表翻成中文，没命中就原样返回"""
    if not s:
        return ""
    s = str(s).strip()
    return ZH_CACHE.get(s, s)


# 补充表：data/notes/*.json 没覆盖到的指令，用它补 what/syntax/examples/notes
AUTO = {}
_AUTO_FILE = os.path.join(os.path.dirname(DATA), "auto_usage.json")
if os.path.isfile(_AUTO_FILE):
    with open(_AUTO_FILE, encoding="utf-8") as _f:
        AUTO = {k: v for k, v in json.load(_f).items() if not k.startswith("_")}

# 参数占位符 → 样例值（用于自动生成「示例」）
SAMPLE = [
    ("player", "Steve"), ("玩家", "Steve"), ("name", "Steve"), ("uuid", "069a79f4-44e9-4726-a5be-fca90e38aaf5"),
    ("material", "diamond"), ("item", "diamond_sword"), ("block", "stone"), ("物品", "diamond_sword"), ("方块", "stone"),
    ("amount", "10"), ("数量", "10"), ("count", "10"), ("number", "10"), ("page", "1"), ("页码", "1"),
    ("world", "world"), ("世界", "world"), ("radius", "10"), ("半径", "10"), ("distance", "10"),
    ("message", "你好"), ("text", "你好"), ("reason", "测试"), ("原因", "测试"), ("msg", "你好"),
    ("second", "30"), ("时间", "30"), ("minute", "5"), ("time", "30"), ("duration", "30"),
    ("x", "0"), ("y", "64"), ("z", "0"), ("enchantment", "sharpness"), ("附魔", "sharpness"),
    ("level", "1"), ("等级", "1"), ("command", "help"), ("子指令", "help"), ("arg", "参数"),
]

TOKEN = re.compile(r"<[^<>]+>|\[[^\[\]]+\]")


def _sample(token):
    """把 <player> / [amount] 这类占位符换成样例值；认不出来就返回空串（表示可选、可省略）"""
    t = token.strip("<>[]").lower()
    t = re.sub(r"[\s_\-:/]+", " ", t).strip()
    for key, val in SAMPLE:
        if t == key or t.startswith(key + " ") or t.endswith(" " + key) or (" " + key + " ") in t:
            return val
    return ""


def derive_syntax(cmd, usage):
    """把 plugin.yml 的 usage（如 `/<command> [Player] - Open ...`）整理成一行语法"""
    if not usage:
        return ""
    u = decolor(usage)
    u = u.replace("/<command>", "/" + cmd).replace("<command>", cmd)
    u = re.split(r"\s+[-\u2013\u2014]\s+", u)[0]      # 去掉 usage 后面的英文解释
    u = re.sub(r"^/(?!%s)" % re.escape(cmd), "/", u)  # 归一化开头的斜杠
    u = re.sub(r"\s+", " ", u).strip()
    return u


def derive_examples(cmd, usage):
    """按语法自动造两条示例：①参数填满 ②只留必填参数"""
    syn = derive_syntax(cmd, usage)
    if not syn:
        return []

    def fill(tokens, keep_optional):
        out, last = [], 0
        for m in TOKEN.finditer(syn):
            out.append(syn[last:m.start()])
            tok = m.group(0)
            val = _sample(tok)
            optional = tok.startswith("[")
            if optional and not keep_optional:
                pass
            else:
                out.append(val or "")
            last = m.end()
        out.append(syn[last:])
        s = re.sub(r"\s+", " ", "".join(out)).strip()
        return s.rstrip(" ").replace("  ", " ")

    full = fill(syn, True)
    mini = fill(syn, False)
    res = [full]
    if mini != full:
        res.append(mini)
    return res


def cmd_info(plugin_name, row, note):
    """合并三层信息：人工注解 > auto_usage.json > plugin.yml 推导"""
    nc = (note or {}).get("commands", {}).get(row["name"], {})
    au = AUTO.get("%s|%s" % (plugin_name, row["name"]), {})
    usage = row.get("usage")
    info = {
        "what": nc.get("what") or au.get("what") or row.get("desc") or "",
        "syntax": nc.get("syntax") or au.get("syntax") or derive_syntax(row["name"], usage),
        "params": nc.get("params") or au.get("params") or [],
        "examples": nc.get("examples") or au.get("examples") or derive_examples(row["name"], usage),
        "notes": nc.get("notes") or au.get("notes") or "",
    }
    return info


def usage_block(cmd, usage):
    u = clean(usage)
    if not u:
        return ""
    u = u.replace("&lt;command&gt;", cmd).replace("<command>", cmd)
    lines = [l.strip() for l in u.split("\n") if l.strip()]
    return "<br>".join(f"`{l}`" for l in lines)


def collect_commands(rec):
    cmds = rec.get("commands") or {}
    alias_all = set()
    for v in cmds.values():
        for a in (v or {}).get("aliases") or []:
            alias_all.add(str(a).lower())
    rows = []
    seen = set()
    for name, v in sorted(cmds.items()):
        v = v or {}
        key = str(name)
        if key.lower() in alias_all and key.lower() != key:
            continue
        # 同一个功能被注册成多个名字时（如 co/core/coreprotect），只保留第一个为主，其余并入别名
        sig = (clean(v.get("description")), clean(v.get("usage")))
        if sig in seen and sig != ("", ""):
            continue
        seen.add(sig)
        rows.append({
            "name": key,
            "desc": clean(zh(v.get("description"))),
            "usage": v.get("usage"),
            "aliases": [str(a) for a in (v.get("aliases") or [])],
            "permission": clean(v.get("permission")),
        })
    return rows


# ---------------- 人工注解 ----------------
def load_note(name):
    """读 data/notes/<slug>.json，返回规整后的 dict 或 None"""
    fn = os.path.join(NOTES, slug(name) + ".json")
    if not os.path.isfile(fn):
        return None
    try:
        with open(fn, encoding="utf-8") as f:
            raw = json.load(f)
    except Exception as ex:  # 坏文件不阻塞整站生成
        print("  !! 注解解析失败 %s: %r" % (fn, ex))
        return None
    if str(raw.get("name", "")).strip() != name:
        print("  !! 注解 name 不匹配（%s != %s），已跳过：%s" % (raw.get("name"), name, fn))
        return None

    def s(v):
        return decolor(v) if isinstance(v, str) else ""

    def sl(v):
        return [decolor(x) for x in v if isinstance(x, str) and str(x).strip()] if isinstance(v, list) else []

    cmds = {}
    for c in raw.get("commands") or []:
        if not isinstance(c, dict):
            continue
        key = str(c.get("cmd") or "").strip().lstrip("/")
        if not key:
            continue
        params = []
        for p in c.get("params") or []:
            if isinstance(p, dict) and p.get("name"):
                params.append({
                    "name": decolor(p.get("name")),
                    "required": bool(p.get("required")),
                    "note": decolor(p.get("note")),
                })
        cmds[key] = {
            "what": s(c.get("what")),
            "syntax": s(c.get("syntax")),
            "params": params,
            "examples": sl(c.get("examples")),
            "notes": s(c.get("notes")),
            "permission": s(c.get("permission")),
        }
    subs = []
    for x in raw.get("subcommands") or []:
        if isinstance(x, dict) and x.get("cmd"):
            subs.append({"cmd": decolor(x.get("cmd")), "desc": decolor(x.get("desc")), "example": decolor(x.get("example"))})
    perm_desc = {}
    for k, v in (raw.get("permissions") or {}).items():
        if isinstance(v, str) and k:
            perm_desc[str(k)] = decolor(v)
    quick = []
    for x in raw.get("quick") or []:
        if isinstance(x, dict) and x.get("cmd"):
            quick.append({"scene": decolor(x.get("scene") or ""), "cmd": decolor(x.get("cmd")),
                          "note": decolor(x.get("note") or "")})
    return {
        "role": s(raw.get("role")),
        "summary": s(raw.get("summary")),
        "whatFor": sl(raw.get("whatFor"))[:4],
        "flow": sl(raw.get("flow")),
        "quick": quick,
        "commands": cmds,
        "subcommands": subs,
        "caution": sl(raw.get("caution")),
        "related": sl(raw.get("related")),
        "permissions": perm_desc,
    }


def main():
    data = [r for r in json.load(open(DATA, encoding="utf-8")) if r.get("commands")]
    plugins = []
    for r in data:
        name = r.get("name") or r.get("file")
        rows = collect_commands(r)
        cat = ASSIGN.get(name, "other")
        note = load_note(name)
        perms = dict(r.get("permissions") or {}) if isinstance(r.get("permissions"), dict) else {}
        if note and note.get("permissions"):
            for k, d in note["permissions"].items():
                cur = perms.get(k)
                cur = dict(cur) if isinstance(cur, dict) else {}
                if d:
                    cur["description"] = d
                perms[k] = cur
        plugins.append({
            "name": name, "cat": cat, "version": str(r.get("version") or "-"),
            "desc": clean(zh(r.get("desc"))), "file": r.get("file"), "rows": rows,
            "perms": perms, "api": r.get("api"),
            "func": FUNC_CN.get(name, ""), "note": note,
        })

    for d in ("",) + tuple("commands/" + c for c in CAT_ORDER):
        os.makedirs(os.path.join(DOCS, d), exist_ok=True)

    index = {c: [] for c in CAT_ORDER}
    total_cmds = 0
    for p in sorted(plugins, key=lambda x: (CAT_ORDER.index(x["cat"]), x["name"].lower())):
        p["slug"] = slug(p["name"])
        p["path"] = "/commands/%s/%s.md" % (p["cat"], p["slug"])
        # 指令数 = plugin.yml 注册指令 + 注解里补充的子指令
        subs_n = sum(1 for k in ((p["note"] or {}).get("commands") or {})
                     if " " in k and k.split(" ")[0] in {x["name"] for x in p["rows"]})
        p["cnt"] = len(p["rows"]) + subs_n
        total_cmds += p["cnt"]
        index[p["cat"]].append(p)

    # 名称 → 页面，供「相关插件」建链
    PMAP = {p["name"]: p for p in plugins}

    noted = 0
    for c in CAT_ORDER:
        for p in index[c]:
            n = p["note"]
            if n:
                noted += 1
            rows = list(p["rows"])
            # 注解里写了、但 plugin.yml 没单独注册的写法（如 /invSaver save 这类子指令）也补进来，
            # 并紧跟在父指令后面，读表时一眼能看出归属
            known = {x["name"] for x in rows}
            extra = {}
            for k, nc0 in ((n or {}).get("commands") or {}).items():
                if k in known or " " not in k:
                    continue
                row = {"name": k, "desc": nc0.get("what") or "", "usage": None,
                       "aliases": [], "permission": nc0.get("permission") or ""}
                extra.setdefault(k.split(" ")[0], []).append(row)
            if extra:
                merged = []
                for x in rows:
                    merged.append(x)
                    merged.extend(extra.pop(x["name"], []))
                for rest in extra.values():
                    merged.extend(rest)
                rows = merged
            head = ("%s · %s" % (p["func"], p["name"])) if p["func"] else p["name"]
            L = ["---", "title: %s" % p["name"].replace(":", "："), "createTime: %s" % TODAY, "---", ""]
            L.append("# %s" % head)
            L.append("")
            meta = ["分类 %s %s" % (CAT_META[p["cat"]]["icon"], CAT_META[p["cat"]]["title"])]
            meta.append("版本 `%s`" % p["version"])
            meta.append("指令 %d 条" % len(rows))
            if p["api"]:
                meta.append("api-version `%s`" % p["api"])
            L.append("> " + " · ".join(meta))
            L.append("")

            if n:
                if n["summary"] or n["role"]:
                    L.append("::: tip %s" % (n["role"] or "这个插件是干什么的"))
                    if n["summary"]:
                        L.append(txt(n["summary"]))
                    L.append(":::")
                    L.append("")
                if n["quick"]:
                    L.append("## 常用用法")
                    L.append("")
                    L.append("| 场景 | 指令 | 说明 |")
                    L.append("| --- | --- | --- |")
                    for q in n["quick"]:
                        L.append("| %s | %s | %s |" % (cell(q["scene"]) or "—", cell(q["cmd"]), cell(q["note"]) or "—"))
                    L.append("")
                if n["whatFor"]:
                    L.append("## 什么时候会用到它")
                    L.append("")
                    for x in n["whatFor"]:
                        L.append("- %s" % txt(x))
                    L.append("")
                if n["flow"]:
                    L.append("## 上手流程")
                    L.append("")
                    for i, x in enumerate(n["flow"], 1):
                        L.append("%d. %s" % (i, txt(x)))
                    L.append("")
            else:
                if p["desc"]:
                    L.append(p["desc"])
                    L.append("")
                L.append("::: tip 用法提示")
                L.append("本页数据由该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**，尚未补人工注解。")
                mint = rows[0]["name"] if rows else p["name"]
                L.append("具体子参数请执行 `/%s help` 查看；需要补注解见 `data/notes/README.md`。" % mint)
                L.append(":::")
                L.append("")

            # 三层信息合并（注解 > 补充表 > plugin.yml 推导）
            infos = {x["name"]: cmd_info(p["name"], x, n) for x in rows}

            # ---------- 指令一览 ----------
            L.append("## 指令一览")
            L.append("")
            L.append("| 指令 | 功能 | 用法 | 权限节点 |")
            L.append("| --- | --- | --- | --- |")
            for x in rows:
                inf = infos[x["name"]]
                what = cell(inf["what"]) if inf["what"] else "—"
                alias = ("<br>别名 %s" % "、".join("`/%s`" % a for a in x["aliases"])) if x["aliases"] else ""
                syn = inf["syntax"]
                if len(syn) > 52:
                    syn = syn[:50] + "…"
                syn_cell = ("`%s`" % syn) if syn else "—"
                perm = ("`%s`" % x["permission"]) if x["permission"] else "—"
                L.append("| `/%s` | %s%s | %s | %s |" % (x["name"], what, alias, cell(syn_cell), perm))
            L.append("")

            # ---------- 指令详解 ----------
            if rows:
                L.append("## 指令详解")
                L.append("")
                for x in rows:
                    inf = infos[x["name"]]
                    title = "`/%s`" % x["name"]
                    if inf["what"]:
                        title += " — %s" % inf["what"]
                    L.append("### %s" % title)
                    L.append("")
                    if inf["syntax"]:
                        L.append("- **语法**：`%s`" % inf["syntax"])
                    if inf["params"]:
                        L.append("")
                        L.append("| 参数 | 必填 | 说明 |")
                        L.append("| --- | --- | --- |")
                        for pr in inf["params"]:
                            L.append("| `%s` | %s | %s |" % (cell(pr.get("name")), "必填" if pr.get("required") else "可选", cell(pr.get("note"))))
                        L.append("")
                    if inf["examples"]:
                        L.append("")
                        L.append("- **示例**：")
                        L.append("")
                        L.append("```")
                        for ex in inf["examples"]:
                            L.append(ex)
                        L.append("```")
                        L.append("")
                    if x["aliases"]:
                        L.append("- **别名**：%s" % "、".join("`/%s`" % a for a in x["aliases"]))
                    if x["permission"]:
                        L.append("- **权限**：`%s`" % x["permission"])
                    if inf["notes"]:
                        L.append("- **备注**：%s" % txt(inf["notes"]))
                    L.append("")

            # ---------- 子指令速查 ----------
            if n and n["subcommands"]:
                L.append("## 子指令速查")
                L.append("")
                L.append("| 子指令 | 功能 | 示例 |")
                L.append("| --- | --- | --- |")
                for sc in n["subcommands"]:
                    L.append("| `%s` | %s | %s |" % (cell(sc["cmd"]), cell(sc["desc"]), ("`%s`" % sc["example"]) if sc["example"] else "—"))
                L.append("")

            # ---------- 注意事项 ----------
            if n and n["caution"]:
                L.append("## 注意事项")
                L.append("")
                L.append("::: warning")
                for x in n["caution"]:
                    L.append("- %s" % txt(x))
                L.append(":::")
                L.append("")

            # ---------- 权限节点 ----------
            perms = p["perms"] if isinstance(p["perms"], dict) else {}
            if perms:
                L.append("## 权限节点")
                L.append("")
                L.append("| 节点 | 说明 | 默认 |")
                L.append("| --- | --- | --- |")
                for k, v in sorted(perms.items()):
                    v = v if isinstance(v, dict) else {}
                    L.append("| `%s` | %s | %s |" % (k, cell(zh(v.get("description") or "")), cell(v.get("default") or "—")))
                L.append("")

            # ---------- 相关插件 ----------
            rel = [x for x in (n or {}).get("related", []) if x]
            if rel:
                parts = []
                for rn in rel:
                    if rn in PMAP:
                        parts.append("[%s](%s)" % (rn, PMAP[rn]["path"]))
                    else:
                        parts.append(rn)
                L.append("## 相关插件")
                L.append("")
                L.append("、".join(parts))
                L.append("")

            open(os.path.join(DOCS, "commands", p["cat"], p["slug"] + ".md"), "w", encoding="utf-8", newline="\n").write(fix_code_spans("\n".join(L)))

    # ---------- 分类索引 ----------
    for c in CAT_ORDER:
        items = index[c]
        if not items:
            continue
        meta = CAT_META[c]
        L = ["---", "title: %s" % meta["title"], "createTime: %s" % TODAY, "---", "", "# %s %s" % (meta["icon"], meta["title"]), ""]
        L.append(meta["desc"])
        L.append("")
        L.append("| 插件 | 定位 | 指令 | 指令数 |")
        L.append("| --- | --- | --- | --- |")
        for p in items:
            n = p["note"]
            role = (n["role"] if n and n["role"] else p["desc"])[:70]
            heads = "、".join("`/%s`" % x["name"] for x in p["rows"][:3])
            more = "…" if len(p["rows"]) > 3 else ""
            L.append("| [%s](%s) | %s | %s%s | %d |" % (p["name"], p["path"], cell(role), heads, more, p["cnt"]))
        L.append("")
        open(os.path.join(DOCS, "commands", c, "index.md"), "w", encoding="utf-8", newline="\n").write(fix_code_spans("\n".join(L)))

    # ---------- 指令总览（站点根页面，取代原「首页」） ----------
    L = ["---", "title: 指令总览", "createTime: %s" % TODAY, "---", ""]
    # 页首装饰与状态条（控制台风格）
    L.append('<p class="sc-eyebrow"><span class="sc-eyebrow__dot"></span>XINGMIAN SERVER <em>//</em> ADMIN COMMAND INDEX</p>')
    L.append("")
    L.append("# 星冕服务器 · 指令总览")
    L.append("")
    L.append('<div class="sc-strip">')
    for k, v in (("PLUGINS", len(plugins)), ("COMMANDS", total_cmds), ("CATEGORIES", len([c for c in CAT_ORDER if index[c]])), ("UPDATED", TODAY.replace("/", "-"))):
        L.append('<span class="sc-strip__cell"><i>%s</i><b>%s</b></span>' % (k, v))
    L.append('<span class="sc-strip__caret"></span>')
    L.append("</div>")
    L.append("")
    L.append("左侧栏已展开全部插件；按 `Ctrl + K` 可直接搜指令名，例如 `co`、`lp`、`res`。每个插件页含「指令一览」与「指令详解（语法 / 参数 / 示例 / 权限）」。")
    L.append("")
    for c in CAT_ORDER:
        items = index[c]
        if not items:
            continue
        meta = CAT_META[c]
        L.append("## %s %s" % (meta["icon"], meta["title"]))
        L.append("")
        L.append(meta["desc"])
        L.append("")
        L.append("| 插件 | 定位 | 主要指令 | 指令数 |")
        L.append("| --- | --- | --- | --- |")
        for p in items:
            n = p["note"]
            role = (n["role"] if n and n["role"] else p["desc"])[:60]
            heads = "、".join("`/%s`" % x["name"] for x in p["rows"][:4])
            more = "…" if len(p["rows"]) > 4 else ""
            L.append("| [%s](%s) | %s | %s%s | %d |" % (p["name"], p["path"], cell(role), heads, more, p["cnt"]))
        L.append("")
    open(os.path.join(DOCS, "index.md"), "w", encoding="utf-8", newline="\n").write(fix_code_spans("\n".join(L)))

    # 旧的「指令总览」二级页不再生成，避免和根页面重复
    old_cmd_index = os.path.join(DOCS, "commands", "index.md")
    if os.path.isfile(old_cmd_index):
        os.remove(old_cmd_index)

    # 权限节点总表已下线（用户要求），同时清掉历史文件
    stale_perm = os.path.join(DOCS, "permissions.md")
    if os.path.isfile(stale_perm):
        os.remove(stale_perm)

    # ---------- 侧边栏 / 导航 ----------
    # 侧边栏只保留一棵「分类 → 插件」树，并让所有页面（含根页面）共用它，
    # 这样网页一打开左边就能直接看到各插件名。
    tree = ["    { text: '指令总览', link: '/' },"]
    for c in CAT_ORDER:
        if not index[c]:
            continue
        meta = CAT_META[c]
        tree.append("    {")
        tree.append("      text: '%s %s'," % (meta["icon"], meta["title"]))
        tree.append("      link: '/commands/%s/'," % c)
        tree.append("      collapsed: false,")
        tree.append("      items: [")
        for p in index[c]:
            label = FUNC_CN.get(p["name"], meta["title"])
            tree.append("        { text: '%s-%s', link: '%s' }," % (label, p["name"].replace("'", ""), p["path"]))
        tree.append("      ],")
        tree.append("    },")

    T = ["import type { ThemeNavItem, ThemeSidebarMulti } from 'vuepress-theme-plume'", ""]
    T.append("export const navbar: ThemeNavItem[] = [")
    T.append("  { text: '指令总览', link: '/' },")
    T.append("]")
    T.append("")
    T.append("export const sidebar: ThemeSidebarMulti = {")
    for key in ("/commands/", "/"):
        T.append("  '%s': [" % key)
        T.extend(tree)
        T.append("  ],")
    T.append("}")
    os.makedirs(os.path.join(DOCS, ".vuepress"), exist_ok=True)
    open(os.path.join(DOCS, ".vuepress", "sidebar.ts"), "w", encoding="utf-8", newline="\n").write("\n".join(T))

    print("插件页 %d 个（其中带人工注解 %d 个），指令 %d 条，分类 %d 个"
          % (len(plugins), noted, total_cmds, len([c for c in CAT_ORDER if index[c]])))


if __name__ == "__main__":
    main()
