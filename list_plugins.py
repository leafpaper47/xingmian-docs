import json, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
d = [r for r in json.load(open("wcdoc/data/plugin_commands.json", encoding="utf-8")) if r.get("commands")]
for r in sorted(d, key=lambda x: x["name"].lower()):
    cmds = ",".join(sorted(r["commands"])[:6])
    print(f"{r['name']:24} {len(r['commands']):3}  [{cmds}]")
print("TOTAL", len(d))
