# -*- coding: utf-8 -*-
"""根据服务器插件 jar 中 plugin.yml 的解析结果（wcdoc/data/plugin_commands.json）
生成 VuePress + theme-plume 的管理员指令文档站内容。"""
import json, os, re, unicodedata, hashlib

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data", "plugin_commands.json")
SITE = os.path.join(ROOT, "site")
DOCS = os.path.join(SITE, "docs")

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

# 侧边栏显示名：功能简称-插件名，例如 控制台屏蔽-ConsoleSpamFixReborn
# 没登记的新插件会退化成「分类名-插件名」，补一行即可
FUNC_CN = {
    "ALCERecipeViewer": "配方查询", "AfDianPay": "爱发电支付", "Ah-Toy-1.0": "小玩具",
    "Ah-WolfmanKill-1.0": "狼人杀", "ArchitectPlugin": "建筑师工具", "ArmorUnbreaking": "盔甲免损耗",
    "ArmoredElytra": "鞘翅护甲", "ArtMap": "画板地图", "BetterRTP": "随机传送",
    "BlockLocker": "箱子锁", "BookEdit": "成书编辑", "BossBarHealth": "BOSS血条",
    "BroadcastPlusPlus": "公告广播", "CMILib": "CMI前置库", "ConsoleSpamFixReborn": "控制台屏蔽",
    "CoreProtect": "方块日志", "CraftBench": "随身工作台", "DeluxeMenus": "菜单配置",
    "DummyPool": "假人池", "EcoEnchants": "自定义附魔", "EditableStands": "盔甲架编辑",
    "EliteMobs": "精英怪物", "EnchantInfuser": "附魔注入", "Essentials": "基础指令",
    "EssentialsSpawn": "出生点", "FancyNpcsGUI": "NPC界面", "FoMiningComp": "挖矿加成",
    "GSit": "坐下趴下", "InBlock": "方块内藏身", "InfiniteFuel": "无限燃料",
    "InvSaver": "背包快照", "ItemEdit": "物品编辑", "KaleidoscopeCookeryPlugin": "森罗厨房",
    "KaoguGuide": "考古指南", "KaoguPlugin": "考古系统", "LeafChat": "聊天管理",
    "LeafHat": "头顶帽子", "LeashPlayers": "玩家拴绳", "LibsDisguises": "伪装",
    "LobbyGames": "大厅小游戏", "LuckPerms": "权限组", "MagicPointsLog": "点券流水",
    "MahjongPlay": "麻将", "MaintenanceMode": "维护模式", "MeteorShowers": "流星雨",
    "Mirrora": "镜像方块", "ModelEngine": "模型引擎", "MythicMobs": "自定义怪物",
    "MythicTools": "神话工具", "OpenInv": "远程背包", "PlaceholderAPI": "变量占位符",
    "PlayerSignIn": "每日签到", "PlayerTask": "玩家任务", "PlayerTitle": "称号",
    "PlugManX": "插件热管", "PVPPlugin": "PVP管理", "Residence": "领地",
    "SenluoBuyer": "森罗商店", "Shopkeepers": "商店NPC", "Skript": "脚本引擎",
    "spark": "性能分析", "StarAFK": "挂机检测", "StarPact": "星契",
    "SweetMail": "邮件", "TAB": "列表计分板", "TownPlugin": "城镇",
    "Vault": "经济前置", "vcm": "语音喇叭", "voicechat": "语音聊天",
    "WeatherCard": "天气卡", "WebBridge": "网页桥接", "WineSuite": "酿酒",
    "WorldGuardGUI": "保护区界面", "XaeroTracker": "小地图追踪", "XingmianElement": "元素系统",
    "XingmianQuiz": "知识问答", "XingmianRPG": "星冕RPG", "YaoqingPlugin": "玩家邀请",
    "YiyunCEskin": "云皮肤", "allmusic": "全服音乐",
}

COLOR = re.compile(r"[§&][0-9a-fk-orxA-FK-ORX]")


def clean(s):
    """去颜色码 + HTML 转义（页面会被当作 Vue 模板编译，裸 < > 会导致构建失败）"""
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


def usage_block(cmd, usage):
    u = clean(usage)
    if not u:
        return ""
    u = u.replace("<command>", cmd)
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


