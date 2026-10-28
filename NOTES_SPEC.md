# 插件注解（notes）编写规范 v2 — 2026 年改版

站点目标是「管理员查指令时 10 秒内找到答案」，所以注解要**短、准、可复制**。

## 1. 文件位置与命名

`wcdoc/data/notes/<slug>.json`，slug = 插件名转小写、非字母数字中文字符替换成 `-`。
不确定就用：

```
python wcdoc/note_tool.py slug <插件名>
```

## 2. 结构

```json
{
  "name": "Residence",                       // 必须与 plugin.yml 里的 name 完全一致
  "role": "领地保护与租赁",                   // 功能简称，≤12 字，用于侧边栏与标题
  "summary": "一句话说清它解决什么问题。",     // ≤100 字，最多两句，不写营销词
  "quick": [                                 // 3–6 条最高频用法，给老手看的速查
    {"scene": "圈一块地", "cmd": "/res select 10", "note": "切到选区模式再点两个对角方块"}
  ],
  "commands": [                              // 核心：覆盖全部注册指令 + 能确认的子指令
    {
      "cmd": "res create",
      "what": "用当前选区创建一个住宅",         // 一句话，动词开头，具体
      "syntax": "/res create <住宅名>",
      "params": [{"name": "住宅名", "required": true, "note": "同世界内唯一，中文可用"}],
      "examples": ["/res create home"],
      "notes": "花费按区块数与 config 费率计算；名字里不能有空格",   // 只写坑/副作用/权限，没有就省略
      "permission": "residence.create"
    }
  ],
  "subcommands": [                           // 可选：子指令速查表（插件子指令很多时才用）
    {"cmd": "/res pset", "desc": "给住宅/子区域设权限标志", "example": "/res pset home build true"}
  ],
  "caution": ["restore 会覆盖当前背包，不可反悔"],   // 1–3 条最该注意的事
  "permissions": {"residence.create": "创建住宅"}    // 只填 plugin.yml 里缺 description 的节点
}
```

## 3. 内容规则（重要）

- **what 一句话**：写「做什么」，不写「允许玩家使用…命令」这种废话。例：`把住宅所有权转给另一个玩家`。
- **examples 必须可执行**：带真实玩家名（Steve）、合理数值、真实住宅名（home），不要写成 `/res create <名字>`。
- **notes 只写有价值的信息**：副作用、覆盖/不可逆、需要额外权限、常见报错原因。没价值的删掉。
- **子指令写法**：`"cmd": "res pset"`（父指令 + 空格 + 子指令），生成器会自动排在一览表里父指令下方。
- **不编造**：证据里没有、自己也拿不准的子指令宁可不写。
- **术语统一**：玩家、背包、末影箱、领地、权限节点、子指令、OP。
- **覆盖度**：
  - 注册指令（plugin.yml 里的）**每一条都要有 what**；
  - 有明确子指令体系的插件（Residence、LuckPerms、CoreProtect、MythicMobs、GSit、LibsDisguises、TAB、Shopkeepers、Essentials…）**每个常用子指令都要有一行**；
  - 子指令特别多的（Essentials 153 条、MythicMobs 上百子命令）：高频的逐条写全，冷门的可在 `subcommands` 里成组列出，并在 `caution` 里注明「完整列表见 `/xx help`」。

## 4. 取证方法（写之前必做）

```
python wcdoc/note_tool.py ev <插件名>        # 打印注册指令、命令包类名（≈子指令）、反编译 token、内置帮助文本
```

- 「命令包下的类名」是最可靠的子指令清单来源（如 Residence 的 `commands.create`）。
- 「资源文件里的用法/帮助行」常含插件自带的 usage 与中文报错文案，可据此写 notes。
- 主流插件（LuckPerms、CoreProtect、Essentials、MythicMobs、Trading 等）可用通用知识补全语义，但子指令名必须与证据一致。

## 5. 自检

```
python wcdoc/validate_notes.py <your-file>.json
```

必须 `errors=0`。warns 可保留，但「示例里没出现指令名」「权限节点未声明」这类要人工看一眼。

## 6. 风格样例

见 `data/notes/residence.json`（子指令体系型）与 `data/notes/invsaver.json`（少量指令但每条写透型）。
