import pathlib, json
p = pathlib.Path("package.json")
print("=== package.json ===")
print(p.read_text("utf-8"))
for f in ["pnpm-lock.yaml", ".npmrc", "package-lock.json"]:
    q = pathlib.Path(f)
    print(f, "exists:", q.exists(), (q.stat().st_size if q.exists() else ""))
print("typescript in node_modules:", pathlib.Path("node_modules/typescript/lib/typescript.js").exists())
