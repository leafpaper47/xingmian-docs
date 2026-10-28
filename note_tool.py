"""注解编写辅助工具。

  python note_tool.py list                     列出所有插件 → 注解文件名
  python note_tool.py slug <PluginName>        打印该插件的注解文件路径
  python note_tool.py ev <PluginName>          打印证据摘要（子指令类名/分发 token/帮助行）
"""
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
NOTES = os.path.join(HERE, "data", "notes")
PLUGINS = os.path.join(HERE, "data", "plugin_commands.json")
SUB = os.path.join(HERE, "data", "subcmds.json")


def slug(name):
    s = name.lower()
    s = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", s).strip("-")
    return s or "x"


def load():
    recs = json.load(open(PLUGINS, encoding="utf-8"))
    subs = {}
    if os.path.exists(SUB):
        subs = json.load(open(SUB, encoding="utf-8"))
    return recs, subs


def cmd_list():
    recs, subs = load()
    for r in recs:
        if not r.get("commands"):
            continue
        nm = r["name"]
        fn = os.path.join(NOTES, slug(nm) + ".json")
        d = subs.get(nm, {})
        subn = len({c.split(".commands.")[1].split("$")[0] for c in d.get("classes", []) if ".commands." in c})
        print("%-28s cmds=%-3d subcls=%-3d note=%s%s" % (
            nm, len(r["commands"]), subn, os.path.basename(fn), "" if os.path.exists(fn) else " (缺失)"))


def cmd_slug(name):
    print(os.path.join(NOTES, slug(name) + ".json"))


def cmd_ev(name):
    recs, subs = load()
    rec = next((r for r in recs if r["name"] == name), None)
    if not rec:
        sys.exit("没有这个插件: %s" % name)
    d = subs.get(name, {})
    print("## 注册指令（plugin.yml）")
    for c, v in rec["commands"].items():
        print("/%s | usage=%r | desc=%r | alias=%r | perm=%r" % (
            c, v.get("usage"), v.get("description"), v.get("aliases"), v.get("permission")))
    print("\n## 权限节点（plugin.yml）")
    for k, v in (rec.get("permissions") or {}).items():
        print("%s | default=%r | desc=%r" % (k, (v or {}).get("default"), (v or {}).get("description")))
    classes = d.get("classes", [])
    groups = {}
    for c in classes:
        m = re.search(r"\.(commands?|cmd)\.([^.$]+)", c)
        if m:
            groups.setdefault(m.group(2), []).append(c.split(".")[-1])
    if groups:
        print("\n## 命令包下的类名（≈子指令，共 %d 个）" % len(groups))
        print("  " + " ".join(sorted(groups)))
    print("\n## javap 字符串 token")
    print("  " + " ".join(d.get("dispatch", [])[:400]))
    print("\n## 资源文件里的用法/帮助行")
    for s in d.get("reslines", [])[:120]:
        print("  · " + s[:180])


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    op = argv[1]
    if op == "list":
        cmd_list()
    elif op == "slug" and len(argv) > 2:
        cmd_slug(argv[2])
    elif op == "ev" and len(argv) > 2:
        cmd_ev(argv[2])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv)
