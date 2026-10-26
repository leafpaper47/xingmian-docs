---
title: Skript
createTime: 2026/10/24
---

# 脚本引擎 · Skript

> 分类 🧩 脚本与菜单 · 版本 `2.16.1` · 指令 1 条 · api-version `1.21`

::: tip 脚本引擎，用接近英语的语句改写服务器机制
Skript 是服务器端的脚本引擎，用接近自然英语的语句编写 .sk 脚本，实现自定义规则、事件响应、定时任务和小游戏逻辑，不用写 Java 插件。脚本放在 plugins/Skript/scripts 下，修改后用 /skript reload 热重载，不需要重启服务器。它也是很多服主实现经济、传送、抽奖、公告等定制功能的低成本方案。
:::

## 什么时候会用到它

- 不写 Java 插件就实现自定义规则，如欢迎语、定时公告、签到奖励
- 监听玩家行为事件做相应处理，如进服提示、死亡掉落控制、区块限制
- 拼接命令与条件判断，做小游戏、任务系统、经济流程等轻量玩法
- 替代频繁改动 jar 的定制需求，改一行脚本即可热重载生效

## 上手流程

1. 把 .sk 脚本文件放到 plugins/Skript/scripts 目录，首次可先看官方示例脚本
2. 在游戏内执行 /skript reload 加载全部脚本，观察控制台是否有语法报错
3. 只改单个脚本时用 /skript reload 脚本名 单独重载，避免影响其它脚本
4. 调试阶段给自己 skript.admin 权限，并留意聊天中的运行时错误提示
5. 脚本不稳定时用 disable 临时停用，确认无误后再正式启用

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/skript` | Skript 主命令，用于查看帮助、重载与启停脚本<br>别名 `/sk` | `/skript help` | `skript.admin` |

## 指令详解

### `/skript` — Skript 主命令，用于查看帮助、重载与启停脚本

- **语法**：`/skript help`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子命令` | 可选 | help 查看帮助；reload、enable、disable、update 等，具体见子指令表 |


- **示例**：

```
/skript help
/skript reload all
/skript reload scripts
/skript update check
```

- **别名**：`/sk`
- **权限**：`skript.admin`
- **备注**：别名 sk；需要 skript.admin 权限。reload 后旧脚本的定时器会被重新注册，重载频繁会有短时卡顿。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `skript help` | 显示帮助与可用子命令列表 | `/skript help` |
| `skript reload all` | 重载脚本、配置与别名等全部内容 | `/skript reload all` |
| `skript reload scripts` | 只重载 scripts 目录下的全部脚本 | `/skript reload scripts` |
| `skript reload 脚本名` | 只重载指定脚本文件，最常见的热更新方式 | `/skript reload welcome.sk` |
| `skript reload config` | 重载 Skript 的配置文件 | `/skript reload config` |
| `skript reload aliases` | 重载 aliases 别名配置 | `/skript reload aliases` |
| `skript enable 脚本名` | 启用被禁用的脚本 | `/skript enable welcome.sk` |
| `skript disable 脚本名` | 临时禁用某个脚本 | `/skript disable welcome.sk` |
| `skript update check` | 检查 Skript 是否有新版本 | `/skript update check` |

## 注意事项

::: warning
- reload 只是重跑脚本，脚本里已创建的实体、记分板或定时任务可能残留，反复重载请观察服务器内存与 TPS
- 脚本语法错误会导致该脚本加载失败，务必看控制台或 skript.see_runtime_errors 的聊天提示，别以为已生效
- skript.effectcommands 允许把效果直接当命令用（如 !set health to 10），权限给错等于给出极大的越权能力
- disable 只在本次运行内有效，服务器重启或 reload 后会按脚本文件重新加载
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `skript.*` | — | — |
| `skript.admin` | 允许使用管理命令并接收新版本的通知。 | op |
| `skript.effectcommands` | 允许将效果用作命令，例如“! set health to 10” | — |
| `skript.reloadnotify` | 当其他人正在重新加载脚本文件时通知。 | — |
| `skript.see_runtime_errors` | 发生运行时错误时在聊天中显示通知。 | op |

## 相关插件

[PlaceholderAPI](/commands/config/placeholderapi.md)、[Vault](/commands/core/vault.md)、[LuckPerms](/commands/core/luckperms.md)、[Essentials](/commands/essentials/essentials.md)
