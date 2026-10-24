---
title: OpenInv
createTime: 2026/10/24
---

# OpenInv

> 版本 `5.3.3` · 指令 10 条 · api-version `1.13` · 文件 `OpenInv.jar`

以宝箱的形式打开玩家的库存，并实时与之互动。

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/anycontainer help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/anycontainer` | AnyContainer允许使用被阻止的容器。 | `openinv.container.any` |
| `/clearender` | 清空玩家的恩德宝箱 | `openinv.clear.self;openinv.clear.other` |
| `/clearinv` | 清除玩家的库存 | `openinv.clear.self;openinv.clear.other` |
| `/openender` | 打开玩家的恩德宝箱 | `openinv.enderchest.open.self;openinv.enderchest.open.other` |
| `/openinv` | 打开玩家的库存 | `openinv.inventory.open.self;openinv.inventory.open.other` |
| `/searchcontainer` | 搜索并列出包含特定材料的容器。 | `openinv.search.container` |
| `/searchenchant` | 搜索并列出具有特定魔法的玩家。 | `openinv.search.inventory` |
| `/searchender` | 搜索并列出在恩德宝箱中有特定物品的玩家 | `openinv.search.inventory` |
| `/searchinv` | 搜索并列出拥有特定道具的玩家 | `openinv.search.inventory` |
| `/silentcontainer` | SilentContainer在使用容器时停止声音和动画。 | `openinv.container.silent` |

## 详细用法

### /anycontainer

- **说明**：AnyContainer允许使用被阻止的容器。
- **用法**：`/&lt;command&gt; [check|on|off] - Check, toggle, or set AnyContainer`
- **别名**：`/ac`、`/anychest`
- **权限**：`openinv.container.any`

### /clearender

- **说明**：清空玩家的恩德宝箱
- **用法**：`/&lt;command&gt; [Player] - Clear a player's ender chest`
- **权限**：`openinv.clear.self;openinv.clear.other`

### /clearinv

- **说明**：清除玩家的库存
- **用法**：`/&lt;command&gt; [Player] - Clear a player's inventory`
- **权限**：`openinv.clear.self;openinv.clear.other`

### /openender

- **说明**：打开玩家的恩德宝箱
- **用法**：`/&lt;command&gt; [Player] - Open a player's ender chest`
- **别名**：`/oe`
- **权限**：`openinv.enderchest.open.self;openinv.enderchest.open.other`

### /openinv

- **说明**：打开玩家的库存
- **用法**：`/&lt;command&gt; [Player] - Open a player's inventory`
- **别名**：`/oi`、`/inv`、`/open`
- **权限**：`openinv.inventory.open.self;openinv.inventory.open.other`

### /searchcontainer

- **说明**：搜索并列出包含特定材料的容器。
- **用法**：`/&lt;command&gt; &lt;Material&gt; [ChunkRadius] - ChunkRadius is optional, the length that will be searched for matching items. Default 5`
- **别名**：`/searchchest`
- **权限**：`openinv.search.container`

### /searchenchant

- **说明**：搜索并列出具有特定魔法的玩家。
- **用法**：`/&lt;command&gt; &lt;[Enchantment] [MinLevel]&gt; - Enchantment is the enchantment type, MinLevel is the minimum level. One is optional`
- **别名**：`/searchenchants`
- **权限**：`openinv.search.inventory`

### /searchender

- **说明**：搜索并列出在恩德宝箱中有特定物品的玩家
- **用法**：`/&lt;command&gt; &lt;Material&gt; [MinAmount] - MinAmount is optional, the minimum amount required`
- **别名**：`/se`
- **权限**：`openinv.search.inventory`

### /searchinv

- **说明**：搜索并列出拥有特定道具的玩家
- **用法**：`/&lt;command&gt; &lt;Material&gt; [MinAmount] - MinAmount is optional, the minimum amount required`
- **别名**：`/si`
- **权限**：`openinv.search.inventory`

### /silentcontainer

- **说明**：SilentContainer在使用容器时停止声音和动画。
- **用法**：`/&lt;command&gt; [check|on|off] - Check, toggle, or set SilentContainer`
- **别名**：`/sc`、`/silent`、`/silentchest`
- **权限**：`openinv.container.silent`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `openinv` | — | — |
