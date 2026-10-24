---
title: PlugManX
createTime: 2026/10/24
---

# PlugManX

> 版本 `3.1.0-Beta.2` · 指令 1 条 · api-version `1.13` · 文件 `PlugManX-3.1.0-Beta.2.jar`

Plugin manager for Bukkit servers

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/plugman help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/plugman` | Manage plugins. | `plugman.help` |

## 详细用法

### /plugman

- **说明**：Manage plugins.
- **用法**：`/plugman (help|dump) /plugman list [-v] /plugman check &lt;plugin|all&gt; [-f] /plugman lookup &lt;command&gt; /plugman deps &lt;plugin&gt; /plugman (enable|disable|restart) &lt;plugin|all&gt; /plugman (info|usage|load|reload|unload) &lt;plugin&gt; /plugman reloadconfig /plugman reloadmode [ALL|REQUIRED_ONLY|OFF]`
- **别名**：`/plm`
- **权限**：`plugman.help`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `plugman.admin` | Allows use of all PlugMan commands. | op |
| `plugman.check` | Allows use of the check command. | op |
| `plugman.check.all` | Allows use of the check all command. | op |
| `plugman.deps` | Allows use of the deps command. | op |
| `plugman.disable` | Allows use of the disable command. | op |
| `plugman.disable.all` | Allows use of the disable all command. | op |
| `plugman.dump` | Allows use of the dump command. | op |
| `plugman.enable` | Allows use of the enable command. | op |
| `plugman.enable.all` | Allows use of the enable all command. | op |
| `plugman.help` | Allows use of the help command. | op |
| `plugman.info` | Allows use of the info command. | op |
| `plugman.list` | Allows use of the list command. | op |
| `plugman.load` | Allows use of the load command. | op |
| `plugman.lookup` | Allows use of the lookup command. | op |
| `plugman.reload` | Allows use of the reload command. | op |
| `plugman.reloadconfig` | Allows use of the reload config command. | op |
| `plugman.reloadmode` | Allows use of the reload mode command. | op |
| `plugman.restart` | Allows use of the restart command. | op |
| `plugman.restart.all` | Allows use of the restart all command. | op |
| `plugman.unload` | Allows use of the unload command. | op |
| `plugman.update` | Allows the player to see the update alerts. | op |
| `plugman.usage` | Allows use of the usage command. | op |
