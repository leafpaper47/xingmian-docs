import json,io
d=json.load(open("data/plugin_commands.json",encoding="utf-8"))
rows=[r for r in d if r.get("name")=="Essentials"][0]
cmds=rows["commands"]
out=io.open("_ev.txt","w",encoding="utf-8",newline="\n")
for n,v in cmds.items():
    out.write("%s | %s | %s\n"%(n,(v.get("usage") or "").replace("/<command>","/"+n),", ".join(v.get("aliases") or [])))
out.close()
print("ok")
