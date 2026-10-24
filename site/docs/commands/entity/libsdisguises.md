---
title: LibsDisguises
createTime: 2026/10/24
---

# LibsDisguises

> 版本 `26.9.26-SNAPSHOT` · 指令 28 条 · api-version `1.13` · 文件 `LibsDisguises.jar`

具有各种伪装的伪装插件。

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/copydisguise help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/copydisguise` | 将伪装输出到可用字符串 | `libsdisguises.seecmd.copydisguise` |
| `/disguise` | 把自己伪装成一个实体。 | `libsdisguises.seecmd.disguise` |
| `/disguiseanimation` | 在您自己的伪装上播放受支持的动画 | `libsdisguises.disguiseanimation` |
| `/disguiseclone` | 复制伪装（或实体），稍后再使用。 | `libsdisguises.seecmd.disguiseclone` |
| `/disguiseentity` | 将实体伪装成另一个实体。 | `libsdisguises.seecmd.disguiseentity` |
| `/disguiseentityanimation` | 在右键单击的实体的伪装上播放支持的动画 | `libsdisguises.disguiseentityanimation` |
| `/disguisehelp` | LibsDisguises的帮助命令。 | `libsdisguises.seecmd.disguisehelp` |
| `/disguisemodify` | 修改自己的伪装 | `libsdisguises.seecmd.disguisemodify` |
| `/disguisemodifyentity` | 右键单击修改伪装 | `libsdisguises.seecmd.disguisemodifyentity` |
| `/disguisemodifyplayer` | 修改玩家的伪装 | `libsdisguises.seecmd.disguisemodifyplayer` |
| `/disguisemodifyradius` | 修改半径内的伪装 | `libsdisguises.seecmd.disguisemodifyradius` |
| `/disguisemodifyselector` | 通过实体选择器修改实体伪装 | `libsdisguises.seecmd.disguisemodifyselector` |
| `/disguiseplayer` | 将另一个玩家伪装成一个实体。 | `libsdisguises.seecmd.disguiseplayer` |
| `/disguiseplayeranimation` | 在玩家/UUID的伪装上播放支持的动画 | `libsdisguises.disguiseplayeranimation` |
| `/disguiseradius` | 将半径内的所有实体伪装成实体。 | `libsdisguises.seecmd.disguiseradius` |
| `/disguiseradiusanimation` | 在半径范围内的所有受支持的伪装上播放受支持的动画 | `libsdisguises.disguiseradiusanimation` |
| `/disguiseselector` | 通过实体选择器伪装实体。 | `libsdisguises.seecmd.disguiseselector` |
| `/disguiseselectoranimation` | 通过实体选择器在所有支持的伪装上播放支持的动画。 | `libsdisguises.disguiseselectoranimation` |
| `/disguiseviewbar` | 打开或关闭您自己的伪装。 | `libsdisguises.seecmd.disguiseviewbar` |
| `/grabhead` | 抓取皮肤、网址或播放器的头部项目 | `libsdisguises.seecmd.grabhead` |
| `/grabskin` | 从文件、网址或玩家名称/uuid中获取皮肤 | `libsdisguises.seecmd.grabskin` |
| `/libsdisguises` | Libsdisguises的主命令。 | — |
| `/savedisguise` | 将自定义伪装保存到disguises.yml | `libsdisguises.seecmd.savedisguise` |
| `/undisguise` | 不伪装自己。 | `libsdisguises.seecmd.undisguise` |
| `/undisguiseentity` | 隐藏实体。 | `libsdisguises.seecmd.undisguiseentity` |
| `/undisguiseplayer` | 隐藏玩家。 | `libsdisguises.seecmd.undisguiseplayer` |
| `/undisguiseradius` | 隐藏半径内的所有实体。 | `libsdisguises.seecmd.undisguiseradius` |
| `/undisguiseselector` | 在实体选择器中隐藏所有实体。 | `libsdisguises.seecmd.undisguiseselector` |

## 详细用法

### /copydisguise

- **说明**：将伪装输出到可用字符串
- **别名**：`/disguisecopy`、`/disgcopy`、`/dcopy`、`/copydisg`、`/copyd`、`/parsedisguise`、`/disguiseparse`
- **权限**：`libsdisguises.seecmd.copydisguise`

### /disguise

- **说明**：把自己伪装成一个实体。
- **别名**：`/d`、`/dis`、`/disg`
- **权限**：`libsdisguises.seecmd.disguise`

### /disguiseanimation

- **说明**：在您自己的伪装上播放受支持的动画
- **权限**：`libsdisguises.disguiseanimation`

### /disguiseclone

- **说明**：复制伪装（或实体），稍后再使用。
- **别名**：`/disguisec`、`/disc`、`/disclone`、`/dclone`、`/clonedisguise`、`/clonedis`、`/cdisguise`、`/cdis`、`/clonedisg`、`/disgclone`
- **权限**：`libsdisguises.seecmd.disguiseclone`

### /disguiseentity

- **说明**：将实体伪装成另一个实体。
- **别名**：`/dentity`、`/disentity`、`/disgentity`
- **权限**：`libsdisguises.seecmd.disguiseentity`

### /disguiseentityanimation

- **说明**：在右键单击的实体的伪装上播放支持的动画
- **权限**：`libsdisguises.disguiseentityanimation`

### /disguisehelp

- **说明**：LibsDisguises的帮助命令。
- **别名**：`/dhelp`、`/dishelp`、`/disghelp`
- **权限**：`libsdisguises.seecmd.disguisehelp`

### /disguisemodify

- **说明**：修改自己的伪装
- **别名**：`/dmodify`、`/dmod`、`/disgmodify`、`/modifydisguise`、`/moddisguise`、`/mdisguise`
- **权限**：`libsdisguises.seecmd.disguisemodify`

### /disguisemodifyentity

- **说明**：右键单击修改伪装
- **别名**：`/dmodifyentity`、`/dmodentity`、`/disgmodentity`、`/dismodentity`、`/modifydisguiseentity`、`/modifydisgentity`、`/modifydentity`、`/moddisguiseentity`、`/moddisgentity`、`/mdisguiseentity`、`/mdisgentity`
- **权限**：`libsdisguises.seecmd.disguisemodifyentity`

### /disguisemodifyplayer

- **说明**：修改玩家的伪装
- **别名**：`/dmodifyplayer`、`/dmodplayer`、`/disgmodifyplayer`、`/dismodplayer`、`/disgmodplayer`、`/modifydisguiseplayer`、`/moddisguiseplayer`、`/mdisguiseplayer`、`/mdisgplayer`、`/dmodifyuuid`、`/dmoduuid`、`/disgmodifyuuid`、`/dismoduuid`、`/disgmoduuid`、`/modifydisguiseuuid`、`/moddisguiseuuid`、`/mdisguiseuuid`、`/mdisguuid`
- **权限**：`libsdisguises.seecmd.disguisemodifyplayer`

### /disguisemodifyradius

- **说明**：修改半径内的伪装
- **别名**：`/dmodifyradius`、`/dmodradius`、`/disgmodradius`、`/dismodradius`、`/modifydisguiseradius`、`/modifydisgradius`、`/moddisguiseradius`、`/mdisguiseradius`、`/moddisgradius`
- **权限**：`libsdisguises.seecmd.disguisemodifyradius`

### /disguisemodifyselector

- **说明**：通过实体选择器修改实体伪装
- **别名**：`/dmodifyselector`、`/dmodselector`、`/disgmodselector`、`/dismodselector`、`/modifydisguiseselector`、`/modifydisgselector`、`/moddisguiseselector`、`/mdisguiseselector`、`/moddisgselector`
- **权限**：`libsdisguises.seecmd.disguisemodifyselector`

### /disguiseplayer

- **说明**：将另一个玩家伪装成一个实体。
- **别名**：`/dplayer`、`/displayer`、`/disgplayer`、`/disguiseuuid`、`/disguuid`、`/duuid`
- **权限**：`libsdisguises.seecmd.disguiseplayer`

### /disguiseplayeranimation

- **说明**：在玩家/UUID的伪装上播放支持的动画
- **别名**：`/disguiseuuidanimation`
- **权限**：`libsdisguises.disguiseplayeranimation`

### /disguiseradius

- **说明**：将半径内的所有实体伪装成实体。
- **别名**：`/disradius`、`/dradius`、`/disgradius`
- **权限**：`libsdisguises.seecmd.disguiseradius`

### /disguiseradiusanimation

- **说明**：在半径范围内的所有受支持的伪装上播放受支持的动画
- **权限**：`libsdisguises.disguiseradiusanimation`

### /disguiseselector

- **说明**：通过实体选择器伪装实体。
- **别名**：`/dselector`、`/disselector`、`/disgselector`
- **权限**：`libsdisguises.seecmd.disguiseselector`

### /disguiseselectoranimation

- **说明**：通过实体选择器在所有支持的伪装上播放支持的动画。
- **权限**：`libsdisguises.disguiseselectoranimation`

### /disguiseviewbar

- **说明**：打开或关闭您自己的伪装。
- **别名**：`/dviewbar`、`/dvb`、`/disguisevb`、`/disvb`、`/viewdisguisebar`、`/viewbardisguise`、`/bardisguise`、`/bardisg`、`/bard`、`/notifybar`、`/viewnotifybar`、`/disguisenotifybar`、`/disgnotifybar`、`/dnotifybar`
- **权限**：`libsdisguises.seecmd.disguiseviewbar`

### /grabhead

- **说明**：抓取皮肤、网址或播放器的头部项目
- **别名**：`/grabskull`、`/playerhead`、`/savehead`、`/gethead`
- **权限**：`libsdisguises.seecmd.grabhead`

### /grabskin

- **说明**：从文件、网址或玩家名称/uuid中获取皮肤
- **别名**：`/uploadskin`、`/skin`、`/saveskin`、`/cacheskin`、`/downloadskin`、`/skincache`
- **权限**：`libsdisguises.seecmd.grabskin`

### /libsdisguises

- **说明**：Libsdisguises的主命令。
- **别名**：`/libsdisg`、`/ld`

### /savedisguise

- **说明**：将自定义伪装保存到disguises.yml
- **别名**：`/customdisguise`、`/savedisg`、`/customdisg`、`/createdisguise`、`/createdisg`
- **权限**：`libsdisguises.seecmd.savedisguise`

### /undisguise

- **说明**：不伪装自己。
- **别名**：`/und`、`/undis`、`/undisg`
- **权限**：`libsdisguises.seecmd.undisguise`

### /undisguiseentity

- **说明**：隐藏实体。
- **别名**：`/undisentity`、`/undentity`、`/undisgentity`
- **权限**：`libsdisguises.seecmd.undisguiseentity`

### /undisguiseplayer

- **说明**：隐藏玩家。
- **别名**：`/undisplayer`、`/undplayer`、`/undisgplayer`、`/undisguiseuuid`、`/unduuid`、`/undisguuid`
- **权限**：`libsdisguises.seecmd.undisguiseplayer`

### /undisguiseradius

- **说明**：隐藏半径内的所有实体。
- **别名**：`/undisradius`、`/undradius`、`/undisgradius`
- **权限**：`libsdisguises.seecmd.undisguiseradius`

### /undisguiseselector

- **说明**：在实体选择器中隐藏所有实体。
- **别名**：`/undisselector`、`/undselector`、`/undisgselector`
- **权限**：`libsdisguises.seecmd.undisguiseselector`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `libsdisguises.config` | 允许玩家检查Lib的伪装配置的值 | — |
| `libsdisguises.count` | 允许用户查看有多少伪装处于活动状态 | — |
| `libsdisguises.debug` | 允许服务器管理员测试玩家伪装在计分板上是否正常 | — |
| `libsdisguises.disguiseanimation` | 在您自己的伪装上播放受支持的动画 | op |
| `libsdisguises.disguiseentityanimation` | 在右键单击的实体的伪装上播放支持的动画 | op |
| `libsdisguises.disguiseplayeranimation` | 在玩家/UUID的伪装上播放支持的动画 | op |
| `libsdisguises.disguiseradiusanimation` | 在半径范围内的所有受支持的伪装上播放受支持的动画 | op |
| `libsdisguises.disguiseselectoranimation` | 通过实体选择器在所有受支持的伪装上播放受支持的动画 | op |
| `libsdisguises.grabhead` | 允许用户使用/grabhead命令 | — |
| `libsdisguises.hidename` | 允许玩家忽略被迫高于伪装的名称 | — |
| `libsdisguises.json` | 允许玩家将保留的项目解析为json | — |
| `libsdisguises.metainfo` | 允许玩家获取元信息 | — |
| `libsdisguises.mods` | 允许用户查看正在使用的MOD。 | — |
| `libsdisguises.multiname` | 允许命令用户设置不同高度的名称 | — |
| `libsdisguises.noactionbar` | 隐藏操作栏，即使在配置中启用 | — |
| `libsdisguises.permtest` | 允许玩家测试权限 | — |
| `libsdisguises.pve` | 允许玩家忽略pve限制。 | — |
| `libsdisguises.pvp` | 允许玩家忽略pvp限制。 | — |
| `libsdisguises.ratelimitbypass` | 允许活着的玩家绕过伪装命令的500ms速率限制，用于防止崩溃 | — |
| `libsdisguises.reload` | 允许用户重新加载LibsDisguises。 | — |
| `libsdisguises.scoreboardtest` | 测试计分板是否有效，这是一个简单的测试。 | — |
| `libsdisguises.seecmd` | 在选项卡完成中查看所有命令 | True |
| `libsdisguises.seecmd.copydisguise` | 请参阅TAB 补全中的/copydisguise命令 | — |
| `libsdisguises.seecmd.disguise` | 请参阅TAB 补全中的/disguise命令 | — |
| `libsdisguises.seecmd.disguiseanimation` | 参见TAB 补全中的/disguiseanimation命令 | — |
| `libsdisguises.seecmd.disguiseclone` | 请参阅TAB 补全中的/disguiseclone命令 | — |
| `libsdisguises.seecmd.disguiseentity` | 请参阅TAB 补全中的/disguiseentity命令 | — |
| `libsdisguises.seecmd.disguiseentityanimation` | 请参阅TAB 补全中的/disguiseentityanimation命令 | — |
| `libsdisguises.seecmd.disguisehelp` | 请参阅选项卡完成中的/disguisehelp命令 | — |
| `libsdisguises.seecmd.disguisemodify` | 请参阅TAB 补全中的/disguisemodify命令 | — |
| `libsdisguises.seecmd.disguisemodifyentity` | 请参阅TAB 补全中的/disguisemodifyentity命令 | — |
| `libsdisguises.seecmd.disguisemodifyplayer` | 请参阅选项卡完成中的/disguisemodifyplayer命令 | — |
| `libsdisguises.seecmd.disguisemodifyradius` | 请参阅TAB 补全中的/disguisemodifyradius命令 | — |
| `libsdisguises.seecmd.disguisemodifyselector` | 请参阅TAB 补全中的/disguisemodifyselector命令 | — |
| `libsdisguises.seecmd.disguiseplayer` | 请参阅制表符完成中的/disguiseplayer命令 | — |
| `libsdisguises.seecmd.disguiseplayeranimation` | 请参阅制表符完成中的/disguiseplayeranimation命令 | — |
| `libsdisguises.seecmd.disguiseradius` | 请参阅TAB 补全中的/disguiseradius命令 | — |
| `libsdisguises.seecmd.disguiseradiusanimation` | 请参阅TAB 补全中的/disguiseradiusanimation命令 | — |
| `libsdisguises.seecmd.disguiseselector` | 请参阅选项卡完成中的/disguiseselector命令 | — |
| `libsdisguises.seecmd.disguiseselectoranimation` | 请参阅TAB 补全中的/disguiseselectoranimation命令 | — |
| `libsdisguises.seecmd.disguiseviewbar` | 请参阅选项卡完成中的/disguiseviewbar命令 | — |
| `libsdisguises.seecmd.disguiseviewself` | 请参阅TAB 补全中的/disguiseviewself命令 | — |
| `libsdisguises.seecmd.grabhead` | 在TAB 补全中查看/grabhead命令 | — |
| `libsdisguises.seecmd.grabskin` | 在选项卡完成中查看/grabskin命令 | — |
| `libsdisguises.seecmd.savedisguise` | 在选项卡完成中查看/savedisguise命令 | — |
| `libsdisguises.seecmd.undisguise` | 请参阅TAB 补全中的/undisguise命令 | — |
| `libsdisguises.seecmd.undisguiseentity` | 请参阅TAB 补全中的/undisguiseentity命令 | — |
| `libsdisguises.seecmd.undisguiseplayer` | 请参阅制表符完成中的/undisguiseplayer命令 | — |
| `libsdisguises.seecmd.undisguiseradius` | 请参阅TAB 补全中的/undisguiseradius命令 | — |
| `libsdisguises.seecmd.undisguiseselector` | 请参阅TAB 补全中的/undisguiseselector命令 | — |
| `libsdisguises.seethrough` | 允许玩家看穿伪装。 | — |
| `libsdisguises.selfdisguises` | 控制玩家是否可以查看自我伪装，默认为true。仅在伪装开始和切换自我伪装命令时选中。如果玩家有权访问/disguisemodify，他们可以将其重新打开。 | True |
| `libsdisguises.update` | 允许用户更新Libs伪装 | — |
