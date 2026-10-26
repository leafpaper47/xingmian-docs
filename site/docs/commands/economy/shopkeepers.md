---
title: Shopkeepers
createTime: 2026/10/24
---

# 商店NPC · Shopkeepers

> 分类 🪙 经济与商店 · 版本 `2.27.0` · 指令 1 条 · api-version `1.21.5`

::: tip 用村民或实体当店主的玩家商店与系统商店系统
Shopkeepers 让你用村民、流浪商人、告示牌甚至 Citizens NPC 当店主，摆一个就能开一家店：玩家店主由玩家自己上架买卖，管理员店主可由你设定无限库存与交易权限。它把创建道具、编辑界面、交易历史、转让与出租都收在 /shopkeeper 一个命令树下。服的通货通常还是用物品（如金币物品、绿宝石），所以它常和 Citizens、PlaceholderAPI 一起装，用来管主城商业区。
:::

## 什么时候会用到它

- 在主城、出生点或玩家市场摆系统商店，让玩家直接右键买卖基础物资
- 给玩家开放摆摊权限，让他们自己开玩家店主卖装备、收材料
- 管理员清理、转让、查找玩家商店，处理占地或违规店铺
- 需要定时或按权限开放的商店（交易权限、可雇佣出租的店主）

## 上手流程

1. 装好插件先执行 /shopkeeper reload，确认加载成功且语言文件正常
2. 用 /shopkeeper give player 拿到玩家店主创建道具，右键地面放置店主
3. 右键店主、或 /shopkeeper edit 店主ID 进入编辑界面，设置交易物、价格与外观
4. 建系统商店则用 /shopkeeper give admin 拿管理员创建道具，编辑时可设无限库存与交易权限
5. 日常维护用 /shopkeeper list 查自家店铺、/shopkeeper history 看交易记录、/shopkeeper remove 删店

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/shopkeeper` | 店主系统总命令，所有创建、编辑、管理功能都在这里<br>别名 `/shopkeepers` | `/shopkeeper help` | — |

## 指令详解

### `/shopkeeper` — 店主系统总命令，所有创建、编辑、管理功能都在这里

- **语法**：`/shopkeeper help`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子命令` | 可选 | 如 help、reload、list、edit、give 等；不带参数执行会提示用法 |


- **示例**：

```
/shopkeeper help
/shopkeeper reload
/shopkeeper list
```

- **别名**：`/shopkeepers`
- **备注**：别名 /shopkeepers。大部分管理类子命令需要 shopkeeper.admin 或对应的 shopkeeper.xxx 权限；编辑店主时在编辑界面里用的是聊天栏输入的关键词，不是斜杠命令。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `help 页码` | 列出全部店主命令与用法，分页查看 | `/shopkeeper help` |
| `reload` | 重载配置文件与语言文案，已经摆好的店主保留 | `/shopkeeper reload` |
| `list 页码` | 列出自己名下的玩家店主及其编号 | `/shopkeeper list` |
| `list admin 页码` | 列出服务器管理员商店 | `/shopkeeper list admin` |
| `edit 店主ID` | 打开指定店主的编辑界面，改类型、交易、名称、外观 | `/shopkeeper edit 12` |
| `remove 店主ID` | 删除指定的店主 | `/shopkeeper remove 12` |
| `remove all` | 删除自己名下的全部店主 | `/shopkeeper remove all` |
| `removeall 玩家名` | 管理员批量删除某位玩家的所有店主 | `/shopkeeper removeall Steve` |
| `teleport 店主ID` | 传送自己到店主所在位置，方便现场处理 | `/shopkeeper teleport 12` |
| `transfer 店主ID 玩家名` | 把玩家店主的所有权转让给别人 | `/shopkeeper transfer 12 Steve` |
| `give player` | 给自己一个玩家店主创建道具，放置后生成店主 | `/shopkeeper give player` |
| `give admin` | 给自己一个管理员商店创建道具 | `/shopkeeper give admin` |
| `givecurrency` | 给自己一个货币道具，用于在编辑界面指定交易货币物品 | `/shopkeeper givecurrency` |
| `setcurrency` | 把手上拿的物品设为店主的交易货币 | `/shopkeeper setcurrency` |
| `notify on` | 打开自己店主的交易通知，off 为关闭 | `/shopkeeper notify on` |
| `history 页码` | 查看自己店主的交易历史记录 | `/shopkeeper history` |
| `remote 店主ID` | 不走到店门口，远程打开商店交易界面 | `/shopkeeper remote 12` |
| `remoteedit 店主ID` | 远程打开商店的编辑界面 | `/shopkeeper remoteedit 12` |
| `setforhire 价格` | 把店主设为可被玩家雇佣出租，执行前需处于该店主的编辑状态 | `/shopkeeper setforhire 500` |
| `settradeperm 权限节点` | 设置管理员商店交易所需的权限节点 | `/shopkeeper settradeperm shopkeeper.trade` |

## 注意事项

::: warning
- 店主是用创建道具放置出来的实体或方块，删掉店主一般不能原地复活，重建要重新配置交易，挪位置前先在测试服试一遍
- 玩家能开几家店受 maxshops 限制，只有 shopkeeper.maxshops.unlimited 才能不限数量，做活动送店铺要临时给权限
- 交易历史会按配置定期清理，查违规刷货币要趁早导出，删店后记录更不好追
- Citizens NPC 店主依赖 Citizens 插件，没装时相关类型不可用；改完语言文件用 /shopkeeper reload 而不是重启验证，具体子命令写法与参数以游戏内 /shopkeeper help 为准
:::

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

## 相关插件

Citizens、[PlaceholderAPI](/commands/config/placeholderapi.md)、[Vault](/commands/core/vault.md)
