import paramiko, os, struct, zlib, json, io, sys
h=os.environ["SH"]; p=int(os.environ["SP"]); u=os.environ["SU"]; pw=os.environ["SW"]
t=paramiko.Transport((h,p)); t.connect(username=u,password=pw)
s=paramiko.SFTPClient.from_transport(t)

def read_at(path, off, n):
    f=s.open(path,"rb"); f.seek(off); d=f.read(n); f.close(); return d

def zip_entries(path, size):
    tail_n=min(size, 70000)
    tail=read_at(path, size-tail_n, tail_n)
    i=tail.rfind(b"PK\x05\x06")
    if i<0: raise RuntimeError("no EOCD")
    cd_size, cd_off = struct.unpack("<II", tail[i+12:i+20])
    cd=read_at(path, cd_off, cd_size)
    out={}; o=0
    while o+46<=len(cd) and cd[o:o+4]==b"PK\x01\x02":
        meth,=struct.unpack("<H", cd[o+10:o+12])
        csize, usize = struct.unpack("<II", cd[o+20:o+28])
        nlen, elen, clen = struct.unpack("<HHH", cd[o+28:o+34])
        lho,=struct.unpack("<I", cd[o+42:o+46])
        name=cd[o+46:o+46+nlen].decode("utf-8","replace")
        out[name]=(meth,csize,usize,lho)
        o+=46+nlen+elen+clen
    return out

def extract(path, ent):
    meth,csize,usize,lho=ent
    lh=read_at(path, lho, 30)
    nlen,elen=struct.unpack("<HH", lh[26:30])
    data=read_at(path, lho+30+nlen+elen, csize)
    if meth==8: return zlib.decompress(data,-15)
    if meth==0: return data
    raise RuntimeError("method %d"%meth)

import yaml
res=[]
names=sorted([x for x in s.listdir("plugins") if x.lower().endswith(".jar")])
print("jars:", len(names), file=sys.stderr)
for n in names:
    path="plugins/"+n
    try:
        st=s.stat(path)
        ents=zip_entries(path, st.st_size)
        key=None
        for cand in ("plugin.yml","paper-plugin.yml","bungee.yml"):
            if cand in ents: key=cand; break
        if not key: 
            res.append({"file":n,"size":st.st_size,"error":"no plugin.yml"}); continue
        d=yaml.safe_load(extract(path, ents[key]).decode("utf-8","replace")) or {}
        cmds=d.get("commands") or {}
        rec={"file":n,"size":st.st_size,"name":d.get("name"),"version":str(d.get("version")),
             "main":d.get("main") or d.get("main-class"),"api":d.get("api-version"),"desc":(d.get("description") or "")[:200],
             "commands":cmds if isinstance(cmds,dict) else {}, "permissions": d.get("permissions") or {}}
        res.append(rec)
    except Exception as ex:
        res.append({"file":n,"error":repr(ex)[:120]})
json.dump(res, open("wcdoc/data/plugin_commands.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
ok=[r for r in res if r.get("commands")]
print("解析成功:", len([r for r in res if not r.get("error")]), "有指令:", len(ok), "指令总数:", sum(len(r["commands"]) for r in ok))
for r in ok: print(f'  {r["name"]:22} {len(r["commands"]):3} 条  {r["file"]}')
s.close(); t.close()
