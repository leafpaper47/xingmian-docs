# 星冕服务器 · 管理员插件指令手册

用 VuePress 2 + `vuepress-theme-plume` 做的服内指令速查站。内容分两层：

1. **机器解析层**：服务器 `plugins/` 下各插件 jar 里的 `plugin.yml` 直接解析出指令名、别名、用法、权限节点 —— 保证「和这台服务器对得上」。
2. **人工注解层**：`data/notes/*.json` 里为每个插件手写的定位、适用场景、上手流程、子指令速查、坑 —— 解决「`plugin.yml` 只有一行潦草说明」的问题。

- 扫描 135 个插件 jar → 85 个插件声明了指令 → 434 条指令（含由注解补全的子指令）
- 站点**没有首页**：打开就是「指令总览」，左侧栏直接展开全部插件名，也可 `Ctrl + K` 搜指令名
- 13 个功能分类、85 个插件页（每页含指令一览与详解、常用示例、权限节点）；纯静态，不需要后端

## 目录

```
.
├─ data/plugin_commands.json     # 解析结果（机器层唯一数据源）
├─ data/zh_cache.json            # 英文说明 → 中文对照（可人工修订）
├─ data/notes/<slug>.json        # 人工注解（定位/场景/流程/子指令/坑），见 notes/README.md
├─ zipyml.py                     # 用 SFTP 读 jar 内 plugin.yml，生成上面的 json
├─ gen_docs.py                   # 生成 docs/ 下所有 markdown + 侧边栏（合并机器层与注解层）
├─ check_notes.py                # 校验注解：结构、指令名是否真实存在、示例格式
├─ translate_ui.py               # 把英文说明批量翻成中文，结果写入 zh_cache.json
├─ check_zh.py                   # 检查还有多少英文没翻、译文是否可疑
├─ list_plugins.py               # 列出服务器 plugins 目录（排查用）
└─ site/                         # VuePress 工程
   ├─ package.json / pnpm-lock.yaml / .npmrc
   └─ docs/
      ├─ .vuepress/config.ts     # 站点配置（base、hostname、主题）
      ├─ .vuepress/sidebar.ts    # 由 gen_docs.py 生成，别手改
      ├─ .vuepress/client.ts     # 挂载自定义样式
      ├─ .vuepress/styles/index.scss  # 表格列宽等站点样式
      ├─ commands/<分类>/<插件>.md  # 插件页
      ├─ index.md                # 指令总览（站点根页面）
```

## 页面结构

| 路径 | 内容 |
| --- | --- |
| `/` | 指令总览：13 个分类 × 全部插件（定位一句话 + 主要指令 + 指令数） |
| `/commands/<分类>/` | 分类索引 |
| `/commands/<分类>/<插件>.md` | 插件页：定位 → 什么时候会用到 → 上手流程 → 指令一览 → 指令详解（语法/参数/示例/权限）→ 子指令速查 → 注意事项 → 权限节点 → 相关插件 |

有注解的插件页是完整版；没有注解的会退回 `plugin.yml` 的极简版（并在页面上标注「尚未补人工注解」）。

## 本地开发

```bash
cd site
pnpm install
pnpm dev      # http://localhost:8088
pnpm build    # 产物在 site/docs/.vuepress/dist
```

> 首次安装注意：`.npmrc` 里已固定 `node-linker=hoisted`。如果之前用别的 linker 装过，先删掉 `node_modules` 和 `pnpm-lock.yaml` 再装，否则会报 `Cannot find package '@vuepress/cli'`。

## 日常更新

**只改文案 / 补注解**（最常见）：

```bash
python check_notes.py     # 先校验，ERROR 必须为 0
python gen_docs.py        # 重新生成页面与侧边栏
cd site && pnpm build
```

**服务器装了新插件或插件升级**：

```bash
export SH=n6-2.yxsjmc.cn SP=2422 SU=<sftp用户名> SW=<sftp密码>
python zipyml.py          # 重新解析 → data/plugin_commands.json
python gen_docs.py        # 重新生成（新插件会先以极简版出现）
cd site && pnpm build
```

`zipyml.py` 的凭据只从环境变量读，**不要写进脚本里再提交**。

## 人工注解（data/notes）

每个插件一个 `data/notes/<slug>.json`（slug = 插件名小写、非字母数字转 `-`）。字段与硬规则见 `data/notes/README.md`，可直接照抄 `luckperms.json`（单主指令 + 大量子指令）和 `coreprotect.json`（流程与风险型）两种范例。

