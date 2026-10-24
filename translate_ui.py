#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""把 data/plugin_commands.json 里的英文说明批量翻成中文，结果缓存到 data/zh_cache.json。

- 只处理不含中文的字符串（含中文的视为已汉化，跳过）
- 按出现频次从高到低翻译，额度不够时优先保证高频文案
- 断点续跑：每翻译完一批就落盘，重跑会自动跳过已有条目
用法:
  python translate_ui.py            # 正常跑（限速 1.1s/条）
  python translate_ui.py --limit 50 # 只翻 50 条试试
"""
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")
SRC = os.path.join(DATA, "plugin_commands.json")
CACHE = os.path.join(DATA, "zh_cache.json")

CJK = re.compile(r"[\u4e00-\u9fff]")
API = "https://api.mymemory.translated.net/get?q=%s&langpair=en|zh-CN&de=%s"
# MyMemory 需要带 de（联系邮箱参数）才会放宽限额，否则很快 429
DE = os.environ.get("MYMEMORY_DE", "docs-builder@example.com")


def is_english(s):
    return bool(s) and not CJK.search(s)


def load_cache():
    if os.path.isfile(CACHE):
        with open(CACHE, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_cache(cache):
    tmp = CACHE + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(cache, f, ensure_ascii=False, indent=0, sort_keys=True)
    os.replace(tmp, CACHE)


def collect():
    """返回 {英文字符串: 出现次数}"""
    with open(SRC, encoding="utf-8") as f:
        records = json.load(f)
    counter = Counter()
    for r in records:
        if r.get("error"):
            continue
        desc = (r.get("desc") or "").strip()
        if is_english(desc):
            counter[desc] += 1
        cmds = r.get("commands") or {}
        if isinstance(cmds, dict):
            for _k, v in cmds.items():
                d = ((v or {}).get("description") or "").strip()
                if is_english(d):
                    counter[d] += 1
        perms = r.get("permissions") or {}
        if isinstance(perms, dict):
            for _k, v in perms.items():
                v = v if isinstance(v, dict) else {}
                d = (v.get("description") or "").strip()
                if is_english(d):
                    counter[d] += 1
    return counter


def translate(text):
    """返回 (中文, 错误信息)"""
    q = urllib.parse.quote(text[:480])
    req = urllib.request.Request(
        API % (q, urllib.parse.quote(DE)),
        headers={"User-Agent": "Mozilla/5.0 (docs-builder)"},
    )
    with urllib.request.urlopen(req, timeout=25) as resp:
        payload = json.loads(resp.read().decode("utf-8", "replace"))
    status = payload.get("responseStatus")
    if status != 200:
        return None, "http %s: %s" % (status, str(payload.get("responseDetails"))[:80])
    if payload.get("quotaFinished"):
        return None, "QUOTA"
    out = (payload.get("responseData") or {}).get("translatedText") or ""
    out = out.strip()
    if not out or not CJK.search(out):
        return None, "no-chinese"
    if "MYMEMORY WARNING" in out.upper():
        return None, "QUOTA"
    return out, None


def main():
    limit = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])

    counter = collect()
    cache = load_cache()
    todo = [(t, n) for t, n in counter.most_common() if t not in cache]
    if limit is not None:
        todo = todo[:limit]
    print("去重英文串 %d 条，已缓存 %d 条，本次待翻 %d 条" % (len(counter), len(cache), len(todo)), flush=True)

    ok = fail = 0
    consecutive_fail = 0
    for idx, (text, freq) in enumerate(todo, 1):
        zh, err = None, None
        for attempt in range(4):
            try:
                zh, err = translate(text)
            except Exception as exc:  # 网络/限流类错误
                zh, err = None, repr(exc)[:80]
            if zh or "429" not in str(err):
                break
            # 被限流就退避重试：30s、60s、90s
            time.sleep(30 * (attempt + 1))
        if zh:
            cache[text] = zh
            ok += 1
            consecutive_fail = 0
        else:
            fail += 1
            consecutive_fail += 1
            if err == "QUOTA" or consecutive_fail >= 8:
                save_cache(cache)
                print("停止：%s（连续失败 %d 次）已翻 %d 条" % (err, consecutive_fail, ok), flush=True)
                break
        if idx % 20 == 0:
            save_cache(cache)
            print("  进度 %d/%d  成功 %d  失败 %d" % (idx, len(todo), ok, fail), flush=True)
        time.sleep(1.1)
    save_cache(cache)
    print("完成：成功 %d，失败 %d，缓存共 %d 条" % (ok, fail, len(cache)), flush=True)


if __name__ == "__main__":
    main()
