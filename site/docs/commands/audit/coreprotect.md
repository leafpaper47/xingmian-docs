---
title: CoreProtect
createTime: 2026/10/24
---

# CoreProtect

> 版本 `24.2-dev` · 指令 1 条 · api-version `1.16` · 文件 `CoreProtect-24.2-dev-zh.jar`

为你的服务器提供方块保护。

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/co help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/co` | 使用该插件 | `coreprotect.co` |

## 详细用法

### /co

- **说明**：使用该插件
- **用法**：`/&lt;command&gt; &lt;params&gt;`
- **权限**：`coreprotect.co`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `coreprotect.*` | 授予所有 CoreProtect 操作与命令的访问权限 | op |
| `coreprotect.co` | 拥有访问 CoreProtect /co 命令的权限 | True |
| `coreprotect.consumer` | 拥有使用消费者命令的权限 | op |
| `coreprotect.core` | 拥有访问 CoreProtect /core 命令的权限 | — |
| `coreprotect.coreprotect` | 拥有访问 CoreProtect /coreprotect 命令的权限 | — |
| `coreprotect.give` | 拥有使用 give 命令的权限 | — |
| `coreprotect.help` | 拥有使用帮助命令的权限 | op |
| `coreprotect.inspect` | 拥有使用检查模式的权限 | op |
| `coreprotect.lookup` | 拥有使用查询命令的权限 | op |
| `coreprotect.lookup.block` | 拥有查询方块数据的权限 | op |
| `coreprotect.lookup.chat` | 拥有查询聊天消息的权限 | op |
| `coreprotect.lookup.click` | 拥有查询玩家交互的权限 | op |
| `coreprotect.lookup.command` | 拥有查询玩家命令的权限 | op |
| `coreprotect.lookup.container` | 拥有查询容器交易的权限 | op |
| `coreprotect.lookup.inventory` | 拥有查询背包交易的权限 | op |
| `coreprotect.lookup.item` | 拥有查询物品交易的权限 | op |
| `coreprotect.lookup.kill` | 拥有查询实体击杀的权限 | op |
| `coreprotect.lookup.near` | 拥有使用 near 命令查询附近改动的权限 | op |
| `coreprotect.lookup.session` | 拥有查询玩家会话的权限 | op |
| `coreprotect.lookup.sign` | 拥有查询告示牌消息的权限 | op |
| `coreprotect.lookup.spawn` | 拥有查询实体生成的权限 | op |
| `coreprotect.lookup.username` | 拥有查询玩家改名记录的权限 | op |
| `coreprotect.networking` | 拥有使用网络 API 的权限 | op |
| `coreprotect.purge` | 拥有使用清理命令的权限 | op |
| `coreprotect.reload` | 拥有使用重载命令的权限 | op |
| `coreprotect.restore` | 拥有执行恢复的权限 | op |
| `coreprotect.rollback` | 拥有执行回滚的权限 | op |
| `coreprotect.status` | 拥有使用状态命令的权限 | op |
| `coreprotect.teleport` | 拥有使用传送命令的权限 | op |
