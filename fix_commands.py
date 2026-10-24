#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""机翻常把指令名一起翻掉：`/tab` → `/选项卡`、`/标签`、`/制表符`。

只做两件保守的事，且不碰非指令场景（如 buy/sell → 购买/出售）：

1. 把 `/选项卡` `/标签` `/制表符` 这类 /tab 的误译换回 `/tab `。
2. 英文原文里出现 "command"/"run" 语境、且某个 `/cmd` 在译文里丢了（变成了 `/中文` 或大小写变了），
   把译文里那个斜杠词换回英文指令名（补一个空格，避免和后面的英文参数粘连）。

幂等，可反复执行；写完重跑 gen_docs.py 生效。
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(ROOT, "data", "zh_cache.json")

TAB_WORDS = ("选项卡", "标签", "制表符", "分页", "tab页")
CMD_EN = re.compile(r"/[A-Za-z][A-Za-z0-9_\-]*")
# 斜杠 + 一串中文（可能后面粘着英文参数）
SLASH_CJK = re.compile(r"/[\u4e00-\u9fff][A-Za-z0-9_\-\u4e00-\u9fff]*")
CTX = re.compile(r"\b(command|commands|run|runs|execut\w*)\b", re.I)


def fix_one(en, zh):
    out = zh
    # 规则 1：/tab 的常见误译
    for w in TAB_WORDS:
        if "/" + w in out and "/tab" in en:
            out = out.replace("/" + w, "/tab ")
    # 规则 2：指令名丢失
    if CTX.search(en):
        for cmd in CMD_EN.findall(en):
            name = cmd[1:]
            if cmd in out or name.lower() in out.lower():
                continue
            m = SLASH_CJK.search(out)
            if m:
                out = out[: m.start()] + cmd + " " + out[m.end():]
    out = re.sub(r" {2,}", " ", out)
    out = re.sub(r"\s+([，。、；：!？])", r"\1", out)
    return out.strip()


def main():
    with open(CACHE, encoding="utf-8") as f:
        cache = json.load(f)
    changed = 0
    for en, zh in list(cache.items()):
        new = fix_one(en, zh)
        if new != zh:
            cache[en] = new
            changed += 1
            if changed <= 6:
                print("EN:", en[:80])
                print("旧:", zh[:80])
                print("新:", new[:80])
                print()
    tmp = CACHE + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(cache, f, ensure_ascii=False, indent=0, sort_keys=True)
    os.replace(tmp, CACHE)
    print("修正 %d / %d 条" % (changed, len(cache)))


if __name__ == "__main__":
    main()
