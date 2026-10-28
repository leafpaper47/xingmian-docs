---
title: CoreProtect
createTime: 2026/10/24
---

# 方块日志 · CoreProtect

> 分类 📊 记录与性能 · 版本 `24.2-dev` · 指令 17 条 · api-version `1.16`

::: tip 方块日志与回滚
把每次放方块、拆方块、开箱子、杀怪、聊天都记进数据库。事后能查「这块石头谁挖的、这个箱子谁开的」，也能把某段时间某个区域的改动整体回滚或恢复。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 看这个箱子谁动过 | /co i | 开检查器后右键箱子看交互记录，左键方块看放置记录 |
| 查某玩家最近干了啥 | /co l u:Steve t:1h r:10 | 只查询不改动，先用它把范围试准 |
| 回滚破坏 | /co rb u:Steve t:1h r:10 | 参数和上一条 lookup 保持一致，才回滚该回滚的 |
| 回滚搞错了撤销 | /co undo | 只撤销自己上一次 rb/rs，做别的操作后就失效 |
| 清旧日志 | /co purge t:30d | 删 30 天前的数据，删完找不回来 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/co` | 日志系统总入口，所有子指令都从这里进 | `/co <子指令> [参数]` | `coreprotect.co` |
| `/co inspect` | 开关检查器模式，点方块/箱子看它的改动记录 | `/co i` | `coreprotect.inspect` |
| `/co lookup` | 按条件列出记录，不改动世界 | `/co l [u:玩家] [t:时间] [r:半径] [a:动作] [p:页码] [w:世界]` | `coreprotect.lookup` |
| `/co rollback` | 把符合条件的历史改动静默撤销 | `/co rb [u:玩家] [t:时间] [r:半径] [a:动作]` | `coreprotect.rollback` |
| `/co restore` | 把被回滚掉的改动重新做回去 | `/co rs [u:玩家] [t:时间] [r:半径] [a:动作]` | `coreprotect.restore` |
| `/co undo` | 撤销自己上一次 rollback 或 restore | `/co undo` | `coreprotect.rollback` |
| `/co near` | 列出你附近最近的方块改动 | `/co near` | `coreprotect.lookup.near` |
| `/co teleport` | 传送到某条查询结果所在的坐标 | `/co tp <结果编号>` | `coreprotect.teleport` |
| `/co purge` | 清理超过指定时间的日志数据 | `/co purge t:<时间>` | `coreprotect.purge` |
| `/co status` | 查看日志库状态：记录数、体积、运行信息 | `/co status` | `coreprotect.status` |
| `/co reload` | 重载 config.yml | `/co reload` | `coreprotect.reload` |
| `/co help` | 打印子指令与参数的完整清单 | `/co help [页码]` | — |
| `/co cancel` | 取消回滚预览 | `/co cancel` | `coreprotect.rollback` |
| `/co apply` | 确认执行回滚预览里的改动 | `/co apply` | `coreprotect.rollback` |
| `/co give` | 把查询到的物品直接发给玩家 | `/co give <玩家> <物品> [数量]` | `coreprotect.give` |
| `/co consumer` | 查看日志写入队列状态 | `/co consumer` | `coreprotect.consumer` |
| `/co version` | 显示 CoreProtect 版本 | `/co version` | — |

## 指令详解

### `/co` — 日志系统总入口，所有子指令都从这里进

- **语法**：`/co <子指令> [参数]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子指令` | 必填 | i / l / rb / rs / undo / near / tp / purge / status / reload / help |


- **示例**：

```
/co help
/co l u:Steve t:1h
/co i
```

- **权限**：`coreprotect.co`
- **备注**：参数写成 键:值，可叠加、顺序不限；/co、/core、/coreprotect 三个写法等价

### `/co inspect` — 开关检查器模式，点方块/箱子看它的改动记录

- **语法**：`/co i`

- **示例**：

```
/co i
```

- **权限**：`coreprotect.inspect`
- **备注**：左键方块=放置记录，右键方块=破坏与容器交互；排查完记得再敲一次关掉

### `/co lookup` — 按条件列出记录，不改动世界

- **语法**：`/co l [u:玩家] [t:时间] [r:半径] [a:动作] [p:页码] [w:世界]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `u:玩家` | 可选 | u:Steve，可多个 |
| `t:时间` | 可选 | t:1h 一小时、t:2d 两天、t:30m |
| `r:半径` | 可选 | r:10 球形半径，r:#global 全服 |
| `a:动作` | 可选 | a:block、a:+block 放置、a:-block 破坏、a:container 容器 |


