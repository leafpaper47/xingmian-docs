---
title: EssentialsSpawn
createTime: 2026/10/24
---

# EssentialsSpawn

> 版本 `2.22.1-dev+12-776f709` · 指令 2 条 · api-version `1.13` · 文件 `EssentialsXSpawn-2.22.1-dev+12-776f709.jar`

提供生成控制命令，利用Essentials。

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/setspawn help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/setspawn` | 将生成点设置为当前位置。 | — |
| `/spawn` | 传送到生成点。 | — |

## 详细用法

### /setspawn

- **说明**：将生成点设置为当前位置。
- **用法**：`/&lt;command&gt; &lt;group&gt;`
- **别名**：`/esetspawn`

### /spawn

- **说明**：传送到生成点。
- **用法**：`/&lt;command&gt; [player]`
- **别名**：`/espawn`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `essentials.setspawn` | Allows access to the /setspawn command | — |
| `essentials.spawn` | Allows access to the /spawn command | — |
| `essentials.spawn-on-join.exempt` | Bypass spawn teleportation on join when spawn-on-join is true | — |
| `essentials.spawn.others` | Allows access to the /spawn command for other players | — |
