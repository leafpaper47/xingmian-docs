---
title: BossBarHealth
createTime: 2026/10/24
---

# BOSS血条 · BossBarHealth

> 分类 🧟 生物与展示 · 版本 `4.1.16-SNAPSHOT` · 指令 1 条 · api-version `1.13`

::: tip 用BOSS栏实时显示玩家
BossBarHealth 把玩家自己以及当前目标生物的生命值画在屏幕顶部的 BOSS 栏上，打架时不用一直盯着血条也知道还剩多少。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 开关 BOSS 血条 | /bossbarhealth | 带玩家参数可单独设置 |

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
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `BossBarHealth.Admin` | 授予对所有命令的访问权限 | op |
| `BossBarHealth.Hide` | 允许访问/bbh hide | True |
| `BossBarHealth.Show` | 允许访问/bbh节目 | True |
