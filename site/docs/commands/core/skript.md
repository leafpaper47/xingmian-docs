---
title: Skript
createTime: 2026/10/24
---

# 脚本引擎 · Skript

> 分类 🛡️ 权限与底座 · 版本 `2.16.1` · 指令 1 条 · api-version `1.21`

::: tip 脚本引擎
用接近自然语言的脚本给服务器加功能，不用编译 jar；本服的自定义玩法（亲密度旁听、摸头、kiss 等）都靠它驱动。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 改完脚本生效 | /sk reload &lt;脚本名&gt; | 只重载一个脚本，最快 |
| 全量重载 | /sk reload all | 脚本多时会有明显卡顿 |
| 看脚本报错 | /sk info | 列出已加载脚本与错误数 |
| 临时关掉某脚本 | /sk disable &lt;脚本名&gt; | 排障用，不用删文件 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/skript` | 脚本引擎主指令<br>别名 `/sk` | `/sk <reload｜enable｜disable｜info｜update｜help>` | `skript.admin` |

## 指令详解

### `/skript` — 脚本引擎主指令

- **语法**：`/sk <reload｜enable｜disable｜info｜update｜help>`

- **示例**：

```
/sk info
```

- **别名**：`/sk`
- **权限**：`skript.admin`
- **备注**：命令名 skript，常用别名 /sk

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/sk reload <脚本｜all>` | 重载指定脚本或全部脚本 | `/sk reload kiss` |
| `/sk enable <脚本>` | 启用某个脚本 | `/sk enable kiss` |
| `/sk disable <脚本>` | 禁用某个脚本（保留文件） | `/sk disable kiss` |
| `/sk info` | 查看已加载脚本清单、变量与错误统计 | `/sk info` |
| `/sk update` | 检查 Skript 本体与 addon 更新 | `/sk update` |
| `/sk help` | 打印子指令帮助 | `/sk help` |

## 注意事项

::: warning
- reload all 会短暂阻塞主线程，脚本多的时候玩家能感到卡顿，线上优先单脚本重载。
- 脚本变量存在 variables.db（SQLite），删掉它等于清空所有脚本存档，动之前先备份。
- 脚本里的 `on command` 会抢占同名命令，命令冲突先用 /plugman lookup 查清楚。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `skript.*` | — | — |
| `skript.admin` | 使用 /sk 管理脚本（reload / enable / disable） | op |
| `skript.effectcommands` | 允许将效果用作命令，例如“! set health to 10” | — |
| `skript.reloadnotify` | 当其他人正在重新加载脚本文件时通知。 | — |
| `skript.see_runtime_errors` | 发生运行时错误时在聊天中显示通知。 | op |
