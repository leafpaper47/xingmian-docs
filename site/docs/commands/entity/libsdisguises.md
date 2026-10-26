---
title: LibsDisguises
createTime: 2026/10/24
---

# 伪装 · LibsDisguises

> 分类 🧟 生物与展示 · 版本 `26.9.26-SNAPSHOT` · 指令 28 条 · api-version `1.13`

::: tip 把玩家和实体伪装成其他生物、玩家或物品
LibsDisguises 是服务端最常用的伪装插件，能让玩家或实体在别人眼里变成另一种生物、另一名玩家、甚至一顶帽子或物品。它的命令按「对象范围」成对设计：自己（disguise）、某个玩家（disguiseplayer）、右键的实体（disguiseentity）、半径内所有实体（disguiseradius）、实体选择器（disguiseselector），撤销命令也一一对应。伪装本身不落盘，重启就没了，想长期保留要用 savedisguise 写进 disguises.yml。所有命令默认只对装了对应权限的管理员开放，给玩家开权限前先想清楚会不会被用来刷怪、卡视角或冒充他人。
:::

## 什么时候会用到它

- 活动、愚人节、彩蛋玩法里给玩家变身成别的生物，做趣味玩点
- 拍剧情、录宣传片时快速把实体或玩家换成指定外观
- 给赞助玩家开放变身权限，做成付费或兑换类玩点
- 巡查、观察玩家时把自己或周围实体伪装起来，避免被打扰

## 上手流程

