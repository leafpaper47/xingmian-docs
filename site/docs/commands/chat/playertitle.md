---
title: PlayerTitle
createTime: 2026/10/24
---

# 称号 · PlayerTitle

> 分类 💬 聊天与社交 · 版本 `5.0.6` · 指令 1 条 · api-version `1.13`

::: tip 称号系统
玩家称号的发放、佩戴、商城与粒子特效，称号可带属性增益与展示粒子，是常用的氪金/活动奖励载体。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 玩家看自己的称号 | /plt open | 主界面里佩戴/卸下 |
| 打开称号商城 | /plt shop | 用点券或称号币购买 |
| 给玩家发称号 | /plt title give Steve &lt;称号id&gt; | 补偿/活动发放 |
| 改完配置生效 | /plt reload | 称号表在配置文件里 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/playerTitle` | 玩家称号<br>别名 `/plt` | — | — |

## 指令详解

### `/playerTitle` — 玩家称号

- **别名**：`/plt`

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/plt open` | 打开称号界面（玩家端） | `/plt open` |
| `/plt shop` | 打称号商城（玩家端） | `/plt shop` |
| `/plt title <give｜remove｜list> <玩家> [称号]` | 发放/回收/查询玩家称号 | `/plt title give Steve vip_2025` |
| `/plt card <玩家> <数量>` | 发放称号卡（抽称号的道具） | `/plt card Steve 5` |
| `/plt buff <玩家> <buff> <时长>` | 给玩家的称号附加临时增益 | `/plt buff Steve speed 600` |
| `/plt particle <玩家> <粒子>` | 设置称号展示粒子效果 | `/plt particle Steve flame` |
| `/plt coin <玩家> <数量>` | 调整玩家称号币余额 | `/plt coin Steve 100` |
| `/plt reward <玩家>` | 手动触发称号奖励结算 | `/plt reward Steve` |
| `/plt clear <玩家>` | 清空玩家已获得的称号 | `/plt clear Steve` |
| `/plt player <玩家>` | 查看玩家称号数据面板 | `/plt player Steve` |
| `/plt view <玩家>` | 以只读方式查看玩家当前佩戴的称号 | `/plt view Steve` |
| `/plt getip <玩家>` | 按称号来源查询相关玩家 IP 归属（风控用） | `/plt getip Steve` |
| `/plt reload` | 重载称号配置与商城 | `/plt reload` |
| `/plt convert` | 转换数据源（换存档格式前先备份） | `/plt convert` |

## 注意事项

::: warning
- clear 会清掉玩家所有已获得称号，且通常不带二次确认，操作前先 /plt player 确认。
- 称号带属性增益时，改称号属性会让在线玩家立即生效，注意别把平衡性调崩。
- convert 属于数据迁移，跑之前备份 plugins/PlayerTitle/。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `playerTitle.*` | 玩家称号 | — |
| `playerTitle.buff` | 称号buff相关 | op |
| `playerTitle.buff.ignoreWorld` | 忽略世界禁用属性限制 | op |
| `playerTitle.card` | 称号卡相关 | op |
| `playerTitle.clear` | 清理数据 | op |
| `playerTitle.coin` | 称号币相关 | op |
| `playerTitle.convert` | 转化数据库 | op |
| `playerTitle.getIp` | 获取服务信息 | op |
| `playerTitle.open` | 称号仓库 | True |
| `playerTitle.particle` | 称号粒子相关 | op |
| `playerTitle.player` | 玩家称号相关 | op |
| `playerTitle.reload` | 重载插件 | op |
| `playerTitle.reward` | 称号数量奖励 | op |
| `playerTitle.shop` | 称号商城 | True |
| `playerTitle.shop.custom` | 自定义称号 | True |
| `playerTitle.title` | 称号相关 | op |
| `playerTitle.view` | 查看管理 | op |
| `playertitle.admin` | 称号管理（发放/回收/重载） | — |
| `playertitle.shop` | 使用称号商城 | — |
| `playertitle.use` | 使用称号界面（默认开启） | — |
