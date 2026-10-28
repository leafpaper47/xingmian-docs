---
title: Residence
createTime: 2026/10/24
---

# 领地 · Residence

> 分类 🔒 领地与保护 · 版本 `6.0.2.4` · 指令 35 条 · api-version `1.13`

::: tip 领地保护
用选区工具圈地创建受保护住宅，配子区域、权限标志、成员管理与出租出售；管理员用 /resadmin 直接干预他人领地。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 圈一块地 | /res select 10 | 进入选区模式后点两个对角方块，再 /res create 名字 |
| 给访客开权限 | /res pset home use true | 常用标志 build/use/container/pvp/move/tp |
| 加同住玩家 | /res set home Trusted Steve | 等级 Order&lt;Member&lt;Trusted |
| 查看自己有哪些地 | /res list | 加玩家名查他人；/res listall 需管理权限 |
| 管理员清违规领地 | /resadmin removeall Steve | 删该玩家全部住宅，先留证据 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/rc` | 领地频道聊天（只在当前领地内可见） | `/rc [消息] · /rc setprefix <前缀> · /rc setcolor <颜色> …` | — |
| `/res` | 领地主指令：创建/管理领地、设置权限、查看列表 | `/res <子指令> [参数...]` | — |
| `/res select` | 进入/退出选区模式（也可直接用选区工具点方块） | `/res select <半径>` | — |
| `/res create` | 把当前选区建成住宅 | `/res create <住宅名>` | `residence.create` |
| `/res remove` | 删除自己的住宅 | `/res remove <住宅名>` | `residence.delete` |
| `/res area` | 在住宅内划子区域（房间、农场分区） | `/res area <add｜remove｜replace> <子区域名> [父住宅]` | — |
| `/res subzone` | 把子区域升级成可单独授权/出租的小领地 | `/res subzone <子区域名> [父住宅]` | — |
| `/res pset` | 给某个玩家或子区域单独设权限标志 | `/res pset <住宅> <玩家｜子区域> <标志> <true｜false｜remove>` | — |
| `/res gset` | 设置整块住宅的全局标志 | `/res gset <住宅> <标志> <值>` | — |
| `/res set` | 添加或移除住宅成员 | `/res set <住宅> <Order｜Member｜Trusted｜None> <玩家>` | — |
| `/res lset` | 按玩家等级批量改标志 | `/res lset <住宅> <等级> <标志> <值>` | — |
| `/res flags` | 列出某住宅全部标志的当前状态 | `/res flags <住宅> [页码]` | — |
| `/res info` | 看住宅详情：所有者、大小、成员、租金 | `/res info <住宅>` | — |
| `/res list` | 列出某玩家名下的住宅 | `/res list [玩家] [页码]` | — |
| `/res listall` | 列出全服所有住宅 | `/res listall [页码]` | `residence.command.listall` |
| `/res tp` | 传送到住宅 | `/res tp <住宅>` | — |
| `/res tpset` | 把你当前位置设为住宅传送点 | `/res tpset [住宅]` | — |
| `/res kick` | 把某玩家踢出住宅 | `/res kick <住宅> <玩家>` | — |
| `/res limits` | 查看自己还能建多少块、多大面积 | `/res limits [玩家]` | — |
| `/res bank` | 住宅租金账户的查询/存入/取出 | `/res bank <deposit｜withdraw｜balance> [金额] [住宅]` | — |
| `/res market` | 挂市场出售/出租住宅，或撤回/成交查询 | `/res market <sell｜rent｜unsell｜unrent｜buy｜info> [价格…` | — |
| `/res lease` | 续租或放弃租约 | `/res lease <renew｜release> <住宅>` | — |
| `/res contract` | 给住宅写出租/出售合同 | `/res contract <住宅> [天数] [价格]` | `residence.command.contract` |
| `/res message` | 设置进出领地时的提示语 | `/res message <住宅> <enter｜leave｜remove> <文本>` | — |
| `/res rename` | 重命名住宅 | `/res rename <旧名> <新名>` | — |
| `/res tool` | 更换选区工具物品 | `/res tool [物品]` | — |
| `/res unstuck` | 卡在领地边界时把自己弹出去 | `/res unstuck` | — |
| `/res version` | 查看版本与更新提示 | `/res version` | — |
| `/resadmin` | 管理员指令：绕过领地限制、改他人领地、强制删除 | `/resadmin <子指令> [参数...]` | — |
| `/resadmin setowner` | 把住宅所有权转给其他玩家 | `/resadmin setowner <住宅> <玩家>` | `residence.admin` |
| `/resadmin removeall` | 删除某玩家名下全部住宅 | `/resadmin removeall <玩家>` | `residence.admin` |
| `/resadmin give` | 把住宅转给指定玩家 | `/resadmin give <住宅> <玩家>` | `residence.admin` |
| `/resadmin server` | 把住宅设为服务器所有（不绑定玩家） | `/resadmin server <住宅>` | `residence.admin` |
| `/resload` | 重新读取住宅存档文件 | `/resload` | — |
| `/resreload` | 重载配置与语言文件 | `/resreload` | — |

## 指令详解

### `/rc` — 领地频道聊天（只在当前领地内可见）

- **语法**：`/rc [消息] · /rc setprefix <前缀> · /rc setcolor <颜色> · /rc kick <玩家>`

- **示例**：

```
/rc 有人吗
/rc setprefix 家园
```

- **备注**：不进领地或不在领地频道里发消息时是普通聊天。

### `/res` — 领地主指令：创建/管理领地、设置权限、查看列表

- **语法**：`/res <子指令> [参数...]`

- **示例**：

```
/res create home
/res list
/res pset home build true
```

- **备注**：输入 `/res` 会显示全部子指令；`/res ?` 打印帮助。

### `/res select` — 进入/退出选区模式（也可直接用选区工具点方块）

- **语法**：`/res select <半径>`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `半径` | 必填 | 以你为中心的水平半径，10 即 20×20 |


- **示例**：

```
/res select 10
```

- **备注**：选区过大超出区块上限会失败

### `/res create` — 把当前选区建成住宅

- **语法**：`/res create <住宅名>`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `住宅名` | 必填 | 自己名下唯一，不能含空格 |


- **示例**：

```
/res create home
```

- **权限**：`residence.create`
- **备注**：按区块数量扣钱；与他人领地重叠直接拒绝

### `/res remove` — 删除自己的住宅

- **语法**：`/res remove <住宅名>`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `住宅名` | 必填 | 可用 /res list 查 |


- **示例**：

```
/res remove home
```

- **权限**：`residence.delete`
- **备注**：不可撤销，需 /res confirm 二次确认

### `/res area` — 在住宅内划子区域（房间、农场分区）

- **语法**：`/res area <add｜remove｜replace> <子区域名> [父住宅]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `add` | 必填 | add 新建、remove 删除、replace 重定义范围 |


- **示例**：

```
/res area add farm home
```

- **备注**：子区域继承父住宅标志，可单独 pset 覆盖

### `/res subzone` — 把子区域升级成可单独授权/出租的小领地

- **语法**：`/res subzone <子区域名> [父住宅]`

- **示例**：

```
/res subzone room1 home
```

- **备注**：升级后能加成员、能挂市场出售

### `/res pset` — 给某个玩家或子区域单独设权限标志

- **语法**：`/res pset <住宅> <玩家｜子区域> <标志> <true｜false｜remove>`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `标志` | 必填 | build/use/container/pvp/move/tp/damage/animals 等 |


- **示例**：

```
/res pset home Steve build true
/res pset home container false
```

- **备注**：remove 表示删掉这条覆盖设置；分组标志（redstone 等）一次设一组

### `/res gset` — 设置整块住宅的全局标志

- **语法**：`/res gset <住宅> <标志> <值>`

- **示例**：

```
/res gset home pvp false
```

- **备注**：影响所有非成员；单人/子区域的 pset 优先级更高

### `/res set` — 添加或移除住宅成员

- **语法**：`/res set <住宅> <Order｜Member｜Trusted｜None> <玩家>`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `等级` | 必填 | Member 能用容器，Trusted 能建造并授权，None 移除 |


- **示例**：

```
/res set home Member Steve
/res set home None Steve
```


### `/res lset` — 按玩家等级批量改标志

- **语法**：`/res lset <住宅> <等级> <标志> <值>`

- **示例**：

```
/res lset home Member use true
```


### `/res flags` — 列出某住宅全部标志的当前状态

- **语法**：`/res flags <住宅> [页码]`

- **示例**：

```
/res flags home
```

- **备注**：排查「为什么他能开箱」先跑这个

### `/res info` — 看住宅详情：所有者、大小、成员、租金

- **语法**：`/res info <住宅>`

- **示例**：

```
/res info home
```

- **备注**：不带参数看自己脚下的领地

### `/res list` — 列出某玩家名下的住宅

- **语法**：`/res list [玩家] [页码]`

- **示例**：

```
/res list
/res list Steve
```


### `/res listall` — 列出全服所有住宅

- **语法**：`/res listall [页码]`

- **示例**：

```
/res listall 1
```

- **权限**：`residence.command.listall`

### `/res tp` — 传送到住宅

- **语法**：`/res tp <住宅>`

- **示例**：

```
/res tp home
```

- **备注**：需要该住宅 tp 标志为 true 或是成员

### `/res tpset` — 把你当前位置设为住宅传送点

- **语法**：`/res tpset [住宅]`

- **示例**：

```
/res tpset home
```


### `/res kick` — 把某玩家踢出住宅

- **语法**：`/res kick <住宅> <玩家>`

- **示例**：

```
/res kick home Griefer
```

- **备注**：对方仍在领地内会被持续弹开

### `/res limits` — 查看自己还能建多少块、多大面积

- **语法**：`/res limits [玩家]`

- **示例**：

```
/res limits
```

- **备注**：上限由权限组发放（residence.maxarea 等），玩家报错常见来源

### `/res bank` — 住宅租金账户的查询/存入/取出

- **语法**：`/res bank <deposit｜withdraw｜balance> [金额] [住宅]`

- **示例**：

```
/res bank deposit 500 home
```

- **备注**：租金从余额扣，不足会走租约到期流程

### `/res market` — 挂市场出售/出租住宅，或撤回/成交查询

- **语法**：`/res market <sell｜rent｜unsell｜unrent｜buy｜info> [价格] [住宅]`

- **示例**：

```
/res market sell 5000 home
```

- **备注**：rent 的价格单位是天

### `/res lease` — 续租或放弃租约

- **语法**：`/res lease <renew｜release> <住宅>`

- **示例**：

```
/res lease renew home
```


### `/res contract` — 给住宅写出租/出售合同

- **语法**：`/res contract <住宅> [天数] [价格]`

- **示例**：

```
/res contract shop 30 2000
```

- **权限**：`residence.command.contract`

### `/res message` — 设置进出领地时的提示语

- **语法**：`/res message <住宅> <enter｜leave｜remove> <文本>`

- **示例**：

```
/res message home enter 欢迎回家
```


### `/res rename` — 重命名住宅

- **语法**：`/res rename <旧名> <新名>`

- **示例**：

```
/res rename home myhome
```


### `/res tool` — 更换选区工具物品

- **语法**：`/res tool [物品]`

- **示例**：

```
/res tool blaze_rod
```

- **备注**：改完要手持该物品点击才生效

### `/res unstuck` — 卡在领地边界时把自己弹出去

- **语法**：`/res unstuck`

- **示例**：

```
/res unstuck
```


### `/res version` — 查看版本与更新提示

- **语法**：`/res version`

- **示例**：

```
/res version
```


### `/resadmin` — 管理员指令：绕过领地限制、改他人领地、强制删除

- **语法**：`/resadmin <子指令> [参数...]`

- **示例**：

```
/resadmin remove 玩家名 领地名
/resadmin setowner 领地名 新主人
```

- **备注**：误用会破坏玩家领地数据，操作前先备份 plugins/Residence 目录。

### `/resadmin setowner` — 把住宅所有权转给其他玩家

- **语法**：`/resadmin setowner <住宅> <玩家>`

- **示例**：

```
/resadmin setowner home Steve
```

- **权限**：`residence.admin`
- **备注**：原所有者立即失去权限，常用于玩家退服资产回收

### `/resadmin removeall` — 删除某玩家名下全部住宅

- **语法**：`/resadmin removeall <玩家>`

- **示例**：

```
/resadmin removeall Griefer
```

- **权限**：`residence.admin`
- **备注**：不可撤销，先 /res list 核对名单

### `/resadmin give` — 把住宅转给指定玩家

- **语法**：`/resadmin give <住宅> <玩家>`

- **示例**：

```
/resadmin give home Steve
```

- **权限**：`residence.admin`

### `/resadmin server` — 把住宅设为服务器所有（不绑定玩家）

- **语法**：`/resadmin server <住宅>`

- **示例**：

```
/resadmin server spawn_market
```

- **权限**：`residence.admin`

### `/resload` — 重新读取住宅存档文件

- **语法**：`/resload`

- **示例**：

```
/resload
```

- **备注**：用磁盘内容覆盖内存，误用会丢最近改动

### `/resreload` — 重载配置与语言文件

- **语法**：`/resreload`

- **示例**：

```
/resreload
```

- **备注**：改完 config.yml 必须跑；不重载玩家数据

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/res ?` | 分页帮助，是最全的子指令清单 | `/res ? 2` |
| `/res signupdate` | 刷新领地牌子上的文字 | `/res signupdate home` |
| `/rc` | 住宅频道聊天（含 setprefix/setcolor/kick） | `/rc setprefix [家里]` |

## 注意事项

::: warning
- /res remove、/resadmin removeall、/resadmin setowner 不可撤销，先 /res list 核对。
- /resload 用磁盘内容覆盖内存，手工改存档后使用，误用丢数据。
- 玩家「建不了地」多半是 /res limits 到顶或选区超区块上限，先查这两条。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `residence.admin` | 完全管理权（含全部 /resadmin 子指令） | op |
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
| `residence.command.contract` | 允许给住宅写出租/出售合同 | True |
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
| `residence.command.listall` | 允许列出全服住宅 | True |
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
| `residence.command.reload` | 允许执行 /resreload 与 /resload | op |
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