def main():
    data = [r for r in json.load(open(DATA, encoding="utf-8")) if r.get("commands")]
    plugins = []
    for r in data:
        name = r.get("name") or r.get("file")
        rows = collect_commands(r)
        cat = ASSIGN.get(name, "other")
        plugins.append({
            "name": name, "cat": cat, "version": str(r.get("version") or "-"),
            "desc": clean(zh(r.get("desc"))), "file": r.get("file"), "rows": rows,
            "perms": r.get("permissions") or {},
            "api": r.get("api"),
        })

    for d in ("", "commands") + tuple("commands/" + c for c in CAT_ORDER):
        os.makedirs(os.path.join(DOCS, d), exist_ok=True)

    # ---------- 单插件页面 ----------
    index = {c: [] for c in CAT_ORDER}
    total_cmds = 0
    for p in sorted(plugins, key=lambda x: (CAT_ORDER.index(x["cat"]), x["name"].lower())):
        p["slug"] = slug(p["name"])
        p["path"] = "/commands/%s/%s.md" % (p["cat"], p["slug"])
        total_cmds += len(p["rows"])
        index[p["cat"]].append(p)

        L = []
        L.append("---")
        L.append("title: %s" % p["name"].replace(":", "："))
        L.append("createTime: 2026/10/24")
        L.append("---")
        L.append("")
        L.append("# %s" % p["name"])
        L.append("")
        meta = []
        meta.append("版本 `%s`" % p["version"])
        meta.append("指令 %d 条" % len(p["rows"]))
        if p["api"]:
            meta.append("api-version `%s`" % p["api"])
        meta.append("文件 `%s`" % p["file"])
        L.append("> " + " · ".join(meta))
        L.append("")
        if p["desc"]:
            L.append(p["desc"])
            L.append("")
        L.append("::: tip 用法提示")
        L.append("本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。")
        L.append("具体子参数可以执行 `/%s help` 或该插件对应子命令的 `help` 查看。" % (p["rows"][0]["name"] if p["rows"] else p["name"]))
        L.append(":::")
        L.append("")
        L.append("## 指令一览")
        L.append("")
        L.append("| 指令 | 说明 | 权限节点 |")
        L.append("| --- | --- | --- |")
        for c in p["rows"]:
            L.append("| `/%s` | %s | %s |" % (c["name"], cell(c["desc"]), ("`%s`" % c["permission"]) if c["permission"] else "—"))
        L.append("")
        detail = [c for c in p["rows"] if c["usage"] or c["aliases"] or c["permission"]]
        if detail:
            L.append("## 详细用法")
            L.append("")
            for c in detail:
                L.append("### /%s" % c["name"])
                L.append("")
                if c["desc"]:
                    L.append("- **说明**：%s" % c["desc"])
                if c["usage"]:
                    L.append("- **用法**：%s" % usage_block(c["name"], c["usage"]))
                if c["aliases"]:
                    L.append("- **别名**：%s" % "、".join("`/%s`" % a for a in c["aliases"]))
                if c["permission"]:
                    L.append("- **权限**：`%s`" % c["permission"])
                L.append("")
        perms = p["perms"] if isinstance(p["perms"], dict) else {}
        if perms:
            L.append("## 权限节点")
            L.append("")
            L.append("| 节点 | 说明 | 默认 |")
            L.append("| --- | --- | --- |")
            for k, v in sorted(perms.items()):
                v = v if isinstance(v, dict) else {}
                L.append("| `%s` | %s | %s |" % (k, cell(v.get("description") or ""), cell(v.get("default") or "—")))
            L.append("")
        open(os.path.join(DOCS, "commands", p["cat"], p["slug"] + ".md"), "w", encoding="utf-8", newline="\n").write("\n".join(L))

    # ---------- 分类首页 ----------
    for c in CAT_ORDER:
        items = index[c]
        if not items:
            continue
        meta = CAT_META[c]
        L = ["---", "title: %s" % meta["title"], "createTime: 2026/10/24", "---", "", "# %s %s" % (meta["icon"], meta["title"]), ""]
        L.append(meta["desc"])
        L.append("")
        L.append("| 插件 | 版本 | 指令数 | 说明 |")
        L.append("| --- | --- | --- | --- |")
        for p in items:
            L.append("| [%s](%s) | %s | %d | %s |" % (p["name"], "./" + p["slug"] + ".md", p["version"], len(p["rows"]), cell(p["desc"])[:60]))
        L.append("")
        open(os.path.join(DOCS, "commands", c, "index.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L))

    # ---------- 指令总览 ----------
    L = ["---", "title: 指令总览", "createTime: 2026/10/24", "---", "", "# 指令总览", ""]
    L.append("共 **%d** 个插件、**%d** 条指令，按功能分类。" % (len(plugins), total_cmds))
    L.append("")
    for c in CAT_ORDER:
        items = index[c]
        if not items:
            continue
        meta = CAT_META[c]
        L.append("## %s %s" % (meta["icon"], meta["title"]))
        L.append("")
        L.append("| 插件 | 指令 | 指令数 |")
        L.append("| --- | --- | --- |")
        for p in items:
            heads = "、".join("`/%s`" % x["name"] for x in p["rows"][:6])
            more = "…" if len(p["rows"]) > 6 else ""
            L.append("| [%s](/commands/%s/%s.md) | %s%s | %d |" % (p["name"], c, p["slug"], heads, more, len(p["rows"])))
        L.append("")
    open(os.path.join(DOCS, "commands", "index.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L))

    # ---------- 权限节点总表 ----------
    L = ["---", "title: 权限节点总表", "createTime: 2026/10/24", "---", "", "# 权限节点总表", ""]
    L.append("下表汇总了各插件 `plugin.yml` 中声明的权限节点。默认值 `op` 表示仅管理员组默认拥有，`true` 表示所有玩家默认拥有。")
    L.append("")
    L.append("::: warning")
    L.append("LuckPerms 等权限插件会覆盖这里的默认值。实际生效权限请以 `lp group <组> permission info` 或游戏内测试为准。")
    L.append(":::")
    L.append("")
    for c in CAT_ORDER:
        items = index[c]
        if not items:
            continue
        block = []
        for p in items:
            perms = p["perms"] if isinstance(p["perms"], dict) else {}
            if not perms:
                continue
            block.append((p, perms))
        if not block:
            continue
        L.append("## %s %s" % (CAT_META[c]["icon"], CAT_META[c]["title"]))
        L.append("")
        L.append("| 插件 | 节点 | 说明 | 默认 |")
        L.append("| --- | --- | --- | --- |")
        for p, perms in block:
            for k, v in sorted(perms.items()):
                v = v if isinstance(v, dict) else {}
                L.append("| [%s](/commands/%s/%s.md) | `%s` | %s | %s |" % (p["name"], c, p["slug"], k, cell(zh(v.get("description")))[:50], cell(v.get("default") or "—")))
        L.append("")
    open(os.path.join(DOCS, "permissions.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L))

    # ---------- 侧边栏 ----------
    T = ["import type { ThemeNavItem, ThemeSidebarMulti } from 'vuepress-theme-plume'", ""]
    T.append("export const navbar: ThemeNavItem[] = [")
    T.append("  { text: '首页', link: '/' },")
    T.append("  { text: '指令总览', link: '/commands/' },")
    T.append("  { text: '权限总表', link: '/permissions.md' },")
    T.append("]")
    T.append("")
    T.append("export const sidebar: ThemeSidebarMulti = {")
    T.append("  '/commands/': [")
    T.append("    { text: '指令总览', link: '/commands/' },")
    for c in CAT_ORDER:
        if not index[c]:
            continue
        meta = CAT_META[c]
        T.append("    {")
        T.append("      text: '%s %s'," % (meta["icon"], meta["title"]))
        T.append("      collapsed: false,")
        T.append("      items: [")
        for p in index[c]:
            label = FUNC_CN.get(p["name"], meta["title"])
            T.append("        { text: '%s-%s', link: '/commands/%s/%s.md' }," % (label, p["name"], c, p["slug"]))
        T.append("      ],")
        T.append("    },")
    T.append("  ],")
    T.append("  '/': [")
    T.append("    { text: '指令总览', link: '/commands/' },")
    T.append("    { text: '权限节点总表', link: '/permissions.md' },")
    T.append("  ],")
    T.append("}")
    os.makedirs(os.path.join(DOCS, ".vuepress"), exist_ok=True)
    open(os.path.join(DOCS, ".vuepress", "sidebar.ts"), "w", encoding="utf-8", newline="\n").write("\n".join(T))

    print("插件页 %d 个，指令 %d 条，分类 %d 个" % (len(plugins), total_cmds, len([c for c in CAT_ORDER if index[c]])))


if __name__ == "__main__":
    main()
