---
title: EliteMobs
createTime: 2026/10/24
---

# 精英怪物 · EliteMobs

> 分类 ⚔️ 战斗与 RPG · 版本 `1.0.0` · 指令 1 条 · api-version `1.21`

::: tip 精英怪物的生成与运维管理
EliteMobs 是星冕服务器用来生成和管理精英怪物的 RPG 插件，用来替代早期的 strong_mobs.sk 脚本方案。管理员只需一条 /elitemobs 指令，就能完成精英怪功能的开关、状态查看、配置重载和手动刷怪。它适合在开活动、调难度或临时关掉精英怪时快速介入，不必改脚本再重启服务端。所有能力都收在 elitemobs.admin 权限节点下。
:::

## 什么时候会用到它

- 开活动前临时开启或关闭精英怪
- 进服后快速确认精英怪功能是否正在运行
- 改完配置后热重载，避免重启服务端
- 在指定场合手动刷出一只精英怪做测试或演出

## 上手流程

1. 先给执行者授予 elitemobs.admin 权限（可用 LuckPerms 加到管理员组）
2. 用 /elitemobs status 确认当前精英怪开关状态
3. 按需执行 /elitemobs on、/elitemobs off 或 /elitemobs toggle 切换功能
4. 改过配置文件后用 /elitemobs reload 让新配置生效
5. 需要现场刷怪时执行 /elitemobs spawn，具体参数先看游戏内 help

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/elitemobs` | 精英怪总开关、状态查询、配置重载与手动刷怪<br>别名 `/elite`、`/em` | `/elitemobs on｜off｜toggle｜status｜reload｜spawn` | `elitemobs.admin` |

## 指令详解

### `/elitemobs` — 精英怪总开关、状态查询、配置重载与手动刷怪

- **语法**：`/elitemobs on｜off｜toggle｜status｜reload｜spawn`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `on｜off｜toggle｜status｜reload｜spawn` | 必填 | 要执行的动作：开启、关闭、切换、查看状态、重载配置或刷怪 |


- **示例**：

```
/elitemobs status
/elitemobs toggle
/elitemobs reload
/em spawn
```

- **别名**：`/elite`、`/em`
- **权限**：`elitemobs.admin`
- **备注**：别名 /elite 与 /em；需要 elitemobs.admin 权限，默认仅 OP 拥有。spawn 的具体参数格式以游戏内 help 为准。

## 注意事项

::: warning
- 本插件是服内自研实现，具体参数以游戏内 help 为准
- spawn 动作的附加参数文档未给出，建议先看 help 再执行，避免刷出意外怪物
- reload 只重载插件自身配置，已在场的精英怪是否被清理需实测确认
- 批量调整前先备份精英怪相关配置文件，出问题可回滚
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `elitemobs.admin` | 管理 EliteMobs（开关/重载/刷怪） | op |

## 相关插件

[LuckPerms](/commands/core/luckperms.md)、[Skript](/commands/config/skript.md)
