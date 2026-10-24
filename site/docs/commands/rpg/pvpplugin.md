---
title: PVPPlugin
createTime: 2026/10/24
---

# PVPPlugin

> 版本 `1.2.26` · 指令 1 条 · api-version `1.21` · 文件 `PVPPlugin-1.2.26.jar`

星冕服务器 PVP 决斗插件（可视化UI / 团战 / 下注 / 赌钱决斗 / 观战 / 公平排位，含排位死亡复活缓冲、排位强制重生修复、排位背包快照历史落盘与每月自动清理、排位死亡经验还原；公平排位赛季排行榜（赛季中实时分段位、封盘定格快照）+前三名皮肤奖励领取，停机跨月自动补封盘、掉线计负、领取先记账后发放、赛季文件保存节流）

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/pvp help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/pvp` | PVP 决斗主命令 | — |

## 详细用法

### /pvp

- **说明**：PVP 决斗主命令
- **用法**：`/pvp [bet|spectate|accept|deny|team|seta|setb|reload|help|rank(join|spectate|cancel|top|stats|season|claim)]`
- **别名**：`/duel`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `pvp.admin` | 管理权限（设置竞技场坐标、重载配置） | op |
| `pvp.bypass` | 跳过竞技场传送 / 飞行限制（OP 默认拥有） | op |
| `pvp.team` | 允许创建团战房间 | True |
| `pvp.use` | 允许使用 PVP 决斗功能 | True |
