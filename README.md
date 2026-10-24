# 星冕服务器 · 管理员插件指令手册

用 VuePress 2 + `vuepress-theme-plume` 做的服内指令速查站。全部内容由服务器 `plugins/` 下各插件 jar 里的 `plugin.yml` **直接解析生成**，不是网上抄的通用文档。

- 扫描 125 个插件 jar → 80 个插件声明了指令 → 322 条指令，合并别名后文档展示 **318 条**
- 13 个功能分类、80 个插件页、权限节点总表
- 搜索（`Ctrl + K`）为本地索引，纯静态，不需要后端

## 目录

```
.
├─ data/plugin_commands.json     # 解析结果（唯一数据源）
├─ data/zh_cache.json            # 英文说明 → 中文对照（可人工修订）
├─ zipyml.py                     # 用 SFTP 读 jar 内 plugin.yml，生成上面的 json
├─ gen_docs.py                   # 生成 docs/ 下所有 markdown + 侧边栏
├─ translate_ui.py               # 把英文说明批量翻成中文，结果写入 zh_cache.json
├─ check_zh.py                   # 检查还有多少英文没翻、译文是否可疑
├─ list_plugins.py               # 列出服务器 plugins 目录（排查用）
└─ site/                         # VuePress 工程
   ├─ package.json / pnpm-lock.yaml / .npmrc
   └─ docs/
      ├─ .vuepress/config.ts     # 站点配置（base、hostname、主题）
      ├─ .vuepress/sidebar.ts    # 由 gen_docs.py 生成，别手改
      ├─ commands/               # 指令页（按分类分目录）
      ├─ index.md                # 首页（分类导航）
      └─ permissions.md          # 权限节点总表
```

## 本地开发

```bash
cd site
pnpm install
pnpm dev      # http://localhost:8088
pnpm build    # 产物在 site/docs/.vuepress/dist
```

> 首次安装注意：`.npmrc` 里已固定 `node-linker=hoisted`。如果之前用别的 linker 装过，先删掉 `node_modules` 和 `pnpm-lock.yaml` 再装，否则会报 `Cannot find package '@vuepress/cli'`。

## 更新数据

服务器装了新插件或插件升级后：

```bash
export SH=n6-2.yxsjmc.cn SP=2422 SU=<sftp用户名> SW=<sftp密码>
python zipyml.py       # 重新解析 → data/plugin_commands.json
python gen_docs.py     # 重新生成 docs/ 下所有页面与侧边栏
cd site && pnpm build
```

`zipyml.py` 的凭据只从环境变量读，**不要写进脚本里再提交**。

## 发布到 GitHub Pages

1. 在 GitHub 新建仓库（例如 `xingmian-docs`），**不要**勾选自动生成 README。
2. 确认仓库名与 `site/docs/.vuepress/config.ts` 顶部一致：
   ```ts
   const BASE = '/xingmian-docs/'        // 必须 /仓库名/，末尾斜杠不能少
   const HOSTNAME = 'https://<用户名>.github.io/'   // 只影响 sitemap/SEO
   ```
3. 本地初始化并推送：
   ```bash
   git init -b main
   git add .
   git commit -m "docs: 管理员插件指令手册"
   git remote add origin https://github.com/<用户名>/xingmian-docs.git
   git push -u origin main
   ```
4. 仓库 **Settings → Pages → Build and deployment → Source** 选 **GitHub Actions**。
5. 之后每次 `git push` 到 `main`，`.github/workflows/deploy.yml` 会自动构建并发布到
   `https://<用户名>.github.io/xingmian-docs/`。

首次发布约 1 分钟；Actions 跑完后地址即可访问，也可以在 **Actions** 页看构建日志。

## ⚠️ 内容敏感性

仓库是**公开**的，因此以下内容对所有人可见：

- 每个插件的完整指令列表、别名、用法
- 全部权限节点及其默认值（`permissions.md`，43 万字符）
- 服务器装了哪些插件（`data/plugin_commands.json` 里的 jar 文件名与版本）

如果不是所有玩家都该知道这些，建议改成私有仓库（Pages 需 GitHub Pro），或者只发布去掉 `permissions.md` 与版本号的对外版。

## 已知限制

- 只解析 `plugin.yml`：代码里动态注册的指令（Skript 自定义命令、DeluxeMenus 菜单指令、MythicMobs 内嵌命令）不会出现
- 子指令不展开：`/lp`、`/co`、`/mm` 这类主指令请用游戏内 `help`
- 颜色码 `§x` 在生成时已清除

## 说明文字汉化

文档里插件自带的英文说明（指令 description、插件简介、权限说明）会先翻成中文再写入页面：

```bash
python translate_ui.py          # 断点续跑，结果存 data/zh_cache.json
python check_zh.py              # 看还差多少、哪些译文可疑
python gen_docs.py              # 重新生成页面（会自动读 zh_cache.json）
```

- 译文有机器翻译成分，`data/zh_cache.json` 是纯文本可版本化文件，**发现译得不对直接改这个文件再重跑 `gen_docs.py` 即可**，不需要重新翻译。
- 想重新翻某一条：从 `zh_cache.json` 里删掉那一条，再跑 `translate_ui.py`。
- 指令参数、权限节点、`/co lookup i:stone` 这类**语法**保持英文，是刻意的，不要翻。