1. 先确认服务端依赖齐全（LibsDisguises 需要 ProtocolLib 这类底层库），启动后用 /disguisehelp 看命令清单
2. 自己试效果：/disguise 实体类型，变形后用 /disguisemodify 改名字、装备、大小等选项
3. 对别人用 /disguiseplayer 玩家名 实体类型；对已有实体先执行 /disguiseentity 再右键点它
4. 批量场景用 /disguiseradius 半径 实体类型 或 /disguiseselector 选择器 实体类型
5. 想长期保留就用 /savedisguise 名称 伪装内容 写进 disguises.yml，之后直接按名字套用
6. 撤销：自己对 /undisguise，实体用 /undisguiseentity 右键，批量用 /undisguiseradius 或 /undisguiseselector

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/copydisguise` | 把当前伪装导出成可复制的字符串<br>别名 `/disguisecopy`、`/disgcopy`、`/dcopy`、`/copydisg`、`/copyd`、`/parsedisguise`、`/disguiseparse` | `/copydisguise` | `libsdisguises.seecmd.copydisguise` |
| `/disguise` | 把自己伪装成指定实体<br>别名 `/d`、`/dis`、`/disg` | `/disguise 实体类型 [更多参数]` | `libsdisguises.seecmd.disguise` |
| `/disguiseanimation` | 在自己的伪装上播放支持的动画 | `/disguiseanimation 动画名` | `libsdisguises.disguiseanimation` |
| `/disguiseclone` | 把伪装或实体存成模板，之后读出来复用<br>别名 `/disguisec`、`/disc`、`/disclone`、`/dclone`、`/clonedisguise`、`/clonedis`、`/cdisguise`、`/cdis`、`/clonedisg`、`/disgclone` | `/disguiseclone save或load 模板名` | `libsdisguises.seecmd.disguiseclone` |
| `/disguiseentity` | 把右键点到的实体伪装成别的实体<br>别名 `/dentity`、`/disentity`、`/disgentity` | `/disguiseentity 实体类型 [更多参数]` | `libsdisguises.seecmd.disguiseentity` |
| `/disguiseentityanimation` | 对右键点到的实体伪装播放动画 | `/disguiseentityanimation 动画名` | `libsdisguises.disguiseentityanimation` |
| `/disguisehelp` | 查看 LibsDisguises 全部命令与用法<br>别名 `/dhelp`、`/dishelp`、`/disghelp` | `/disguisehelp [页码]` | `libsdisguises.seecmd.disguisehelp` |
| `/disguisemodify` | 修改自己伪装的名字、装备、大小等选项<br>别名 `/dmodify`、`/dmod`、`/disgmodify`、`/modifydisguise`、`/moddisguise`、`/mdisguise` | `/disguisemodify 选项 [值]` | `libsdisguises.seecmd.disguisemodify` |
| `/disguisemodifyentity` | 右键修改某个实体的伪装选项<br>别名 `/dmodifyentity`、`/dmodentity`、`/disgmodentity`、`/dismodentity`、`/modifydisguiseentity`、`/modifydisgentity`、`/modifydentity`、`/moddisguiseentity`、`/moddisgentity`、`/mdisguiseentity`、`/mdisgentity` | `/disguisemodifyentity 选项 [值]` | `libsdisguises.seecmd.disguisemodifyentity` |
| `/disguisemodifyplayer` | 修改指定玩家的伪装选项<br>别名 `/dmodifyplayer`、`/dmodplayer`、`/disgmodifyplayer`、`/dismodplayer`、`/disgmodplayer`、`/modifydisguiseplayer`、`/moddisguiseplayer`、`/mdisguiseplayer`、`/mdisgplayer`、`/dmodifyuuid`、`/dmoduuid`、`/disgmodifyuuid`、`/dismoduuid`、`/disgmoduuid`、`/modifydisguiseuuid`、`/moddisguiseuuid`、`/mdisguiseuuid`、`/mdisguuid` | `/disguisemodifyplayer 玩家名 选项 [值]` | `libsdisguises.seecmd.disguisemodifyplayer` |
| `/disguisemodifyradius` | 批量修改半径内所有伪装的选项<br>别名 `/dmodifyradius`、`/dmodradius`、`/disgmodradius`、`/dismodradius`、`/modifydisguiseradius`、`/modifydisgradius`、`/moddisguiseradius`、`/mdisguiseradius`、`/moddisgradius` | `/disguisemodifyradius 半径 选项 [值]` | `libsdisguises.seecmd.disguisemodifyradius` |
| `/disguisemodifyselector` | 用实体选择器批量修改伪装选项<br>别名 `/dmodifyselector`、`/dmodselector`、`/disgmodselector`、`/dismodselector`、`/modifydisguiseselector`、`/modifydisgselector`、`/moddisguiseselector`、`/mdisguiseselector`、`/moddisgselector` | `/disguisemodifyselector 选择器 选项 [值]` | `libsdisguises.seecmd.disguisemodifyselector` |
| `/disguiseplayer` | 把指定玩家伪装成某个实体<br>别名 `/dplayer`、`/displayer`、`/disgplayer`、`/disguiseuuid`、`/disguuid`、`/duuid` | `/disguiseplayer 玩家名 实体类型 [更多参数]` | `libsdisguises.seecmd.disguiseplayer` |
| `/disguiseplayeranimation` | 在指定玩家的伪装上播放支持动画<br>别名 `/disguiseuuidanimation` | `/disguiseplayeranimation 玩家名 动画名` | `libsdisguises.disguiseplayeranimation` |
| `/disguiseradius` | 把半径内所有实体伪装成某实体<br>别名 `/disradius`、`/dradius`、`/disgradius` | `/disguiseradius 半径 实体类型 [更多参数]` | `libsdisguises.seecmd.disguiseradius` |
| `/disguiseradiusanimation` | 在半径内所有支持的伪装上播放动画 | `/disguiseradiusanimation 半径 动画名` | `libsdisguises.disguiseradiusanimation` |
| `/disguiseselector` | 用实体选择器批量伪装实体<br>别名 `/dselector`、`/disselector`、`/disgselector` | `/disguiseselector 选择器 实体类型 [更多参数]` | `libsdisguises.seecmd.disguiseselector` |
| `/disguiseselectoranimation` | 用选择器给所有支持的伪装播放动画 | `/disguiseselectoranimation 选择器 动画名` | `libsdisguises.disguiseselectoranimation` |
| `/disguiseviewbar` | 开关自己伪装信息在提示栏的显示<br>别名 `/dviewbar`、`/dvb`、`/disguisevb`、`/disvb`、`/viewdisguisebar`、`/viewbardisguise`、`/bardisguise`、`/bardisg`、`/bard`、`/notifybar`、`/viewnotifybar`、`/disguisenotifybar`、`/disgnotifybar`、`/dnotifybar` | `/disguiseviewbar` | `libsdisguises.seecmd.disguiseviewbar` |
| `/grabhead` | 按玩家名或皮肤网址抓一个头颅物品<br>别名 `/grabskull`、`/playerhead`、`/savehead`、`/gethead` | `/grabhead 玩家名或网址` | `libsdisguises.seecmd.grabhead` |
| `/grabskin` | 从玩家名、网址或文件抓取皮肤<br>别名 `/uploadskin`、`/skin`、`/saveskin`、`/cacheskin`、`/downloadskin`、`/skincache` | `/grabskin 玩家名或网址或文件` | `libsdisguises.seecmd.grabskin` |
| `/libsdisguises` | 插件主命令，重载配置、看伪装数量等<br>别名 `/libsdisg`、`/ld` | `/libsdisguises reload` | — |
| `/savedisguise` | 把自定义伪装保存进 disguises.yml<br>别名 `/customdisguise`、`/savedisg`、`/customdisg`、`/createdisguise`、`/createdisg` | `/savedisguise 名称 伪装内容` | `libsdisguises.seecmd.savedisguise` |
| `/undisguise` | 取消自己的伪装<br>别名 `/und`、`/undis`、`/undisg` | `/undisguise` | `libsdisguises.seecmd.undisguise` |
| `/undisguiseentity` | 取消右键实体的伪装<br>别名 `/undisentity`、`/undentity`、`/undisgentity` | `/undisguiseentity` | `libsdisguises.seecmd.undisguiseentity` |
| `/undisguiseplayer` | 取消指定玩家的伪装<br>别名 `/undisplayer`、`/undplayer`、`/undisgplayer`、`/undisguiseuuid`、`/unduuid`、`/undisguuid` | `/undisguiseplayer 玩家名` | `libsdisguises.seecmd.undisguiseplayer` |
| `/undisguiseradius` | 取消半径内所有实体的伪装<br>别名 `/undisradius`、`/undradius`、`/undisgradius` | `/undisguiseradius 半径` | `libsdisguises.seecmd.undisguiseradius` |
| `/undisguiseselector` | 用选择器批量取消实体伪装<br>别名 `/undisselector`、`/undselector`、`/undisgselector` | `/undisguiseselector 选择器` | `libsdisguises.seecmd.undisguiseselector` |

## 指令详解

### `/copydisguise` — 把当前伪装导出成可复制的字符串

- **语法**：`/copydisguise`

- **示例**：

```
/copydisguise
```

- **别名**：`/disguisecopy`、`/disgcopy`、`/dcopy`、`/copydisg`、`/copyd`、`/parsedisguise`、`/disguiseparse`
- **权限**：`libsdisguises.seecmd.copydisguise`
- **备注**：拿到的字符串可以直接粘到别的命令或配置文件里复用；别名 parsedisguise、disguisecopy 等。

### `/disguise` — 把自己伪装成指定实体

- **语法**：`/disguise 实体类型 [更多参数]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `实体类型` | 必填 | 如 zombie、creeper、player、item 等，TAB 可补全；player 类还要再跟玩家名 |


