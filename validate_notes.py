"""校验 data/notes/*.json 的结构与内容一致性。

用法：
  python validate_notes.py                # 校验全部
  python validate_notes.py residence.json essentials.json
"""
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
NOTES = os.path.join(HERE, "data", "notes")
PLUGINS = os.path.join(HERE, "data", "plugin_commands.json")

PL = {}
for rec in json.load(open(PLUGINS, encoding="utf-8")):
    PL[rec["name"]] = rec


def check_file(path):
    errs, warns = [], []
    try:
        raw = json.loads(io.open(path, encoding="utf-8").read())
    except Exception as exc:
        return ["JSON 解析失败: %r" % (exc,)], []
    name = str(raw.get("name") or "")
    rec = PL.get(name)
    if not rec:
        return ["name=%r 不在 plugin_commands.json 里" % name], []
    cmds_reg = {k.lower() for k in (rec.get("commands") or {})}
    aliases = set()
    for v in (rec.get("commands") or {}).values():
        for a in (v or {}).get("aliases") or []:
            aliases.add(str(a).lower())

    role = str(raw.get("role") or "")
    summary = str(raw.get("summary") or "")
    if not role:
        errs.append("缺 role")
    if len(role) > 24:
        warns.append("role 太长(%d 字)" % len(role))
    if not summary:
        errs.append("缺 summary")
    if len(summary) > 140:
        warns.append("summary 偏长(%d 字)" % len(summary))

    cmds = raw.get("commands") or []
    if not isinstance(cmds, list):
        errs.append("commands 必须是数组")
        cmds = []
    seen = set()
    for c in cmds:
        if not isinstance(c, dict):
            errs.append("commands 里有非对象项")
            continue
        cmd = str(c.get("cmd") or "").strip().lstrip("/")
        if not cmd:
            errs.append("有 commands 项缺 cmd")
            continue
        if cmd in seen:
            errs.append("重复的 cmd: %s" % cmd)
        seen.add(cmd)
        head = cmd.split(" ")[0].lower()
        if head not in cmds_reg and head not in aliases:
            errs.append("cmd=%r 的首个词不是已注册指令（注册列表：%s）" % (cmd, ", ".join(sorted(cmds_reg))[:200]))
        if not str(c.get("what") or "").strip():
            errs.append("cmd=%r 缺 what（功能说明）" % cmd)
        for ex in c.get("examples") or []:
            if not str(ex).startswith("/"):
                errs.append("cmd=%r 的示例不以 / 开头: %s" % (cmd, ex))
            elif head not in str(ex).lower():
                warns.append("cmd=%r 的示例里没出现指令名: %s" % (cmd, ex))
        for p in c.get("params") or []:
            if isinstance(p, dict) and not p.get("name"):
                errs.append("cmd=%r 有参数项缺 name" % cmd)

    for x in raw.get("subcommands") or []:
        if not isinstance(x, dict) or not x.get("cmd"):
            errs.append("subcommands 项缺 cmd")
            continue
        if not str(x.get("desc") or "").strip():
            errs.append("subcommands[%s] 缺 desc" % x.get("cmd"))

    perms_reg = {k for k in (rec.get("permissions") or {})}
    for k in (raw.get("permissions") or {}):
        if perms_reg and k not in perms_reg:
            warns.append("权限节点 %r 未在 plugin.yml 中声明（确认是否手工加过）" % k)

    if not cmds:
        warns.append("commands 为空")
    return errs, warns


def main(argv):
    files = argv[1:]
    if not files:
        files = sorted(f for f in os.listdir(NOTES) if f.endswith(".json"))
    bad = 0
    for f in files:
        path = f if os.path.isabs(f) else os.path.join(NOTES, f)
        errs, warns = check_file(path)
        tag = "OK  " if not errs else "FAIL"
        print("%s %-32s errors=%d warns=%d" % (tag, os.path.basename(path), len(errs), len(warns)))
        for e in errs:
            print("     E %s" % e)
        for w in warns:
            print("     W %s" % w)
        if errs:
            bad += 1
    print("\n%d 个文件有错误" % bad)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
