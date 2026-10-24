#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""对 data/zh_cache.json 做一轮人工修订：修最常见的机翻错词 + 补回 `<参数>` 前的空格。

可反复执行（幂等）。改完重跑 gen_docs.py 即可生效。
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(ROOT, "data", "zh_cache.json")

# 逐条改写的译文（键 = 英文原文）
OVERRIDE = {
    "Allow editing item lore": "允许编辑物品的说明文本",
    "Allows the bearer to use heal signs": "允许持有者使用治疗告示牌",
    "Allow to delete stored items": "允许删除已存储的物品",
    "Allow to show stored items": "允许查看已存储的物品",
    "Allow to store items": "允许存储物品",
    "Allow to update stored items": "允许更新已存储的物品",
    "Allows a server admin to test a player disguise for scoreboard issues": "允许服务器管理员测试玩家伪装在计分板上是否正常",
    "Permissions associated with tools": "与工具相关的权限",
    "Gives full access to the plugin": "拥有该插件的全部权限",
    "Allows access to particular command": "允许使用指定指令",
}

# 全局术语替换（顺序敏感，长的在前）
TERMS = [
    ("记分牌", "计分板"),
    ("tab-completion", "TAB 补全"),
    ("Tab-completion", "TAB 补全"),
    ("TAB-completion", "TAB 补全"),
]

# `<参数>` 前面若紧贴英文/数字/右括号，补一个空格
GLUED = re.compile(r"([A-Za-z0-9_\]\)>}])(<)")


def fix(zh):
    out = zh
    for a, b in TERMS:
        out = out.replace(a, b)
    out = GLUED.sub(r"\1 \2", out)
    return out


def main():
    with open(CACHE, encoding="utf-8") as f:
        cache = json.load(f)
    changed = 0
    for en, zh in list(cache.items()):
        new = OVERRIDE.get(en, fix(zh))
        if new != zh:
            cache[en] = new
            changed += 1
    tmp = CACHE + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(cache, f, ensure_ascii=False, indent=0, sort_keys=True)
    os.replace(tmp, CACHE)
    print("修订条目 %d，缓存共 %d 条" % (changed, len(cache)))
    for en in list(OVERRIDE)[:3]:
        print("  例:", en[:50], "->", cache.get(en))


if __name__ == "__main__":
    main()
