---
title: WineSuite
createTime: 2026/10/24
---

# 酿酒 · WineSuite

> 分类 🪙 经济与商店 · 版本 `1.2.0` · 指令 2 条 · api-version `1.21`

::: tip 自研酒水套装：酿酒图鉴加酒水收购
WineSuite 是星冕服务器自研的酒水套装插件，把酿酒图鉴和酒水收购合并成两个入口。图鉴会自动跟随主酿造插件 TBP 的配方变动，管理员无需手工维护酒单。收购侧提供界面化的收酒与单价管理，玩家把酒交给收购员即可换钱。管理与重载指令都受独立权限节点控制。
:::

## 什么时候会用到它

- 给玩家展示当前服内可酿的酒种与配方
- 结算玩家上缴酒水的收购价
- TBP 配方变动后同步刷新图鉴内容
- 临期或活动期间重置收购配置

## 上手流程

1. 确认主酿造插件 TBP 已正常加载，酒水配方已生成
2. 执行 /winebook reload 与 /winebuyer reload 刷新两侧配置
3. 用 /winebuyer list 核对收购清单与单价是否符合预期
4. 先在测试号上验证一次上缴与结算，再向玩家开放

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/winebook` | 打开酿酒图鉴界面，可带 reload 重载图鉴<br>别名 `/酒鉴`、`/酿酒图鉴`、`/图鉴`、`/wbk` | `/winebook [reload]` | — |
| `/winebuyer` | 打开酒水收购界面，可查清单、重载或重置<br>别名 `/wb`、`/收酒`、`/酒收` | `/winebuyer [list｜reload｜reset]` | — |

## 指令详解

### `/winebook` — 打开酿酒图鉴界面，可带 reload 重载图鉴

- **语法**：`/winebook [reload]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `reload` | 可选 | 重载图鉴数据，需要 winebook.admin 权限 |


- **示例**：

```
/winebook
/winebook reload
```

- **别名**：`/酒鉴`、`/酿酒图鉴`、`/图鉴`、`/wbk`
- **备注**：别名 酒鉴、酿酒图鉴、图鉴、wbk；无参时直接为玩家打开图鉴界面，图鉴内容自动跟随 TBP 配方。

### `/winebuyer` — 打开酒水收购界面，可查清单、重载或重置

- **语法**：`/winebuyer [list｜reload｜reset]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `list` | 可选 | 列出当前收购清单与单价，便于核对 |
| `reload` | 可选 | 重载收购配置，需要 winebuyer.admin 权限 |
| `reset` | 可选 | 重置收购配置，需要 winebuyer.admin 权限 |


- **示例**：

```
/winebuyer
/winebuyer list
/winebuyer reload
/winebuyer reset
```

- **别名**：`/wb`、`/收酒`、`/酒收`
- **备注**：别名 wb、收酒、酒收；reset 会覆盖现有收购设置，执行前先备份配置文件。

## 注意事项

::: warning
- WineSuite 为自研插件，参数与细节以游戏内 help 输出为准
- 图鉴数据依赖主酿造插件 TBP，TBP 未加载时图鉴可能为空
- reset 会覆盖已有收购配置，务必先备份再执行
- reload 与 reset 需要对应 admin 权限节点，普通玩家无法触发
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `winebook.admin` | 允许管理图鉴 | op |
| `winebook.use` | 允许使用酿酒图鉴 | True |
| `winebuyer.admin` | 允许重载/重置收购配置 | op |
| `winebuyer.use` | 允许使用酒水收购 | True |

## 相关插件

TBP
