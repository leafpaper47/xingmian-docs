---
title: TAB
createTime: 2026/10/24
---

# 列表计分板 · TAB

> 分类 💬 聊天与社交 · 版本 `6.1.2` · 指令 1 条 · api-version `1.13`

::: tip 统一管理 TAB 列表、计分板、侧边栏与名称标签
TAB 是服务端最常用的一体化显示插件，负责玩家列表（TAB 键列表）的排版、排序、前缀后缀、血条与延迟显示，同时接管计分板、BossBar 与头顶名称标签。所有显示内容都由 config.yml 与 groups.yml 里的组和占位符渲染，支持 PlaceholderAPI 变量。日常运维主要用 /tab reload 重载配置、/tab cpu 看性能开销、/tab parse 调试占位符输出。
:::

## 什么时候会用到它

- 自定义 TAB 玩家列表的列数、排序、血量与延迟显示
- 按权限组给不同玩家配置前缀、后缀、颜色
- 统一管理侧边栏计分板与多人 BossBar 显示
- 调试占位符在 TAB 里的实际解析结果
- 重载 TAB 配置而不用重启服务器

## 上手流程

1. 先安装 PlaceholderAPI 与权限插件（LuckPerms 等），确认占位符可用
2. 编辑 plugins/TAB/config.yml 与 groups.yml，写好组、排序与显示内容
3. 在游戏内执行 /tab reload 载入，若报错先看控制台的具体行号
4. 用 /tab parse 玩家 占位符 验证变量是否输出预期，再 /tab cpu 观察开销
5. 确认无误后给管理组分配 tab.admin 或按需细分权限节点

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/tab` | TAB 主命令，重载配置、查看状态与调试显示 | `/tab 子指令` | — |

## 指令详解

### `/tab` — TAB 主命令，重载配置、查看状态与调试显示

- **语法**：`/tab 子指令`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子指令` | 必填 | 如 reload、cpu、dump、group、parse 等，详见子指令表 |


- **示例**：

```
/tab reload
/tab cpu
/tab dump Steve
```

- **备注**：多数子指令需要对应权限节点（tab.reload、tab.cpu 等），只给 tab.admin 一次性全开更省事。配置写错时 reload 会整段报错并保留旧配置，改完务必回看控制台。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `reload` | 重载 config.yml 与 groups.yml 等配置 | `/tab reload` |
| `cpu` | 查看 TAB 的 CPU 占用与刷新开销统计 | `/tab cpu` |
| `dump 玩家名` | 导出该玩家当前的 TAB 数据，排错用 | `/tab dump Steve` |
| `group` | 列出当前已定义的所有组 | `/tab group` |
| `group 组名` | 查看某个组的具体配置与生效成员 | `/tab group default` |
| `parse 玩家名 占位符` | 查看占位符对该玩家的解析结果 | `/tab parse Steve %player_health%` |
| `setcollision 玩家名 true 或 false` | 设置玩家是否与其他玩家发生碰撞 | `/tab setcollision Steve false` |
| `bossbar toggle [玩家]` | 开关某个玩家的 BossBar 显示 | `/tab bossbar toggle Steve` |
| `bossbar announce 名称 秒数` | 向全服公告一条 BossBar，持续指定秒数 | `/tab bossbar announce restart 10` |
| `bossbar send 玩家名 名称` | 把指定 BossBar 单独发给某个玩家 | `/tab bossbar send Steve restart` |
| `announce bar 名称 秒数` | 公告类 BossBar 的另一种写法，效果同上 | `/tab announce bar restart 10` |
| `announce scoreboard 名称 秒数` | 临时用指定计分板覆盖玩家侧边栏若干秒 | `/tab announce scoreboard event 15` |
| `scoreboard toggle [玩家]` | 开关侧边栏计分板显示 | `/tab scoreboard toggle` |
| `scoreboard show 名称 [玩家]` | 让玩家显示某个自定义计分板 | `/tab scoreboard show default Steve` |
| `nametag toggle [玩家]` | 开关头顶名称标签显示 | `/tab nametag toggle` |
| `mysql download` | 从 MySQL 拉取数据覆盖本地数据 | `/tab mysql download` |
| `mysql upload` | 把本地数据上传到 MySQL | `/tab mysql upload` |

## 注意事项

::: warning
- TAB 的刷新非常频繁，占位符写得过多或用重查询占位符（如跨库统计）会明显拉高 CPU，上线前用 /tab cpu 实测
- properties 里用错占位符不会报错，只会显示空白或原文，务必用 /tab parse 逐个验证
- reload 只重载配置，某些结构性改动（如切换 MySQL、改刷新机制）建议整服重启才完全生效
- 与其他改 TAB 列表、名称标签的插件（如部分聊天/昵称插件）容易互相覆盖，冲突时先停用另一方
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `tab.admin` | 授予所有标签页权限 | op |
| `tab.announce.bar` | 允许玩家运行/tab bossbar公告 | op |
| `tab.announce.scoreboard` | 允许玩家运行/tab 计分板公告 | op |
| `tab.bossbar.toggle` | 允许玩家运行/tab bossbar | op |
| `tab.bypass` | 如果启用了绕过权限，则使每个世界玩家列表的玩家绕过 | op |
| `tab.change.*` | 允许玩家使用命令更改属性 | op |
| `tab.cpu` | 允许播放器运行/tab cpu | op |
| `tab.dump` | 允许播放器运行/tab 转储 &lt;player&gt; | op |
| `tab.group.*` | 如果通过权限分配，则考虑组中的玩家 | op |
| `tab.groupinfo` | 允许播放器运行/tab 组 &lt;group&gt; | op |
| `tab.grouplist` | 允许玩家运行/tab 组 | op |
| `tab.mysql.download` | 允许播放器运行/tab mysql下载 | op |
| `tab.mysql.upload` | 允许播放器运行/tab mysql上传 | op |
| `tab.nametag.toggle` | 允许玩家运行/tab 名称标签切换 | op |
| `tab.nametag.toggle.other` | 允许玩家运行/tab 名称标签切换[其他玩家] | op |
| `tab.parse` | 允许播放器运行/tab 解析 &lt;player&gt; &lt;placeholder&gt; | op |
| `tab.reload` | 允许播放器运行/tab 重新加载 | op |
| `tab.remove` | 允许玩家使用命令删除组/user | op |
| `tab.scoreboard.show` | 允许玩家运行/tab 记分板显示 | op |
| `tab.scoreboard.show.other` | 允许玩家为其他玩家运行/tab 计分板显示 | op |
| `tab.scoreboard.toggle` | 允许玩家运行/tab 记分板 | op |
| `tab.scoreboard.toggle.other` | 允许玩家为其他玩家运行/tab 记分板 | op |
| `tab.seevanished` | 将玩家标记为能够看到消失的玩家，因为功能挂钩到消失的插件中 | op |
| `tab.send.bar` | 允许玩家运行/tab BOSSBAR发送 | op |
| `tab.setcollision` | 允许玩家运行/tab setcollision &lt;player&gt; &lt;true/false&gt; | op |
| `tab.spectatorbypass` | 使玩家绕过旁观者修复 | op |
| `tab.staff` | 使玩家在% staffonline %占位符中计数 | op |
| `tab.tabcomplete` | 允许玩家完成所有选项卡命令 | op |

## 相关插件

[PlaceholderAPI](/commands/config/placeholderapi.md)、[LuckPerms](/commands/core/luckperms.md)、[Vault](/commands/core/vault.md)、[Essentials](/commands/essentials/essentials.md)
