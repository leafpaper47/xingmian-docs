#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""检查翻译质量：还有多少英文没翻、哪些结果可疑。"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")

CJK = re.compile(r"[\u4e00-\u9fff]")
LATIN_WORD = re.compile(r"[A-Za-z]{3,}")


def main():
    src = json.load(open(os.path.join(DATA, "plugin_commands.json"), encoding="utf-8"))
    cache_path = os.path.join(DATA, "zh_cache.json")
    cache = json.load(open(cache_path, encoding="utf-8")) if os.path.isfile(cache_path) else {}

    # 收集所有英文串
    strings = set()
    for r in src:
        if r.get("error"):
            continue
        for key in ("desc",):
            v = (r.get(key) or "").strip()
            if v and not CJK.search(v):
                strings.add(v)
        for group in ("commands", "permissions"):
            g = r.get(group) or {}
            if isinstance(g, dict):
                for _k, v in g.items():
                    v = v if isinstance(v, dict) else {}
                    d = (v.get("description") or "").strip()
                    if d and not CJK.search(d):
                        strings.add(d)

    missing = sorted(s for s in strings if s not in cache)
    translated = [s for s in strings if s in cache]
    print("英文串总数 %d，已翻译 %d，未翻译 %d" % (len(strings), len(translated), len(missing)))
    if missing:
        print("\n--- 未翻译样例（前 15 条）---")
        for s in missing[:15]:
            print(" ", s[:90])

    # 可疑结果：译文里还剩较多英文单词，或与原文一模一样
    suspicious = []
    for s in translated:
        zh = cache[s]
        if zh.strip() == s.strip():
            suspicious.append(("原文照抄", s, zh))
            continue
        if len(LATIN_WORD.findall(zh)) >= 3 and len(zh) < len(s) * 0.9:
            suspicious.append(("残留英文", s, zh))
    print("\n可疑译文 %d 条" % len(suspicious))
    for kind, s, zh in suspicious[:20]:
        print("  [%s] %s\n        -> %s" % (kind, s[:70], zh[:70]))

    # 抽样看整体质量
    print("\n--- 随机抽样 8 条 ---")
    import random
    random.seed(7)
    for s in random.sample(translated, min(8, len(translated))):
        print("  EN:", s[:80])
        print("  ZH:", cache[s][:80])
        print()


if __name__ == "__main__":
    main()