- **示例**：

```
/disguise zombie
```

- **别名**：`/d`、`/dis`、`/disg`
- **权限**：`libsdisguises.seecmd.disguise`
- **备注**：最常用的入口命令，别名 /d。连着猛刷会被 500ms 速率限制挡住，防止刷崩服务端。

### `/disguiseanimation` — 在自己的伪装上播放支持的动画

- **语法**：`/disguiseanimation 动画名`

- **示例**：

```
/disguiseanimation swing_mainhand
```

- **权限**：`libsdisguises.disguiseanimation`
- **备注**：只有部分伪装支持动画；可用动画名以 TAB 补全为准，需要 libsdisguises.disguiseanimation 权限。

### `/disguiseclone` — 把伪装或实体存成模板，之后读出来复用

- **语法**：`/disguiseclone save或load 模板名`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `save/load` | 必填 | save 保存当前或右键实体的伪装，load 读回该模板 |
| `模板名` | 必填 | 自己起的名字，方便反复调用 |


- **示例**：

```
/disguiseclone save 主城守卫
```

- **别名**：`/disguisec`、`/disc`、`/disclone`、`/dclone`、`/clonedisguise`、`/clonedis`、`/cdisguise`、`/cdis`、`/clonedisg`、`/disgclone`
- **权限**：`libsdisguises.seecmd.disguiseclone`
- **备注**：保存时按提示右键目标实体；适合同一套复杂伪装要重复在很多实体上用的场景。

### `/disguiseentity` — 把右键点到的实体伪装成别的实体

- **语法**：`/disguiseentity 实体类型 [更多参数]`

- **示例**：

```
/disguiseentity zombie
```

- **别名**：`/dentity`、`/disentity`、`/disgentity`
- **权限**：`libsdisguises.seecmd.disguiseentity`
- **备注**：执行命令后再右键目标实体生效；想改已伪装的实体用 disguisemodifyentity。

### `/disguiseentityanimation` — 对右键点到的实体伪装播放动画

- **语法**：`/disguiseentityanimation 动画名`

