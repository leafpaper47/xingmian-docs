---
title: Residence
createTime: 2026/10/24
---

# Residence

> 版本 `6.0.2.4` · 指令 5 条 · api-version `1.13` · 文件 `Residence6.0.2.4.jar`

Cuboid Residence Plugin

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/rc help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/rc` | Chat in current residence channel. | — |
| `/res` | Manage Residences | — |
| `/resadmin` | Residence admin functions. | — |
| `/resload` | Load the save file again after you have made modifications. | — |
| `/resreload` | Reload the entire residence plugin. | — |

## 详细用法

### /rc

- **说明**：Chat in current residence channel.
- **用法**：`/rc to toggle, /rc l to leave, /rc setprefix to set prefix, /rc setcolor to set color or /rc kick to kick player`

### /resadmin

- **说明**：Residence admin functions.
- **用法**：`/res ? or /resadmin ? for more info`

### /resload

- **说明**：Load the save file again after you have made modifications.
- **用法**：`/resload`

### /resreload

- **说明**：Reload the entire residence plugin.
- **用法**：`/resreload`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `residence.admin` | Gives you access to /resadmin | op |
| `residence.admin.move` | Allows to override move flag | op |
| `residence.admin.tp` | Allows to override tp flag | op |
| `residence.bypass.command` | Bypasses command flag in residence | op |
| `residence.bypass.nofly` | Bypasses nofly flag in residence | op |
| `residence.chatcolor` | Allows to change residence chat color | True |
| `residence.chatkick` | Allows to kick players from residence chat | True |
| `residence.chatprefix` | Allows to change residence chat prefix | op |
| `residence.command.area` | Allows to access particular command | True |
| `residence.command.auto` | Allows to create max residence | True |
| `residence.command.bank` | Allows to access particular command | True |
| `residence.command.check` | Allows to access particular command | True |
| `residence.command.clearflags` | Allows to access particular command | op |
| `residence.command.command` | Allows to access particular command | True |
| `residence.command.compass` | Allows to access particular command | True |
| `residence.command.confirm` | Allows to access particular command | True |
| `residence.command.contract` | Allows to access particular command | True |
| `residence.command.create` | Allows to access particular command | True |
| `residence.command.current` | Allows to access particular command | True |
| `residence.command.expand` | Allows to access particular command | True |
| `residence.command.flags` | Allows to access particular command | True |
| `residence.command.give` | Allows to access particular command | True |
| `residence.command.gset` | Allows to access particular command | True |
| `residence.command.gui` | Allows to access particular command | True |
| `residence.command.info` | Allows to access particular command | True |
| `residence.command.kick` | Allows to access particular command | True |
| `residence.command.lease` | Allows to access particular command | True |
| `residence.command.limits` | Allows to access particular command | True |
| `residence.command.list` | Allows to access particular command | True |
| `residence.command.list.others` | Allows to access particular command | True |
| `residence.command.listall` | Allows to access particular command | True |
| `residence.command.listallhidden` | Allows to access particular command | op |
| `residence.command.listhidden` | Allows to access particular command | op |
| `residence.command.lists` | Allows to access particular command | True |
| `residence.command.lset` | Allows to access particular command | True |
| `residence.command.market` | Allows to access particular command | True |
| `residence.command.material` | Allows to access particular command | True |
| `residence.command.message` | Allows to access particular command | True |
| `residence.command.message.enter` | Allows to access particular command | True |
| `residence.command.message.enter.remove` | Allows to access particular command | True |
| `residence.command.message.leave` | Allows to access particular command | True |
| `residence.command.message.leave.remove` | Allows to access particular command | True |
| `residence.command.mirror` | Allows to access particular command | True |
| `residence.command.padd` | Allows to access particular command | True |
| `residence.command.pdel` | Allows to access particular command | True |
| `residence.command.pset` | Allows to access particular command | True |
| `residence.command.rc` | Allows to access particular command | True |
| `residence.command.reload` | Allows to access particular command | op |
| `residence.command.remove` | Allows to access particular command | True |
| `residence.command.removeall` | Allows to access particular command | op |
| `residence.command.removeworld` | Allows to access particular command | op |
| `residence.command.rename` | Allows to access particular command | True |
| `residence.command.renamearea` | Allows to access particular command | True |
| `residence.command.resadmin` | Allows to access particular command | op |
| `residence.command.resbank` | Allows to access particular command | True |
| `residence.command.reset` | Allows to access particular command | True |
| `residence.command.rt` | Allows to access particular command | True |
| `residence.command.select` | Allows to access particular command | True |
| `residence.command.server` | Allows to access particular command | op |
| `residence.command.set` | Allows to access particular command | True |
| `residence.command.setdefaultflags` | Allows to access particular command | True |
| `residence.command.setmain` | Allows to access particular command | True |
| `residence.command.setowner` | Allows to access particular command | op |
| `residence.command.shop` | Allows to access particular command | True |
| `residence.command.show` | Allows to access particular command | True |
| `residence.command.siege` | Allows to access particular command | True |
| `residence.command.signconvert` | Allows to access particular command | op |
| `residence.command.signupdate` | Allows to access particular command | op |
| `residence.command.sublist` | Allows to access particular command | True |
| `residence.command.subzone` | Allows to access particular command | True |
| `residence.command.tool` | Allows to access particular command | True |
| `residence.command.tp` | Allows to access particular command | True |
| `residence.command.tpconfirm` | Allows to access particular command | True |
| `residence.command.tpset` | Allows to access particular command | True |
| `residence.command.unstuck` | Allows to access particular command | True |
| `residence.command.version` | Allows to access particular command | True |
| `residence.compass` | Allows to set compass pointer to residence | True |
| `residence.contract` | Allows you to contract residence | True |
| `residence.contract.subzone` | Allows you to contract residences subzone | True |
| `residence.create` | Allows you to create residences | True |
| `residence.create.subzone` | Allows you to create residences subzone | True |
| `residence.delete` | Allows you to delete residences | True |
| `residence.delete.subzone` | Allows you to delete residences subzone | True |
| `residence.expand` | Allows you to expand residence | True |
| `residence.expand.subzone` | Allows you to expand residences subzone | True |
| `residence.newguyresidence` | Allows for auto residence creation on chest place | True |
| `residence.randomtp` | Allows to use /res rt command | True |
| `residence.rename` | Allows you to rename residences | True |
| `residence.resize` | Allows you to resize an area | True |
| `residence.select` | Allows you to select an area to make residences | True |
| `residence.select.auto.others` | Allows to turn on auto selection for other players | op |
| `residence.topadmin` | Gives you access to /resreload and /resload commands | op |
| `residence.versioncheck` | Notice to new version after connect | op |
