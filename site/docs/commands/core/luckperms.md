---
title: LuckPerms
createTime: 2026/10/24
---

# 权限组 · LuckPerms

> 分类 🛡️ 基础与权限 · 版本 `5.5.53` · 指令 1 条 · api-version `1.13`

::: tip 全局权限系统：组 / 玩家 / 权限节点
服务器里「谁能用什么指令、谁能进哪个世界」最终都由 LuckPerms 说了算。它把权限节点挂在「组」或「玩家」身上，玩家可以继承多个组，最终按继承链算出他能干什么。其它插件（Essentials、Residence、MythicMobs 等）只负责声明权限节点，真正发不发权限看这里。
:::

## 什么时候会用到它

- 给某个组开/关某条指令的权限，比如让 VIP 组能用 /fly、能进 /warp vip
- 查某个玩家到底有哪些权限、是从哪个组继承来的（排查「我明明给了权限他还是用不了」）
- 给玩家或组设置聊天前缀/后缀、权重，配合 TAB、聊天插件显示
- 临时给某个玩家单独加一条权限（不改组），活动结束再收回

## 上手流程

1. 改权限前先想清楚改「组」还是改「个人」：长期规则改组，临时特例改个人，否则后期没人记得清理
2. 推荐用网页编辑器：`/lp editor` 会给一个链接，在浏览器里批量勾选，保存后自动生效
3. 命令行逐条改：`/lp group <组> permission set <节点> true`（收回用 `false`）
4. 改完用 `/lp user <玩家> permission check <节点>` 或 `/lp verbose on` 验证是否真的生效
5. 多服（群组服）环境改完执行 `/lp sync` 让其它子服立刻同步

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/luckperms` | 权限系统总入口，所有操作都通过它的子指令完成<br>别名 `/lp`、`/perm`、`/perms`、`/permission`、`/permissions` | `/lp <子指令> [参数]` | — |

## 指令详解

### `/luckperms` — 权限系统总入口，所有操作都通过它的子指令完成

- **语法**：`/lp <子指令> [参数]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `<子指令>` | 必填 | user / group / editor / sync / verbose / info / tree / log 等，见下方子指令速查 |
| `[参数]` | 可选 | 依子指令而定，例如 `permission set <节点> true` |


- **示例**：

```
/lp editor
/lp group vip permission set essentials.fly true
/lp user Steve info
/lp verbose on
```

- **别名**：`/lp`、`/perm`、`/perms`、`/permission`、`/permissions`
- **备注**：所有子指令都以 `/lp` 开头（`/luckperms` 等价）。子指令支持简写：`perm` = `permission`，`u` = `user`，`g` = `group`。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `editor` | 生成网页编辑器链接，在浏览器里批量改权限（最推荐） | `/lp editor` |
| `user <玩家> info` | 查看玩家的组、权限节点、meta、继承链 | `/lp user Steve info` |
| `user <玩家> permission set <节点> <true｜false>` | 给单个玩家开/关某条权限（临时特例用这个） | `/lp user Steve permission set essentials.fly true` |
| `group <组> info` | 查看某个组的全部权限与继承关系 | `/lp group vip info` |
| `group <组> permission set <节点> <true｜false>` | 给组开/关某条权限（长期规则用这个） | `/lp group vip permission set essentials.fly true` |
| `group <组> parent add <父组>` | 让组继承另一个组（做 VIP→MVP 这种分层） | `/lp group mvp parent add vip` |
| `user <玩家> parent add <组>` | 把玩家加进某个组 | `/lp user Steve parent add vip` |
| `user <玩家> meta setprefix <前缀>` | 设置聊天前缀（配合 TAB / 聊天插件显示） | `/lp user Steve meta setprefix "[VIP] "` |
| `verbose on` | 监听权限判定过程，排查「这个指令为什么没权限」的利器 | `/lp verbose on` |
| `sync` | 多服环境强制同步数据（单服可不执行） | `/lp sync` |
| `log search <关键字>` | 查谁什么时候改了权限（变更审计） | `/lp log search Steve` |

## 注意事项

::: warning
- `permission set <节点> false` 是「显式拒绝」，会盖过继承来的 true；想恢复继承请用 `unset`，别用 `false`
- 改完组权限后，已经在线且带这个组的玩家通常立刻生效；但某些插件缓存了权限（如部分经济/商店插件），需要重新进服
- 多服环境不同步时，会出现「这个子服能用、那个子服不能用」，先 `/lp sync` 再排查
- `/lp editor` 的链接是一次性的、带过期时间，别外传（拿到链接就能改全服权限）
:::

## 相关插件

[PlaceholderAPI](/commands/config/placeholderapi.md)、[Vault](/commands/core/vault.md)、[TAB](/commands/chat/tab.md)
