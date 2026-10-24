---
title: PlugManX
createTime: 2026/10/24
---

# PlugManX

> 版本 `3.1.0-Beta.2` · 指令 1 条 · api-version `1.13` · 文件 `PlugManX-3.1.0-Beta.2.jar`

Bukkit服务器的插件管理器

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/plugman help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/plugman` | 管理插件 | `plugman.help` |

## 详细用法

### /plugman

- **说明**：管理插件
- **用法**：`/plugman (help|dump) /plugman list [-v] /plugman check &lt;plugin|all&gt; [-f] /plugman lookup &lt;command&gt; /plugman deps &lt;plugin&gt; /plugman (enable|disable|restart) &lt;plugin|all&gt; /plugman (info|usage|load|reload|unload) &lt;plugin&gt; /plugman reloadconfig /plugman reloadmode [ALL|REQUIRED_ONLY|OFF]`
- **别名**：`/plm`
- **权限**：`plugman.help`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `plugman.admin` | 允许使用所有PlugMan命令。 | op |
| `plugman.check` | 允许使用check命令。 | op |
| `plugman.check.all` | 允许使用check all命令。 | op |
| `plugman.deps` | 允许使用deps命令。 | op |
| `plugman.disable` | 允许使用disable命令。 | op |
| `plugman.disable.all` | 允许使用disable all命令。 | op |
| `plugman.dump` | 允许使用dump命令。 | op |
| `plugman.enable` | 允许使用enable命令。 | op |
| `plugman.enable.all` | 允许使用enable all命令。 | op |
| `plugman.help` | 允许使用help命令。 | op |
| `plugman.info` | 允许使用info命令。 | op |
| `plugman.list` | 允许使用list命令。 | op |
| `plugman.load` | 允许使用load命令。 | op |
| `plugman.lookup` | 允许使用查找命令。 | op |
| `plugman.reload` | 允许使用reload命令。 | op |
| `plugman.reloadconfig` | 允许使用reload config命令。 | op |
| `plugman.reloadmode` | 允许使用reload mode命令。 | op |
| `plugman.restart` | 允许使用重新启动命令。 | op |
| `plugman.restart.all` | 允许使用RESTART ALL命令。 | op |
| `plugman.unload` | 允许使用unload命令。 | op |
| `plugman.update` | 允许玩家查看更新警报。 | op |
| `plugman.usage` | 允许使用usage命令。 | op |
