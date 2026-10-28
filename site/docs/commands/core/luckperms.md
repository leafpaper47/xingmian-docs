---
title: LuckPerms
createTime: 2026/10/24
---

# 权限组 · LuckPerms

> 分类 🛡️ 权限与底座 · 版本 `5.5.53` · 指令 18 条 · api-version `1.13`

::: tip 权限与组管理
全服权限的总闸门：把权限节点挂在组或玩家身上，按继承链算出谁能用什么指令。其它插件只声明节点，发不发权限看它。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 给组开一条权限 | /lp group vip permission set essentials.fly true | 长期规则改组，别改个人 |
| 临时给一个玩家 | /lp user Steve permission settemp essentials.fly true 7d | 到期自动失效，不用手动收 |
| 把玩家加进组 | /lp user Steve parent add vip | 先用 /lp user Steve info 看现有组 |
| 查他到底有什么权限 | /lp user Steve permission check essentials.fly | 显示结果与来自哪个组，排查「明明给了还是不行」 |
| 批量改（推荐） | /lp editor | 网页里勾选保存，比逐条敲安全 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/luckperms` | 管理权限<br>别名 `/lp`、`/perm`、`/perms`、`/permission`、`/permissions` | — | — |
| `/lp user` | 对单个玩家操作：权限、组、前缀、元数据 | `/lp user <玩家> <子指令> [参数]` | — |
| `/lp group` | 对一个权限组操作：权限、继承、权重、成员 | `/lp group <组> <子指令> [参数]` | — |
| `/lp creategroup` | 新建一个权限组 | `/lp creategroup <组名>` | — |
| `/lp deletegroup` | 删除一个权限组 | `/lp deletegroup <组名>` | — |
| `/lp track` | 查看/编辑晋升轨道（vip→mvp 这种有序组链） | `/lp track <轨道名> <info｜group｜clear> [参数]` | — |
| `/lp log` | 查权限变更审计日志，或开关变更通知 | `/lp log <search｜recent｜user｜history｜notification> …` | — |
| `/lp info` | 显示 LuckPerms 版本、存储类型与同步状态 | `/lp info` | — |
| `/lp sync` | 强制从存储拉取一次最新数据 | `/lp sync` | — |
| `/lp verbose` | 实时打印权限判定过程，或检测某玩家某节点 | `/lp verbose <on｜off｜record｜paste｜check>` | — |
| `/lp editor` | 生成网页编辑器链接，批量改权限 | `/lp editor [玩家｜组]` | — |
| `/lp tree` | 树状查看某玩家或组的权限来源 | `/lp tree <玩家｜组>` | — |
| `/lp search` | 反查哪些玩家/组带着某条权限 | `/lp search <权限节点>` | — |
| `/lp bulkupdate` | 按规则批量增删权限（整组、整服） | `/lp bulkupdate <类型> <动作> [参数]` | — |
| `/lp applyedits` | 提交 bulkupdate 生成的批量改动 | `/lp applyedits` | — |
| `/lp reloadconfig` | 重载 LuckPerms 自身配置文件 | `/lp reloadconfig` | — |
| `/lp export` | 把全部权限数据导出成文件 | `/lp export <文件名>` | — |
| `/lp import` | 从导出文件导入权限数据 | `/lp import <文件名>` | — |

## 指令详解

### `/luckperms` — 管理权限

- **别名**：`/lp`、`/perm`、`/perms`、`/permission`、`/permissions`

### `/lp user` — 对单个玩家操作：权限、组、前缀、元数据

- **语法**：`/lp user <玩家> <子指令> [参数]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `玩家` | 必填 | 在线名或已入服的离线名 |


- **示例**：

```
/lp user Steve info
/lp user Steve permission set essentials.fly true
```

- **备注**：玩家名带中文或大小写不一致时会查不到，用 Tab 补全出的名字最稳

### `/lp group` — 对一个权限组操作：权限、继承、权重、成员

