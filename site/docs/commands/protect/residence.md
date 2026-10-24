---
title: Residence
createTime: 2026/10/24
---

# Residence

> 版本 `6.0.2.4` · 指令 5 条 · api-version `1.13` · 文件 `Residence6.0.2.4.jar`

Cuboid Residence插件

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/rc help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/rc` | §在当前居住频道中进行聊天。 | — |
| `/res` | 管理住宅 | — |
| `/resadmin` | 住宅管理功能。 | — |
| `/resload` | 修改后再次加载保存文件。 | — |
| `/resreload` | 重新加载整个住宅插件。 | — |

## 详细用法

### /rc

- **说明**：§在当前居住频道中进行聊天。
- **用法**：`/rc to toggle, /rc l to leave, /rc setprefix to set prefix, /rc setcolor to set color or /rc kick to kick player`

### /resadmin

- **说明**：住宅管理功能。
- **用法**：`/res ? or /resadmin ? for more info`

### /resload

- **说明**：修改后再次加载保存文件。
- **用法**：`/resload`

### /resreload

- **说明**：重新加载整个住宅插件。
- **用法**：`/resreload`

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