要点：

- `commands[].cmd` 必须是插件**真实注册**的指令名，不能编；子指令写进 `subcommands[]`
- 自研插件（Xingmian / Kaogu / Senluo / Leaf / Star 等）不写子指令，`syntax` 直接用 `plugin.yml` 的 usage，坑里标注「以游戏内 help 为准」
- 竖线 `|` 会在生成时换成全角，尖括号参数在页面里会正确显示，不用自己转义
- `check_notes.py` 会拦：JSON 语法错、`name` 对不上、`cmd` 不存在、示例不以 `/` 开头、含 `{{ }}`

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
- 各插件页里的权限节点及其默认值
- 服务器装了哪些插件（`data/plugin_commands.json` 里的 jar 文件名与版本）

如果不是所有玩家都该知道这些，建议改成私有仓库（Pages 需 GitHub Pro），或者只发布去掉权限表与版本号的对外版。

## 已知限制

- 只解析 `plugin.yml`：代码里动态注册的指令（Skript 自定义命令、DeluxeMenus 菜单指令、MythicMobs 内嵌命令）不会出现
- 子指令靠人工注解补：`/lp`、`/co`、`/mm` 这类主指令的真子指令写在 `data/notes/` 里；没写注解的插件仍只显示主指令
- 颜色码 `§x` 在生成时已清除

## 说明文字汉化

文档里插件自带的英文说明（指令 description、插件简介、权限说明）会先翻成中文再写入页面：

```bash
python translate_ui.py          # 断点续跑，结果存 data/zh_cache.json
python polish_zh.py             # 人工修订：常用术语、<参数> 前补空格
python fix_commands.py          # 把机翻掉的 /tab、/exp 这类指令名换回英文
python check_zh.py              # 看还差多少、哪些译文可疑
python gen_docs.py              # 重新生成页面（会自动读 zh_cache.json）
```

- 译文有机器翻译成分，`data/zh_cache.json` 是纯文本可版本化文件，**发现译得不对直接改这个文件再重跑 `gen_docs.py` 即可**，不需要重新翻译。
- 想重新翻某一条：从 `zh_cache.json` 里删掉那一条，再跑 `translate_ui.py`。
- 指令参数、权限节点、`/co lookup i:stone` 这类**语法**保持英文，是刻意的，不要翻。

## 指令说明的三层来源

每个插件页的「指令一览」与「指令详解」按下面的优先级拼装，改数据不用改生成器：

1. `data/notes/<插件>.json` —— 人工注解（插件定位、上手流程、每条指令的 what/语法/参数/示例/备注），优先级最高
2. `data/auto_usage.json` —— 补充表，键为 `插件名|指令名`，用于补注解里没写到的指令（LibsDisguises、OpenInv、GSit、Residence 等）
3. `plugin.yml` 自动推导 —— 上面两层都没有时，用 usage 整理成一行语法，并把 `<player>`/`[amount]` 这类占位符替换成样例值自动生成示例

新增一个插件的完整说明，只需要新建 `data/notes/<slug>.json`（字段参考 `data/notes/README.md`），或在 `data/auto_usage.json` 里加一条 `'插件名|指令名'`。

## 站点结构

- `/` 直接是**指令总览**（不再有单独首页），进来就是 13 个分类的插件表
- `/commands/<分类>/<插件>.md` 插件页：定位 → 上手流程 → 指令一览（指令/功能/用法/权限）→ 指令详解（语法/参数/示例/别名/权限/备注）→ 子指令速查 → 注意事项 → 权限节点 → 相关插件

## 字体

站点正文与代码全部使用 **Fusion Pixel 12px**（像素字体，视觉上是 Minecraft 那一挂）：
正文用比例宽度版、结构与代码用等宽版。字体文件随仓库分发，位于
`site/docs/.vuepress/styles/fonts/`（`prop/` 与 `mono/` 各 78 个按 unicode-range 切分的 woff2
子集，浏览器只下载页面实际用到的分片）。由 `styles/_fusion-*.scss` 里的 `@font-face` 引入。

- 字体：Fusion Pixel Font，作者 TakWolf
- 授权：SIL Open Font License 1.1（可自由分发与商用，保留授权文件即可）
- 注意：Minecraft 官方字体（Mojang 的 `Minecraft.ttf`）授权不允许随站点再分发，
  所以这里用同为像素风的开源字体替代，观感一致且无授权风险。
