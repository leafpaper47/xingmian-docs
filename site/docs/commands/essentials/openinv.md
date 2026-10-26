---
title: OpenInv
createTime: 2026/10/24
---

# 远程背包 · OpenInv

> 分类 🧰 基础工具 · 版本 `5.3.3` · 指令 10 条 · api-version `1.13`

::: tip 宝箱式远程查看与编辑玩家背包、末影箱
OpenInv 把玩家背包或末影箱渲染成一个普通箱子界面，管理员可直接拖拽物品、实时与对方互动。它还提供清空背包、按物品或附魔搜索全服玩家等功能，是排查丢失物品、定位违规道具的核心工具。所有操作都受权限节点控制，可区分为只读、可编辑与他人的背包三种档次。使用前请确认已给对应分组配置权限，避免误开导致误删。
:::

## 什么时候会用到它

- 远程检查某玩家是否携带违禁或作弊物品
- 帮玩家找回误丢的物品、整理或清空背包
- 按物品名或附魔等级搜索全服谁持有该道具
- 清空或查看玩家末影箱内容以处理藏匿违规物
- 关闭开箱音效与动画，做无痕巡查

## 上手流程

1. 先确认自己拥有 openinv.inventory.open.other 或对应子权限
2. 执行 /openinv 玩家名 打开对方背包，界面按箱子上半部分是背包、下方是快捷栏与护甲
3. 在界面中直接取出、放入或替换物品，改动即时生效
4. 处理完毕后关闭界面，必要时用 /clearinv 玩家名 彻底清空

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/anycontainer` | 开关对任意容器的访问，绕过被阻止的容器限制<br>别名 `/ac`、`/anychest` | `/anycontainer [check｜on｜off]` | `openinv.container.any` |
| `/clearender` | 清空指定玩家的末影箱 | `/clearender [玩家名]` | `openinv.clear.self;openinv.clear.other` |
| `/clearinv` | 清空指定玩家的背包物品 | `/clearinv [玩家名]` | `openinv.clear.self;openinv.clear.other` |
| `/openender` | 以箱子界面打开玩家末影箱<br>别名 `/oe` | `/openender [玩家名]` | `openinv.enderchest.open.self;openinv.enderchest.open.other` |
| `/openinv` | 以箱子界面打开玩家背包并实时编辑<br>别名 `/oi`、`/inv`、`/open` | `/openinv [玩家名]` | `openinv.inventory.open.self;openinv.inventory.open.other` |
| `/searchcontainer` | 按材料搜索附近区块内存放该物品的容器<br>别名 `/searchchest` | `/searchcontainer 材料 [区块半径]` | `openinv.search.container` |
| `/searchenchant` | 按附魔类型与最低等级搜索持有该附魔的玩家<br>别名 `/searchenchants` | `/searchenchant [附魔] [最低等级]` | `openinv.search.inventory` |
| `/searchender` | 搜索末影箱中含指定物品的玩家<br>别名 `/se` | `/searchender 材料 [最小数量]` | `openinv.search.inventory` |
| `/searchinv` | 搜索背包中含指定物品的玩家<br>别名 `/si` | `/searchinv 材料 [最小数量]` | `openinv.search.inventory` |
| `/silentcontainer` | 开关使用容器时的声音与开合动画<br>别名 `/sc`、`/silent`、`/silentchest` | `/silentcontainer [check｜on｜off]` | `openinv.container.silent` |

## 指令详解

### `/anycontainer` — 开关对任意容器的访问，绕过被阻止的容器限制

- **语法**：`/anycontainer [check｜on｜off]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `mode` | 可选 | check 查看当前状态，on 开启，off 关闭，不填默认切换 |


- **示例**：

```
/anycontainer
/anycontainer check
/anycontainer on
```

- **别名**：`/ac`、`/anychest`
- **权限**：`openinv.container.any`
- **备注**：别名 ac、anychest；权限 openinv.container.any。开启后可以打开通常被插件阻止的容器。

### `/clearender` — 清空指定玩家的末影箱

- **语法**：`/clearender [玩家名]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `玩家名` | 可选 | 目标玩家，省略时作用于自己 |


- **示例**：

```
/clearender Steve
/clearender
```

- **权限**：`openinv.clear.self;openinv.clear.other`
- **备注**：权限 openinv.clear.self 与 openinv.clear.other；清空不可撤销，建议先 /openender 确认内容。

### `/clearinv` — 清空指定玩家的背包物品

- **语法**：`/clearinv [玩家名]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `玩家名` | 可选 | 目标玩家，省略时作用于自己 |


- **示例**：

```
/clearinv Steve
/clearinv
```

- **权限**：`openinv.clear.self;openinv.clear.other`
- **备注**：权限 openinv.clear.self 与 openinv.clear.other；只清背包，不含末影箱，需另行 /clearender。

### `/openender` — 以箱子界面打开玩家末影箱

- **语法**：`/openender [玩家名]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `玩家名` | 可选 | 目标玩家，省略时打开自己的末影箱 |


- **示例**：

```
/openender Steve
/openender
```

- **别名**：`/oe`
- **权限**：`openinv.enderchest.open.self;openinv.enderchest.open.other`
- **备注**：别名 oe；权限 openinv.enderchest.open.self 与 openinv.enderchest.open.other。

### `/openinv` — 以箱子界面打开玩家背包并实时编辑

- **语法**：`/openinv [玩家名]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `玩家名` | 可选 | 目标玩家，省略时打开自己的背包 |


