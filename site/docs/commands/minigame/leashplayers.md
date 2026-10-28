---
title: LeashPlayers
createTime: 2026/10/24
---

# 玩家拴绳 · LeashPlayers

> 分类 🎲 休闲与小游戏 · 版本 `1.0.0` · 指令 1 条 · api-version `26.2`

::: tip 用栓绳把玩家当动物一样牵走的小游戏插件
LeashPlayers 让管理员或玩家用栓绳栓住其他玩家，被栓的人会像拴着的动物一样被牵着走。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 把玩家拴起来 | /leash Steve | 再执行一次解除 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/leash` | 栓住目标玩家、查询或解除已有的栓绳 | `/leash <player｜release｜list｜status｜info｜selftest｜r…` | `leashplayers.use` |

## 指令详解

### `/leash` — 栓住目标玩家、查询或解除已有的栓绳

- **语法**：`/leash <player｜release｜list｜status｜info｜selftest｜reload｜version>`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `player` | 必填 | 要栓住的玩家名字，把栓绳拴到这名玩家身上 |
| `release` | 可选 | 解除栓绳，不填玩家名时一般解除自己相关的拴绳 |
| `list` | 可选 | 列出当前所有生效的栓绳关系 |
| `status` | 可选 | 查看指定玩家或自己当前的被栓状态 |
| `info` | 可选 | 查看插件信息 |
| `selftest` | 可选 | 插件自检，排查功能是否正常 |
| `reload` | 可选 | 重载插件配置，需要 leashplayers.admin |
| `version` | 可选 | 显示插件版本号 |


- **示例**：

```
/leash Steve
/leash list
```

- **权限**：`leashplayers.use`
- **备注**：子参数的实际写法与是否支持在线玩家自动补全以游戏内 help 为准；用完记得 release，避免玩家一直被栓着。

## 注意事项

::: warning
- 具体参数以游戏内 help 为准，不同版本的子指令可能略有差异
- reload 属于管理操作，需要 leashplayers.admin，普通权限执行会被拒
- 别在正式活动或玩家不方便时长时间拴着人，容易被当成恶意整活投诉
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `leashplayers.admin` | 允许管理所有人的栓绳 / 重载配置 | op |
| `leashplayers.use` | 允许使用栓绳栓玩家 | True |
