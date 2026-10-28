---
title: SenluoBuyer
createTime: 2026/10/24
---

# 菜品收购 · SenluoBuyer

> 分类 🍳 烹饪与采集 · 版本 `1.0.0` · 指令 1 条 · api-version `1.21`

::: tip 森罗厨房每日随机收购回收面板
给每位玩家每天随机指派 5 道森罗厨房菜品，玩家做好后通过界面点交回收换钱。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 打开收购界面 | /senluobuyer | 玩家自助卖物品 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/senluobuyer` | 打开森罗收购界面，可用 reload 重载配置<br>别名 `/senluo`、`/sely`、`/收购` | `/senluobuyer [reload]` | — |

## 指令详解

### `/senluobuyer` — 打开森罗收购界面，可用 reload 重载配置

- **语法**：`/senluobuyer [reload]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `reload` | 可选 | 加该参数为重载配置，仅管理员可用；不写则打开收购界面 |


- **示例**：

```
/senluobuyer
/senluo
```

- **别名**：`/senluo`、`/sely`、`/收购`
- **备注**：别名 senluo、sely、收购 等价；普通玩家只需 senluobuyer.use（默认开启），重载需要 senluobuyer.admin（默认仅 OP）…

## 注意事项

::: warning
- 具体参数与子指令以游戏内 help 为准，本文按官方 usage 与权限节点推断，不同版本可能有差异
- 收购名单是每位玩家每天随机 5 道菜，玩家之间看到的清单可能不一样，别按别人的清单备菜
- reload 只能重载配置，已下发的当日清单不一定会立刻刷新，改完最好等次日或重启生效
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `senluobuyer.admin` | 允许重载配置 | op |
| `senluobuyer.use` | 允许使用森罗收购 | True |
