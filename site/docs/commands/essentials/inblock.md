---
title: InBlock
createTime: 2026/10/24
---

# InBlock

> 版本 `1.0.0` · 指令 1 条 · api-version `1.21` · 文件 `InBlock-1.0.0.jar`

自定义命令方块插件 —— 像工作台一样右键执行自定义指令

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/inb help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/inb` | InBlock 主命令 | — |

## 详细用法

### /inb

- **说明**：InBlock 主命令
- **用法**：`/inb open               打开仓库界面`<br>`/inb give &lt;玩家&gt; &lt;方块ID&gt; &lt;数量&gt;   给予自定义方块物品`<br>`/inb reload             重载配置`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `Inblock.give` | 允许给予自定义方块物品 | op |
| `Inblock.open` | 允许打开仓库界面 | op |
| `Inblock.reload` | 允许重载配置 | op |
