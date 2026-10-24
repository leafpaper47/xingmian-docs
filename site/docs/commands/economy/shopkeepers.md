---
title: Shopkeepers
createTime: 2026/10/24
---

# Shopkeepers

> 版本 `2.27.0` · 指令 1 条 · api-version `1.21.5` · 文件 `Shopkeepers-2.27.0.jar`

定制村民店主

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/shopkeeper help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/shopkeeper` | 所有店主命令的基础。 | — |

## 详细用法

### /shopkeeper

- **说明**：所有店主命令的基础。
- **用法**：`Unknown command! Try /&lt;command&gt; help`
- **别名**：`/shopkeepers`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `shopkeeper.*` | 无障碍通道 | op |
| `shopkeeper.admin` | 创建和修改管理员店主 | op |
| `shopkeeper.bypass` | 绕过玩家商店限制（进入其他玩家的商店） | op |
| `shopkeeper.citizen` | 创建公民NPC店主 | op |
| `shopkeeper.cleanup-citizen-shopkeepers` | 通过命令删除无效的公民店主 | op |
| `shopkeeper.create` | 允许通过命令创建店主 | op |
| `shopkeeper.debug` | 切换调试模式并访问调试命令 | op |
| `shopkeeper.delete-unspawnable-shopkeepers` | 通过命令删除不可生成的店主 | op |
| `shopkeeper.edit-villagers` | 编辑常规村民 | op |
| `shopkeeper.edit-wandering-traders` | 编辑经常流浪的商人 | op |
| `shopkeeper.entity.*` | 创建任何类型的店主 | True |
| `shopkeeper.give` | 通过命令给商店创建道具 | op |
| `shopkeeper.givecurrency` | 通过命令提供货币道具 | op |
| `shopkeeper.hanging-sign` | 创建吊牌店主 | True |
| `shopkeeper.help` | 显示命令帮助 | True |
| `shopkeeper.hire` | 允许雇佣店主 | True |
| `shopkeeper.history.admin` | 查看他人和管理员商店的交易历史记录 | op |
| `shopkeeper.history.own` | 查看您自己的交易历史记录 | True |
| `shopkeeper.list.admin` | 列出管理员商店 | op |
| `shopkeeper.list.others` | 列出其他玩家的玩家商店 | op |
| `shopkeeper.list.own` | 列出您自己的玩家商店 | True |
| `shopkeeper.maxshops.unlimited` | 允许创建无限数量的商店 | op |
| `shopkeeper.notify.trades` | 允许通过命令为您打开或关闭交易通知 | True |
| `shopkeeper.player` | 创建任何类型的玩家店主 | True |
| `shopkeeper.player.book` | 创建出售玩家店主的书籍 | — |
| `shopkeeper.player.buy` | 创建购买玩家店主 | — |
| `shopkeeper.player.sell` | 创建销售玩家店主 | — |
| `shopkeeper.player.trade` | 创建交易玩家店主 | — |
| `shopkeeper.reload` | 重新加载插件 | op |
| `shopkeeper.remote` | 通过命令远程打开商店 | op |
| `shopkeeper.remote.otherplayers` | 为其他玩家远程开放商店 | op |
| `shopkeeper.remoteedit` | 通过命令远程编辑商店 | op |
| `shopkeeper.remove-all.admin` | 通过命令删除所有管理员商店 | op |
| `shopkeeper.remove-all.others` | 通过命令移除其他玩家的所有商店 | op |
| `shopkeeper.remove-all.own` | 通过命令移除您自己的所有商店 | op |
| `shopkeeper.remove-all.player` | 通过命令移除所有玩家的商店 | op |
| `shopkeeper.remove.admin` | 通过命令删除管理员商店 | op |
| `shopkeeper.remove.others` | 通过命令移除其他玩家的商店 | op |
| `shopkeeper.remove.own` | 通过命令移除您自己的商店 | op |
| `shopkeeper.setcurrency` | 通过命令设置货币项目 | op |
| `shopkeeper.setforhire` | 将店主设置为出租 | op |
| `shopkeeper.settradedcommand` | 为持有的道具设置交易命令 | op |
| `shopkeeper.settradeperm` | 设置管理员商店的交易权限 | op |
| `shopkeeper.sign` | 创建标志店主 | True |
| `shopkeeper.snapshot` | 访问店主快照命令 | op |
| `shopkeeper.teleport` | 通过命令传送给店主 | op |
| `shopkeeper.teleport.others` | 将其他玩家传送给店主 | op |
| `shopkeeper.trade` | 允许与店主交易 | True |
| `shopkeeper.trade-notifications.admin` | 接收管理员商店的交易通知 | — |
| `shopkeeper.trade-notifications.player` | 接收玩家商店的交易通知 | — |
| `shopkeeper.transfer` | 转让玩家商店的所有权 | op |
| `shopkeeper.updateitems` | 更新第三方餐点 | op |
