---
title: OpenInv
createTime: 2026/10/24
---

# OpenInv

> 版本 `5.3.3` · 指令 10 条 · api-version `1.13` · 文件 `OpenInv.jar`

Open a player's inventory as a chest and interact with it in real time.

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/anycontainer help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/anycontainer` | AnyContainer allows using blocked containers. | `openinv.container.any` |
| `/clearender` | Clear a player's ender chest | `openinv.clear.self;openinv.clear.other` |
| `/clearinv` | Clear a player's inventory | `openinv.clear.self;openinv.clear.other` |
| `/openender` | Open a player's ender chest | `openinv.enderchest.open.self;openinv.enderchest.open.other` |
| `/openinv` | Open a player's inventory | `openinv.inventory.open.self;openinv.inventory.open.other` |
| `/searchcontainer` | Search and list containers with a specific material. | `openinv.search.container` |
| `/searchenchant` | Search and list players with a specific enchantment. | `openinv.search.inventory` |
| `/searchender` | Search and list players having a specific item in their ender chest | `openinv.search.inventory` |
| `/searchinv` | Search and list players having a specific item | `openinv.search.inventory` |
| `/silentcontainer` | SilentContainer stops sounds and animations when using containers. | `openinv.container.silent` |

## 详细用法

### /anycontainer

- **说明**：AnyContainer allows using blocked containers.
- **用法**：`/&lt;command&gt; [check|on|off] - Check, toggle, or set AnyContainer`
- **别名**：`/ac`、`/anychest`
- **权限**：`openinv.container.any`

### /clearender

- **说明**：Clear a player's ender chest
- **用法**：`/&lt;command&gt; [Player] - Clear a player's ender chest`
- **权限**：`openinv.clear.self;openinv.clear.other`

### /clearinv

- **说明**：Clear a player's inventory
- **用法**：`/&lt;command&gt; [Player] - Clear a player's inventory`
- **权限**：`openinv.clear.self;openinv.clear.other`

### /openender

- **说明**：Open a player's ender chest
- **用法**：`/&lt;command&gt; [Player] - Open a player's ender chest`
- **别名**：`/oe`
- **权限**：`openinv.enderchest.open.self;openinv.enderchest.open.other`

### /openinv

- **说明**：Open a player's inventory
- **用法**：`/&lt;command&gt; [Player] - Open a player's inventory`
- **别名**：`/oi`、`/inv`、`/open`
- **权限**：`openinv.inventory.open.self;openinv.inventory.open.other`

### /searchcontainer

- **说明**：Search and list containers with a specific material.
- **用法**：`/&lt;command&gt; &lt;Material&gt; [ChunkRadius] - ChunkRadius is optional, the length that will be searched for matching items. Default 5`
- **别名**：`/searchchest`
- **权限**：`openinv.search.container`

### /searchenchant

- **说明**：Search and list players with a specific enchantment.
- **用法**：`/&lt;command&gt; &lt;[Enchantment] [MinLevel]&gt; - Enchantment is the enchantment type, MinLevel is the minimum level. One is optional`
- **别名**：`/searchenchants`
- **权限**：`openinv.search.inventory`

### /searchender

- **说明**：Search and list players having a specific item in their ender chest
- **用法**：`/&lt;command&gt; &lt;Material&gt; [MinAmount] - MinAmount is optional, the minimum amount required`
- **别名**：`/se`
- **权限**：`openinv.search.inventory`

### /searchinv

- **说明**：Search and list players having a specific item
- **用法**：`/&lt;command&gt; &lt;Material&gt; [MinAmount] - MinAmount is optional, the minimum amount required`
- **别名**：`/si`
- **权限**：`openinv.search.inventory`

### /silentcontainer

- **说明**：SilentContainer stops sounds and animations when using containers.
- **用法**：`/&lt;command&gt; [check|on|off] - Check, toggle, or set SilentContainer`
- **别名**：`/sc`、`/silent`、`/silentchest`
- **权限**：`openinv.container.silent`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `openinv` | — | — |
