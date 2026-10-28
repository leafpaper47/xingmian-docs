---
title: KaoguPlugin
createTime: 2026/10/24
---

# 考古系统 · KaoguPlugin

> 分类 🍳 烹饪与采集 · 版本 `1.0.1-CE-fix` · 指令 1 条 · api-version `1.21`

::: tip 考古玩法
星冕自研考古：钓鱼挖矿出化石，花钱鉴定成古物，修复完整后可在 NPC 处卖钱，配收集图鉴与每日限购。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 鉴定手里的化石 | /kaogu identify | 扣金币手续费，有概率直接出钻石/煤炭 |
| 修复破损古物 | /kaogu repair | 要花钱且要等修复时长（分钟级） |
| 卖古物换钱 | /kaogu sell | 每日限卖数量见配置 sell 上限 |
| 改概率或手续费 | /kaogu reload | 改完 config 必须重载 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/kaogu` | 考古主指令，所有功能都挂在它下面<br>别名 `/kg` | `/kaogu <identify｜repair｜sell｜price｜give｜reload｜help>` | — |

## 指令详解

### `/kaogu` — 考古主指令，所有功能都挂在它下面

- **语法**：`/kaogu <identify｜repair｜sell｜price｜give｜reload｜help>`

- **示例**：

```
/kaogu help
```

- **别名**：`/kg`
- **备注**：别名 /kg；不带参数等于 /kaogu help

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/kaogu identify` | 鉴定手持化石，消耗手续费，按概率出钻石/煤炭/古物碎片或完整古物 | `/kaogu identify` |
| `/kaogu repair` | 修复手里的破损古物，按件收费并需要等待修复时长 | `/kaogu repair` |
| `/kaogu sell` | 把手上的古物卖给收购方换金币 | `/kaogu sell` |
| `/kaogu price` | 查询某类古物的鉴定/修复/回收价格 | `/kaogu price` |
| `/kaogu give <玩家> <物品> [数量]` | 给玩家发化石或古物（管理用） | `/kaogu give Steve fossil 5` |
| `/kaogu reload` | 重载配置（概率、价格、冷却、方块列表） | `/kaogu reload` |
| `/kaogu help` | 打印可用子指令与说明 | `/kaogu help` |

## 注意事项

::: warning
- 鉴定/修复/回收都有冷却（默认按秒配置），连点会被拦下但不提示，误判成「没反应」时先等冷却。
- 化石掉落率分钓鱼与挖矿两条线，且都有「每人每日上限」，玩家抱怨「挖一整天不出」先看上限。
- give 与 reload 只该给 kaogu.admin；把 kaogu.use 全服开没问题，admin 别整组下发。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `kaogu.admin` | 管理权限：give / reload 等 | op |
| `kaogu.use` | 使用考古功能（默认开启） | True |
