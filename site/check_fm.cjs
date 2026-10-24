const fs=require('fs'), path=require('path'), yaml=require('js-yaml');
function walk(d,acc=[]){for(const e of fs.readdirSync(d,{withFileTypes:true})){const p=path.join(d,e.name); if(e.isDirectory()){if(e.name!=='.vuepress'&&e.name!=='public')walk(p,acc);} else if(e.name.endsWith('.md'))acc.push(p);} return acc;}
let bad=0, count=0;
for(const f of walk('docs')){
  const t=fs.readFileSync(f,'utf8');
  const m=t.match(/^---\n([\s\S]*?)\n---/);
  count++;
  if(!m){console.log('NO FRONTMATTER:',f);continue;}
  try{ yaml.load(m[1]); }catch(e){ bad++; console.log('BAD:',f); console.log('   '+m[1].split('\n').slice(0,4).join(' | ')); }
}
console.log('scanned',count,'bad',bad);
