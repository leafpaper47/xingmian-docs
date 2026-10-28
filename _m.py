import json,io
n=json.load(open("data/notes/essentials.json",encoding="utf-8"))
def sz(o): return len(json.dumps(o,ensure_ascii=False,separators=(",",":")).encode())
cs=n["commands"]
base=sum(sz({k:v for k,v in c.items()}) for c in cs)
wh=sum(sz(c["what"]) for c in cs); sy=sum(sz(c["syntax"]) for c in cs)
ex=sum(sz(c.get("examples") or []) for c in cs if c.get("examples"))
pa=sum(sz(c.get("params") or []) for c in cs if c.get("params"))
print("commands-bytes",base,"what",wh,"syntax",sy,"examples",ex,"params",pa)
print("header", sz(n["summary"]), sz(n["whatFor"]), sz(n["quick"]), sz(n["caution"]), sz(n["role"]), sz(n["name"]))
print("syntax avg", sy/len(cs), "empty-syntax count", sum(1 for c in cs if not (c.get("syntax") or "").strip()))
