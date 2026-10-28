---
title: YiyunCEskin
createTime: 2026/10/24
---

# 云皮肤 · YiyunCEskin

> 分类 🧟 生物与展示 · 版本 `1.3.0` · 指令 1 条 · api-version `1.21`

::: tip 给 CraftEngin
YiyunCEskin 是星冕自研的皮肤类插件，定位是 CraftEngine 兼容项目，用于把皮肤外观挂到 CraftEngine 的条目上。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 换皮肤或查皮肤 | /yiyunceskin | 子命令以 help 为准 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/yiyunceskin` | 插件主命令，用于执行皮肤相关操作，具体子命令以游戏内 help 为准<br>别名 `/yskin` | `/yiyunceskin` | `yiyunceskin.use` |

## 指令详解

### `/yiyunceskin` — 插件主命令，用于执行皮肤相关操作，具体子命令以游戏内 help 为准

- **语法**：`/yiyunceskin`

- **示例**：

```
/yiyunceskin
/yskin
```

- **别名**：`/yskin`
- **权限**：`yiyunceskin.use`
- **备注**：别名 yskin；玩家侧需 yiyunceskin.use（默认 true），管理操作用 yiyunceskin.admin（默认 op）

## 注意事项

::: warning
- 本插件为星冕自研，官方只公布了主命令，具体参数以游戏内 help 为准，不要凭猜测拼参数
- 皮肤条目依赖 CraftEngine，CraftEngine 未装或版本不匹配时功能会异常
- yiyunceskin.admin 默认仅 op 拥有，普通管理组需在 LuckPerms 中单独授予
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `yiyunceskin.admin` | YiyunCEskin的管理员权限 | op |
| `yiyunceskin.use` | 基本皮肤使用权限 | true |
