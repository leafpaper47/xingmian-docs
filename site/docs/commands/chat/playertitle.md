---
title: PlayerTitle
createTime: 2026/10/24
---

# 称号 · PlayerTitle

> 分类 💬 聊天与社交 · 版本 `5.0.6` · 指令 1 条 · api-version `1.13`

::: tip 称号系统：发放、展示、商城与收藏
PlayerTitle 给服务器加一套完整的「称号」玩法：玩家可以从称号仓库里更换头顶/聊天显示的称号，也能在称号商城里用称号币购买新称号。管理侧负责发称号、发称号币和称号卡，并可给称号挂粒子和属性 buff。它通常和聊天格式、经济类插件一起用，称号通过占位符显示到聊天、计分板或 TAB 列表里。
:::

## 什么时候会用到它

- 想给服务器加一个玩家可以自己收集、切换的称号系统时
- 做活动或充值回馈，要给玩家发限定称号、称号币、称号卡时
- 需要称号带粒子特效或属性加成，做成「有特效的称号」时
- 玩家称号显示错乱或数据异常，需要查人、清理某人称号数据时

## 上手流程

1. 先把插件放进 plugins 目录启动一次，生成配置与数据库，再按需改配置里的称号列表和商城价格
2. 执行 /playerTitle 打开主界面，确认自己能看到称号仓库和称号商城的入口
3. 给自己的管理账号加上 playerTitle.* 或其下需要的子权限，避免用 OP 直接测
4. 给测试玩家发一个称号并让他在仓库里换上，确认聊天/头顶显示正常
5. 接第三方显示时，到聊天格式或 TAB 配置里写 PlayerTitle 提供的称号占位符

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/playerTitle` | 称号插件主指令，打开界面或进入各类称号子功能<br>别名 `/plt` | `/playerTitle` | — |

## 指令详解

### `/playerTitle` — 称号插件主指令，打开界面或进入各类称号子功能

- **语法**：`/playerTitle`

- **示例**：

```
/playerTitle
/plt
```

- **别名**：`/plt`
- **备注**：别名 /plt。输入后一般会输出可用子指令列表或直接打开称号仓库界面；具体子指令与参数以游戏内输入该指令后的提示和 help 输出为准。玩家侧常用的是打开仓库和商城，管理侧对应 reload、发放称号、称号币、称号卡、buff、粒子、查人、清理数据等权限节点。

## 注意事项

::: warning
- 本插件以主指令加子功能的形式工作，具体参数与子指令以游戏内 help 为准，不同版本可能增删，不要照抄网上旧教程的写法
- playerTitle.open 与 playerTitle.shop 默认对所有人开放，其余权限默认仅 OP；给普通玩家放开时要逐个确认，别直接给 playerTitle.*
- 称号数据存数据库，重载配置前先在测试服验证；涉及清数据、转数据库类操作务必先备份
- 称号粒子与 buff 可能受世界限制（有忽略世界限制的独立权限），换世界后效果消失属正常现象，先确认是不是被世界限制了
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `playerTitle.*` | 玩家称号 | — |
| `playerTitle.buff` | 称号buff相关 | op |
| `playerTitle.buff.ignoreWorld` | 忽略世界禁用属性限制 | op |
| `playerTitle.card` | 称号卡相关 | op |
| `playerTitle.clear` | 清理数据 | op |
| `playerTitle.coin` | 称号币相关 | op |
| `playerTitle.convert` | 转化数据库 | op |
| `playerTitle.getIp` | 获取服务信息 | op |
| `playerTitle.open` | 称号仓库 | True |
| `playerTitle.particle` | 称号粒子相关 | op |
| `playerTitle.player` | 玩家称号相关 | op |
| `playerTitle.reload` | 重载插件 | op |
| `playerTitle.reward` | 称号数量奖励 | op |
| `playerTitle.shop` | 称号商城 | True |
| `playerTitle.shop.custom` | 自定义称号 | True |
| `playerTitle.title` | 称号相关 | op |
| `playerTitle.view` | 查看管理 | op |

## 相关插件

[PlaceholderAPI](/commands/config/placeholderapi.md)、[LuckPerms](/commands/core/luckperms.md)、[Vault](/commands/core/vault.md)、[TAB](/commands/chat/tab.md)
