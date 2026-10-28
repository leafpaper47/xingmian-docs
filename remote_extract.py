"""远程按需抽取：不整包下载，只经 SFTP 读取 jar 中央目录里「命令相关 class」与「文本资源」。

产物：
  ext/<plugin>/...       抽出的 class 与 yml/properties（保持包路径，可直接作为 javap -cp）
  data/remote_extract.json  每个插件的抽取清单
"""
import io
import json
import os
import re
import struct
import sys
import zlib

import paramiko

HOST = "n6-2.yxsjmc.cn"
PORT = 2422
USER = "gameworld_flgti1.16bbc9ac"
PWD = "xingmian741"
REMOTE_DIR = "plugins"

HERE = os.path.dirname(os.path.abspath(__file__))
EXT = os.path.join(HERE, "ext")
DATA = os.path.join(HERE, "data", "plugin_commands.json")

CLS_PAT = re.compile(r"(?i)(command|cmd|subcmd)")
RES_PAT = re.compile(r"(?i)\.(yml|yaml|properties|json|txt)$")


def read_exact(fh, n):
    buf = b""
    while len(buf) < n:
        chunk = fh.read(n - len(buf))
        if not chunk:
            break
        buf += chunk
    return buf


def central_directory(fh, size):
    tail = min(size, 66_000)
    fh.seek(size - tail)
    data = fh.read(tail)
    pos = data.rfind(b"PK\x05\x06")
    if pos < 0:
        raise ValueError("no EOCD")
    cd_size, cd_off = struct.unpack("<II", data[pos + 12:pos + 20])
    fh.seek(cd_off)
    cd = read_exact(fh, cd_size)
    entries = []
    i = 0
    while i + 46 <= len(cd) and cd[i:i + 4] == b"PK\x01\x02":
        (method,) = struct.unpack("<H", cd[i + 10:i + 12])
        (csize,) = struct.unpack("<I", cd[i + 20:i + 24])
        (usize,) = struct.unpack("<I", cd[i + 24:i + 28])
        (nlen,) = struct.unpack("<H", cd[i + 28:i + 30])
        (elen,) = struct.unpack("<H", cd[i + 30:i + 32])
        (clen,) = struct.unpack("<H", cd[i + 32:i + 34])
        (lho,) = struct.unpack("<I", cd[i + 42:i + 46])
        name = cd[i + 46:i + 46 + nlen].decode("utf-8", "replace")
        entries.append({"name": name, "method": method, "csize": csize,
                        "usize": usize, "lho": lho})
        i += 46 + nlen + elen + clen
    return entries


def read_entry(fh, e):
    fh.seek(e["lho"])
    head = read_exact(fh, 30)
    if head[:4] != b"PK\x03\x04":
        raise ValueError("bad local header")
    (nlen,) = struct.unpack("<H", head[26:28])
    (elen,) = struct.unpack("<H", head[28:30])
    fh.seek(e["lho"] + 30 + nlen + elen)
    raw = read_exact(fh, e["csize"])
    if e["method"] == 0:
        return raw
    d = zlib.decompressobj(-15)
    return d.decompress(raw) + d.flush()


def main():
    data = json.load(open(DATA, encoding="utf-8"))
    plugins = data if isinstance(data, list) else data.get("plugins")
    targets = [p for p in plugins if p.get("commands")]
    os.makedirs(EXT, exist_ok=True)

    t = paramiko.Transport((HOST, PORT))
    t.connect(username=USER, password=PWD)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.chdir(REMOTE_DIR)

    manifest = {}
    for idx, p in enumerate(targets, 1):
        jar = p["file"]
        try:
            fh = sftp.open(jar, "rb")
            size = sftp.stat(jar).st_size
            entries = central_directory(fh, size)
            picks = []
            for e in entries:
                nm = e["name"]
                if nm.endswith(".class") and CLS_PAT.search(nm):
                    picks.append(e)
                elif RES_PAT.search(nm) and e["usize"] < 400_000 and not re.search(r"(?i)(sql|logback|liquibase)", nm):
                    picks.append(e)
            outdir = os.path.join(EXT, p["name"].replace("/", "_"))
            got = []
            for e in picks:
                dest = os.path.join(outdir, e["name"].replace("/", os.sep))
                if os.path.exists(dest) and os.path.getsize(dest) == e["usize"]:
                    got.append(e["name"])
                    continue
                try:
                    blob = read_entry(fh, e)
                    os.makedirs(os.path.dirname(dest) or outdir, exist_ok=True)
                    with open(dest, "wb") as w:
                        w.write(blob)
                    got.append(e["name"])
                except Exception as exc:
                    pass
            fh.close()
            manifest[p["name"]] = {"file": jar, "jar_size": size,
                                   "entries_total": len(entries), "extracted": got}
            print("[%d/%d] %-38s entries=%-5d picked=%-4d" % (idx, len(targets), p["name"][:38], len(entries), len(got)), flush=True)
        except Exception as exc:
            manifest[p["name"]] = {"file": jar, "error": str(exc)}
            print("[%d/%d] FAIL %s: %s" % (idx, len(targets), jar, exc), flush=True)

    sftp.close()
    t.close()
    json.dump(manifest, open(os.path.join(HERE, "data", "remote_extract.json"), "w",
                             encoding="utf-8"), ensure_ascii=False, indent=1)
    print("done")


if __name__ == "__main__":
    sys.exit(main())
