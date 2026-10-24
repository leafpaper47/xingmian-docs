---
title: ArchitectPlugin
createTime: 2026/10/24
---

# ArchitectPlugin

> 版本 `1.3.7` · 指令 4 条 · api-version `1.21` · 文件 `ArchitectPlugin-1.3.7.jar`

星冕服务器建筑师认证与雇佣插件

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/arch help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/arch` | 建筑师界面（注册/认证/接单/晋升进度） | — |
| `/archadmin` | 管理员界面（系统任务/申诉处理/邀请首席/调试模式） | `architect.admin` |
| `/archshop` | 建材商店（资深/architect.shop/管理员） | — |
| `/task` | 玩家任务发布界面（发布/我的发布/评价/申诉/加价） | — |

## 详细用法

### /arch

- **说明**：建筑师界面（注册/认证/接单/晋升进度）
- **用法**：`/arch`

### /archadmin

- **说明**：管理员界面（系统任务/申诉处理/邀请首席/调试模式）
- **用法**：`/archadmin`
- **权限**：`architect.admin`

### /archshop

- **说明**：建材商店（资深/architect.shop/管理员）
- **用法**：`/archshop`

### /task

- **说明**：玩家任务发布界面（发布/我的发布/评价/申诉/加价）
- **用法**：`/task`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `architect.admin` | 建筑师插件管理员 | op |
| `architect.shop` | 建材商店使用权（资深及以上默认可进，本权限用于单独开通） | op |
| `architect.use` | 使用建筑师插件 | True |
