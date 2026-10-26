---
title: GSit
createTime: 2026/10/24
---

# 坐下趴下 · GSit

> 分类 🎲 小游戏与娱乐 · 版本 `3.5.1` · 指令 7 条 · api-version `1.16`

::: tip 让玩家坐下、躺下、爬行与旋转的姿势插件
GSit 给玩家提供坐下、躺下、仰躺、趴地、爬行、原地旋转等一系列姿势动作，常用于大厅、酒馆、影院等服务区的氛围装饰。玩家除了用指令外，还可以直接右键点击台阶、楼梯、半砖等方块自动就坐，右键其他玩家则可坐到对方身上。所有姿势都能被配置文件按世界、区域、权限逐项开关，管理员可以用重载指令在线改完立即生效。
:::

## 什么时候会用到它

- 给主城、酒馆、影院等休息区做坐姿、躺姿的氛围演出
- 允许玩家两两互动：一人右键另一人，坐到对方身上
- 做活动或拍照场景时让玩家躺成一排、趴地摆造型
- 用爬行姿势做小游戏、潜行逃脱类玩法
- 用旋转姿势在展示台、舞台中心做展示动作

## 上手流程

1. 确认插件已加载，并在配置文件里打开需要启用的姿势与允许使用的世界、区域
2. 按需给玩家组下发对应权限节点，例如 GSit.Sit、GSit.Lay、GSit.Spin
3. 玩家在游戏内输入 /gsit、/glay 等指令，或直接右键台阶类方块、右键其他玩家触发姿势
4. 改完配置后执行 /gsitreload 让设置立即生效，不必重启服务器
5. 用 GSit.Kick.Sit 与 GSit.Kick.Pose 处理被卡在座位上或姿势异常的玩家

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/gbellyflop` | 让玩家趴下做出腹部先着地的扑街姿势<br>别名 `/bellyflop` | `/gbellyflop` | `GSit.Bellyflop` |
| `/gcrawl` | 进入或退出爬行姿态<br>别名 `/crawl` | `/gcrawl [toggle]` | — |
| `/glay` | 让玩家平平躺下<br>别名 `/lay` | `/glay` | `GSit.Lay` |
| `/glayback` | 让玩家以躺靠姿势仰躺<br>别名 `/layback` | `/glayback` | `GSit.LayBack` |
| `/gsit` | 让玩家就地坐下，或切换坐姿相关开关<br>别名 `/sit` | `/gsit [toggle｜playertoggle]` | — |
| `/gsitreload` | 重新加载 GSit 的配置文件<br>别名 `/gsitrl` | `/gsitreload` | `GSit.Reload` |
| `/gspin` | 让玩家原地旋转展示<br>别名 `/spin` | `/gspin` | `GSit.Spin` |

## 指令详解

### `/gbellyflop` — 让玩家趴下做出腹部先着地的扑街姿势

- **语法**：`/gbellyflop`

- **示例**：

```
/gbellyflop
```

- **别名**：`/bellyflop`
- **权限**：`GSit.Bellyflop`
- **备注**：别名为 /bellyflop，需要权限 GSit.BellyFlop（默认对所有玩家开放）。属于姿势类动作，同样受配置里的世界与区域开关限制。

### `/gcrawl` — 进入或退出爬行姿态

- **语法**：`/gcrawl [toggle]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `toggle` | 可选 | 可选参数，用于切换爬行能力的开关状态，省略时直接进入或退出爬行 |


- **示例**：

```
/gcrawl
/gcrawl toggle
```

- **别名**：`/crawl`
- **备注**：别名为 /crawl，基础权限 GSit.Crawl；切换开关需要 GSit.CrawlToggle，潜行触发爬行需要 GSit.CrawlSneak。爬行会改变碰撞箱高度，狭窄处进出要小心。

### `/glay` — 让玩家平平躺下

- **语法**：`/glay`

- **示例**：

```
/glay
```

- **别名**：`/lay`
- **权限**：`GSit.Lay`
- **备注**：别名为 /lay，需要权限 GSit.Lay。再执行一次或移动、跳跃即可起身。

### `/glayback` — 让玩家以躺靠姿势仰躺

- **语法**：`/glayback`

- **示例**：

```
/glayback
```

- **别名**：`/layback`
- **权限**：`GSit.LayBack`
- **备注**：别名为 /layback，需要权限 GSit.LayBack，是 glay 之外的另一种躺姿，适合沙发、躺椅一类场景。

### `/gsit` — 让玩家就地坐下，或切换坐姿相关开关

