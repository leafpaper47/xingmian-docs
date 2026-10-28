import subprocess, sys, re
JV = r"D:\Program Files\Zulu\zulu-25\bin\javap.exe"
classes = sys.argv[1:]
cp = "ext\\TAB"
for cn in classes:
    p = subprocess.run([JV,"-c","-p","-cp",cp,cn],capture_output=True)
    txt = p.stdout.decode("gbk",errors="replace")
    print("="*20, cn)
    strs = re.findall(r"// (?:String|class|Method|Field) (.*)", txt)
    seen=[]
    for s in strs:
        if s not in seen: seen.append(s)
    for s in seen: print("  ", s[:160])
