---
title: PlugManX
createTime: 2026/10/24
---

# 插件热管 · PlugManX

> 分类 🛡️ 基础与权限 · 版本 `3.1.0-Beta.2` · 指令 1 条 · api-version `1.13`

::: tip 插件热管，不关服就能装、卸、启停插件
PlugManX 是 Bukkit 系服务端（Paper/Spigot 等）的插件管理器，能列出、查看、启用、禁用、加载、卸载、重载单个插件，全程不需要重启整个服务器。它负责的是插件生命周期的热操作，配合权限插件（如 LuckPerms）分配 plugman 系列权限即可交给指定管理员使用。日常改配置、临时关插件排查报错、装新插件试水，都靠它省一次重启。
:::

## 什么时候会用到它

- 改完某个插件的配置文件，只想让它自己重读生效，不想停服影响其他人
- 装上新下载的插件 jar，想先加载试跑，出问题立刻卸掉
- 某个插件刷屏报错或卡服，需要临时禁用排查，又不想全服重启
- 想知道某条指令到底是被哪个插件注册的，或者某插件占了哪些指令

## 上手流程

1. 先 /plugman list 看清服务器上装了哪些插件、哪些没启用
2. /plugman info 插件名 看版本、作者、依赖关系和当前状态
3. 改完配置用 /plugman reload 插件名 让它重读；新插件用 /plugman load 插件名
4. 效果不对就 /plugman disable 插件名 回退，必要时 /plugman reloadmode 调整重载模式

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/plugman` | 插件热管的唯一入口，靠子指令完成列出、启停、加载、重载、排查<br>别名 `/plm` | `/plugman (help｜dump｜reloadconfig) 或 /plugman list …` | `plugman.help` |

## 指令详解

### `/plugman` — 插件热管的唯一入口，靠子指令完成列出、启停、加载、重载、排查

- **语法**：`/plugman (help｜dump｜reloadconfig) 或 /plugman list [-v] 或 /plugman check 插件名或all [-f] 或 /plugman lookup 指令名 或 /plugman deps 插件名 或 /plugman (enable｜disable｜restart) 插件名或all 或 /plugman (info｜usage｜load｜reload｜unload) 插件名 或 /plugman reloadmode 模式`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子指令` | 必填 | help、dump、list、check、lookup、deps、enable、disable、restart、info、usage、load、reload、unload、reloadconfig、reloadmode 之一 |
| `插件名` | 必填 | 插件的准确名称，可用 Tab 补全；enable、disable、restart、check 还接受 all |
| `指令名` | 可选 | lookup 用，写不带斜杠的指令名，用来反查是哪个插件注册的 |
| `模式` | 可选 | reloadmode 用，取值 ALL、REQUIRED_ONLY、OFF，控制重载时连带处理哪些插件 |


- **示例**：

```
/plugman list
/plugman info Essentials
/plugman reload Essentials
/plugman disable Essentials
/plugman lookup home
/plugman deps Essentials
/plugman reloadmode REQUIRED_ONLY
```

- **别名**：`/plm`
- **权限**：`plugman.help`
- **备注**：别名 /plm；每个子指令都有独立权限节点（如 plugman.reload、plugman.disable.all），只给 plugman.admin 相当于全开；插件名写错不会帮你猜，大小写一般要与插件 jar 内的名称一致。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `help` | 列出 PlugManX 的所有子指令与用法 | `/plugman help` |
| `list [-v]` | 列出全部插件；加 -v 显示版本号 | `/plugman list -v` |
| `info 插件名` | 查看单个插件的版本、作者、依赖、已注册指令等详情 | `/plugman info Essentials` |
| `usage 插件名` | 列出该插件注册了哪些指令 | `/plugman usage Essentials` |
| `lookup 指令名` | 反查某条指令是由哪个插件注册的 | `/plugman lookup home` |
| `deps 插件名` | 查看该插件的依赖关系（谁依赖它、它依赖谁） | `/plugman deps Essentials` |
| `check 插件名或all [-f]` | 检查插件依赖是否齐全；加 -f 强制检查全部 | `/plugman check Essentials` |
| `enable 插件名或all` | 启用已禁用但仍在内存中的插件 | `/plugman enable Essentials` |
| `disable 插件名或all` | 禁用插件但不卸载，配置文件与文件本体保留 | `/plugman disable Essentials` |
| `restart 插件名或all` | 等于先禁用再启用，用于让插件重新初始化 | `/plugman restart Essentials` |
| `load 插件名` | 把放在 plugins 目录但尚未载入的插件加载进来 | `/plugman load Essentials` |
| `unload 插件名` | 从运行中彻底卸载插件（比 disable 更彻底） | `/plugman unload Essentials` |
| `reload 插件名` | 重新加载插件，常用别名式做法是先 unload 再 load | `/plugman reload Essentials` |
| `reloadconfig` | 重载 PlugManX 自身的配置文件 | `/plugman reloadconfig` |
| `reloadmode 模式` | 设置重载模式：ALL 连带依赖、REQUIRED_ONLY 只处理必需的、OFF 关闭连带 | `/plugman reloadmode REQUIRED_ONLY` |
| `dump` | 导出插件与指令的完整清单文本，方便排查冲突或反馈问题 | `/plugman dump` |

## 注意事项

::: warning
- 热重载不等于干净重启：很多插件 reload 后会残留旧的监听器、任务和缓存，可能造成事件重复触发或内存缓慢上涨，重要更新还是安排重启
- disable all、unload all、restart all 会波及整个服务器上所有插件，容易连带把依赖它们的插件拖挂，正式服不要随手用
- reloadmode 设为 ALL 时重载会顺带重启所有依赖插件，一次操作可能掀翻半个服；不确定就先用 REQUIRED_ONLY 或 OFF
- 找不到插件名时先用 /plugman list 复制准确名称，写错或大小写不符会直接失败；操作前建议先备份 plugins 目录
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

## 相关插件

PlugMan、[spark](/commands/audit/spark.md)
