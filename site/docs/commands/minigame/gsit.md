---
title: GSit
createTime: 2026/10/24
---

# 坐下趴下 · GSit

> 分类 🎲 小游戏与娱乐 · 版本 `3.5.1` · 指令 7 条 · api-version `1.16`

::: tip 坐姿动作
让玩家坐、躺、趴、转圈、爬行的动作插件，右键台阶就能坐下，不用敲命令也能玩。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 坐下 | /sit | 右键台阶/楼梯也能坐，按 Shift 起身 |
| 躺下 | /lay | 床以外的地方也能躺 |
| 关掉右键自动坐 | /sit toggle | 个人开关，不影响别人 |
| 改完配置重载 | /gsitreload | 别名 /gsitrl |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/gbellyflop` | 肚皮朝下摔趴<br>别名 `/bellyflop` | `/gbellyflop` | `GSit.Bellyflop` |
| `/gcrawl` | 进入/退出爬行姿态<br>别名 `/crawl` | `/gcrawl [toggle]` | — |
| `/glay` | 躺下（仰卧）<br>别名 `/lay` | `/glay` | `GSit.Lay` |
| `/glayback` | 趴着躺（俯卧）<br>别名 `/layback` | `/glayback` | `GSit.LayBack` |
| `/gsit` | 坐下；带参数可坐下他人或切换开关<br>别名 `/sit` | `/gsit [toggle｜playertoggle｜玩家]` | — |
| `/gsitreload` | 重载 GSit 配置<br>别名 `/gsitrl` | `/gsitreload` | `GSit.Reload` |
| `/gspin` | 原地转圈<br>别名 `/spin` | `/gspin` | `GSit.Spin` |

## 指令详解

### `/gbellyflop` — 肚皮朝下摔趴

- **语法**：`/gbellyflop`

- **示例**：

```
/bellyflop
```

- **别名**：`/bellyflop`
- **权限**：`GSit.Bellyflop`

### `/gcrawl` — 进入/退出爬行姿态

- **语法**：`/gcrawl [toggle]`

- **示例**：

```
/crawl
```

- **别名**：`/crawl`
- **备注**：爬行时身高降到 0.6 格，可钻 1 格洞

### `/glay` — 躺下（仰卧）

- **语法**：`/glay`

- **示例**：

```
/lay
```

- **别名**：`/lay`
- **权限**：`GSit.Lay`

### `/glayback` — 趴着躺（俯卧）

- **语法**：`/glayback`

- **示例**：

```
/layback
```

- **别名**：`/layback`
- **权限**：`GSit.LayBack`

### `/gsit` — 坐下；带参数可坐下他人或切换开关

- **语法**：`/gsit [toggle｜playertoggle｜玩家]`

- **示例**：

```
/sit
/sit Steve
```

- **别名**：`/sit`
- **备注**：toggle 关自己右键自动坐；playertoggle 关掉别人坐你身上的能力

### `/gsitreload` — 重载 GSit 配置

- **语法**：`/gsitreload`

- **示例**：

```
/gsitreload
```

- **别名**：`/gsitrl`
- **权限**：`GSit.Reload`
- **备注**：别名 /gsitrl；改完 config 必须执行

### `/gspin` — 原地转圈

- **语法**：`/gspin`

- **示例**：

```
/spin
```

- **别名**：`/spin`
- **权限**：`GSit.Spin`
- **备注**：转圈期间视角被带动，别在跑图时用

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/sit toggle` | 关闭/开启自己右键自动就坐 | `/sit toggle` |
| `/sit playertoggle` | 允许/禁止其他玩家坐到你身上 | `/sit playertoggle` |
| `/sit <玩家>` | 把指定玩家按到座位上 | `/sit Steve` |

## 注意事项

::: warning
- 玩家「右键坐不下去」先查 GSit.Sit 与 GSit.SitClick 权限，再看自己是不是关了 toggle。
- 爬行与躺下会改碰撞箱，狭窄矿道里容易卡住。
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
| `GSit.Kick.Sit` | 允许把坐着的人踢起来 | op |
| `GSit.Lay` | Lay命令\|权限 | True |
| `GSit.LayBack` | LayBack命令\|权限 | True |
| `GSit.PlayerSit` | 允许坐其他玩家 | True |
| `GSit.PlayerSit.*` | PlayerSit \|权限 | op |
| `GSit.PlayerSitToggle` | 切换PlayerSit能力\|权限 | True |
| `GSit.Pose.*` | 姿势\|权限 | op |
| `GSit.Reload` | 插件重新加载命令\|权限 | op |
| `GSit.Sit` | 使用 /sit 坐下（默认开启） | True |
| `GSit.Sit.*` | SIT \|权限 | op |
| `GSit.SitClick` | 右键台阶自动坐下 | True |
| `GSit.SitToggle` | 允许 /sit toggle 关闭自动就坐 | True |
| `GSit.Spin` | 旋转命令\|权限 | True |
| `GSit.Update` | 更新通知\|权限 | op |