- **示例**：

```
/co l u:Steve t:1h r:10
/co l a:container t:2h
/co l u:Steve a:-block t:3d r:#global
```

- **权限**：`coreprotect.lookup`
- **备注**：结果分页，翻页用 p:2；查容器用 a:container，查被杀用 a:kill

### `/co rollback` — 把符合条件的历史改动静默撤销

- **语法**：`/co rb [u:玩家] [t:时间] [r:半径] [a:动作]`

- **示例**：

```
/co rb u:Steve t:1h r:10
/co rb t:30m r:#global
```

- **权限**：`coreprotect.rollback`
- **备注**：真的会改世界；先把同样的参数跑一遍 /co l 确认范围；大范围很吃性能，挑人少时段做

### `/co restore` — 把被回滚掉的改动重新做回去

- **语法**：`/co rs [u:玩家] [t:时间] [r:半径] [a:动作]`

- **示例**：

```
/co rs u:Steve t:1h r:10
```

- **权限**：`coreprotect.restore`
- **备注**：用来救回误回滚的玩家建筑，参数要和当初 rb 的一致

### `/co undo` — 撤销自己上一次 rollback 或 restore

- **语法**：`/co undo`

- **示例**：

```
/co undo
```

- **权限**：`coreprotect.rollback`
- **备注**：一次只退一步；又做了别的 rb/rs 或过太久就退不回去了

### `/co near` — 列出你附近最近的方块改动

- **语法**：`/co near`

- **示例**：

```
/co near
```

- **权限**：`coreprotect.lookup.near`
- **备注**：默认以你为中心小范围查，适合当场看破坏现场

### `/co teleport` — 传送到某条查询结果所在的坐标

- **语法**：`/co tp <结果编号>`

- **示例**：

```
/co tp 1
```

- **权限**：`coreprotect.teleport`
- **备注**：编号来自 /co l 结果列表里的序号，先 lookup 再 tp

### `/co purge` — 清理超过指定时间的日志数据

- **语法**：`/co purge t:<时间>`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `t:时间` | 必填 | 保留多久之内的数据，如 t:30d |


- **示例**：

```
/co purge t:30d
```

- **权限**：`coreprotect.purge`
- **备注**：数据库会瞬间瘦身但数据不可恢复；执行期间别关服，删之前确认纠纷追溯期

### `/co status` — 查看日志库状态：记录数、体积、运行信息

- **语法**：`/co status`

- **示例**：

```
/co status
```

- **权限**：`coreprotect.status`
- **备注**：怀疑日志写不进去时先看这里

### `/co reload` — 重载 config.yml

- **语法**：`/co reload`

- **示例**：

```
/co reload
```

- **权限**：`coreprotect.reload`
- **备注**：改完要记录的方块/世界黑白名单必须重载才生效

### `/co help` — 打印子指令与参数的完整清单

- **语法**：`/co help [页码]`

- **示例**：

```
/co help
```

- **备注**：a: 动作的完整取值以这里为准

### `/co cancel` — 取消回滚预览

- **语法**：`/co cancel`

- **示例**：

```
/co cancel
```

- **权限**：`coreprotect.rollback`
- **备注**：只在回滚预览阶段有用；直接敲 rb 不预览的话用它无用

### `/co apply` — 确认执行回滚预览里的改动

- **语法**：`/co apply`

- **示例**：

```
/co apply
```

- **权限**：`coreprotect.rollback`
- **备注**：预览模式下不敲 apply 就不会真的改世界

### `/co give` — 把查询到的物品直接发给玩家

- **语法**：`/co give <玩家> <物品> [数量]`

- **示例**：

```
/co give Steve diamond 8
```

- **权限**：`coreprotect.give`
- **备注**：默认权限关闭（default=false），要单独给 coreprotect.give；补发被偷物品用

### `/co consumer` — 查看日志写入队列状态

- **语法**：`/co consumer`

- **示例**：

```
/co consumer
```

- **权限**：`coreprotect.consumer`
- **备注**：队列堆积严重说明数据库写不动了，先看 /co status

### `/co version` — 显示 CoreProtect 版本

- **语法**：`/co version`

- **示例**：

