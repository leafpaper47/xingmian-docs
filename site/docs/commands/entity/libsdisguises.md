---
title: LibsDisguises
createTime: 2026/10/24
---

# 伪装 · LibsDisguises

> 分类 🧟 生物与展示 · 版本 `26.9.26-SNAPSHOT` · 指令 28 条 · api-version `1.13`

::: tip 伪装系统
把玩家或实体伪装成任何生物/物品，带玩家皮肤、自定义名称、动画与选项；活动整活、剧情演出与反作弊排查的主力工具。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 把自己变成苦力怕 | /disguise creeper | 别名 /d、/dis |
| 取消伪装 | /undisguise | 别名 /und、/undis |
| 把某人变成僵尸 | /disguiseplayer Steve zombie | 需对目标玩家的伪装权限 |
| 整片区域全变 | /disguiseradius 10 bat | 半径内全部实体，慎用 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/copydisguise` | 把伪装导出为可复用字符串<br>别名 `/disguisecopy`、`/disgcopy`、`/dcopy`、`/copydisg`、`/copyd`、`/parsedisguise`、`/disguiseparse` | `/copydisguise [参数]` | `libsdisguises.seecmd.copydisguise` |
| `/disguise` | 把自己伪装成指定实体（可带名称、皮肤、选项）<br>别名 `/d`、`/dis`、`/disg` | `/disguise <类型> [参数...]` | `libsdisguises.seecmd.disguise` |
| `/disguiseanimation` | 在自己的伪装上播放动画 | `/disguiseanimation <动画>` | `libsdisguises.disguiseanimation` |
| `/disguiseclone` | 复制某个实体的伪装，之后再套用<br>别名 `/disguisec`、`/disc`、`/disclone`、`/dclone`、`/clonedisguise`、`/clonedis`、`/cdisguise`、`/cdis`、`/clonedisg`、`/disgclone` | `/disguiseclone <参数>` | `libsdisguises.seecmd.disguiseclone` |
| `/disguiseentity` | 把准星指向的实体伪装成另一实体<br>别名 `/dentity`、`/disentity`、`/disgentity` | `/disguiseentity <类型> [参数]` | `libsdisguises.seecmd.disguiseentity` |
| `/disguiseentityanimation` | 让右键选中实体的伪装播放动画 | `/disguiseentityanimation <动画名>` | `libsdisguises.disguiseentityanimation` |
| `/disguisehelp` | 打印伪装可用类型与参数帮助<br>别名 `/dhelp`、`/dishelp`、`/disghelp` | `/disguisehelp [类型]` | `libsdisguises.seecmd.disguisehelp` |
| `/disguisemodify` | 修改自己现有伪装的选项（名称、皮肤等）<br>别名 `/dmodify`、`/dmod`、`/disgmodify`、`/modifydisguise`、`/moddisguise`、`/mdisguise` | `/disguisemodify <选项> <值>` | `libsdisguises.seecmd.disguisemodify` |
| `/disguisemodifyentity` | 修改右键选中实体伪装的参数<br>别名 `/dmodifyentity`、`/dmodentity`、`/disgmodentity`、`/dismodentity`、`/modifydisguiseentity`、`/modifydisgentity`、`/modifydentity`、`/moddisguiseentity`、`/moddisgentity`、`/mdisguiseentity`、`/mdisgentity` | `/disguisemodifyentity <参数> <值>` | `libsdisguises.seecmd.disguisemodifyentity` |
| `/disguisemodifyplayer` | 修改指定玩家伪装的选项<br>别名 `/dmodifyplayer`、`/dmodplayer`、`/disgmodifyplayer`、`/dismodplayer`、`/disgmodplayer`、`/modifydisguiseplayer`、`/moddisguiseplayer`、`/mdisguiseplayer`、`/mdisgplayer`、`/dmodifyuuid`、`/dmoduuid`、`/disgmodifyuuid`、`/dismoduuid`、`/disgmoduuid`、`/modifydisguiseuuid`、`/moddisguiseuuid`、`/mdisguiseuuid`、`/mdisguuid` | `/disguisemodifyplayer <玩家> <选项> <值>` | `libsdisguises.seecmd.disguisemodifyplayer` |
| `/disguisemodifyradius` | 批量修改半径内伪装的参数<br>别名 `/dmodifyradius`、`/dmodradius`、`/disgmodradius`、`/dismodradius`、`/modifydisguiseradius`、`/modifydisgradius`、`/moddisguiseradius`、`/mdisguiseradius`、`/moddisgradius` | `/disguisemodifyradius <半径> <参数> <值>` | `libsdisguises.seecmd.disguisemodifyradius` |
| `/disguisemodifyselector` | 用选择器批量修改伪装参数<br>别名 `/dmodifyselector`、`/dmodselector`、`/disgmodselector`、`/dismodselector`、`/modifydisguiseselector`、`/modifydisgselector`、`/moddisguiseselector`、`/mdisguiseselector`、`/moddisgselector` | `/disguisemodifyselector <选择器> <参数> <值>` | `libsdisguises.seecmd.disguisemodifyselector` |
| `/disguiseplayer` | 把指定玩家伪装成某实体<br>别名 `/dplayer`、`/displayer`、`/disgplayer`、`/disguiseuuid`、`/disguuid`、`/duuid` | `/disguiseplayer <玩家> <类型> [参数]` | `libsdisguises.seecmd.disguiseplayer` |
| `/disguiseplayeranimation` | 在指定玩家的伪装上播放动画<br>别名 `/disguiseuuidanimation` | `/disguiseplayeranimation <玩家> <动画>` | `libsdisguises.disguiseplayeranimation` |
| `/disguiseradius` | 半径内所有实体统一伪装<br>别名 `/disradius`、`/dradius`、`/disgradius` | `/disguiseradius <半径> <类型>` | `libsdisguises.seecmd.disguiseradius` |
| `/disguiseradiusanimation` | 让半径内所有伪装播放动画 | `/disguiseradiusanimation <半径> <动画名>` | `libsdisguises.disguiseradiusanimation` |
| `/disguiseselector` | 用实体选择器批量伪装<br>别名 `/dselector`、`/disselector`、`/disgselector` | `/disguiseselector <选择器> <类型>` | `libsdisguises.seecmd.disguiseselector` |
| `/disguiseselectoranimation` | 让选择器命中的伪装播放动画 | `/disguiseselectoranimation <选择器> <动画名>` | `libsdisguises.disguiseselectoranimation` |
| `/disguiseviewbar` | 开关伪装状态条提示（BOSS 条显示状态）<br>别名 `/dviewbar`、`/dvb`、`/disguisevb`、`/disvb`、`/viewdisguisebar`、`/viewbardisguise`、`/bardisguise`、`/bardisg`、`/bard`、`/notifybar`、`/viewnotifybar`、`/disguisenotifybar`、`/disgnotifybar`、`/dnotifybar` | `/disguiseviewbar` | `libsdisguises.seecmd.disguiseviewbar` |
| `/grabhead` | 获取某皮肤对应的头颅物品<br>别名 `/grabskull`、`/playerhead`、`/savehead`、`/gethead` | `/grabhead <玩家名｜URL>` | `libsdisguises.seecmd.grabhead` |
| `/grabskin` | 抓取玩家/URL 皮肤并缓存供伪装使用<br>别名 `/uploadskin`、`/skin`、`/saveskin`、`/cacheskin`、`/downloadskin`、`/skincache` | `/grabskin <玩家名｜URL>` | `libsdisguises.seecmd.grabskin` |
| `/libsdisguises` | 插件管理指令：重载、配置、调试、统计<br>别名 `/libsdisg`、`/ld` | `/ld <reload｜config｜count｜debug｜json｜permtest｜updat…` | — |
| `/savedisguise` | 把自定义伪装存进 disguises.yml<br>别名 `/customdisguise`、`/savedisg`、`/customdisg`、`/createdisguise`、`/createdisg` | `/savedisguise <名称> <伪装串>` | `libsdisguises.seecmd.savedisguise` |
| `/undisguise` | 取消自己的伪装<br>别名 `/und`、`/undis`、`/undisg` | `/undisguise` | `libsdisguises.seecmd.undisguise` |
| `/undisguiseentity` | 取消准星实体的伪装<br>别名 `/undisentity`、`/undentity`、`/undisgentity` | `/undisguiseentity` | `libsdisguises.seecmd.undisguiseentity` |
| `/undisguiseplayer` | 取消指定玩家的伪装<br>别名 `/undisplayer`、`/undplayer`、`/undisgplayer`、`/undisguiseuuid`、`/unduuid`、`/undisguuid` | `/undisguiseplayer <玩家>` | `libsdisguises.seecmd.undisguiseplayer` |
| `/undisguiseradius` | 取消半径内全部伪装<br>别名 `/undisradius`、`/undradius`、`/undisgradius` | `/undisguiseradius <半径>` | `libsdisguises.seecmd.undisguiseradius` |
| `/undisguiseselector` | 用选择器批量取消伪装<br>别名 `/undisselector`、`/undselector`、`/undisgselector` | `/undisguiseselector <选择器>` | `libsdisguises.seecmd.undisguiseselector` |

## 指令详解

### `/copydisguise` — 把伪装导出为可复用字符串

- **语法**：`/copydisguise [参数]`

- **示例**：

```
/copydisguise
```

- **别名**：`/disguisecopy`、`/disgcopy`、`/dcopy`、`/copydisg`、`/copyd`、`/parsedisguise`、`/disguiseparse`
- **权限**：`libsdisguises.seecmd.copydisguise`
- **备注**：配合 /savedisguise 存进配置

### `/disguise` — 把自己伪装成指定实体（可带名称、皮肤、选项）

- **语法**：`/disguise <类型> [参数...]`

- **示例**：

```
/disguise creeper
/disguise player Notch setname 假玩家
```

- **别名**：`/d`、`/dis`、`/disg`
- **权限**：`libsdisguises.seecmd.disguise`
- **备注**：别名 /d、/dis、/disg

### `/disguiseanimation` — 在自己的伪装上播放动画

- **语法**：`/disguiseanimation <动画>`

- **示例**：

```
/disguiseanimation swing_main_hand
```

- **权限**：`libsdisguises.disguiseanimation`

### `/disguiseclone` — 复制某个实体的伪装，之后再套用

- **语法**：`/disguiseclone <参数>`

- **示例**：

```
/disguiseclone
```

- **别名**：`/disguisec`、`/disc`、`/disclone`、`/dclone`、`/clonedisguise`、`/clonedis`、`/cdisguise`、`/cdis`、`/clonedisg`、`/disgclone`
- **权限**：`libsdisguises.seecmd.disguiseclone`
- **备注**：调试同一套伪装反复使用时省事

### `/disguiseentity` — 把准星指向的实体伪装成另一实体

- **语法**：`/disguiseentity <类型> [参数]`

- **示例**：

```
/disguiseentity cow
```

- **别名**：`/dentity`、`/disentity`、`/disgentity`
- **权限**：`libsdisguises.seecmd.disguiseentity`
- **备注**：要先右键实体选中目标

### `/disguiseentityanimation` — 让右键选中实体的伪装播放动画

- **语法**：`/disguiseentityanimation <动画名>`

- **示例**：

```
/disguiseentityanimation swing_mainhand
```

- **权限**：`libsdisguises.disguiseentityanimation`

### `/disguisehelp` — 打印伪装可用类型与参数帮助

- **语法**：`/disguisehelp [类型]`

- **示例**：

```
/disguisehelp
```

- **别名**：`/dhelp`、`/dishelp`、`/disghelp`
- **权限**：`libsdisguises.seecmd.disguisehelp`

### `/disguisemodify` — 修改自己现有伪装的选项（名称、皮肤等）

- **语法**：`/disguisemodify <选项> <值>`

- **示例**：

```
/disguisemodify setname 假苦力怕
```

- **别名**：`/dmodify`、`/dmod`、`/disgmodify`、`/modifydisguise`、`/moddisguise`、`/mdisguise`
- **权限**：`libsdisguises.seecmd.disguisemodify`
- **备注**：参数名用 `/disguisemodify` 不带参数时的列表里的写法。

### `/disguisemodifyentity` — 修改右键选中实体伪装的参数

- **语法**：`/disguisemodifyentity <参数> <值>`

- **示例**：

```
/disguisemodifyentity setglowing true
```

- **别名**：`/dmodifyentity`、`/dmodentity`、`/disgmodentity`、`/dismodentity`、`/modifydisguiseentity`、`/modifydisgentity`、`/modifydentity`、`/moddisguiseentity`、`/moddisgentity`、`/mdisguiseentity`、`/mdisgentity`
- **权限**：`libsdisguises.seecmd.disguisemodifyentity`

### `/disguisemodifyplayer` — 修改指定玩家伪装的选项

- **语法**：`/disguisemodifyplayer <玩家> <选项> <值>`

- **示例**：

```
/disguisemodifyplayer Steve setname 假僵尸
```

- **别名**：`/dmodifyplayer`、`/dmodplayer`、`/disgmodifyplayer`、`/dismodplayer`、`/disgmodplayer`、`/modifydisguiseplayer`、`/moddisguiseplayer`、`/mdisguiseplayer`、`/mdisgplayer`、`/dmodifyuuid`、`/dmoduuid`、`/disgmodifyuuid`、`/dismoduuid`、`/disgmoduuid`、`/modifydisguiseuuid`、`/moddisguiseuuid`、`/mdisguiseuuid`、`/mdisguuid`
- **权限**：`libsdisguises.seecmd.disguisemodifyplayer`

### `/disguisemodifyradius` — 批量修改半径内伪装的参数

- **语法**：`/disguisemodifyradius <半径> <参数> <值>`

- **示例**：

```
/disguisemodifyradius 10 setburning false
```

- **别名**：`/dmodifyradius`、`/dmodradius`、`/disgmodradius`、`/dismodradius`、`/modifydisguiseradius`、`/modifydisgradius`、`/moddisguiseradius`、`/mdisguiseradius`、`/moddisgradius`
- **权限**：`libsdisguises.seecmd.disguisemodifyradius`

### `/disguisemodifyselector` — 用选择器批量修改伪装参数

- **语法**：`/disguisemodifyselector <选择器> <参数> <值>`

- **示例**：

```
/disguisemodifyselector @e[type=zombie] setburning false
```

- **别名**：`/dmodifyselector`、`/dmodselector`、`/disgmodselector`、`/dismodselector`、`/modifydisguiseselector`、`/modifydisgselector`、`/moddisguiseselector`、`/mdisguiseselector`、`/moddisgselector`
- **权限**：`libsdisguises.seecmd.disguisemodifyselector`

### `/disguiseplayer` — 把指定玩家伪装成某实体

- **语法**：`/disguiseplayer <玩家> <类型> [参数]`

- **示例**：

```
/disguiseplayer Steve zombie
```

- **别名**：`/dplayer`、`/displayer`、`/disgplayer`、`/disguiseuuid`、`/disguuid`、`/duuid`
- **权限**：`libsdisguises.seecmd.disguiseplayer`

### `/disguiseplayeranimation` — 在指定玩家的伪装上播放动画

- **语法**：`/disguiseplayeranimation <玩家> <动画>`

- **示例**：

```
/disguiseplayeranimation Steve swing_main_hand
```

- **别名**：`/disguiseuuidanimation`
- **权限**：`libsdisguises.disguiseplayeranimation`

### `/disguiseradius` — 半径内所有实体统一伪装

- **语法**：`/disguiseradius <半径> <类型>`

- **示例**：

```
/disguiseradius 10 bat
```

- **别名**：`/disradius`、`/dradius`、`/disgradius`
- **权限**：`libsdisguises.seecmd.disguiseradius`
- **备注**：会把玩家一起改，线上慎用

### `/disguiseradiusanimation` — 让半径内所有伪装播放动画

- **语法**：`/disguiseradiusanimation <半径> <动画名>`

- **示例**：

```
/disguiseradiusanimation 8 swing_offhand
```

- **权限**：`libsdisguises.disguiseradiusanimation`

### `/disguiseselector` — 用实体选择器批量伪装

- **语法**：`/disguiseselector <选择器> <类型>`

- **示例**：

```
/disguiseselector @e[type=zombie] bat
```

- **别名**：`/dselector`、`/disselector`、`/disgselector`
- **权限**：`libsdisguises.seecmd.disguiseselector`
- **备注**：适合精准整片区域，比 radius 安全

### `/disguiseselectoranimation` — 让选择器命中的伪装播放动画

- **语法**：`/disguiseselectoranimation <选择器> <动画名>`

- **示例**：

```
/disguiseselectoranimation @e[type=pig] swing_offhand
```

- **权限**：`libsdisguises.disguiseselectoranimation`

### `/disguiseviewbar` — 开关伪装状态条提示（BOSS 条显示状态）

- **语法**：`/disguiseviewbar`

- **示例**：

```
/disguiseviewbar
```

- **别名**：`/dviewbar`、`/dvb`、`/disguisevb`、`/disvb`、`/viewdisguisebar`、`/viewbardisguise`、`/bardisguise`、`/bardisg`、`/bard`、`/notifybar`、`/viewnotifybar`、`/disguisenotifybar`、`/disgnotifybar`、`/dnotifybar`
- **权限**：`libsdisguises.seecmd.disguiseviewbar`

### `/grabhead` — 获取某皮肤对应的头颅物品

- **语法**：`/grabhead <玩家名｜URL>`

- **示例**：

```
/grabhead Notch
```

- **别名**：`/grabskull`、`/playerhead`、`/savehead`、`/gethead`
- **权限**：`libsdisguises.seecmd.grabhead`

### `/grabskin` — 抓取玩家/URL 皮肤并缓存供伪装使用

- **语法**：`/grabskin <玩家名｜URL>`

- **示例**：

```
/grabskin Notch
```

- **别名**：`/uploadskin`、`/skin`、`/saveskin`、`/cacheskin`、`/downloadskin`、`/skincache`
- **权限**：`libsdisguises.seecmd.grabskin`
- **备注**：抓到的皮肤可在 `/disguise player <皮肤名> setskin` 里用。

### `/libsdisguises` — 插件管理指令：重载、配置、调试、统计

- **语法**：`/ld <reload｜config｜count｜debug｜json｜permtest｜update｜uploadlogs>`

- **示例**：

```
/ld reload
```

- **别名**：`/libsdisg`、`/ld`
- **备注**：别名 /libsdisg

### `/savedisguise` — 把自定义伪装存进 disguises.yml

- **语法**：`/savedisguise <名称> <伪装串>`

- **示例**：

```
/savedisguise 假苦力怕 creeper setname:苦力怕
```

- **别名**：`/customdisguise`、`/savedisg`、`/customdisg`、`/createdisguise`、`/createdisg`
- **权限**：`libsdisguises.seecmd.savedisguise`
- **备注**：保存的是当前伪装的全部参数；改名或换皮肤后需重新保存。

### `/undisguise` — 取消自己的伪装

- **语法**：`/undisguise`

- **示例**：

```
/undisguise
```

- **别名**：`/und`、`/undis`、`/undisg`
- **权限**：`libsdisguises.seecmd.undisguise`
- **备注**：别名 /und、/undis

### `/undisguiseentity` — 取消准星实体的伪装

- **语法**：`/undisguiseentity`

- **示例**：

```
/undisguiseentity
```

- **别名**：`/undisentity`、`/undentity`、`/undisgentity`
- **权限**：`libsdisguises.seecmd.undisguiseentity`

### `/undisguiseplayer` — 取消指定玩家的伪装

- **语法**：`/undisguiseplayer <玩家>`

- **示例**：

```
/undisguiseplayer Steve
```

- **别名**：`/undisplayer`、`/undplayer`、`/undisgplayer`、`/undisguiseuuid`、`/unduuid`、`/undisguuid`
- **权限**：`libsdisguises.seecmd.undisguiseplayer`

### `/undisguiseradius` — 取消半径内全部伪装

- **语法**：`/undisguiseradius <半径>`

- **示例**：

```
/undisguiseradius 10
```

- **别名**：`/undisradius`、`/undradius`、`/undisgradius`
- **权限**：`libsdisguises.seecmd.undisguiseradius`

### `/undisguiseselector` — 用选择器批量取消伪装

- **语法**：`/undisguiseselector <选择器>`

- **示例**：

```
/undisguiseselector @e[type=zombie]
```

- **别名**：`/undisselector`、`/undselector`、`/undisgselector`
- **权限**：`libsdisguises.seecmd.undisguiseselector`

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/ld reload` | 重载配置与 disguise 定义 | `/ld reload` |
| `/ld config` | 查看/修改运行期配置项 | `/ld config` |
| `/ld count` | 统计当前伪装数量与类型分布 | `/ld count` |
| `/ld permtest <玩家>` | 检查某玩家对指定伪装的权限 | `/ld permtest Steve` |
| `/ld debug` | 开启调试输出（排查伪装不显示） | `/ld debug` |
| `/ld json` | 导出伪装 JSON 供排查 | `/ld json` |
| `/ld update` | 检查插件更新 | `/ld update` |
| `/ld uploadlogs` | 上传日志生成排查链接 | `/ld uploadlogs` |

