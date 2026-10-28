---
title: KaoguGuide
createTime: 2026/10/24
---

# 考古图鉴 · KaoguGuide

> 分类 🍳 烹饪与采集 · 版本 `1.0.0` · 指令 1 条 · api-version `1.13`

::: tip 考古图鉴
展示玩家已修复过的古物收集进度，是考古玩法的收集册界面，本身不含玩法逻辑。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 玩家看收集进度 | /kaoguguide | 别名 /tg、/kaogutujian |
| 改完图鉴数据 | /kaoguguide reload | 需 kaoguguide.admin；无反应就 /plugman reload KaoguGuide |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/kaoguguide` | 打开考古收集图鉴<br>别名 `/kaogutujian`、`/tg` | `/kaoguguide [reload]` | — |

## 指令详解

### `/kaoguguide` — 打开考古收集图鉴

- **语法**：`/kaoguguide [reload]`

- **示例**：

```
/kaoguguide
```

- **别名**：`/kaogutujian`、`/tg`
- **备注**：别名 /kaogutujian、/tg；数据来自 KaoguPlugin 的玩家修复记录

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/kaoguguide reload` | 重载图鉴配置与古物清单 | `/kaoguguide reload` |

## 注意事项

::: warning
- 图鉴显示的是「已修复过」的古物，只有化石没修复过的不会点亮。
- 图鉴与 KaoguPlugin 是两套数据，KaoguPlugin 重载后本插件不会自动同步，需要 reload 一次。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `kaoguguide.admin` | 重载图鉴数据 | op |
| `kaoguguide.use` | 使用考古图鉴（默认开启） | True |
