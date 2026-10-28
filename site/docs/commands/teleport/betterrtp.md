---
title: BetterRTP
createTime: 2026/10/24
---

# 随机传送 · BetterRTP

> 分类 🌀 传送与出生点 · 版本 `3.6.13` · 指令 1 条 · api-version `1.13`

::: tip 随机传送
随机传送玩家到安全落点，支持按世界/生物群系指定、组队队列、冷却与经济扣费，是生存服最常用的传送工具。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 玩家随机传送 | /rtp | 默认在当前世界随机找安全点 |
| 传到指定世界 | /rtp world resource | 世界名用 Multiverse 里的名字 |
| 传送到某生物群系 | /rtp biome desert | 找不到符合条件的点会失败重试 |
| 帮别人传送 | /rtp player Steve | 管理员代传，不影响自己位置 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/betterrtp` | 随机传送到一个位置<br>别名 `/brtp`、`/rtp`、`/randomtp`、`/wild`、`/wildtp` | — | — |

## 指令详解

### `/betterrtp` — 随机传送到一个位置

- **别名**：`/brtp`、`/rtp`、`/randomtp`、`/wild`、`/wildtp`

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/rtp world <世界>` | 在指定世界随机传送 | `/rtp world resource` |
| `/rtp biome <群系>` | 传送到指定生物群系 | `/rtp biome desert` |
| `/rtp player <玩家>` | 把指定玩家随机传送 | `/rtp player Steve` |
| `/rtp location <世界> <x> <z>` | 传送到指定的坐标点（不走随机） | `/rtp location world 100 200` |
| `/rtp queue` | 查看/管理排队中的传送请求 | `/rtp queue` |
| `/rtp settings` | 查看当前生效的传送参数（范围/冷却/重试） | `/rtp settings` |
| `/rtp info` | 查看玩家或世界的传送限制 | `/rtp info` |
| `/rtp reload` | 重载配置 | `/rtp reload` |
| `/rtp test` | 跑一次落点测试（不实际传送） | `/rtp test` |
| `/rtp version` | 查看版本与更新状态 | `/rtp version` |
| `/rtp logger` | 开启/关闭传送日志记录 | `/rtp logger` |
| `/rtp edit` | 交互式修改配置项 | `/rtp edit` |

## 注意事项

::: warning
- 落点安全判定有重试上限，重试打满会直接失败；把「最大尝试次数」调太低会导致频繁传送失败。
- 跨世界传送要求世界名与服务器实际世界键一致（Multiverse 自定义维度名容易写错）。
- 冷却与经济扣费分「成功才扣」和「发起就扣」两种配置，改错会让玩家白扣钱。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `betterrtp.*` | — | — |
| `betterrtp.admin` | 管理指令（reload / edit / settings） | — |
| `betterrtp.biome` | 允许按生物群系传送 | — |
| `betterrtp.bypass.*` | — | — |
| `betterrtp.bypass.cooldown` | 跳过传送冷却 | — |
| `betterrtp.bypass.delay` | 绕过延迟 | — |
| `betterrtp.bypass.economy` | 旁路经济 | — |
| `betterrtp.bypass.hunger` | 绕过饥饿 | — |
| `betterrtp.edit` | 编辑自定义/默认世界rtp中心/半径 | op |
| `betterrtp.group.*` | 使用权限组以不同的限制进行rtp | — |
| `betterrtp.info` | 查看有关rtp将工作的所有世界的信息 | op |
| `betterrtp.location` | 使用特定位置的RTP | — |
| `betterrtp.other` | 给其他玩家传送（player / playersudo） | — |
| `betterrtp.player` | RTP其他玩家 | — |
| `betterrtp.reload` | 重新加载配置 | op |
| `betterrtp.sign` | 能够创建RTP标志 | — |
| `betterrtp.test` | 启用调试器后，能够测试粒子、药水效果和声音 | op |
| `betterrtp.updater` | 获取有关新更新的通知 | op |
| `betterrtp.use` | 使用 /rtp 随机传送 | True |
| `betterrtp.version` | 查看正在运行的版本 | — |
| `betterrtp.world` | 使用世界命令 | — |
| `betterrtp.world.*` | 所有已启用世界中的RTP | — |
| `betterrtp.world.<世界>` | 允许传送到指定世界 | — |
