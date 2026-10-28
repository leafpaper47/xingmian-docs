#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""为缺少 examples 的指令，按 syntax 自动补常用示例（保守：只填空缺，不改已有）。

用法： python fill_examples.py data/notes/essentials.json [...]
规则：
  - 必填 <x> 用 SAMPLE 表换成可复制的样例值；
  - 可选 [x] 第一例省略、第二例填入；
  - 括号形式 (x) 视作必填说明，直接替换。
"""
import io
import json
import re
import sys

SAMPLE = {
    "player": "Steve", "players": "Steve", "name": "Steve", "target": "Steve",
    "玩家": "Steve", "玩家名": "Steve", "目标玩家": "Steve", "目标": "Steve",
    "amount": "10", "数量": "10", "数值": "10", "count": "10", "次数": "10",
    "radius": "10", "半径": "10", "distance": "10", "range": "10",
    "world": "world", "世界": "world", "世界名": "world",
    "kit": "starter", "礼包": "starter", "warp": "spawn", "地标": "spawn",
    "home": "home", "家": "home", "jail": "jail", "监狱": "jail",
    "item": "diamond", "物品": "diamond", "material": "diamond",
    "id": "1", "编号": "1", "type": "1", "类型": "1",
    "message": "你好", "文本": "你好", "msg": "你好", "留言": "你好",
    "time": "60", "时间": "60", "seconds": "30", "秒": "30",
    "money": "100", "金额": "100", "price": "100",
    "enchant": "sharpness", "附魔": "sharpness", "level": "3", "等级": "3",
    "reason": "违规", "原因": "违规", "text": "你好", "内容": "你好",
}

REQ = re.compile(r"<([^>]+)>")
OPT = re.compile(r"\[([^\]]+)\]")


def sample_for(inner, default="值"):
    key = inner.strip().lower()
    if key in SAMPLE:
        return SAMPLE[key]
    for k, v in SAMPLE.items():
        if k in key:
            return v
    return default


def build(syntax):
    """返回 (仅必填示例, 含一个可选参数的示例)"""
    s = syntax.strip()
    if not s.startswith("/"):
        s = "/" + s
    # 只要必填：去掉所有 [..]，替换 <..> 与 (..)
    only_req = OPT.sub("", s)
    only_req = REQ.sub(lambda m: sample_for(m.group(1)), only_req)
    only_req = re.sub(r"\(([^)]+)\)", lambda m: sample_for(m.group(1)), only_req)
    only_req = re.sub(r"\s+", " ", only_req).strip()

    # 含第一个可选：把第一个 [..] 替换成它的样例值，其余仍去掉
    m = OPT.search(s)
    with_opt = None
    if m:
        filled = s[: m.start()] + " " + sample_for(m.group(1)) + s[m.end():]
        with_opt = OPT.sub("", filled)
        with_opt = REQ.sub(lambda mm: sample_for(mm.group(1)), with_opt)
        with_opt = re.sub(r"\(([^)]+)\)", lambda mm: sample_for(mm.group(1)), with_opt)
        with_opt = re.sub(r"\s+", " ", with_opt).strip()
        if with_opt == only_req:
            with_opt = None
    return only_req, with_opt


def main(paths):
    total = 0
    for p in paths:
        d = json.load(io.open(p, encoding="utf-8"))
        changed = 0
        for c in d.get("commands") or []:
            if c.get("examples"):
                continue
            syn = c.get("syntax") or ""
            if not syn:
                base = "/" + (c.get("cmd") or "").split()[0]
                c["examples"] = [base]
                changed += 1
                continue
            a, b = build(syn)
            ex = [a] if a else []
            if b and b != a:
                ex.append(b)
            if ex:
                c["examples"] = ex
                changed += 1
        if changed:
            io.open(p, "w", encoding="utf-8", newline="\n").write(
                json.dumps(d, ensure_ascii=False, indent=1) + "\n")
            print("%-40s +%d" % (p, changed))
            total += changed
        else:
            print("%-40s =0" % p)
    print("共补 %d 条示例" % total)


if __name__ == "__main__":
    main(sys.argv[1:] or ["data/notes/essentials.json"])
