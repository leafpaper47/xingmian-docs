---
title: Shopkeepers
createTime: 2026/10/24
---

# Shopkeepers

> 版本 `2.27.0` · 指令 1 条 · api-version `1.21.5` · 文件 `Shopkeepers-2.27.0.jar`

Custom villager shopkeepers

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/shopkeeper help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/shopkeeper` | Base for all shopkeeper commands. | — |

## 详细用法

### /shopkeeper

- **说明**：Base for all shopkeeper commands.
- **用法**：`Unknown command! Try /&lt;command&gt; help`
- **别名**：`/shopkeepers`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `shopkeeper.*` | Access to everything | op |
| `shopkeeper.admin` | Create and modify admin shopkeepers | op |
| `shopkeeper.bypass` | Bypass player shop restrictions (access player shops of others) | op |
| `shopkeeper.citizen` | Create Citizens NPC shopkeepers | op |
| `shopkeeper.cleanup-citizen-shopkeepers` | Delete invalid Citizen shopkeepers via command | op |
| `shopkeeper.create` | Allows the creation of shopkeepers via command | op |
| `shopkeeper.debug` | Toggle debug mode and access debugging commands | op |
| `shopkeeper.delete-unspawnable-shopkeepers` | Delete unspawnable shopkeepers via command | op |
| `shopkeeper.edit-villagers` | Edit regular villagers | op |
| `shopkeeper.edit-wandering-traders` | Edit regular wandering traders | op |
| `shopkeeper.entity.*` | Create shopkeepers of any mob type | True |
| `shopkeeper.give` | Give shop creation items via command | op |
| `shopkeeper.givecurrency` | Give currency items via command | op |
| `shopkeeper.hanging-sign` | Create hanging sign shopkeepers | True |
| `shopkeeper.help` | Display the command help | True |
| `shopkeeper.hire` | Allows hiring of shopkeepers | True |
| `shopkeeper.history.admin` | View the trading history of others and admin shops | op |
| `shopkeeper.history.own` | View your own trading history | True |
| `shopkeeper.list.admin` | List the admin shops | op |
| `shopkeeper.list.others` | List the player shops of other players | op |
| `shopkeeper.list.own` | List your own player shops | True |
| `shopkeeper.maxshops.unlimited` | Allows the creation of an unlimited number of shops | op |
| `shopkeeper.notify.trades` | Allows turning trade notifications for you on or off by command | True |
| `shopkeeper.player` | Create any type of player shopkeeper | True |
| `shopkeeper.player.book` | Create books selling player shopkeepers | — |
| `shopkeeper.player.buy` | Create buying player shopkeepers | — |
| `shopkeeper.player.sell` | Create selling player shopkeepers | — |
| `shopkeeper.player.trade` | Create trading player shopkeepers | — |
| `shopkeeper.reload` | Reload the plugin | op |
| `shopkeeper.remote` | Remotely open shops via command | op |
| `shopkeeper.remote.otherplayers` | Remotely open shops for other players | op |
| `shopkeeper.remoteedit` | Remotely edit shops via command | op |
| `shopkeeper.remove-all.admin` | Remove all admin shops via command | op |
| `shopkeeper.remove-all.others` | Remove all the shops of another player via command | op |
| `shopkeeper.remove-all.own` | Remove all of your own shops via command | op |
| `shopkeeper.remove-all.player` | Remove the player shops of all players via command | op |
| `shopkeeper.remove.admin` | Remove admin shops via command | op |
| `shopkeeper.remove.others` | Remove the shops of other players via command | op |
| `shopkeeper.remove.own` | Remove your own shops via command | op |
| `shopkeeper.setcurrency` | Set the currency items via command | op |
| `shopkeeper.setforhire` | Set a shopkeeper to be for hire | op |
| `shopkeeper.settradedcommand` | Set the traded command for the held item | op |
| `shopkeeper.settradeperm` | Set the trade permissions for admin shops | op |
| `shopkeeper.sign` | Create sign shopkeepers | True |
| `shopkeeper.snapshot` | Access shopkeeper snapshot commands | op |
| `shopkeeper.teleport` | Teleport to shopkeepers via command | op |
| `shopkeeper.teleport.others` | Teleport other players to shopkeepers | op |
| `shopkeeper.trade` | Allows trading with shopkeepers | True |
| `shopkeeper.trade-notifications.admin` | Receive trade notifications for admin shops | — |
| `shopkeeper.trade-notifications.player` | Receive trade notifications for player shops | — |
| `shopkeeper.transfer` | Transfer ownership of player shops | op |
| `shopkeeper.updateitems` | Update third-party items | op |
