---
title: KaoguGuide
createTime: 2026/10/24
---

# 考古指南 · KaoguGuide

> 分类 ⚔️ 战斗与 RPG · 版本 `1.0.0` · 指令 1 条 · api-version `1.13`

::: tip 用图鉴界面查看玩家已修复过的古物
KaoguGuide 是星冕服务器自研的考古图鉴插件，用于把玩家在考古玩法中修复过的古物记录成一份可视化图鉴。玩家打开图鉴界面后，可以查看自己已解锁与尚未解锁的古物条目。它本身不产生古物，只负责整理与展示考古进度，权限节点分为普通使用与管理员重载两级。
:::

## 什么时候会用到它

- 让玩家查看自己已修复过哪些古物、还差哪些没解锁
- 作为考古玩法的进度面板，给玩家一个长期收集目标
- 排查玩家考古记录异常时用来核对图鉴里实际显示的内容
- 活动或赛季初期向玩家展示新的古物收集清单

## 上手流程

1. 确认服务端已安装 KaoguGuide，并且考古玩法本身已能正常产出与修复古物
2. 确认玩家拥有 kaoguguide.use 权限（默认所有玩家都有）
3. 玩家在游戏内输入 /kaoguguide 或别名 /tg 打开图鉴
4. 在图鉴界面里逐项查看已修复与未修复的古物；数据改动后由管理员重载图鉴数据

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/kaoguguide` | 打开玩家自己的考古图鉴界面<br>别名 `/kaogutujian`、`/tg` | `/kaoguguide` | — |

## 指令详解

### `/kaoguguide` — 打开玩家自己的考古图鉴界面

- **语法**：`/kaoguguide`

- **示例**：

```
/kaoguguide
/tg
/kaogutujian
```

- **别名**：`/kaogutujian`、`/tg`
- **备注**：别名 kaogutujian、tg 均指向同一指令；使用需要 kaoguguide.use 权限，默认对所有玩家开放。图鉴只展示记录，不能在此界面里修复或兑换古物。

## 注意事项

::: warning
- 这是星冕自研插件，具体参数与子指令以游戏内 help 为准，本页只覆盖已知的用法。
- 图鉴内容依赖考古玩法产生的修复记录，若玩家看不到条目前先确认上游记录是否真的写入。
- 重载图鉴数据需要 kaoguguide.admin（默认仅 OP），重载前建议先确认没有玩家正在浏览界面。
- 别把图鉴当作进度备份，重载或清理数据前先备份相关存档文件。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `kaoguguide.admin` | 允许重载图鉴数据 | op |
| `kaoguguide.use` | 允许使用考古图鉴 | True |

## 相关插件

[LuckPerms](/commands/core/luckperms.md)、[PlaceholderAPI](/commands/config/placeholderapi.md)、[CMILib](/commands/essentials/cmilib.md)
