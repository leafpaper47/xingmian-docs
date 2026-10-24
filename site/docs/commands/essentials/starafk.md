---
title: StarAFK
createTime: 2026/10/24
---

# StarAFK

> 版本 `0.2.0` · 指令 1 条 · api-version `1.21` · 文件 `StarAFK-0.2.0.jar`

星冕服挂机插件 —— 自动/手动 AFK、Tab 图标、头顶飘 Zzz、视距降低

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/afk help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/afk` | 切换挂机状态；/afk reload 重载配置 | — |

## 详细用法

### /afk

- **说明**：切换挂机状态；/afk reload 重载配置
- **用法**：`/afk [reload]`
- **别名**：`/starafk`、`/guaji`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `starafk.auto` | 参与自动挂机判定 | True |
| `starafk.bypass` | 永不被自动挂机（不进 AFK 状态）。默认不授予任何人，需要豁免时用 LuckPerms 单独给 | — |
| `starafk.reload` | 允许 /afk reload | op |
| `starafk.silent` | 其进出 AFK 不广播。默认不授予任何人，需要静默时用 LuckPerms 单独给 | — |
| `starafk.use` | 允许使用 /afk | True |
