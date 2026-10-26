---
title: BossBarHealth
createTime: 2026/10/24
---

# BOSS血条 · BossBarHealth

> 分类 🧟 生物与展示 · 版本 `4.1.16-SNAPSHOT` · 指令 1 条 · api-version `1.13`

::: tip 用BOSS栏实时显示玩家与敌人血量的HUD插件
BossBarHealth 把玩家自己以及当前目标生物的生命值画在屏幕顶部的 BOSS 栏上，打架时不用一直盯着血条也知道还剩多少。它对外只暴露一个主命令，实际效果主要靠权限节点和插件自带配置决定。适合想让战斗信息更直观的生存服或 RPG 服使用，属于小众插件，命令细节请以游戏内 help 为准。
:::

## 什么时候会用到它

- 战斗时随时看到自己与敌人的剩余生命值
- 给生存服或RPG服增加一条直观的血量HUD
- 按玩家权限分别控制谁能显示、谁能隐藏这条BOSS栏

## 上手流程

1. 把插件放入 plugins 目录后重启服务器
2. 按需编辑插件配置，调整显示样式与刷新频率
3. 给对应玩家组配置 BossBarHealth.Show 与 BossBarHealth.Hide 权限
4. 玩家用主命令及其子指令打开或关闭血条显示

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/bossbarhealth` | 插件主命令，用于管理或开关BOSS栏血量显示<br>别名 `/bbh` | `/bossbarhealth` | — |

## 指令详解

### `/bossbarhealth` — 插件主命令，用于管理或开关BOSS栏血量显示

- **语法**：`/bossbarhealth`

- **示例**：

```
/bossbarhealth
/bbh
```

- **别名**：`/bbh`
- **备注**：别名为 bbh；输入后按提示继续，具体子指令与参数以游戏内 help 为准

## 注意事项

::: warning
- 本插件属于小众插件，命令与配置项请以游戏内 help 和插件自带配置为准，不要照搬其它血条插件的写法
- 具体参数以游戏内 help 为准
- BossBarHealth.Admin 默认只有 OP 拥有，给管理组授权时需要单独添加
- Show 与 Hide 两个节点默认对所有玩家开放，不希望玩家自己关掉血条时可以改默认值
- 同时安装多个血条类插件可能抢占同一个 BOSS 栏位置，出现不显示时先排查冲突
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `BossBarHealth.Admin` | 授予对所有命令的访问权限 | op |
| `BossBarHealth.Hide` | 允许访问/bbh hide | True |
| `BossBarHealth.Show` | 允许访问/bbh节目 | True |

## 相关插件

[TAB](/commands/chat/tab.md)、[PlaceholderAPI](/commands/config/placeholderapi.md)
