"""把有指令的插件 jar 从生产服 SFTP 拉到本地 jars/，供反编译分析子指令。"""
import json
import os
import sys
import time

import paramiko

HOST = "n6-2.yxsjmc.cn"
PORT = 2422
USER = "gameworld_flgti1.16bbc9ac"
PWD = "xingmian741"
REMOTE_DIR = "plugins"

HERE = os.path.dirname(os.path.abspath(__file__))
JARS = os.path.join(HERE, "jars")
DATA = os.path.join(HERE, "data", "plugin_commands.json")


def main():
    data = json.load(open(DATA, encoding="utf-8"))
    plugins = data if isinstance(data, list) else data.get("plugins")
    targets = [p for p in plugins if p.get("commands")]
    os.makedirs(JARS, exist_ok=True)

    t = paramiko.Transport((HOST, PORT))
    t.connect(username=USER, password=PWD)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.chdir(REMOTE_DIR)

    ok = skip = fail = 0
    done_bytes = 0
    for i, p in enumerate(targets, 1):
        name = p["file"]
        local = os.path.join(JARS, name)
        want = p.get("size") or 0
        if os.path.exists(local) and os.path.getsize(local) == want:
            skip += 1
            continue
        t0 = time.time()
        try:
            sftp.get(name, local)
            got = os.path.getsize(local)
            if want and got != want:
                raise IOError("size mismatch %s != %s" % (got, want))
            ok += 1
            done_bytes += got
            print("[%d/%d] %-55s %6.1f MB  %.1fs" % (i, len(targets), name[:55], got / 1048576.0, time.time() - t0), flush=True)
        except Exception as exc:
            fail += 1
            print("[%d/%d] FAIL %s: %s" % (i, len(targets), name, exc), flush=True)

    sftp.close()
    t.close()
    print("downloaded=%d skipped=%d failed=%d bytes=%.1fMB" % (ok, skip, fail, done_bytes / 1048576.0))


if __name__ == "__main__":
    sys.exit(main())
