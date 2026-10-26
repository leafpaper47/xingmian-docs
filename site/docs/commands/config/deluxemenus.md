---
title: DeluxeMenus
createTime: 2026/10/24
---

# 菜单配置 · DeluxeMenus

> 分类 🧩 脚本与菜单 · 版本 `1.14.1-Release` · 指令 1 条 · api-version `1.13`

::: tip 用 YAML 配置箱子菜单的界面插件
DeluxeMenus 让你在配置文件里画出任意箱子界面（商店入口、传送菜单、功能面板、会员特权页），玩家点物品就能执行指令、发消息、开下一个菜单。它本身不含经济或权限逻辑，通常配合 PlaceholderAPI 显示变量、Vault 或经济插件做购买、LuckPerms 做权限判断。服务器里所有「点一下弹个 GUI」的需求基本都由它实现。
:::

## 什么时候会用到它

- 做服务器主菜单、传送点菜单、商店分类入口这类图形界面
- 把长串指令包装成玩家点一下就执行的按钮，避免玩家记指令
- 给不同权限组展示不同内容（VIP 专属菜单、每日签到面板）
- 用占位符在物品说明里显示玩家余额、在线人数、等级等实时数据

## 上手流程

1. 在 plugins/DeluxeMenus/gui_menus 下新建或修改菜单 YAML，写好 menu_title、size、items 三大部分
2. 进游戏执行 /dm reload 重载配置，看后台有没有报 YAML 错误
3. 用 /dm open 菜单名 试开自己的菜单，确认排版、占位符、点击动作都正常
4. 需要给玩家开放时，把菜单设为 open_command 或用一条指令/告示牌/其他插件触发打开，并配上权限节点

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/deluxemenus` | 菜单主命令，管理重载、打开、新建、删除菜单<br>别名 `/dm`、`/deluxemenu`、`/dmenu` | `/deluxemenus 子指令 参数` | — |

## 指令详解

### `/deluxemenus` — 菜单主命令，管理重载、打开、新建、删除菜单

- **语法**：`/deluxemenus 子指令 参数`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子指令` | 必填 | open 打开菜单、reload 重载、list 列出菜单、create 新建、delete 删除、template 模板菜单 |
| `菜单名` | 可选 | open/reload/create/delete 时需要，写 YAML 里的菜单 id |
| `玩家名` | 可选 | open 时可加，代表替别人打开菜单 |


- **示例**：

```
/dm list
/dm open main
/dm open main Steve
/dm reload
/dm reload main
```

- **别名**：`/dm`、`/deluxemenu`、`/dmenu`
- **备注**：别名 dm、dmenu、deluxemenu。别名短，日常都用 /dm。管理员完整权限是 deluxemenus.admin；普通玩家只需要 deluxemenus.open，替别人开要 deluxemenus.open.others 和 deluxemenus.placeholdersfor。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `open 菜单名` | 给自己打开指定菜单 | `/dm open main` |
| `open 菜单名 玩家名` | 替指定玩家打开菜单，需要 open.others 权限 | `/dm open main Steve` |
| `list` | 列出当前已加载的所有菜单 id | `/dm list` |
| `reload` | 重载全部菜单配置（改完 YAML 必用） | `/dm reload` |
| `reload 菜单名` | 只重载某一个菜单，改动小时更快更安全 | `/dm reload main` |
| `create 菜单名` | 在 gui_menus 下生成一份带注释的示例菜单文件，方便从零写 | `/dm create shop` |
| `delete 菜单名` | 删除指定菜单的配置文件，操作不可撤销 | `/dm delete shop` |
| `template 模板名` | 按 template 配置打开模板菜单，用于做统一风格的动态界面 | `/dm template vip` |

## 注意事项

::: warning
- YAML 对缩进极其敏感，写错一格整个菜单会加载失败；每次改完都用 /dm reload 看后台报错信息
- 菜单物品上的点击动作（left_click_commands 等）默认以玩家身份执行，要提权写 op 字段并谨慎，别把 op 动作暴露给玩家
- 替换了菜单文件的 id 或删掉菜单后，旧的打开指令、告示牌、NPC 绑定会失效
- 占位符依赖 PlaceholderAPI 及对应扩展，变量位置显示空白或原样留着一串百分号包裹的占位符时，先查 papi 扩展是否装了、/papi parse me 是否解析得出来
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `deluxemenus.admin` | 管理员指令 | op |
| `deluxemenus.menu.*` | 所有菜单的权限 | op |
| `deluxemenus.open` | 打开菜单，打开/dm &lt;menu&gt; | op |
| `deluxemenus.open.bypass` | 尝试为观众打开菜单，跳过播放器的观看要求检查 | op |
| `deluxemenus.open.others` | 打开菜单，打开/dm &lt;menu&gt; &lt;player&gt; | op |
| `deluxemenus.openrequirement.bypass.*` | 允许查看器绕过所有菜单打开要求 | op |
| `deluxemenus.placeholdersfor` | /dm open &lt;menu&gt; p解析菜单占位符的权限：&lt;player&gt; | op |
| `deluxemenus.placeholdersfor.exempt` | 当/dm为具有&lt;menu p:&lt;player&gt;此权限的玩家打开时，免于解析占位符 | op |

## 相关插件

[PlaceholderAPI](/commands/config/placeholderapi.md)、[Vault](/commands/core/vault.md)、[LuckPerms](/commands/core/luckperms.md)
