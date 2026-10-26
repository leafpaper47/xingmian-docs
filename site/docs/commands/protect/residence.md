---
title: Residence
createTime: 2026/10/24
---

# 领地 · Residence

> 分类 🔒 领地与保护 · 版本 `6.0.2.4` · 指令 5 条 · api-version `1.13`

::: tip 方块领地保护与经济租赁一体化管理
Residence 是主流的立方体领地方块保护插件，玩家用木锄选区后即可创建住宅，支持子区域、标志位、成员权限、传送点、租赁与市场交易。管理员通过 resadmin 命令行直接干预他人领地，通过 resreload 与 resload 重载配置和数据。住宅内的建造、容器、传送、PVP 等行为由 flags 精细控制，是服务器防破坏体系的核心。
:::

## 什么时候会用到它

- 玩家用 /res select 与 /res create 圈地建房并保护方块与容器
- 按区域设置 PVP、怪物生成、飞行、容器访问等 flags 权限
- 给其他玩家分配住宅成员权限或划分子区域分工
- 管理员排查破坏事件、转移住宅所有权、清理违规住宅
- 出租或出售住宅，做服务器经济系统的房产交易
- 设置住宅传送点与指南针导航，方便玩家回家

## 上手流程

1. 玩家手持木锄或执行 /res select 分别左键、右键点选领地两个对角点
2. 执行 /res create 住宅名 付费创建住宅，再用 /res area add 划分子区域或 /res set 调整标志位
3. 用 /res pset 住宅名 玩家名 权限 true 与 /res padd、/res pdel 增删住宅成员
4. 玩家用 /res tp 住宅名 回家，管理员用 /resadmin 检查、改名或接管问题领地
5. 改动配置文件后先 /resload 只重载数据，需要整体生效时再 /resreload

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/rc` | 住宅聊天频道开关、离开、前缀颜色设置与踢人 | `/rc ｜ /rc to ｜ /rc l ｜ /rc setprefix 前缀 ｜ /rc setc…` | — |
| `/res` | 玩家侧住宅主命令，全部领地操作的入口 | `/res 子指令 参数` | — |
| `/resadmin` | 管理员侧住宅管理命令，可操作任意玩家领地 | `/resadmin 子指令 参数` | — |
| `/resload` | 只重新加载住宅数据文件，不重启插件 | `/resload` | — |
| `/resreload` | 整体重载插件配置与语言文件 | `/resreload` | — |

## 指令详解

### `/rc` — 住宅聊天频道开关、离开、前缀颜色设置与踢人

- **语法**：`/rc ｜ /rc to ｜ /rc l ｜ /rc setprefix 前缀 ｜ /rc setcolor 颜色 ｜ /rc kick 玩家名`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `to` | 可选 | 切换进入或退出当前住宅聊天频道 |
| `l` | 可选 | 离开当前住宅聊天频道 |
| `setprefix` | 可选 | 设置自己在住宅聊天中显示的前缀，需 residence.chatprefix 权限 |
| `setcolor` | 可选 | 设置自己的住宅聊天文字颜色，需 residence.chatcolor 权限 |
| `kick` | 可选 | 把指定玩家踢出当前住宅聊天频道，仅频道管理者或管理员可用 |


- **示例**：

```
/rc to
/rc setprefix 星冕
/rc setcolor red
/rc kick Steve
```

- **备注**：只有站在某个住宅范围内才处于该住宅频道，跨领地后频道会随住宅切换，不要把它当全服频道使用。

### `/res` — 玩家侧住宅主命令，全部领地操作的入口

- **语法**：`/res 子指令 参数`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子指令` | 必填 | select、create、remove、area、subzone、expand、set、pset、tp 等 |
| `住宅名` | 可选 | 目标住宅名称，省略时默认为脚下所在住宅 |


- **示例**：

```
/res ?
/res select
/res create home
/res info
/res tp home
```

- **备注**：不写子指令或写 ? 会打印自己的可用子指令列表，权限不足的条目不会显示。