- **语法**：`/lp group <组> <子指令> [参数]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `组` | 必填 | 组必须已存在，用 /lp creategroup 新建 |


- **示例**：

```
/lp group vip info
/lp group vip permission set essentials.fly true
```

- **备注**：玩家可继承多个组，最终按权重与继承链合并，冲突时显式 false 优先

### `/lp creategroup` — 新建一个权限组

- **语法**：`/lp creategroup <组名>`

- **示例**：

```
/lp creategroup vip
```

- **备注**：建完是空的，不继承任何组，需自己加 parent 或节点

### `/lp deletegroup` — 删除一个权限组

- **语法**：`/lp deletegroup <组名>`

- **示例**：

```
/lp deletegroup tmpvip
```

- **备注**：组内玩家会掉组，先 /lp group tmpvip listmembers 核对

### `/lp track` — 查看/编辑晋升轨道（vip→mvp 这种有序组链）

- **语法**：`/lp track <轨道名> <info｜group｜clear> [参数]`

- **示例**：

```
/lp track staff group append mvp
```

- **备注**：轨道要先建好才能挂组；/lp user Steve promote staff 沿轨道升一级

### `/lp log` — 查权限变更审计日志，或开关变更通知

- **语法**：`/lp log <search｜recent｜user｜history｜notification> [参数]`

- **示例**：

```
/lp log search Steve
/lp log recent
```

- **备注**：误删权限、追查谁改了组，全靠这里；日志默认会定期清理

### `/lp info` — 显示 LuckPerms 版本、存储类型与同步状态

- **语法**：`/lp info`

- **示例**：

```
/lp info
```

- **备注**：存储显示 H2 说明还是本地库，多服必须换 MySQL 才能同步

### `/lp sync` — 强制从存储拉取一次最新数据

- **语法**：`/lp sync`

- **示例**：

```
/lp sync
```

- **备注**：多服环境改完权限别的子服没生效，先跑它再排查

### `/lp verbose` — 实时打印权限判定过程，或检测某玩家某节点

- **语法**：`/lp verbose <on｜off｜record｜paste｜check>`

- **示例**：

```
/lp verbose on
/lp verbose check Steve essentials.fly
```

- **备注**：开着时全服判定刷屏，排查完立刻 off；输出可 /lp verbose paste 上传成链接

### `/lp editor` — 生成网页编辑器链接，批量改权限

- **语法**：`/lp editor [玩家｜组]`

- **示例**：

```
/lp editor
/lp editor group vip
```

- **备注**：链接带权限、有时效，别外传；保存后自动应用才能生效

### `/lp tree` — 树状查看某玩家或组的权限来源

- **语法**：`/lp tree <玩家｜组>`

- **示例**：

```
/lp tree Steve
```

- **备注**：看某条权限是从哪个父组继承来的最直观

### `/lp search` — 反查哪些玩家/组带着某条权限

- **语法**：`/lp search <权限节点>`

- **示例**：

```
/lp search essentials.fly
```

- **备注**：清理废弃权限前先搜一遍，避免误删还在用的

### `/lp bulkupdate` — 按规则批量增删权限（整组、整服）

- **语法**：`/lp bulkupdate <类型> <动作> [参数]`

- **示例**：

```
/lp bulkupdate all update permission unset essentials.fly
```

- **备注**：先生成待执行改动，要再跑 /lp applyedits 才真正写入

### `/lp applyedits` — 提交 bulkupdate 生成的批量改动

- **语法**：`/lp applyedits`

- **示例**：

```
/lp applyedits
```

- **备注**：不跑这一步，bulkupdate 等于没做

### `/lp reloadconfig` — 重载 LuckPerms 自身配置文件

- **语法**：`/lp reloadconfig`

- **示例**：

```
/lp reloadconfig
```

- **备注**：只重载配置，不动权限数据；改存储方式要重启

### `/lp export` — 把全部权限数据导出成文件

- **语法**：`/lp export <文件名>`

- **示例**：

```
/lp export backup-2026
```

- **备注**：迁服、换库前的保命操作，导出的文件在插件目录里

### `/lp import` — 从导出文件导入权限数据

- **语法**：`/lp import <文件名>`

- **示例**：

```
/lp import backup-2026
```

- **备注**：会按文件内容覆盖现有数据，导入前先 export 一份当前状态

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/lp user <玩家> permission set` | 给玩家开/关一条权限 | `/lp user Steve permission set essentials.fly true` |
| `/lp user <玩家> permission unset` | 删掉玩家身上的这条权限，恢复继承 | `/lp user Steve permission unset essentials.fly` |
| `/lp user <玩家> permission settemp` | 限时授权，到期自动消失 | `/lp user Steve permission settemp essentials.fly true 7d` |
| `/lp user <玩家> parent add` | 把玩家加进组（继承该组全部权限） | `/lp user Steve parent add vip` |
| `/lp user <玩家> parent remove` | 把玩家从组里移除 | `/lp user Steve parent remove vip` |
| `/lp user <玩家> parent addtemp` | 限时进组 | `/lp user Steve parent addtemp vip 7d` |
| `/lp user <玩家> meta setprefix` | 设聊天前缀，第二个参数是权重 | `/lp user Steve meta setprefix 100 [VIP]` |
| `/lp user <玩家> promote` | 沿轨道升一级 | `/lp user Steve promote staff` |
| `/lp user <玩家> demote` | 沿轨道降一级 | `/lp user Steve demote staff` |
| `/lp user <玩家> switchprimarygroup` | 改主组（影响默认显示与前缀） | `/lp user Steve switchprimarygroup vip` |
| `/lp user <玩家> clear` | 清空该玩家的全部权限与组 | `/lp user Griefer clear` |
| `/lp group <组> permission set` | 给组开/关一条权限 | `/lp group vip permission set essentials.fly true` |
| `/lp group <组> parent add` | 让组继承另一个组 | `/lp group mvp parent add vip` |
| `/lp group <组> listmembers` | 列出组内玩家 | `/lp group vip listmembers` |
| `/lp group <组> setweight` | 调组权重，数字大的优先 | `/lp group mvp setweight 100` |
| `/lp track <轨道> group append` | 往轨道末尾加一个组 | `/lp track staff group append mvp` |
| `/lp verbose on` | 打开权限判定实时输出 | `/lp verbose on` |

## 注意事项

::: warning
- 收回权限用 unset，不要用 set false：false 是显式拒绝，会盖掉继承来的 true，事后很难看出来源。
- 5.5.x 起必须用完整形式 /lp group &lt;组&gt; permission set｜unset &lt;节点&gt;，简写 set/unset/setperm 会静默不报错也不生效。
- 多服改了权限某个子服不认，先 /lp sync；存储还在 H2 的话必须先迁 MySQL，否则永远同步不上。
- 改完一定用 /lp user &lt;玩家&gt; permission check &lt;节点&gt; 或 /lp verbose check 验证，别只看提示文字。
:::
