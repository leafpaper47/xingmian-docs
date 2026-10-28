---
title: DeluxeMenus
createTime: 2026/10/24
---

# GUI菜单 · DeluxeMenus

> 分类 🧩 脚本与菜单 · 版本 `1.14.1-Release` · 指令 1 条 · api-version `1.13`

::: tip GUI 菜单
用 YAML 定义箱子菜单：按钮、图标、点击动作全配置化，服务端的商店、传送、活动面板基本都靠它。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 打开某个菜单 | /dm open shop | 菜单名就是 gui_menu 里的名字 |
| 帮别人打开菜单 | /dm open shop Steve | 活动/补偿时批量发面板用 |
| 改完菜单生效 | /dm reload | 改 yml 必须重载，改完不重载等于没改 |
| 看有哪些菜单 | /dm list | 含菜单名与权限要求 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/deluxemenus` | 菜单主指令：打开、列表、重载、调试<br>别名 `/dm`、`/deluxemenu`、`/dmenu` | `/dm <open｜list｜reload｜execute｜dump｜meta｜help>` | — |

## 指令详解

### `/deluxemenus` — 菜单主指令：打开、列表、重载、调试

- **语法**：`/dm <open｜list｜reload｜execute｜dump｜meta｜help>`

- **示例**：

```
/dm list
```

- **别名**：`/dm`、`/deluxemenu`、`/dmenu`
- **备注**：别名 /dm

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/dm open <菜单> [玩家]` | 打开指定菜单，可指定目标玩家 | `/dm open shop Steve` |
| `/dm list` | 列出全部菜单及其所需权限 | `/dm list` |
| `/dm reload` | 重载所有菜单配置 | `/dm reload` |
| `/dm execute <动作>` | 直接执行配置里的某个动作（调试用） | `/dm execute '[console] say hi'` |
| `/dm dump` | 导出当前菜单/物品/动作的诊断快照 | `/dm dump` |
| `/dm meta` | 查看或设置菜单的元数据（ContextKeys） | `/dm meta` |
| `/dm help` | 打印子指令帮助 | `/dm help` |

## 注意事项

::: warning
- 菜单按钮写了 `[console]` 动作就等于把控制台权限交给了配置，只给可信任的人改 yml。
- 重载只重载菜单，不动已打开的 GUI：改完要玩家关掉重开才看得到效果。
- 菜单里引用 %占位符% 依赖 PlaceholderAPI，变量名错会原样显示而不是报错，很隐蔽。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `deluxemenus.admin` | 管理员（execute / dump / meta） | op |
| `deluxemenus.list` | 查看菜单列表 | — |
| `deluxemenus.menu.*` | 所有菜单的权限 | op |
| `deluxemenus.open` | 打开菜单（各菜单还可单独限权） | op |
| `deluxemenus.open.bypass` | 尝试为观众打开菜单，跳过播放器的观看要求检查 | op |
| `deluxemenus.open.others` | 打开菜单，打开/dm &lt;menu&gt; &lt;player&gt; | op |
| `deluxemenus.openrequirement.bypass.*` | 允许查看器绕过所有菜单打开要求 | op |
| `deluxemenus.placeholdersfor` | /dm open &lt;menu&gt; p解析菜单占位符的权限：&lt;player&gt; | op |
| `deluxemenus.placeholdersfor.exempt` | 当/dm为具有&lt;menu p:&lt;player&gt;此权限的玩家打开时，免于解析占位符 | op |
| `deluxemenus.reload` | 重载菜单 | — |
