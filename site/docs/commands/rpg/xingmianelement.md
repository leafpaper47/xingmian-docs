---
title: XingmianElement
createTime: 2026/10/24
---

# 元素系统 · XingmianElement

> 分类 ⚔️ 战斗与 RPG · 版本 `0.1.17` · 指令 2 条 · api-version `1.21`

::: tip 星冕自研的元素等级与法杖技能系统
给玩家一条以元素为核心的成长线：打怪、做任务攒经验来提升元素等级，再用元素法杖释放对应技能。元素还牵动元素 BOSS 的强度与表现，所以它同时是 RPG 玩法与 BOSS 战之间的连接层。本插件为星冕服务器自研模块，官方说明写得比较潦草，实际细节以游戏内帮助为准。
:::

## 什么时候会用到它

- 玩家问「我的元素等级怎么升」「法杖技能怎么放」时，指给他看元素面板与帮助
- 新玩家刚进服，需要引导他了解元素属性这条养成线
- 测试或调活动时，要临时指定下一只元素 BOSS 带几个元素
- 排查「为什么这只元素 BOSS 打起来强度不对」时，查当前 BOSS 的元素配置状态

## 上手流程

1. 先给玩家或自己加上 xingmianelement.admin 权限（该节点默认仅 OP 拥有），否则 xmbe 调试指令用不了
2. 管理员在游戏里执行 /element help 看一眼这版插件实际开放的用法，别照抄网上或旧版说明
3. 玩家侧从元素面板确认自己的元素属性与等级进度，再按提示去获取元素法杖
4. 需要调节 BOSS 难度时，用 /xmbe info 看当前设定，再用 /xmbe next 指定数量做验证，测完记得用 /xmbe next off 关掉

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/element` | 元素之力主指令，打开帮助、查看元素等级与法杖技能入口<br>别名 `/elem`、`/ys` | `/element help` | — |
| `/xmbe` | 元素 BOSS 调试，强制指定下一只 BOSS 的元素数量或查看状态 | `/xmbe next 数量1-5 ｜ /xmbe next off ｜ /xmbe info` | `xingmianelement.admin` |

## 指令详解

### `/element` — 元素之力主指令，打开帮助、查看元素等级与法杖技能入口

- **语法**：`/element help`

- **示例**：

```
/element help
```

- **别名**：`/elem`、`/ys`
- **备注**：别名 /elem、/ys，玩家常用别名进来。无需权限即可使用。这条指令下的子指令各服版本差异较大，以游戏内 help 输出的为准，不要凭猜测输入。

### `/xmbe` — 元素 BOSS 调试，强制指定下一只 BOSS 的元素数量或查看状态

- **语法**：`/xmbe next 数量1-5 ｜ /xmbe next off ｜ /xmbe info`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `next 数量` | 必填 | 填 1 到 5 之间的整数，表示下一只元素 BOSS 要带几个元素；off 表示取消这个强制设定，info 查看当前状态 |


- **示例**：

```
/xmbe info
/xmbe next 3
/xmbe next off
```

- **权限**：`xingmianelement.admin`
- **备注**：需要 xingmianelement.admin 权限（默认 OP）。这是调试用指令，只影响下一次刷新，测完务必用 off 恢复，否则线上 BOSS 难度会跟你测试时的设定一致。

## 注意事项

::: warning
- 本插件为星冕自研，具体参数与子指令以游戏内 help 为准，本页只保证 /element help 与 /xmbe 三条用法存在
- xmbe 的 next 设定是「下一只」生效的临时调试开关，忘了关会让线上元素 BOSS 数量异常，收尾一定执行 /xmbe next off
- xingmianelement.admin 默认只有 OP 有，给管理员配组权限时记得在 LuckPerms 里显式加上，别只给普通管理组
- 元素等级与法杖技能的具体数值走配置文件，改完记得确认生效方式（重载还是重启），不要在 BOSS 战进行中乱改
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `xingmianelement.admin` | 元素之力管理权限 | op |

## 相关插件

[LuckPerms](/commands/core/luckperms.md)
