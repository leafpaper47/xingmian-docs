---
title: LeafHat
createTime: 2026/10/24
---

# 头顶帽子 · LeafHat

> 分类 🧰 基础工具 · 版本 `1.0.3` · 指令 2 条 · api-version `1.21`

::: tip 把手上物品戴到头上，替代 Essentials 帽子功能
LeafHat 是一个专门做头顶穿戴的小插件，用来替代 Essentials 自带的 hat 功能，行为更干净也更好控权。玩家手上拿着想戴的东西执行指令即可顶到头上，再执行一次或加参数即可脱下。是否可用由权限节点控制，适合把「戴帽子」这件事单独交给某一批玩家或某个权限组。
:::

## 什么时候会用到它

- 让玩家把头盔、南瓜、方块、工具等任意手持物品戴在头上当装饰
- 想用独立权限精细控制谁能戴帽子，而不是笼统给 Essentials 全部权限
- 需要一条明确的脱帽指令来快速恢复头部装备

## 上手流程

1. 把 LeafHat 放进 plugins 目录并重启服务端，确认插件正常启用
2. 给需要的玩家或权限组授予 leafhat.use 权限节点
3. 玩家手持想要戴上的物品执行 /hat，物品即被移到头部栏位
4. 要摘下时执行 /unhat，或执行 /hat remove
5. 改过配置后用 /hat reload 重载，无需重启

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/hat` | 把手上物品戴到头上，或按参数脱下帽子<br>别名 `/wearhat` | `/hat [remove]` | — |
| `/unhat` | 单独脱下头顶物品的快捷指令 | `/unhat` | — |

## 指令详解

### `/hat` — 把手上物品戴到头上，或按参数脱下帽子

- **语法**：`/hat [remove]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `remove` | 可选 | 可选参数，填 remove 表示脱下当前头上的物品 |


- **示例**：

```
/hat
/hat remove
```

- **别名**：`/wearhat`
- **备注**：别名 /wearhat 等价；需要 leafhat.use 权限。手上为空时正常不会戴出东西，先确保主手有物品。

### `/unhat` — 单独脱下头顶物品的快捷指令

- **语法**：`/unhat`

- **示例**：

```
/unhat
```

- **备注**：无参数，等价于 /hat remove；需要 leafhat.use 权限。头部为空时执行一般只会提示没有帽子。

## 注意事项

::: warning
- 具体参数与子指令以游戏内 /hat 或插件 help 的实际输出为准，本手册只覆盖已知用法
- leafhat.use 默认仅 OP 拥有，普通玩家需要显式授权才能戴帽子，别忘了给权限组加节点
- 头顶物品占用头盔栏位，脱下/戴上前注意别把原有头盔弄丢，重要装备建议先收进背包
- leafhat.reload 只允许 OP 或显式授权者使用，改配置前先备份文件
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `leafhat.reload` | 允许使用 /hat reload 重载配置 | op |
| `leafhat.use` | 允许使用 /hat 与 /unhat | op |

## 相关插件

[Essentials](/commands/essentials/essentials.md)、[LuckPerms](/commands/core/luckperms.md)
