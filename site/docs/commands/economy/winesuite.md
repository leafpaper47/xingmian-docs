---
title: WineSuite
createTime: 2026/10/24
---

# WineSuite

> 版本 `1.2.0` · 指令 2 条 · api-version `1.21` · 文件 `WineSuite-1.2.0.jar`

星冕酒水套装：酿酒图鉴 + 酒水收购 合并插件，自动跟随主酿造插件 TBP 的配方变动。

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/winebook help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/winebook` | 打开酿酒图鉴 | — |
| `/winebuyer` | 打开酒水收购界面 | — |

## 详细用法

### /winebook

- **说明**：打开酿酒图鉴
- **用法**：`/winebook [reload]`
- **别名**：`/酒鉴`、`/酿酒图鉴`、`/图鉴`、`/wbk`

### /winebuyer

- **说明**：打开酒水收购界面
- **用法**：`/winebuyer [list|reload|reset]`
- **别名**：`/wb`、`/收酒`、`/酒收`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `winebook.admin` | 允许管理图鉴 | op |
| `winebook.use` | 允许使用酿酒图鉴 | True |
| `winebuyer.admin` | 允许重载/重置收购配置 | op |
| `winebuyer.use` | 允许使用酒水收购 | True |
