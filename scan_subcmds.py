"""从 ext/ 里已抽取的命令相关 class + 文本资源中挖子指令与帮助文本。

输出：
  data/subcmds.json        结构化结果（dispatch token / 帮助文本 / 资源行）
  subcmds/<插件>.txt        人类可读证据
"""
import io
import json
import os
import re
import struct
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EXT = os.path.join(HERE, "ext")
OUT_JSON = os.path.join(HERE, "data", "subcmds.json")
OUT_DIR = os.path.join(HERE, "subcmds")
JAVAP = r"D:\Program Files\Zulu\zulu-25\bin\javap.exe"

JUNK = re.compile(r"^(java/|javax/|jdk/|sun/|kotlin/|net/minecraft|com/google/|org/bukkit/|io/papermc/|net/kyori/|org/jetbrains/|org/apache/|com/mojang/|com/destroystokyo/)")
TOKEN = re.compile(r"^[a-z][a-z0-9_\-]{0,24}$")


def pool_strings(data):
    try:
        if data[:4] != b"\xca\xfe\xba\xbe":
            return []
        n = struct.unpack(">H", data[8:10])[0]
        i, idx, out = 10, 1, []
        while idx < n:
            tag = data[i]
            i += 1
            if tag == 1:
                ln = struct.unpack(">H", data[i:i + 2])[0]
                i += 2
                out.append(data[i:i + ln].decode("utf-8", "replace"))
                i += ln
            elif tag in (7, 8, 16, 19, 20):
                i += 2
            elif tag == 15:
                i += 3
            elif tag in (3, 4, 9, 10, 11, 12, 17, 18):
                i += 4
            elif tag in (5, 6):
                i += 8
                idx += 1
            else:
                break
            idx += 1
        return out
    except Exception:
        return []


def javap_strings(root, cls):
    try:
        p = subprocess.run([JAVAP, "-c", "-p", "-cp", root, cls],
                           capture_output=True, timeout=240)
        return re.findall(r"// String ([^\n]+)", p.stdout.decode("utf-8", "replace"))
    except Exception:
        return []


def keep(s):
    return (s and 2 <= len(s) <= 160 and not JUNK.match(s)
            and not s.startswith(("(", "[", "<", "/")))


def main():
    data = json.load(open(os.path.join(HERE, "data", "plugin_commands.json"), encoding="utf-8"))
    plugins = data if isinstance(data, list) else data.get("plugins")
    targets = [p for p in plugins if p.get("commands")]
    os.makedirs(OUT_DIR, exist_ok=True)
    result = {}

    for i, p in enumerate(targets, 1):
        root = os.path.join(EXT, p["name"].replace("/", "_"))
        if not os.path.isdir(root):
            continue
        cmds = list(p["commands"].keys())
        cmdset = {c.lower() for c in cmds}

        classes, strings, reslines = [], [], []
        for dirpath, _, files in os.walk(root):
            for fn in files:
                full = os.path.join(dirpath, fn)
                rel = os.path.relpath(full, root).replace(os.sep, "/")
                if fn.endswith(".class"):
                    try:
                        raw = open(full, "rb").read()
                    except OSError:
                        continue
                    classes.append(rel[:-6].replace("/", "."))
                    for s in pool_strings(raw):
                        if keep(s):
                            strings.append(s)
                else:
                    try:
                        txt = io.open(full, encoding="utf-8", errors="replace").read()
                    except OSError:
                        continue
                    for line in txt.splitlines():
                        low = line.lower()
                        if any(("/" + c) in low for c in cmdset if len(c) >= 3) or \
                                (re.search(r"[\u4e00-\u9fff]", line) and len(line.strip()) >= 4):
                            reslines.append(line.strip()[:200])

        dispatch = {}
        for cls in classes[:150]:
            for s in javap_strings(root, cls):
                t = s.strip().lower()
                if TOKEN.match(t):
                    dispatch[t] = dispatch.get(t, 0) + 1

        helps, seen = [], set()
        for s in strings:
            low = s.lower()
            hit = any(("/" + c) in low for c in cmdset if len(c) >= 3) or \
                  (re.search(r"[\u4e00-\u9fff]", s) and len(s) >= 3)
            if hit and s not in seen:
                seen.add(s)
                helps.append(s)

        result[p["name"]] = {
            "file": p["file"], "commands": cmds,
            "dispatch": sorted(dispatch.keys()),
            "strings": helps[:800],
            "reslines": reslines[:400],
            "classes": classes[:200],
        }

        with io.open(os.path.join(OUT_DIR, p["name"].replace("/", "_") + ".txt"), "w",
                     encoding="utf-8", newline="\n") as fh:
            fh.write("# %s  (%s)\n" % (p["name"], p["file"]))
            fh.write("## 注册指令\n")
            for c, v in p["commands"].items():
                fh.write("  /%s  usage=%r desc=%r alias=%r perm=%r\n" % (
                    c, v.get("usage"), v.get("description"), v.get("aliases"), v.get("permission")))
            fh.write("\n## 代码类\n  %s\n" % "\n  ".join(classes[:80]))
            fh.write("\n## javap 字符串 token\n  %s\n" % " ".join(sorted(dispatch.keys()))[:6000])
            fh.write("\n## 文本资源里的帮助/用法行\n")
            for s in reslines[:400]:
                fh.write("  · %s\n" % s)
            fh.write("\n## 常量池帮助/描述文本\n")
            for s in helps[:800]:
                fh.write("  · %s\n" % s)

        print("[%d/%d] %-40s cls=%-3d tok=%-4d res=%-4d str=%d" % (
            i, len(targets), p["name"][:40], len(classes), len(dispatch), len(reslines), len(helps)), flush=True)

    json.dump(result, open(OUT_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", OUT_JSON)


if __name__ == "__main__":
    sys.exit(main())
