---
title: OpenInv
createTime: 2026/10/24
---

# 远程背包 · OpenInv

> 分类 🎒 物品与合成 · 版本 `5.3.3` · 指令 10 条 · api-version `1.13`

::: tip 远程开箱
管理员远程打开玩家背包与末影箱并搜索物品，还能按材料、附魔、半径查容器，查盗号查赃物必备。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 看某人背包 | /openinv Steve | 不填玩家= 看自己 |
| 查谁身上有钻石 | /searchinv diamond 64 | 第二个参数是最少数量 |
| 查附近箱子 | /searchcontainer diamond_block 5 | 半径按区块算，默认 5 |
| 查谁有抢夺附魔 | /searchenchant looting 3 | 附魔名用原版 id |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/anycontainer` | 允许打开被方块挡住的容器<br>别名 `/ac`、`/anychest` | `/anycontainer [check｜on｜off]` | `openinv.container.any` |
| `/clearender` | 清空玩家末影箱 | `/clearender [玩家]` | `openinv.clear.self;openinv.clear.other` |
| `/clearinv` | 清空玩家背包 | `/clearinv [玩家]` | `openinv.clear.self;openinv.clear.other` |
| `/openender` | 打开玩家末影箱<br>别名 `/oe` | `/openender [玩家]` | `openinv.enderchest.open.self;openinv.enderchest.open.other` |
| `/openinv` | 打开玩家背包（可编辑）<br>别名 `/oi`、`/inv`、`/open` | `/openinv [玩家]` | `openinv.inventory.open.self;openinv.inventory.open.other` |
| `/searchcontainer` | 搜索周围区块内装着某材料的容器<br>别名 `/searchchest` | `/searchcontainer <材料> [区块半径]` | `openinv.search.container` |
| `/searchenchant` | 按附魔与等级搜索在线玩家<br>别名 `/searchenchants` | `/searchenchant <附魔> [等级]` | `openinv.search.inventory` |
| `/searchender` | 搜索哪些玩家末影箱里有某材料<br>别名 `/se` | `/searchender <材料> [最少数量]` | `openinv.search.inventory` |
| `/searchinv` | 搜索哪些在线玩家背包里有某材料<br>别名 `/si` | `/searchinv <材料> [最少数量]` | `openinv.search.inventory` |
| `/silentcontainer` | 静默容器：开关箱子无音效无开盖动画<br>别名 `/sc`、`/silent`、`/silentchest` | `/silentcontainer [check｜on｜off]` | `openinv.container.silent` |

## 指令详解

### `/anycontainer` — 允许打开被方块挡住的容器

- **语法**：`/anycontainer [check｜on｜off]`

- **示例**：

```
/anycontainer on
```

- **别名**：`/ac`、`/anychest`
- **权限**：`openinv.container.any`
- **备注**：配 /silentcontainer on 一起用最隐蔽

### `/clearender` — 清空玩家末影箱

- **语法**：`/clearender [玩家]`

- **示例**：

```
/clearender Steve
```

- **权限**：`openinv.clear.self;openinv.clear.other`
- **备注**：不可撤销。

### `/clearinv` — 清空玩家背包

- **语法**：`/clearinv [玩家]`

- **示例**：

```
/clearinv Steve
```

- **权限**：`openinv.clear.self;openinv.clear.other`
- **备注**：不可撤销，先用 /openinv 确认内容

### `/openender` — 打开玩家末影箱

- **语法**：`/openender [玩家]`

- **示例**：

```
/openender Steve
```

- **别名**：`/oe`
- **权限**：`openinv.enderchest.open.self;openinv.enderchest.open.other`

### `/openinv` — 打开玩家背包（可编辑）

- **语法**：`/openinv [玩家]`

- **示例**：

```
/openinv Steve
```

- **别名**：`/oi`、`/inv`、`/open`
- **权限**：`openinv.inventory.open.self;openinv.inventory.open.other`
- **备注**：改动会直接落到对方背包，操作前先截图留证

### `/searchcontainer` — 搜索周围区块内装着某材料的容器

- **语法**：`/searchcontainer <材料> [区块半径]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `区块半径` | 可选 | 默认 5，过大容易卡服 |


- **示例**：

```
/searchcontainer diamond_block 5
```

- **别名**：`/searchchest`
- **权限**：`openinv.search.container`
- **备注**：只扫已加载区块

### `/searchenchant` — 按附魔与等级搜索在线玩家

- **语法**：`/searchenchant <附魔> [等级]`

- **示例**：

```
/searchenchant mending
```

- **别名**：`/searchenchants`
- **权限**：`openinv.search.inventory`
- **备注**：附魔名不带命名空间，等级不填则任意等级

### `/searchender` — 搜索哪些玩家末影箱里有某材料

- **语法**：`/searchender <材料> [最少数量]`

- **示例**：

```
/searchender shulker_box
```

- **别名**：`/se`
- **权限**：`openinv.search.inventory`

### `/searchinv` — 搜索哪些在线玩家背包里有某材料

- **语法**：`/searchinv <材料> [最少数量]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `材料` | 必填 | 原版 id，如 diamond、netherite_ingot |


- **示例**：

```
/searchinv diamond 64
```

- **别名**：`/si`
- **权限**：`openinv.search.inventory`
- **备注**：物品用原版 ID，可带命名空间。

### `/silentcontainer` — 静默容器：开关箱子无音效无开盖动画

- **语法**：`/silentcontainer [check｜on｜off]`

- **示例**：

```
/silentcontainer on
```

- **别名**：`/sc`、`/silent`、`/silentchest`
- **权限**：`openinv.container.silent`
- **备注**：查号时用，避免在线玩家听到箱子声

## 注意事项

::: warning
- /clearinv 与 /clearender 不可撤销，先 /openinv 或 /searchinv 取证。
- 远程开箱是真改数据，动过的物品会真的落到玩家身上，别当只读查看用。
- 搜索只覆盖在线玩家与已加载区块，离线玩家查不到。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `openinv` | — | — |
| `openinv.clear.other` | 清空他人背包/末影箱 | — |
| `openinv.container.any` | 使用 /anycontainer | — |
| `openinv.container.silent` | 使用静默容器 | — |
| `openinv.enderchest.open.other` | 打开他人末影箱 | — |
| `openinv.inventory.open.other` | 打开他人背包 | — |
| `openinv.search.container` | 使用 /searchcontainer | — |
| `openinv.search.inventory` | 使用 /searchinv /searchender /searchenchant | — |
