---
title: BetterRTP
createTime: 2026/10/24
---

# 随机传送 · BetterRTP

> 分类 🌀 传送与出生点 · 版本 `3.6.13` · 指令 1 条 · api-version `1.13`

::: tip 功能全面的随机传送插件，主世界野外探索标配
BetterRTP 负责把玩家随机丢到指定世界的安全落点，是开荒服、生存服替代固定出生点的主要手段。它支持按世界、生物群系、指定玩家、指定坐标发起随机传送，并可配置冷却、传送延迟、扣费、饥饿消耗等限制。落点安全性由插件自行搜索合适方块决定，避免把玩家送进岩浆或虚空。权限可细化到世界与权限组，方便做不同档位的传送额度。
:::

## 什么时候会用到它

- 给新玩家一个随机落点，避免全服挤在出生点
- 让玩家用 /rtp 快速去远处开荒挖矿
- 把玩家随机传送到下界、末地等指定世界
- 限定生物群系传送，做特定玩法或资源区
- 用权限组区分普通玩家与捐赠玩家的传送冷却和范围

## 上手流程

1. 确认 config 里已启用目标世界并设好中心点与半径
2. 在 LuckPerms 给玩家组 betterrtp.use，需要跨世界则加 betterrtp.world 及对应世界节点
3. 改完配置执行 /rtp reload 让设置生效，用 /rtp info 核对各世界参数
4. 首次上线前用 /rtp test 检查粒子、音效、药水提示是否正常
5. 正式使用后观察日志与玩家反馈，按需调半径、冷却与落点搜索次数

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/betterrtp` | 随机传送到安全落点，可加子指令指定世界、玩家、生物群系或坐标<br>别名 `/brtp`、`/rtp`、`/randomtp`、`/wild`、`/wildtp` | `/rtp [子指令] [参数]` | — |

## 指令详解

### `/betterrtp` — 随机传送到安全落点，可加子指令指定世界、玩家、生物群系或坐标

- **语法**：`/rtp [子指令] [参数]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子指令` | 可选 | world 世界名 / player 玩家名 / biome 生物群系 / location 坐标 / reload / info / version / help |
| `参数` | 可选 | 随子指令变化，如世界名、玩家名、生物群系 id 或 x z 坐标 |


- **示例**：

```
/rtp
/rtp world world_nether
/rtp player Steve
/rtp biome desert
/rtp reload
```

- **别名**：`/brtp`、`/rtp`、`/randomtp`、`/wild`、`/wildtp`
- **备注**：别名 brtp、rtp、randomtp、wild、wildtp 均可用；不带子指令时在当前世界随机传送。子指令的具体参数顺序以游戏内 /rtp help 为准。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `world 世界名` | 在指定世界随机传送，需要 betterrtp.world 与该世界的权限节点 | `/rtp world world_nether` |
| `player 玩家名` | 把指定玩家随机传送走，需要 betterrtp.player | `/rtp player Steve` |
| `biome 生物群系` | 传送到指定生物群系的随机位置，需要 betterrtp.biome | `/rtp biome desert` |
| `location 坐标` | 以指定位置为中心随机传送，需要 betterrtp.location | `/rtp location 0 0` |
| `reload` | 重载配置文件，需要 betterrtp.reload | `/rtp reload` |
| `info` | 查看各世界的随机传送参数与生效情况，需要 betterrtp.info | `/rtp info` |
| `version` | 查看当前运行版本，需要 betterrtp.version | `/rtp version` |
| `edit 世界 中心或半径 数值` | 直接改某世界的传送中心或半径，需要 betterrtp.edit | `/rtp edit world 5000` |
| `test 类型` | 开启调试后测试粒子、药水效果与声音，需要 betterrtp.test | `/rtp test particle` |
| `help` | 列出全部子指令与用法 | `/rtp help` |

## 注意事项

::: warning
- 跨世界传送要该世界已在配置里启用并给到对应 betterrtp.world.世界名 权限，否则玩家只会被拒
- 半径设太大或玩家频繁使用会明显吃性能，建议配合冷却与传送延迟限制
- betterrtp.bypass.cooldown、delay、economy、hunger 属特权，只给管理员或特定组，否则限流形同虚设
- 改完配置务必 /rtp reload 并用 /rtp info 确认生效，语法细节以游戏内 /rtp help 为准
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `betterrtp.*` | — | — |
| `betterrtp.biome` | 特定生物群落的RTP | — |
| `betterrtp.bypass.*` | — | — |
| `betterrtp.bypass.cooldown` | 绕过冷却时间 | — |
| `betterrtp.bypass.delay` | 绕过延迟 | — |
| `betterrtp.bypass.economy` | 旁路经济 | — |
| `betterrtp.bypass.hunger` | 绕过饥饿 | — |
| `betterrtp.edit` | 编辑自定义/默认世界rtp中心/半径 | op |
| `betterrtp.group.*` | 使用权限组以不同的限制进行rtp | — |
| `betterrtp.info` | 查看有关rtp将工作的所有世界的信息 | op |
| `betterrtp.location` | 使用特定位置的RTP | — |
| `betterrtp.player` | RTP其他玩家 | — |
| `betterrtp.reload` | 重新加载配置 | op |
| `betterrtp.sign` | 能够创建RTP标志 | — |
| `betterrtp.test` | 启用调试器后，能够测试粒子、药水效果和声音 | op |
| `betterrtp.updater` | 获取有关新更新的通知 | op |
| `betterrtp.use` | 使用RTP命令 | True |
| `betterrtp.version` | 查看正在运行的版本 | — |
| `betterrtp.world` | 使用世界命令 | — |
| `betterrtp.world.*` | 所有已启用世界中的RTP | — |

## 相关插件

[Vault](/commands/core/vault.md)、[LuckPerms](/commands/core/luckperms.md)、[PlaceholderAPI](/commands/config/placeholderapi.md)、[Essentials](/commands/essentials/essentials.md)
