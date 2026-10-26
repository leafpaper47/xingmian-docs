---
title: YiyunCEskin
createTime: 2026/10/24
---

# 云皮肤 · YiyunCEskin

> 分类 🧟 生物与展示 · 版本 `1.3.0` · 指令 1 条 · api-version `1.21`

::: tip 给 CraftEngine 物品条目套用云皮肤的配套插件
YiyunCEskin 是星冕自研的皮肤类插件，定位是 CraftEngine 兼容项目，用于把皮肤外观挂到 CraftEngine 的条目上。插件只注册一个主命令 yiyunceskin（别名 yskin），日常玩家使用只受 yiyunceskin.use 控制，管理侧改动需要 yiyunceskin.admin。官方资料只给出了插件名与权限节点，没有公开子指令清单，因此具体用法要以游戏内 help 与配置为准。
:::

## 什么时候会用到它

- 给 CraftEngine 物品或外观条目套用并切换皮肤
- 让玩家用 yskin 命令查看或更换自己的皮肤外观
- 服主调整皮肤配置与权限后做验证

## 上手流程

1. 先确认服务器已安装 CraftEngine，且本插件与之版本匹配
2. 在 config 等配置文件中准备好可用的皮肤条目
3. 给玩家组分配 yiyunceskin.use（默认即为 true），管理操作再给 yiyunceskin.admin
4. 进游戏执行 yiyunceskin 或 yskin 查看可用子命令并逐项试跑

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
- 改配置后建议重启而非热重载，避免皮肤缓存未刷新
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `yiyunceskin.admin` | YiyunCEskin的管理员权限 | op |
| `yiyunceskin.use` | 基本皮肤使用权限 | true |

## 相关插件

CraftEngine
