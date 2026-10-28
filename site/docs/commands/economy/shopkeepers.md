---
title: Shopkeepers
createTime: 2026/10/24
---

# 商店NPC · Shopkeepers

> 分类 🪙 经济与商店 · 版本 `2.27.0` · 指令 1 条 · api-version `1.21.5`

::: tip NPC 商店
用村民等实体当店主：玩家右键交易，管理员可创建/编辑/移动/删除店主，支持玩家商店与管理员商店两种模式。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 新建一个店主 | /shopkeeper create | 对着准星位置的实体创建，先看好类型 |
| 编辑店主商品 | /shopkeeper edit | 右键店主进入编辑界面加/改商品 |
| 把店主挪位置 | /shopkeeper move | 先左键选中店主再执行 |
| 改完配置生效 | /shopkeeper reload | 改 config 后必须重载 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/shopkeeper` | 店主管理主指令<br>别名 `/shopkeepers` | `/sk <help｜list｜reload｜create｜edit｜move｜delete｜tele…` | — |

## 指令详解

### `/shopkeeper` — 店主管理主指令

- **语法**：`/sk <help｜list｜reload｜create｜edit｜move｜delete｜teleport｜give｜confirm>`

- **示例**：

```
/sk help
```

- **别名**：`/shopkeepers`
- **备注**：命令名 shopkeeper，别名 /shopkeepers、/sk

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/sk help` | 打印可用子指令与用法 | `/sk help` |
| `/sk list` | 列出全部店主（可按玩家/管理员商店筛选） | `/sk list` |
| `/sk reload` | 重载配置与全部店主数据 | `/sk reload` |
| `/sk create` | 在准星目标位置创建店主（默认管理员商店） | `/sk create` |
| `/sk edit` | 编辑店主：商品、价格、名称、交易类型 | `/sk edit` |
| `/sk move` | 把选中店主移动到当前位置 | `/sk move` |
| `/sk teleport` | 传送到指定店主附近 | `/sk teleport` |
| `/sk delete` | 删除店主（需确认） | `/sk delete` |
| `/sk give <玩家>` | 把店主所有权转移给玩家 | `/sk give Steve` |
| `/sk confirm` | 确认上一个待确认的危险操作 | `/sk confirm` |

## 注意事项

::: warning
- create 用错模式会建成「玩家商店」，普通玩家能随意改商品价格，创建前先确认模式。
- delete 需要二次确认，误删店主商品配置不会自动备份，重要商店先 /sk list 记下名字。
- 店主实体被其他插件清掉（区块清理、实体清理类）后会变成隐形空店主，先 /sk list 核对再重建。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `shopkeeper.*` | 无障碍通道 | op |
| `shopkeeper.admin` | 创建/删除/移动任意店主 | op |
| `shopkeeper.bypass` | 绕过玩家商店限制（进入其他玩家的商店） | op |
| `shopkeeper.citizen` | 创建公民NPC店主 | op |
| `shopkeeper.cleanup-citizen-shopkeepers` | 通过命令删除无效的公民店主 | op |
| `shopkeeper.create` | 允许通过命令创建店主 | op |
| `shopkeeper.debug` | 切换调试模式并访问调试命令 | op |
| `shopkeeper.delete-unspawnable-shopkeepers` | 通过命令删除不可生成的店主 | op |
| `shopkeeper.edit` | 编辑店主内容 | — |
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
| `shopkeeper.player` | 创建自己的玩家商店 | True |
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
