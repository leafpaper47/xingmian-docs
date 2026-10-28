---
title: PlugManX
createTime: 2026/10/24
---

# 插件管理 · PlugManX

> 分类 🛡️ 基础与权限 · 版本 `3.1.0-Beta.2` · 指令 1 条 · api-version `1.13`

::: tip 插件热管理
不重启服务器就能卸载、装载、重载单个插件，并检查插件依赖与命令占用，装新插件、救崩溃插件的首选工具。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 重载某个插件 | /plugman reload Essentials | 多数插件重载后配置才生效 |
| 看谁占了这个命令 | /plugman lookup sit | 排查命令冲突最直接 |
| 看插件依赖关系 | /plugman deps Essentials | 决定卸载顺序，别把被依赖的卸了 |
| 全部插件列表 | /plugman list | 带状态与版本 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/plugman` | 插件热管理主指令<br>别名 `/plm` | `/plugman <list｜info｜load｜unload｜reload｜enable｜disa…` | `plugman.help` |

## 指令详解

### `/plugman` — 插件热管理主指令

- **语法**：`/plugman <list｜info｜load｜unload｜reload｜enable｜disable｜check｜deps｜lookup｜usage｜dump｜help>`

- **示例**：

```
/plugman list
```

- **别名**：`/plm`
- **权限**：`plugman.help`
- **备注**：别名 /pm

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/plugman list` | 列出全部插件与启用状态 | `/plugman list` |
| `/plugman info <插件>` | 查看插件版本、作者、依赖与命令 | `/plugman info Essentials` |
| `/plugman load <插件/jar>` | 装载新插件（不重启） | `/plugman load MyPlugin.jar` |
| `/plugman unload <插件>` | 卸载插件并从内存移除 | `/plugman unload MyPlugin` |
| `/plugman reload <插件>` | 重载插件（= unload + load） | `/plugman reload Essentials` |
| `/plugman enable <插件>` | 启用已加载但被禁用的插件 | `/plugman enable MyPlugin` |
| `/plugman disable <插件>` | 禁用插件但保留在内存中 | `/plugman disable MyPlugin` |
| `/plugman check <插件>` | 检查插件完整性与可安全重载性 | `/plugman check Essentials` |
| `/plugman deps <插件>` | 查看依赖链（含反向依赖） | `/plugman deps Essentials` |
| `/plugman lookup <命令>` | 查询某个命令被哪个插件注册 | `/plugman lookup sit` |
| `/plugman usage <插件>` | 查看插件注册的全部命令与用法 | `/plugman usage Essentials` |
| `/plugman dump` | 导出插件环境诊断（反馈问题用） | `/plugman dump` |
| `/plugman restart` | 重启服务器（等价于安全重载全部） | `/plugman restart` |
| `/plugman reloadconfig` | 重载 PlugManX 自身配置 | `/plugman reloadconfig` |

## 注意事项

::: warning
- reload 一个插件不会重载它注册的任务与已打开的会话，很多插件「重载后行为怪」还是得重启。
- unload 被其他插件依赖的插件会连带把依赖方打挂，先 /plugman deps 看清方向。
- 正在写入数据的插件（CoreProtect、经济类）别热重载，可能造成数据库句柄泄漏或事务中断。
:::

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
| `plugman.list` | 查看插件列表与信息 | op |
| `plugman.load` | 装载插件 | op |
| `plugman.lookup` | 查询命令归属 | op |
| `plugman.reload` | 重载插件 | op |
| `plugman.reloadconfig` | 允许使用reload config命令。 | op |
| `plugman.reloadmode` | 允许使用reload mode命令。 | op |
| `plugman.restart` | 允许使用重新启动命令。 | op |
| `plugman.restart.all` | 允许使用RESTART ALL命令。 | op |
| `plugman.unload` | 卸载插件 | op |
| `plugman.update` | 允许玩家查看更新警报。 | op |
| `plugman.usage` | 允许使用usage命令。 | op |