- **语法**：`/gsit [toggle｜playertoggle]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `toggle` | 可选 | 切换本人是否允许被右键坐上以及坐姿相关功能，需要权限 GSit.SitToggle |
| `playertoggle` | 可选 | 切换本人是否允许其他玩家右键坐到自己身上，需要权限 GSit.PlayerSitToggle |


- **示例**：

```
/gsit
/gsit toggle
/gsit playertoggle
```

- **别名**：`/sit`
- **备注**：别名为 /sit，基础权限 GSit.Sit。右键台阶、楼梯、半砖等方块自动就坐受 GSit.SitClick 控制，右键其他玩家坐到对方身上受 GSit.PlayerSit 控制。

### `/gsitreload` — 重新加载 GSit 的配置文件

- **语法**：`/gsitreload`

- **示例**：

```
/gsitreload
```

- **别名**：`/gsitrl`
- **权限**：`GSit.Reload`
- **备注**：别名为 /gsitrl，需要权限 GSit.Reload，默认仅管理员可用。改完姿势开关、世界或区域限制后用它在线生效。

### `/gspin` — 让玩家原地旋转展示

- **语法**：`/gspin`

- **示例**：

```
/gspin
```

- **别名**：`/spin`
- **权限**：`GSit.Spin`
- **备注**：别名为 /spin，需要权限 GSit.Spin。旋转速度与是否允许在服务器里使用都由配置决定。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `gsit toggle` | 切换自己是否允许被右键坐上（坐姿功能开关） | `/gsit toggle` |
| `gsit playertoggle` | 切换自己是否允许其他玩家右键坐到自己身上 | `/gsit playertoggle` |
| `gcrawl toggle` | 切换爬行功能开关，关闭后即使有权限也无法进入爬行姿态 | `/gcrawl toggle` |

## 注意事项

::: warning
- 玩家坐在座位上时会被固定住，若地形被改动或区域重置，可能卡在半空，管理员可用 GSit.Kick.Sit 权限把玩家从座位上踢下来
- GSit.ByPass.World 与 GSit.ByPass.Region 会让玩家无视世界、区域的禁用限制使用姿势，只应给管理层
- 爬行会改变碰撞箱高度，在低矮通道或基岩附近反复切换有卡进方块的风险，出问题用 GSit.Kick.Pose 处理
- 玩家坐姿、躺姿状态有时会被其他插件的传送、重生、旁观切换影响而残留，重启或重新触发姿势通常可恢复
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `GSit.*` | GSit \|权限 | op |
| `GSit.BellyFlop` | BellyFlop命令\|权限 | True |
| `GSit.ByPass.*` | ByPass \|权限 | op |
| `GSit.ByPass.Command` | ByPass命令\|权限 | op |
| `GSit.ByPass.Region` | ByPass区域\|权限 | op |
| `GSit.ByPass.World` | ByPass WORLD \|权限 | op |
| `GSit.Crawl` | 爬网命令\|权限 | True |
| `GSit.Crawl.*` | 爬网\|权限 | op |
| `GSit.CrawlSneak` | 潜行\|权限 | True |
| `GSit.CrawlToggle` | 切换爬网能力\|权限 | True |
| `GSit.Kick.*` | 踢出\|权限 | op |
| `GSit.Kick.Pose` | 踢腿姿势\|权限 | op |
| `GSit.Kick.Sit` | Kick SIT \|权限 | op |
| `GSit.Lay` | Lay命令\|权限 | True |
| `GSit.LayBack` | LayBack命令\|权限 | True |
| `GSit.PlayerSit` | PlayerSit单击\|权限 | True |
| `GSit.PlayerSit.*` | PlayerSit \|权限 | op |
| `GSit.PlayerSitToggle` | 切换PlayerSit能力\|权限 | True |
| `GSit.Pose.*` | 姿势\|权限 | op |
| `GSit.Reload` | 插件重新加载命令\|权限 | op |
| `GSit.Sit` | SIT命令\|权限 | True |
| `GSit.Sit.*` | SIT \|权限 | op |
| `GSit.SitClick` | SIT单击\|权限 | True |
| `GSit.SitToggle` | 切换坐姿能力\|权限 | True |
| `GSit.Spin` | 旋转命令\|权限 | True |
| `GSit.Update` | 更新通知\|权限 | op |

## 相关插件

[OpenInv](/commands/essentials/openinv.md)、[Residence](/commands/protect/residence.md)、WorldGuard、[LuckPerms](/commands/core/luckperms.md)、[PlaceholderAPI](/commands/config/placeholderapi.md)