## 注意事项

::: warning
- disguiseradius 会把范围内的玩家也一起改，线上整活前先确认没别人在旁边。
- 伪装需要客户端接受实体元数据，配合 ProtocolLib/新版服务端时出问题优先 /ld reload 再看 debug。
- 玩家伪装成生物后碰撞箱与受击判定仍按原玩家，别用伪装做「隐藏玩家」的安全手段。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `libsdisguises.admin` | 管理指令（reload / config / debug） | — |
| `libsdisguises.config` | 允许玩家检查Lib的伪装配置的值 | — |
| `libsdisguises.count` | 允许用户查看有多少伪装处于活动状态 | — |
| `libsdisguises.debug` | 允许服务器管理员测试玩家伪装在计分板上是否正常 | — |
| `libsdisguises.disguise` | 使用 /disguise | — |
| `libsdisguises.disguise.<类型>` | 允许伪装成某个具体生物类型 | — |
| `libsdisguises.disguise.player` | 把自己伪装成玩家（带皮肤） | — |
| `libsdisguises.disguiseanimation` | 在您自己的伪装上播放受支持的动画 | op |
| `libsdisguises.disguiseentityanimation` | 在右键单击的实体的伪装上播放支持的动画 | op |
| `libsdisguises.disguiseplayer` | 使用 /disguiseplayer | — |
| `libsdisguises.disguiseplayeranimation` | 在玩家/UUID的伪装上播放支持的动画 | op |
| `libsdisguises.disguiseradius` | 使用 /disguiseradius | — |
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
