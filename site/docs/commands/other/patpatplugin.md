---
title: PatPatPlugin
createTime: 2026/10/24
---

# PatPatPlugin

> 分类 📦 其他 · 版本 `1.2.5+0268419` · 指令 1 条 · api-version `1.16`

::: tip 拍拍互动
玩家之间「拍一拍」的轻互动：记录次数与排行榜，支持限速、权限与列表维护；管理员用它查数据、封禁刷屏者。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 看谁拍得多 | /patpat list | 排行榜，可选页码 |
| 查某个人的拍拍数据 | /patpat info Steve | 拍人与被拍次数 |
| 有人刷屏，先关他的限速开关 | /patpat ratelimit disable Steve | 禁用后不能再拍 |
| 给玩家单独设冷却 | /patpat ratelimit limit Steve 30 | 30 秒一次 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/patpat` | 拍拍主指令（数据/限速/权限/列表/重载） | `/patpat <info｜list｜ratelimit｜permission｜reload｜pat…` | — |

## 指令详解

### `/patpat` — 拍拍主指令（数据/限速/权限/列表/重载）

- **语法**：`/patpat <info｜list｜ratelimit｜permission｜reload｜pat> [参数]`

- **示例**：

```
/patpat list
/patpat info Steve
```

- **备注**：只有这一个入口，其余都是子指令

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/patpat pat <玩家>` | 管理员代发一次「拍一拍」（测文案/音效） | `/patpat pat Steve` |
| `/patpat info <玩家>` | 查看玩家的拍人/被拍统计 | `/patpat info Steve` |
| `/patpat list [页码]` | 查看拍拍排行榜 | `/patpat list 1` |
| `/patpat list add <玩家> <数量>` | 手工给榜单加分（调数据用） | `/patpat list add Steve 10` |
| `/patpat list set <玩家> <数量>` | 直接设定榜单数值 | `/patpat list set Steve 100` |
| `/patpat list remove <玩家>` | 把玩家从榜单移除 | `/patpat list remove Steve` |
| `/patpat list info` | 查看榜单自身信息（条目数等） | `/patpat list info` |
| `/patpat ratelimit info <玩家>` | 查询玩家当前冷却状态 | `/patpat ratelimit info Steve` |
| `/patpat ratelimit limit <玩家> <秒>` | 设置该玩家的冷却秒数 | `/patpat ratelimit limit Steve 30` |
| `/patpat ratelimit enable｜disable <玩家>` | 开启/关闭限速检查 | `/patpat ratelimit disable Steve` |
| `/patpat ratelimit toggle <玩家>` | 切换限速开关 | `/patpat ratelimit toggle Steve` |
| `/patpat permission enable｜disable <玩家>` | 临时允许/禁止某玩家使用拍拍 | `/patpat permission disable Steve` |
| `/patpat permission set <玩家> <true｜false>` | 显式设置该玩家的拍拍开关 | `/patpat permission set Steve false` |
| `/patpat reload` | 重载配置（冷却、文案、音效） | `/patpat reload` |

## 注意事项

::: warning
- 改完 config.yml 必须 /patpat reload，否则冷却与文案不生效。
- ratelimit disable 与 permission disable 效果相近但来源不同（一个走限速、一个走权限判定），排查「他为什么还能拍」时两处都要看。
- list set/add 会直接改写排行榜数据，调之前记下原值，避免玩家实际数据被覆盖。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `patpat.admin` | info / list / ratelimit / permission / reload 管理子指令 | — |
| `patpat.use` | 普通玩家拍拍他人 | — |
