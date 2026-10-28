---
title: StarAFK
createTime: 2026/10/24
---

# 挂机检测 · StarAFK

> 分类 🧰 基础指令 · 版本 `0.2.0` · 指令 1 条 · api-version `1.21`

::: tip 自动与手动挂机状态管理
星冕服自研的挂机插件，负责判断谁在挂机、把挂机状态显示给所有人看。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 切换挂机状态 | /afk | reload 重载配置 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/afk` | 切换自己的挂机状态；带 reload 则重载插件配置<br>别名 `/starafk`、`/guaji` | `/afk [reload]` | — |

## 指令详解

### `/afk` — 切换自己的挂机状态；带 reload 则重载插件配置

- **语法**：`/afk [reload]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `reload` | 可选 | 可选，填 reload 时执行配置重载，需要 starafk.reload 权限；不填则切换自己的挂机状态 |


- **示例**：

```
/afk
/afk reload
```

- **别名**：`/starafk`、`/guaji`
- **备注**：另有别名 /starafk 和 /guaji，效果一样。切换挂机状态需要 starafk.use，重载需要 starafk.reload（默认仅 OP）。被授予…

## 注意事项

::: warning
- 这是星冕服自研插件，具体参数与子指令以游戏内 help 为准，不要照搬其它挂机插件的写法
- starafk.bypass 和 starafk.silent 默认不授予任何人，需要时用 LuckPerms 单独给，别整组批量给
- /afk 是每个玩家切换自己的状态，没有针对别人的参数；想改别人的状态请让对方自己执行
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `starafk.auto` | 参与自动挂机判定 | True |
| `starafk.bypass` | 永不被自动挂机（不进 AFK 状态）。默认不授予任何人，需要豁免时用 LuckPerms 单独给 | — |
| `starafk.reload` | 允许 /afk reload | op |
| `starafk.silent` | 其进出 AFK 不广播。默认不授予任何人，需要静默时用 LuckPerms 单独给 | — |
| `starafk.use` | 允许使用 /afk | True |
