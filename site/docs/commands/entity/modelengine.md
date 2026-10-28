---
title: ModelEngine
createTime: 2026/10/24
---

# 模型引擎 · ModelEngine

> 分类 🧟 生物与展示 · 版本 `R4.1.1` · 指令 1 条 · api-version `1.19`

::: tip 自定义模型
把 Blockbench 做的 3D 模型挂到生物或玩家身上，提供召唤、伪装、状态机与 LOD 控制，是自定义 BOSS 外观的底层支撑。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 召唤一个模型 | /meg summon &lt;模型id&gt; | 模型 id 来自 blueprints 目录 |
| 把玩家伪装成模型 | /meg disguise &lt;模型id&gt; | 剧情演出/娱乐用 |
| 加了新模型 | /meg reload | 重载后玩家需重连才收到资源包 |
| 模型显示异常 | /meg resync | 强制客户端重新同步 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/meg` | 模型引擎主指令 | `/meg <reload｜summon｜disguise｜undisguise｜menu｜debug…` | — |

## 指令详解

### `/meg` — 模型引擎主指令

- **语法**：`/meg <reload｜summon｜disguise｜undisguise｜menu｜debug｜resync｜test｜health｜togglelod>`

- **示例**：

```
/meg reload
/meg help
```

- **备注**：注册指令即 /meg

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/meg reload` | 重载全部模型与配置 | `/meg reload` |
| `/meg summon <模型> [位置]` | 在世界里召唤一个模型实体 | `/meg summon star_dragon` |
| `/meg disguise <模型> [玩家]` | 把玩家或实体伪装成模型 | `/meg disguise star_dragon Steve` |
| `/meg undisguise [玩家]` | 取消伪装 | `/meg undisguise Steve` |
| `/meg menu` | 打开模型选择菜单 | `/meg menu` |
| `/meg debug` | 输出调试信息（状态、渲染层、LOD） | `/meg debug` |
| `/meg resync` | 强制客户端重新同步模型资源包 | `/meg resync` |
| `/meg test` | 跑内置自检（动画/状态机） | `/meg test` |
| `/meg health` | 查看模型引擎运行健康度 | `/meg health` |
| `/meg togglelod` | 开关 LOD 分级渲染 | `/meg togglelod` |

## 注意事项

::: warning
- 新模型必须 reload，且玩家要重连客户端才会收到新资源包，别以为是没生效。
- 模型绑在实体上，区块卸载或 /kill 可能留残影，出问题先 resync。
- debug 与 test 会刷大量日志，线上别长开。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `modelengine.admin` | 管理权限（reload / debug / summon） | — |
| `modelengine.command` | 使用 ModelEngine 指令 | op |
