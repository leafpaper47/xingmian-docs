"""把尚未改版的旧注解批量瘦身成 v2 结构（不改变事实，只做收敛与补全）。

- role 收到 ≤12 字；summary 只留第一句（≤95 字）；whatFor ≤3 条；flow ≤4 步；caution ≤3 条
- 每条注册指令都必须出现在 commands 里（缺的用 plugin.yml 说明 + 中文缓存补）
- 没有 quick 的，用现有 examples 自动生成 3–5 条速查
- 已改版的文件（近 4 小时内改过）跳过
"""
import io
import json
import os
import re
import time

HERE = os.path.dirname(os.path.abspath(__file__))
NOTES = os.path.join(HERE, "data", "notes")
PLUGINS = os.path.join(HERE, "data", "plugin_commands.json")
ZH = os.path.join(HERE, "data", "zh_cache.json")

ZH_MAP = {}
if os.path.exists(ZH):
    ZH_MAP = json.load(io.open(ZH, encoding="utf-8"))

RECS = {}
for rec in json.load(io.open(PLUGINS, encoding="utf-8")):
    RECS[rec["name"]] = rec


def slug(name):
    s = name.lower()
    s = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", s).strip("-")
    return s


def zh(s):
    s = (s or "").strip()
    return ZH_MAP.get(s, s)


def first_sentence(text, limit=95):
    text = re.sub(r"\s+", " ", (text or "").strip())
    if not text:
        return ""
    m = re.split(r"(?<=[。！？!?])", text)
    out = m[0].strip()
    if len(out) > limit:
        out = out[:limit].rstrip("，、,;；") + "…"
    return out


def shorten_role(note, rec):
    role = str((note or {}).get("role") or "").strip()
    if role and len(role) <= 12:
        return role
    cand = re.split(r"[，、,（(]", role)[0].strip() if role else ""
    if cand and len(cand) <= 12:
        return cand
    d = first_sentence(zh(rec.get("desc")), 12)
    return cand[:12] or d[:12] or rec["name"]


def derive_syntax(cmd, usage):
    u = (usage or "").strip()
    if not u:
        return "/" + cmd
    u = re.sub(r"§.", "", u).strip()
    u = u.split("\n")[0].strip()
    u = re.sub(r"<command>", cmd, u)
    return u if u.startswith("/") else "/" + cmd


def main():
    now = time.time()
    changed = 0
    for name, rec in RECS.items():
        if not rec.get("commands"):
            continue
        path = os.path.join(NOTES, slug(name) + ".json")
        if os.path.exists(path) and (now - os.path.getmtime(path)) / 60 < 240:
            continue
        old = {}
        if os.path.exists(path):
            try:
                old = json.load(io.open(path, encoding="utf-8"))
            except Exception:
                old = {}
        if str(old.get("name") or "") not in ("", name):
            old = {}

        cmds = []
        seen = set()
        for c in old.get("commands") or []:
            if not isinstance(c, dict):
                continue
            cmd = str(c.get("cmd") or "").strip().lstrip("/")
            if not cmd or cmd in seen:
                continue
            seen.add(cmd)
            item = {"cmd": cmd}
            what = str(c.get("what") or "").strip()
            if what:
                item["what"] = what if len(what) <= 120 else what[:120] + "…"
            if c.get("syntax"):
                item["syntax"] = str(c["syntax"]).strip()
            if c.get("params"):
                item["params"] = [p for p in c["params"] if isinstance(p, dict) and p.get("name")]
            if c.get("examples"):
                item["examples"] = [str(x) for x in c["examples"] if str(x).strip()][:2]
            note_txt = str(c.get("notes") or "").strip()
            if note_txt:
                item["notes"] = note_txt if len(note_txt) <= 80 else note_txt[:80] + "…"
            if c.get("permission"):
                item["permission"] = str(c["permission"]).strip()
            cmds.append(item)

        # 补全漏掉的注册指令
        for cname, meta in rec["commands"].items():
            if cname in seen:
                continue
            meta = meta or {}
            what = zh(meta.get("description")) or ""
            head = what.split("。")[0].strip() if what else ""
            if head.lower().startswith(("allows", "permission", "the ")):
                head = ""
            cmds.append({
                "cmd": cname,
                "what": head or ("%s 指令（说明见 plugin.yml）" % cname),
                "syntax": derive_syntax(cname, meta.get("usage")),
            })
            seen.add(cname)

        quick = old.get("quick") or []
        if not quick:
            for c in cmds:
                if len(quick) >= 4:
                    break
                ex = (c.get("examples") or [None])[0]
                if ex:
                    quick.append({"scene": (c.get("what") or c["cmd"])[:16], "cmd": ex,
                                  "note": ""})

        out = {
            "name": name,
            "role": shorten_role(old, rec),
            "summary": first_sentence(str(old.get("summary") or ""))
                       or first_sentence(zh(rec.get("desc"))),
            "quick": quick[:6],
            "commands": cmds,
        }
        if old.get("subcommands"):
            out["subcommands"] = old["subcommands"]
        caution = [str(x) for x in (old.get("caution") or []) if str(x).strip()][:3]
        if caution:
            out["caution"] = caution
        if old.get("permissions"):
            out["permissions"] = old["permissions"]

        with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(out, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
        changed += 1
        print("slimmed %-28s cmds=%-3d quick=%d" % (name, len(out["commands"]), len(out["quick"])))

    print("\n共处理 %d 个注解" % changed)


if __name__ == "__main__":
    main()
