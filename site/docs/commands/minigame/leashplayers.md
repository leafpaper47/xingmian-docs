---
title: LeashPlayers
createTime: 2026/10/24
---

# 玩家拴绳 · LeashPlayers

> 分类 🎲 小游戏与娱乐 · 版本 `1.0.0` · 指令 1 条 · api-version `26.2`

::: tip 用栓绳把玩家当动物一样牵走的小游戏插件
LeashPlayers 让管理员或玩家用栓绳栓住其他玩家，被栓的人会像拴着的动物一样被牵着走。默认所有玩家都能使用 /leash 指令，谁被栓、谁在牵都可以在指令里查询或解除。适合做整活、惩罚、小游戏和直播互动环节。
:::

## 什么时候会用到它

- 小游戏或活动里把玩家当宠物牵来牵去
- 对捣乱玩家做无伤大雅的整活式惩罚
- 直播互动时逗弄观众或队友
- 测试服务器时快速搬动不能或不愿自己走路的玩家

## 上手流程

1. 先确认权限：普通玩家默认有 leashplayers.use，管理别人的拴绳和重载配置需要 leashplayers.admin（默认仅 OP）
2. 用 /leash 加上目标玩家名，把栓绳栓到对方身上
3. 用 /leash list 或 /leash status 查看当前谁被栓、谁在牵
4. 用 /leash release 解除，完事可以 /leash reload 重载配置，/leash version 看插件版本

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/leash` | 栓住目标玩家、查询或解除已有的栓绳 | `/leash &lt;player｜release｜list｜status｜info｜selftes…` | `leashplayers.use` |

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
/leash release Steve
/leash version
```

- **权限**：`leashplayers.use`
- **备注**：子参数的实际写法与是否支持在线玩家自动补全以游戏内 help 为准；用完记得 release，避免玩家一直被栓着。

## 注意事项

::: warning
- 具体参数以游戏内 help 为准，不同版本的子指令可能略有差异
- reload 属于管理操作，需要 leashplayers.admin，普通权限执行会被拒
- 别在正式活动或玩家不方便时长时间拴着人，容易被当成恶意整活投诉
- 被栓玩家跨越传送、死亡、掉线后的状态不一定自动解除，活动结束前统一 /leash release 清理一遍
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `leashplayers.admin` | 允许管理所有人的栓绳 / 重载配置 | op |
| `leashplayers.use` | 允许使用栓绳栓玩家 | True |

## 相关插件

[Essentials](/commands/essentials/essentials.md)、[LuckPerms](/commands/core/luckperms.md)、[Vault](/commands/core/vault.md)