- **示例**：

```
/disguiseentityanimation swing_mainhand
```

- **权限**：`libsdisguises.disguiseentityanimation`
- **备注**：需要 libsdisguises.disguiseentityanimation 权限，动画名以 TAB 补全为准。

### `/disguisehelp` — 查看 LibsDisguises 全部命令与用法

- **语法**：`/disguisehelp [页码]`

- **示例**：

```
/disguisehelp
```

- **别名**：`/dhelp`、`/dishelp`、`/disghelp`
- **权限**：`libsdisguises.seecmd.disguisehelp`
- **备注**：命令多，第一次接手先用它加 TAB 补全摸清语法，比翻文档快。

### `/disguisemodify` — 修改自己伪装的名字、装备、大小等选项

- **语法**：`/disguisemodify 选项 [值]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `选项` | 必填 | 如 name、setSkin、size、addride、glow 等，TAB 可补全 |
| `值` | 可选 | 部分选项需要填值，不填则按提示操作 |


- **示例**：

```
/disguisemodify name 神秘商人
```

- **别名**：`/dmodify`、`/dmod`、`/disgmodify`、`/modifydisguise`、`/moddisguise`、`/mdisguise`
- **权限**：`libsdisguises.seecmd.disguisemodify`
- **备注**：改名字、换皮、加骑乘、调大小基本都在这；还有 disguisemodifyplayer / radius / selector / entity 四个对应不同对象范围。

### `/disguisemodifyentity` — 右键修改某个实体的伪装选项

- **语法**：`/disguisemodifyentity 选项 [值]`

- **示例**：

```
/disguisemodifyentity name 宝箱怪
```

- **别名**：`/dmodifyentity`、`/dmodentity`、`/disgmodentity`、`/dismodentity`、`/modifydisguiseentity`、`/modifydisgentity`、`/modifydentity`、`/moddisguiseentity`、`/moddisgentity`、`/mdisguiseentity`、`/mdisgentity`
- **权限**：`libsdisguises.seecmd.disguisemodifyentity`
- **备注**：执行后右键目标实体生效；别名很多，如 dmodentity。

### `/disguisemodifyplayer` — 修改指定玩家的伪装选项

- **语法**：`/disguisemodifyplayer 玩家名 选项 [值]`

- **示例**：

```
/disguisemodifyplayer Steve name 老板
```

- **别名**：`/dmodifyplayer`、`/dmodplayer`、`/disgmodifyplayer`、`/dismodplayer`、`/disgmodplayer`、`/modifydisguiseplayer`、`/moddisguiseplayer`、`/mdisguiseplayer`、`/mdisgplayer`、`/dmodifyuuid`、`/dmoduuid`、`/disgmodifyuuid`、`/dismoduuid`、`/disgmoduuid`、`/modifydisguiseuuid`、`/moddisguiseuuid`、`/mdisguiseuuid`、`/mdisguuid`
- **权限**：`libsdisguises.seecmd.disguisemodifyplayer`
- **备注**：也支持用 UUID 指定玩家；改别人的伪装前最好先私聊说一声，避免被当成恶作剧。

### `/disguisemodifyradius` — 批量修改半径内所有伪装的选项

- **语法**：`/disguisemodifyradius 半径 选项 [值]`

- **示例**：

```
/disguisemodifyradius 10 glow
```

- **别名**：`/dmodifyradius`、`/dmodradius`、`/disgmodradius`、`/dismodradius`、`/modifydisguiseradius`、`/modifydisgradius`、`/moddisguiseradius`、`/mdisguiseradius`、`/moddisgradius`
- **权限**：`libsdisguises.seecmd.disguisemodifyradius`
- **备注**：只影响已有伪装的实体，不会凭空给没伪装的实体上伪装。

### `/disguisemodifyselector` — 用实体选择器批量修改伪装选项

- **语法**：`/disguisemodifyselector 选择器 选项 [值]`

- **示例**：

```
/disguisemodifyselector @e[type=zombie] name 僵尸哨兵
```

- **别名**：`/dmodifyselector`、`/dmodselector`、`/disgmodselector`、`/dismodselector`、`/modifydisguiseselector`、`/modifydisgselector`、`/moddisguiseselector`、`/mdisguiseselector`、`/moddisgselector`
- **权限**：`libsdisguises.seecmd.disguisemodifyselector`
- **备注**：选择器写法同原版 @e 语法；范围写大了容易一次改一片，先在小范围试。

### `/disguiseplayer` — 把指定玩家伪装成某个实体

- **语法**：`/disguiseplayer 玩家名 实体类型 [更多参数]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `玩家名` | 必填 | 在线玩家名或 UUID |
| `实体类型` | 必填 | 要伪装成的目标，TAB 可补全 |