```
/co version
```


## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/co l a:container` | 只查箱子/熔炉这类容器的存取记录 | `/co l a:container t:6h r:5` |
| `/co l a:-block` | 只查「拆方块」 | `/co l a:-block u:Steve t:1d` |
| `/co l a:+block` | 只查「放方块」 | `/co l a:+block t:1d r:20` |
| `/co l u:Steve a:kill` | 查击杀记录 | `/co l u:Steve a:kill t:1d` |
| `/co l a:chat` | 查聊天记录（需 coreprotect.lookup.chat） | `/co l a:chat t:2h` |
| `/co l a:command` | 查玩家执行过的指令（需 coreprotect.lookup.command） | `/co l a:command u:Steve t:1d` |
| `/co l a:session` | 查登录登出会话（需 coreprotect.lookup.session） | `/co l a:session u:Steve t:7d` |
| `/co l a:username` | 查改名记录（需 coreprotect.lookup.username） | `/co l a:username u:Steve` |
| `/co l a:sign` | 查告示牌文字变化 | `/co l a:sign t:1d r:10` |
| `/co l r:#global` | 把半径放开到全服，注意性能 | `/co l u:Steve t:1h r:#global` |
| `/co network-debug` | 网络接口调试，排查多服数据问题 | `/co network-debug` |

## 注意事项

::: warning
- rb / rs 真的改世界：先用同一套参数跑 /co l 看结果，再换成 rb；回滚完去现场转一圈，不对立刻 /co undo。
- 回滚只还原方块与容器内容，玩家背包里已拿走的东西、造成的伤害不会自动还原，被偷物品要另外补。
- r: 不填只处理你附近；r:#global 全服回滚很吃性能，挑在线人数少时做，别一边回滚一边让人建东西。
- purge 删掉的数据不可恢复，执行前确认服务器对纠纷追溯的要求，最好先备份数据库。
- a: 的完整动作列表以 /co help 为准，别凭记忆猜动作名，猜错会查不到记录还以为库里没数据。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `coreprotect.*` | 全部权限（默认仅 OP） | op |
| `coreprotect.co` | 访问 /co 主指令（默认所有人可用） | True |
| `coreprotect.consumer` | 拥有使用消费者命令的权限 | op |
| `coreprotect.core` | 拥有访问 CoreProtect /core 命令的权限 | — |
| `coreprotect.coreprotect` | 拥有访问 CoreProtect /coreprotect 命令的权限 | — |
| `coreprotect.give` | 使用 /co give 补发物品（默认关闭） | — |
| `coreprotect.help` | 拥有使用帮助命令的权限 | op |
| `coreprotect.inspect` | 使用检查器模式 /co i | op |
| `coreprotect.lookup` | 使用查询类子指令 | op |
| `coreprotect.lookup.block` | 拥有查询方块数据的权限 | op |
| `coreprotect.lookup.chat` | 拥有查询聊天消息的权限 | op |
| `coreprotect.lookup.click` | 拥有查询玩家交互的权限 | op |
| `coreprotect.lookup.command` | 拥有查询玩家命令的权限 | op |
| `coreprotect.lookup.container` | 拥有查询容器交易的权限 | op |
| `coreprotect.lookup.inventory` | 拥有查询背包交易的权限 | op |
| `coreprotect.lookup.item` | 拥有查询物品交易的权限 | op |
| `coreprotect.lookup.kill` | 拥有查询实体击杀的权限 | op |
| `coreprotect.lookup.near` | 使用 /co near | op |
| `coreprotect.lookup.session` | 拥有查询玩家会话的权限 | op |
| `coreprotect.lookup.sign` | 拥有查询告示牌消息的权限 | op |
| `coreprotect.lookup.spawn` | 拥有查询实体生成的权限 | op |
| `coreprotect.lookup.username` | 拥有查询玩家改名记录的权限 | op |
| `coreprotect.networking` | 拥有使用网络 API 的权限 | op |
| `coreprotect.purge` | 清理日志 /co purge | op |
| `coreprotect.reload` | 重载配置 /co reload | op |
| `coreprotect.restore` | 执行恢复 /co rs | op |
| `coreprotect.rollback` | 执行回滚 /co rb 与 /co undo | op |
| `coreprotect.status` | 查看状态 /co status | op |
| `coreprotect.teleport` | 传送到查询结果 /co tp | op |