- **示例**：

```
/openinv Steve
/openinv
```

- **别名**：`/oi`、`/inv`、`/open`
- **权限**：`openinv.inventory.open.self;openinv.inventory.open.other`
- **备注**：别名 oi、inv、open；权限 openinv.inventory.open.self 与 openinv.inventory.open.other。对方在线时改动会实时同步。

### `/searchcontainer` — 按材料搜索附近区块内存放该物品的容器

- **语法**：`/searchcontainer 材料 [区块半径]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `材料` | 必填 | 要查找的 Bukkit 材料名，如 DIAMOND |
| `区块半径` | 可选 | 搜索的区块半径，默认 5 |


- **示例**：

```
/searchcontainer DIAMOND
/searchcontainer DIAMOND 10
```

- **别名**：`/searchchest`
- **权限**：`openinv.search.container`
- **备注**：别名 searchchest；权限 openinv.search.container。半径越大越耗性能，主城慎用大值。

### `/searchenchant` — 按附魔类型与最低等级搜索持有该附魔的玩家

- **语法**：`/searchenchant [附魔] [最低等级]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `附魔` | 可选 | 附魔名，如 SHARPNESS，可与等级二选一 |
| `最低等级` | 可选 | 最低附魔等级，整数 |


- **示例**：

```
/searchenchant SHARPNESS
/searchenchant SHARPNESS 5
```

- **别名**：`/searchenchants`
- **权限**：`openinv.search.inventory`
- **备注**：别名 searchenchants；权限 openinv.search.inventory。两个参数至少填一个，常用来排查非法附魔装备。

### `/searchender` — 搜索末影箱中含指定物品的玩家

- **语法**：`/searchender 材料 [最小数量]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `材料` | 必填 | 要查找的材料名 |
| `最小数量` | 可选 | 该物品的最小堆叠数量 |


- **示例**：

```
/searchender DIAMOND
/searchender DIAMOND 64
```

- **别名**：`/se`
- **权限**：`openinv.search.inventory`
- **备注**：别名 se；权限 openinv.search.inventory。

### `/searchinv` — 搜索背包中含指定物品的玩家

- **语法**：`/searchinv 材料 [最小数量]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `材料` | 必填 | 要查找的材料名 |
| `最小数量` | 可选 | 该物品的最小堆叠数量 |


- **示例**：

```
/searchinv NETHERITE_SWORD
/searchinv DIAMOND 32
```

- **别名**：`/si`
- **权限**：`openinv.search.inventory`
- **备注**：别名 si；权限 openinv.search.inventory。结果按玩家列出持有数量。

### `/silentcontainer` — 开关使用容器时的声音与开合动画

- **语法**：`/silentcontainer [check｜on｜off]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `mode` | 可选 | check 查看当前状态，on 静音，off 恢复，不填默认切换 |


- **示例**：

```
/silentcontainer check
/silentcontainer on
```

- **别名**：`/sc`、`/silent`、`/silentchest`
- **权限**：`openinv.container.silent`
- **备注**：别名 sc、silent、silentchest；权限 openinv.container.silent。静音巡查时对方不易察觉。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `anycontainer check` | 查看任意容器访问当前是开还是关 | `/anycontainer check` |
| `anycontainer on` | 开启任意容器访问 | `/anycontainer on` |
| `anycontainer off` | 关闭任意容器访问 | `/anycontainer off` |
| `anycontainer（无参数）` | 在当前状态之间切换 | `/anycontainer` |
| `silentcontainer check` | 查看静音模式当前状态 | `/silentcontainer check` |
| `silentcontainer on` | 开启静音，容器无声音无动画 | `/silentcontainer on` |
| `silentcontainer off` | 关闭静音，恢复默认效果 | `/silentcontainer off` |
| `silentcontainer（无参数）` | 在当前状态之间切换 | `/silentcontainer` |
| `oi self` | 不带玩家名时只看自己的背包，等价于查看自身 | `/oi` |
| `清空类命令组合` | 先用 openender 核实内容，再用 clearender 清空末影箱 | `/openender Steve` |

## 注意事项

::: warning
- clearinv 与 clearender 不可撤销，且不区分在线离线，执行前务必用 openinv 或 openender 先核对目标玩家名，避免同名或拼错导致清空无辜玩家
- searchcontainer 按区块半径扫描容器，半径过大在主城区域会造成明显卡顿，建议不超过 10 并避开高峰
- openinv.inventory.open.other 属于高敏感权限，只授予信任的管理组，可另外配合只读权限节点限制为只能查看不能拿取
- 对方在线时背包改动会实时同步并可能被其立即看到，巡查隐弊物品时建议先开启 silentcontainer 并关掉任何广播提示
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `openinv` | — | — |

## 相关插件

InvSee++、EssentialsX、[LuckPerms](/commands/core/luckperms.md)、[PlaceholderAPI](/commands/config/placeholderapi.md)
