# -*- coding: utf-8 -*-
"""把构建产物 site/docs/.vuepress/dist 打包成 xingmian-plugin-docs.zip（压缩包根目录即站点根）。

用法：python pack.py   （先 python gen_docs.py && cd site && pnpm build）
"""
import os
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "site", "docs", ".vuepress", "dist")
OUT = os.path.join(ROOT, "xingmian-plugin-docs.zip")


def main():
    if not os.path.isdir(DIST):
        raise SystemExit("找不到 dist，请先构建：cd site && pnpm build")
    n = 0
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _dirs, files in os.walk(DIST):
            for f in sorted(files):
                p = os.path.join(root, f)
                rel = os.path.relpath(p, DIST).replace("\\", "/")
                z.write(p, rel)
                n += 1
    print("打包完成：%s（%d 个文件，%.2f MB）" % (os.path.basename(OUT), n, os.path.getsize(OUT) / 1048576))


if __name__ == "__main__":
    main()