- **示例**：

```
/disguiseplayer Steve zombie
```

- **别名**：`/dplayer`、`/displayer`、`/disgplayer`、`/disguiseuuid`、`/disguuid`、`/duuid`
- **权限**：`libsdisguises.seecmd.disguiseplayer`
- **备注**：别名 disguiseuuid、dplayer；把别人变成生物后，对方视角和碰撞体积可能跟着变，注意别让人卡墙里。

### `/disguiseplayeranimation` — 在指定玩家的伪装上播放支持动画

- **语法**：`/disguiseplayeranimation 玩家名 动画名`

- **示例**：

```
/disguiseplayeranimation Steve swing_mainhand
```

- **别名**：`/disguiseuuidanimation`
- **权限**：`libsdisguises.disguiseplayeranimation`
- **备注**：也支持用 UUID 指定；需要 libsdisguises.disguiseplayeranimation 权限。

### `/disguiseradius` — 把半径内所有实体伪装成某实体

- **语法**：`/disguiseradius 半径 实体类型 [更多参数]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `半径` | 必填 | 以自己为中心的方块距离 |
| `实体类型` | 必填 | 要伪装成的目标，TAB 可补全 |


- **示例**：

```
/disguiseradius 10 zombie
```

- **别名**：`/disradius`、`/dradius`、`/disgradius`
- **权限**：`libsdisguises.seecmd.disguiseradius`
- **备注**：会把范围内的玩家和生物一起变，慎用；撤销要配 /undisguiseradius 同半径。

### `/disguiseradiusanimation` — 在半径内所有支持的伪装上播放动画

- **语法**：`/disguiseradiusanimation 半径 动画名`

- **示例**：

```
/disguiseradiusanimation 10 swing_mainhand
```

- **权限**：`libsdisguises.disguiseradiusanimation`
- **备注**：只对支持该动画的伪装生效，其余会被跳过。

### `/disguiseselector` — 用实体选择器批量伪装实体

- **语法**：`/disguiseselector 选择器 实体类型 [更多参数]`

- **示例**：

```
/disguiseselector @e[type=zombie,limit=5] skeleton
```

- **别名**：`/dselector`、`/disselector`、`/disgselector`
- **权限**：`libsdisguises.seecmd.disguiseselector`
- **备注**：适合给成批刷出来的怪统一换外观；选择器写错会报语法错误，先用 @e[limit=1] 试。

### `/disguiseselectoranimation` — 用选择器给所有支持的伪装播放动画

- **语法**：`/disguiseselectoranimation 选择器 动画名`

- **示例**：

```
/disguiseselectoranimation @e[type=zombie] swing_mainhand
```

- **权限**：`libsdisguises.disguiseselectoranimation`
- **备注**：动画名以 TAB 补全为准；一次影响整批实体，建议先限定 limit。

### `/disguiseviewbar` — 开关自己伪装信息在提示栏的显示

- **语法**：`/disguiseviewbar`

- **示例**：

```
/disguiseviewbar
```

- **别名**：`/dviewbar`、`/dvb`、`/disguisevb`、`/disvb`、`/viewdisguisebar`、`/viewbardisguise`、`/bardisguise`、`/bardisg`、`/bard`、`/notifybar`、`/viewnotifybar`、`/disguisenotifybar`、`/disgnotifybar`、`/dnotifybar`
- **权限**：`libsdisguises.seecmd.disguiseviewbar`
- **备注**：别名 /dvb；如果玩家嫌操作栏一直跳自己的伪装信息，可用 libsdisguises.noactionbar 整服关掉。

### `/grabhead` — 按玩家名或皮肤网址抓一个头颅物品

- **语法**：`/grabhead 玩家名或网址`

- **示例**：

```
/grabhead Steve
```

- **别名**：`/grabskull`、`/playerhead`、`/savehead`、`/gethead`
- **权限**：`libsdisguises.seecmd.grabhead`
- **备注**：拿到的是手里/地上的头颅物品，可做装饰或活动道具；需要 libsdisguises.grabhead 权限。

### `/grabskin` — 从玩家名、网址或文件抓取皮肤

- **语法**：`/grabskin 玩家名或网址或文件`

- **示例**：

```
/grabskin Steve
```

- **别名**：`/uploadskin`、`/skin`、`/saveskin`、`/cacheskin`、`/downloadskin`、`/skincache`
- **权限**：`libsdisguises.seecmd.grabskin`
- **备注**：别名 /skin；抓到的皮肤会进缓存，之后可在伪装里按名字引用。

### `/libsdisguises` — 插件主命令，重载配置、看伪装数量等

- **语法**：`/libsdisguises reload`

- **示例**：

```
/libsdisguises reload
```

- **别名**：`/libsdisg`、`/ld`
- **备注**：别名 /ld；改完配置用 reload，已经在身上的伪装一般不会自动刷新，需要重新伪装一次。

### `/savedisguise` — 把自定义伪装保存进 disguises.yml

- **语法**：`/savedisguise 名称 伪装内容`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `名称` | 必填 | 保存后的伪装名，之后直接用这个名字套用 |
| `伪装内容` | 必填 | 伪装参数串，可从 /copydisguise 得到的字符串改写 |


- **示例**：

```
/savedisguise 宝箱怪 item minecraft:chest
```

- **别名**：`/customdisguise`、`/savedisg`、`/customdisg`、`/createdisguise`、`/createdisg`
- **权限**：`libsdisguises.seecmd.savedisguise`
- **备注**：配置里配好权限与冷却后，可把某些伪装只开放给特定权限组，做付费变身。

### `/undisguise` — 取消自己的伪装

- **语法**：`/undisguise`

- **示例**：

```
/undisguise
```

- **别名**：`/und`、`/undis`、`/undisg`
- **权限**：`libsdisguises.seecmd.undisguise`
- **备注**：别名 /und；取消后碰撞箱和视角恢复正常，卡在方块里时先取消伪装再挪位置。

### `/undisguiseentity` — 取消右键实体的伪装

- **语法**：`/undisguiseentity`

- **示例**：

```
/undisguiseentity
```

- **别名**：`/undisentity`、`/undentity`、`/undisgentity`
- **权限**：`libsdisguises.seecmd.undisguiseentity`
- **备注**：执行后右键目标实体；对没伪装过的实体使用不会有反应。

### `/undisguiseplayer` — 取消指定玩家的伪装

- **语法**：`/undisguiseplayer 玩家名`

- **示例**：

```
/undisguiseplayer Steve
```

- **别名**：`/undisplayer`、`/undplayer`、`/undisgplayer`、`/undisguiseuuid`、`/unduuid`、`/undisguuid`
- **权限**：`libsdisguises.seecmd.undisguiseplayer`
- **备注**：也支持 UUID；玩家下线后再上线，此前的伪装通常已失效。

### `/undisguiseradius` — 取消半径内所有实体的伪装

- **语法**：`/undisguiseradius 半径`

- **示例**：

```
/undisguiseradius 10
```

- **别名**：`/undisradius`、`/undradius`、`/undisgradius`
- **权限**：`libsdisguises.seecmd.undisguiseradius`
- **备注**：收尾清理最省事；半径填得比当初伪装的半径更大才清得干净。

### `/undisguiseselector` — 用选择器批量取消实体伪装

- **语法**：`/undisguiseselector 选择器`

- **示例**：

```
/undisguiseselector @e[type=zombie]
```

- **别名**：`/undisselector`、`/undselector`、`/undisgselector`
- **权限**：`libsdisguises.seecmd.undisguiseselector`
- **备注**：适合精确清理某一类实体；写 @e 不带条件会清掉范围内全部实体伪装。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `reload` | 重载 LibsDisguises 配置文件与 disguises.yml | `/libsdisguises reload` |
| `help` | 列出主命令的可用子命令 | `/libsdisguises help` |

## 注意事项

::: warning
- 伪装不落盘：服务器重启或区块卸载后通常就没了，需要固定外观就用 savedisguise 存进 disguises.yml，或用 clone 模板重新套用
- 伪装命令有 500ms 速率限制防刷崩，连点会被拒绝；只有持 libsdisguises.ratelimitbypass 的玩家能绕过
- libsdisguises.seecmd 只控制 TAB 补全里是否看得到命令，默认就是 true，真正能执行还要给对应节点的权限，别以为开了 seecmd 就等于给了权限
- 把玩家伪装成体积不同的生物可能出现卡方块、进不去门、看不到自己等情况；出问题先 /undisguise 复原，再做调整
:::

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

## 相关插件

ProtocolLib、[PlaceholderAPI](/commands/config/placeholderapi.md)、Citizens