### `/resadmin` — 管理员侧住宅管理命令，可操作任意玩家领地

- **语法**：`/resadmin 子指令 参数`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子指令` | 必填 | 与 /res 同名的子指令集合，此外还有 setowner、removeall、removeworld、server 等管理指令 |
| `住宅名` | 可选 | 目标住宅全名，涉及他人领地时不可省略 |


- **示例**：

```
/resadmin ?
/resadmin info home
/resadmin setowner home Steve
/resadmin removeall Steve
```

- **备注**：需要 residence.admin 权限；对他人领地执行 setowner、remove、rename 等操作会留下管理记录，建议操作前先 /resadmin info 确认目标。

### `/resload` — 只重新加载住宅数据文件，不重启插件

- **语法**：`/resload`

- **示例**：

```
/resload
```

- **备注**：用于手工修正 save 文件后让内存数据重新对齐，需要 residence.topadmin 权限；不读取 config.yml 的改动。

### `/resreload` — 整体重载插件配置与语言文件

- **语法**：`/resreload`

- **示例**：

```
/resreload
```

- **备注**：改动 config.yml 后使用，需要 residence.topadmin 权限；重载期间短暂卡顿属正常，别在高峰时段频繁执行。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `select` | 进入选区模式，左键、右键各点一个对角方块 | `/res select` |
| `create` | 按已选区域创建住宅，可带价格扣费 | `/res create home` |
| `auto` | 以当前权限允许的最大尺寸自动圈地建宅 | `/res auto home 20` |
| `remove` | 删除自己的住宅，需二次确认 | `/res remove home` |
| `confirm` | 确认上一步的高危操作，如删除、买地 | `/res confirm` |
| `area add` | 在住宅内新增一个矩形子区域 | `/res area add home shop` |
| `area remove` | 删除指定子区域 | `/res area remove home shop` |
| `subzone` | 创建独立计费的子领地，有自己的所有者 | `/res subzone home sub1` |
| `expand` | 向视线方向扩展住宅边界，按方块计费 | `/res expand home 10` |
| `contract` | 向内收缩住宅边界 | `/res contract home 5` |
| `set` | 设置住宅标志位，如 pvp、build、use、move | `/res set home pvp false` |
| `gset` | 设置全局默认标志位，对全部住宅生效 | `/res gset pvp false` |
| `lset` | 设置租赁类标志位，控制租金与租期行为 | `/res lset home rentable true` |
| `pset` | 设置某个玩家或权限组在住宅内的单项权限 | `/res pset home Steve build true` |
| `padd` | 把玩家加为住宅成员，给一组默认权限 | `/res padd home Steve` |
| `pdel` | 移除住宅成员及其全部权限 | `/res pdel home Steve` |
| `flags` | 查看当前住宅全部标志位状态 | `/res flags home` |
| `info` | 查看住宅所有者、尺寸、标志位与成员 | `/res info home` |
| `list` | 列出自己拥有的住宅 | `/res list` |
| `listall` | 列出自己可见的全部住宅，含他人领地 | `/res listall` |
| `lists` | 列出住宅及其子区域的层级结构 | `/res lists home` |
| `current` | 查看当前所在住宅与子区域 | `/res current` |
| `tp` | 传送到指定住宅，或住宅的某个子区域坐标 | `/res tp home` |
| `tpset` | 把当前站位设为住宅的传送点 | `/res tpset home` |
| `tpconfirm` | 确认有价格或跨世界的传送请求 | `/res tpconfirm` |
| `kick` | 把玩家从自己的住宅中强制移出 | `/res kick home Steve` |
| `rename` | 重命名自己的住宅 | `/res rename home base` |
| `setmain` | 把某个子区域设为主区域，主区域不可删除 | `/res setmain home shop` |
| `limits` | 查看自己的住宅数量与尺寸上限 | `/res limits` |
| `market` | 把住宅挂到市场出租或出售 | `/res market home 5000` |
| `lease` | 查看或管理自己租下的住宅 | `/res lease` |
| `gui` | 用图形界面管理当前住宅的标志位与成员 | `/res gui home` |
| `tool` | 获取选区工具，默认是木锄 | `/res tool` |
| `rt` | 随机传送到一处可公开访问的住宅 | `/res rt` |
| `unstuck` | 卡在领地边界或方块里时脱困 | `/res unstuck` |
| `bank` | 查看住宅银行余额与收支 | `/res bank home` |
| `version` | 查看插件版本 | `/res version` |
| `setowner` | 管理员把住宅所有权转给其他玩家 | `/resadmin setowner home Steve` |
| `removeall` | 管理员删除某个玩家的全部住宅 | `/resadmin removeall Steve` |
| `clearflags` | 管理员清空指定住宅的全部标志位 | `/resadmin clearflags home` |
| `setdefaultflags` | 把全局默认标志位写回指定住宅 | `/resadmin setdefaultflags home` |

## 注意事项

::: warning
- resremove 与 removeall 不可撤销，执行前先用 /resadmin info 或 /res listall 核对住宅名与所有者
- resreload 会重载全部配置，手工改过的 save 文件若格式有误会丢数据，改前先备份 plugins/Residence
- 子区域与主住宅的标志位存在继承关系，只改主区域往往不生效，要按子区域逐层确认
- 与 WorldGuard 等其它区域插件同区域叠加时权限判定容易冲突，排查保护失效时先确认哪一层拒绝
- resadmin 的越权操作默认受 residence.admin 等权限控制，给管理组授权时按最小原则只放必要节点
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `residence.admin` | 允许您访问/resadmin | op |
| `residence.admin.move` | 允许覆盖移动标志 | op |
| `residence.admin.tp` | 允许覆盖tp标志 | op |
| `residence.bypass.command` | 在驻留中绕过命令标志 | op |
| `residence.bypass.nofly` | 在住宅内绕过禁飞旗 | op |
| `residence.chatcolor` | 允许更改住宅聊天颜色 | True |
| `residence.chatkick` | 允许将玩家从住宅聊天中踢出 | True |
| `residence.chatprefix` | 允许更改住宅聊天前缀 | op |
| `residence.command.area` | 允许访问特定命令 | True |
| `residence.command.auto` | 允许创建最大住宅 | True |
| `residence.command.bank` | 允许访问特定命令 | True |
| `residence.command.check` | 允许访问特定命令 | True |
| `residence.command.clearflags` | 允许访问特定命令 | op |
| `residence.command.command` | 允许访问特定命令 | True |
| `residence.command.compass` | 允许访问特定命令 | True |
| `residence.command.confirm` | 允许访问特定命令 | True |
| `residence.command.contract` | 允许访问特定命令 | True |
| `residence.command.create` | 允许访问特定命令 | True |
| `residence.command.current` | 允许访问特定命令 | True |
| `residence.command.expand` | 允许访问特定命令 | True |
| `residence.command.flags` | 允许访问特定命令 | True |
| `residence.command.give` | 允许访问特定命令 | True |
| `residence.command.gset` | 允许访问特定命令 | True |
| `residence.command.gui` | 允许访问特定命令 | True |
| `residence.command.info` | 允许访问特定命令 | True |
| `residence.command.kick` | 允许访问特定命令 | True |
| `residence.command.lease` | 允许访问特定命令 | True |
| `residence.command.limits` | 允许访问特定命令 | True |
| `residence.command.list` | 允许访问特定命令 | True |
| `residence.command.list.others` | 允许访问特定命令 | True |
| `residence.command.listall` | 允许访问特定命令 | True |
| `residence.command.listallhidden` | 允许访问特定命令 | op |
| `residence.command.listhidden` | 允许访问特定命令 | op |
| `residence.command.lists` | 允许访问特定命令 | True |
| `residence.command.lset` | 允许访问特定命令 | True |
| `residence.command.market` | 允许访问特定命令 | True |
| `residence.command.material` | 允许访问特定命令 | True |
| `residence.command.message` | 允许访问特定命令 | True |
| `residence.command.message.enter` | 允许访问特定命令 | True |
| `residence.command.message.enter.remove` | 允许访问特定命令 | True |
| `residence.command.message.leave` | 允许访问特定命令 | True |
| `residence.command.message.leave.remove` | 允许访问特定命令 | True |
| `residence.command.mirror` | 允许访问特定命令 | True |
| `residence.command.padd` | 允许访问特定命令 | True |
| `residence.command.pdel` | 允许访问特定命令 | True |
| `residence.command.pset` | 允许访问特定命令 | True |
| `residence.command.rc` | 允许访问特定命令 | True |
| `residence.command.reload` | 允许访问特定命令 | op |
| `residence.command.remove` | 允许访问特定命令 | True |
| `residence.command.removeall` | 允许访问特定命令 | op |
| `residence.command.removeworld` | 允许访问特定命令 | op |
| `residence.command.rename` | 允许访问特定命令 | True |
| `residence.command.renamearea` | 允许访问特定命令 | True |
| `residence.command.resadmin` | 允许访问特定命令 | op |
| `residence.command.resbank` | 允许访问特定命令 | True |
| `residence.command.reset` | 允许访问特定命令 | True |
| `residence.command.rt` | 允许访问特定命令 | True |
| `residence.command.select` | 允许访问特定命令 | True |
| `residence.command.server` | 允许访问特定命令 | op |
| `residence.command.set` | 允许访问特定命令 | True |
| `residence.command.setdefaultflags` | 允许访问特定命令 | True |
| `residence.command.setmain` | 允许访问特定命令 | True |
| `residence.command.setowner` | 允许访问特定命令 | op |
| `residence.command.shop` | 允许访问特定命令 | True |
| `residence.command.show` | 允许访问特定命令 | True |
| `residence.command.siege` | 允许访问特定命令 | True |
| `residence.command.signconvert` | 允许访问特定命令 | op |
| `residence.command.signupdate` | 允许访问特定命令 | op |
| `residence.command.sublist` | 允许访问特定命令 | True |
| `residence.command.subzone` | 允许访问特定命令 | True |
| `residence.command.tool` | 允许访问特定命令 | True |
| `residence.command.tp` | 允许访问特定命令 | True |
| `residence.command.tpconfirm` | 允许访问特定命令 | True |
| `residence.command.tpset` | 允许访问特定命令 | True |
| `residence.command.unstuck` | 允许访问特定命令 | True |
| `residence.command.version` | 允许访问特定命令 | True |
| `residence.compass` | 允许设置指向驻留的指南针指针 | True |
| `residence.contract` | 允许您签约居住 | True |
| `residence.contract.subzone` | 允许您签约住宅子区 | True |
| `residence.create` | 允许您创建住宅 | True |
| `residence.create.subzone` | 允许您创建住宅子区域 | True |
| `residence.delete` | 允许您删除住宅 | True |
| `residence.delete.subzone` | 允许您删除住宅子区域 | True |
| `residence.expand` | 允许您扩展住所 | True |
| `residence.expand.subzone` | 允许您扩展住宅子区域 | True |
| `residence.newguyresidence` | 允许在胸部位置自动创建居所 | True |
| `residence.randomtp` | 允许使用/res rt命令 | True |
| `residence.rename` | 允许您重命名住宅 | True |
| `residence.resize` | 允许您调整区域的大小 | True |
| `residence.select` | 允许您选择一个区域来建造住宅 | True |
| `residence.select.auto.others` | 允许为其他玩家打开自动选择 | op |
| `residence.topadmin` | 允许您访问/resreload和/resload命令 | op |
| `residence.versioncheck` | 连接后通知新版本 | op |

## 相关插件

WorldGuard、[LuckPerms](/commands/core/luckperms.md)、[Vault](/commands/core/vault.md)、[PlaceholderAPI](/commands/config/placeholderapi.md)
