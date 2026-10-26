---
title: BlockLocker
createTime: 2026/10/24
---

# 箱子锁 · BlockLocker

> 分类 🔒 领地与保护 · 版本 `1.14.1` · 指令 1 条 · api-version `1.20`

::: tip 用告示牌给箱子门做私有上锁
BlockLocker 让玩家把告示牌贴在箱子、熔炉、门等容器或方块上，写上标签就完成上锁与授权，不必依赖命令或额外 GUI。它管的是「某个箱子/门谁能开」，与领地类插件（如 Residence、TownGuard）分属两层：领地管地皮，BlockLocker 管单个容器。管理员只保留少量维护命令，日常操作基本都在游戏内贴牌子完成。
:::

## 什么时候会用到它

- 玩家在公共区域放箱子，怕仓库、熔炉被翻，需要只给自己的容器上锁
- 多名玩家合住一个基地，需要把某个箱子共享给队友（而不是所有人）
- 开门联动的红石机关或计时器需要对外公开，又不能顺带泄漏里面的箱子
- 管理员排查「这箱子到底谁锁的」，或玩家退服后需要解除/转交他人保护

## 上手流程

1. 确认配置里启用了告示牌保护，并给普通玩家保留 blocklocker.protect 权限（默认开启）
2. 进游戏拿告示牌贴在箱子上，第一行写 Private（私有）即完成上锁；需共享时换成 More Users 并把队友名字写在后面
3. 告诉玩家上锁后自己是唯一能开箱/开门的 Owner，被授权者写在同一张牌上即可，无需再装插件或进菜单
4. 管理员用 blocklocker.bypass 只查看不改动，需要真正改他人保护时用 blocklocker.admin
5. 改动配置或语言文件后执行 /blocklocker reload 生效，不必重启服务端

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/blocklocker` | 插件管理命令，目前主要用于重载配置<br>别名 `/b`、`/l` | `/blocklocker reload` | `blocklocker.reload` |

## 指令详解

### `/blocklocker` — 插件管理命令，目前主要用于重载配置

- **语法**：`/blocklocker reload`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `reload` | 必填 | 重新读取配置文件与语言文件，改动后才需要执行 |


- **示例**：

```
/blocklocker reload
```

- **别名**：`/b`、`/l`
- **权限**：`blocklocker.reload`
- **备注**：输入 /blocklocker 不带参数会提示用法；别名可用 /bl 等短写。需要 blocklocker.reload 权限（默认仅 OP）。玩家侧上锁不靠命令，而是贴告示牌写标签，例如第一行写 Private 表示私有、写 More Users 表示额外授权名单（玩家名写在同一张牌的下方各行）。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `blocklocker reload` | 重载插件配置与语言文件 | `/blocklocker reload` |

## 注意事项

::: warning
- 别把 blocklocker.bypass 当日常权限发给管理组：它能直接打开他人容器，容易误操作或引发玩家纠纷；只想查看状态时更应慎用
- blocklocker.admin 可以改别人的保护标记甚至完全取消保护，属于破坏性操作，建议只给服主或极少数人，操作前先告知玩家
- 告示牌一旦被破坏或掉落，保护可能随之失效，配置里若有告示牌掉落/破坏相关开关请谨慎调整
- 与领地类插件是叠加关系而不是替代：在 Towny 领地内荒野权限（blocklocker.wilderness）不生效，排查「为什么锁不上」时先看所在区域归属
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `blocklocker.admin` | 编辑某人的防护标志，或完全取消防护。 | op |
| `blocklocker.bypass` | 绕过他人的保护，但不要允许破坏它。 | op |
| `blocklocker.protect` | 保护容器和门。 | True |
| `blocklocker.reload` | 使用/blocklocker reload重新加载插件。 | op |
| `blocklocker.wilderness` | 在荒野中放置宝箱（在Towny领地之外） | True |

## 相关插件

WorldGuard、[Residence](/commands/protect/residence.md)、Towny、[CoreProtect](/commands/audit/coreprotect.md)
