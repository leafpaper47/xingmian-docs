---
title: TAB
createTime: 2026/10/24
---

# 列表计分板 · TAB

> 分类 💬 聊天与社交 · 版本 `6.1.2` · 指令 1 条 · api-version `1.13`

::: tip TAB 列表
统一管 TAB 列表、计分板侧栏与头顶名称/血条，支持按组、按条件、按动画配置，是全服展示层的底座。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 改完配置生效 | /tab reload | 改 yml 后必须重载才看得到 |
| 看某玩家的 TAB 状态 | /tab debug Steve | 输出该玩家当前的组、属性与解析结果 |
| 看性能开销 | /tab cpu | TAB 自身占用的 CPU 统计 |
| 查看帮助 | /tab help | 列出全部子指令 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/tab` | TAB 主指令：重载、调试、性能与玩家视图 | `/tab <help｜reload｜debug｜cpu｜player>` | — |

## 指令详解

### `/tab` — TAB 主指令：重载、调试、性能与玩家视图

- **语法**：`/tab <help｜reload｜debug｜cpu｜player>`

- **示例**：

```
/tab help
```

- **备注**：命令名 tab

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/tab reload` | 重载全部配置（列表/计分板/头顶/组） | `/tab reload` |
| `/tab debug <玩家>` | 输出该玩家的组、条件与占位符解析结果 | `/tab debug Steve` |
| `/tab cpu` | 查看 TAB 的 CPU 占用统计 | `/tab cpu` |
| `/tab player <玩家>` | 以该玩家视角查看当前 TAB 输出 | `/tab player Steve` |
| `/tab help` | 打印子指令帮助 | `/tab help` |

## 注意事项

::: warning
- 改完 yml 必须 /tab reload，重载会重建全部玩家列表，玩家能看到一次闪烁。
- TAB 的条件与占位符写错不会报错，只会静默显示原样文本，排查先看 /tab debug &lt;玩家&gt;。
- TAB 与其它计分板插件（如 DeluxeMenus 侧栏、HUD 类）同时开侧栏会互相覆盖，只保留一个。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `tab.admin` | 使用 /tab 管理指令（reload / debug / cpu） | op |
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
