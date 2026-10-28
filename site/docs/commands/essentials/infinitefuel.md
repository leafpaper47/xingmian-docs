---
title: InfiniteFuel
createTime: 2026/10/24
---

# 无限燃料 · InfiniteFuel

> 分类 🧰 基础工具 · 版本 `1.0.0` · 指令 1 条 · api-version `1.21`

::: tip 让熔炉烧不完的无限燃料小插件
InfiniteFuel 给服务器提供一种“无限煤块”类燃料：放进熔炉后熔炉会一直燃烧，燃料槽里的那块煤不会被消耗。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 发无限燃料 | /infinitefuel give Steve | 一根就够，别重复发 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/infinitefuel` | 给玩家发放无限燃料，或重载插件配置 | `/infinitefuel give [玩家名] [数量] ｜ /infinitefuel reload` | `infinitefuel.admin` |

## 指令详解

### `/infinitefuel` — 给玩家发放无限燃料，或重载插件配置

- **语法**：`/infinitefuel give [玩家名] [数量] ｜ /infinitefuel reload`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `give` | 可选 | 子动作：给指定玩家发放无限燃料 |
| `玩家名` | 必填 | give 的目标玩家，需在线 |
| `数量` | 可选 | 发放的燃料数量，省略时按默认值发放 |
| `reload` | 可选 | 子动作：重新载入插件配置，不重启服务端 |


- **示例**：

```
/infinitefuel give Steve
/infinitefuel give Steve 8
```

- **权限**：`infinitefuel.admin`
- **备注**：只有两个子动作：give 发放、reload 重载；不带子动作时通常只会提示用法。指令需要 infinitefuel.admin 权限（默认仅 OP 拥有）。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `give [玩家名] [数量]` | 给指定在线玩家发放无限燃料，数量可省略 | `/infinitefuel give Steve 8` |
| `reload` | 重新加载插件配置，无需重启服务端 | `/infinitefuel reload` |

## 注意事项

::: warning
- 重载后一定要实际点火一次并检查燃料槽，确认永燃生效、取出后确实立刻熄火
- 该燃料只对放进熔炉燃料槽的用法生效，不要用它在其他燃料相关机制上做收益玩法，容易出预期外结果
- 给玩家发放前先想清楚回收方式：无限燃料一旦流出，建议只发给可信玩家或限定在公共熔炉
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `infinitefuel.admin` | — | op |
