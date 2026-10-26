# -*- coding: utf-8 -*-
"""校验 data/notes/*.json：结构、指令名对齐、示例格式、模板危险字符。

用法：python check_notes.py [--strict]
  默认只报告，不阻断；--strict 时存在 error 级问题则退出码 1。
"""
import json, os, sys, re, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data", "plugin_commands.json")
NOTES = os.path.join(ROOT, "data", "notes")

ERR, WARN = [], []


def slug(name):
    s = name.lower()
    s = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", s).strip("-")
    return s


def main():
    strict = "--strict" in sys.argv
    data = {r.get("name"): r for r in json.load(open(DATA, encoding="utf-8")) if r.get("commands")}
    files = sorted(glob.glob(os.path.join(NOTES, "*.json")))
    seen = set()
    for fn in files:
        base = os.path.basename(fn)
        try:
            o = json.load(open(fn, encoding="utf-8"))
        except Exception as ex:
            ERR.append("%s: JSON 解析失败 %r" % (base, ex))
            continue
        name = o.get("name")
        if not name:
            ERR.append("%s: 缺 name" % base)
            continue
        if name not in data:
            ERR.append("%s: name=%s 不在 plugin_commands.json 里" % (base, name))
            continue
        if base != slug(name) + ".json":
            WARN.append("%s: 文件名与 slug(%s) 不一致，生成器会读不到" % (base, slug(name)))
        seen.add(name)
        # 必填
        for k in ("role", "summary", "whatFor", "commands"):
            if not o.get(k):
                ERR.append("%s: 缺字段 %s" % (base, k))
        if len(str(o.get("role", ""))) > 34:
            WARN.append("%s: role 偏长（%d 字）" % (base, len(o["role"])))
        if len(o.get("whatFor") or []) < 2:
            WARN.append("%s: whatFor 少于 2 条" % base)
        # 指令对齐
        real = set(data[name].get("commands") or {})
        alias = set()
        for v in (data[name].get("commands") or {}).values():
            for a in (v or {}).get("aliases") or []:
                alias.add(str(a).lower())
        got = []
        for c in o.get("commands") or []:
            cmd = str((c or {}).get("cmd") or "").strip().lstrip("/")
            if not cmd:
                ERR.append("%s: 有空 cmd" % base)
                continue
            got.append(cmd)
            if cmd not in real:
                if cmd.lower() in alias:
                    WARN.append("%s: cmd=%s 只是别名，不是独立指令" % (base, cmd))
                else:
                    ERR.append("%s: cmd=%s 不存在于该插件（真实：%s）" % (base, cmd, ",".join(sorted(real))[:120]))
            for ex in (c or {}).get("examples") or []:
                if not str(ex).strip().startswith("/"):
                    ERR.append("%s: %s 的示例不以 / 开头：%s" % (base, cmd, ex))
        miss = sorted(real - set(got) - alias)
        if miss:
            WARN.append("%s: 有 %d 条指令未写注解：%s" % (base, len(miss), ",".join(miss)[:120]))
        # 危险字符
        blob = json.dumps(o, ensure_ascii=False)
        if "{{" in blob or "}}" in blob:
            ERR.append("%s: 含 {{ }}（会被 Vue 模板吃掉）" % base)
        for field in ("role", "summary"):
            if re.search(r"[<>]", str(o.get(field, ""))):
                WARN.append("%s: %s 含裸尖括号" % (base, field))

    missing = sorted(set(data) - seen)
    print("注解文件 %d 个，覆盖插件 %d / %d" % (len(files), len(seen), len(data)))
    if missing:
        print("未写注解的插件（%d）：%s" % (len(missing), "、".join(missing)))
    for w in WARN:
        print("WARN  " + w)
    for e in ERR:
        print("ERROR " + e)
    print("小计：ERROR %d，WARN %d" % (len(ERR), len(WARN)))
    if strict and ERR:
        sys.exit(1)


if __name__ == "__main__":
    main()
