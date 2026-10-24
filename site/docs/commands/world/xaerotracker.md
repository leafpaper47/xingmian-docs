---
title: XaeroTracker
createTime: 2026/10/24
---

# XaeroTracker

> 版本 `1.4.0-xm` · 指令 1 条 · api-version `1.20` · 文件 `XaeroTracker-1.4.0-xm.jar`

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/xaerotracker help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/xaerotracker` | XaeroTracker 主命令 | `xaerotracker.use` |

## 详细用法

### /xaerotracker

- **说明**：XaeroTracker 主命令
- **用法**：`/xt &lt;tracked|town|seeall&gt;`
- **别名**：`/xt`
- **权限**：`xaerotracker.use`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `xaerotracker.*` | XaeroTracker 全部权限 | — |
| `xaerotracker.admin` | 管理其他玩家的追踪设置 | — |
| `xaerotracker.seeall` | 看得见地图上的所有玩家。默认连 OP 也不拥有 | — |
| `xaerotracker.town` | 开关是否看得见同镇成员 | True |
| `xaerotracker.tracked` | 开关自己是否被追踪 | True |
| `xaerotracker.tracker` | 追踪指定玩家（动态权限，实际为 xaerotracker.tracker.&lt;玩家名&gt;） | — |
| `xaerotracker.use` | 使用 /xt 命令 | True |
