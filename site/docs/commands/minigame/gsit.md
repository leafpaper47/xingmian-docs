---
title: GSit
createTime: 2026/10/24
---

# GSit

> 版本 `3.5.1` · 指令 7 条 · api-version `1.16` · 文件 `GSit-3.5.1.jar`

与其他玩家在漂亮的座位上放松身心！

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/gbellyflop help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/gbellyflop` | Bellyflop命令 | `GSit.Bellyflop` |
| `/gcrawl` | 爬网命令 | — |
| `/glay` | Lay命令 | `GSit.Lay` |
| `/glayback` | Lay back命令 | `GSit.LayBack` |
| `/gsit` | SIT命令 | — |
| `/gsitreload` | 插件重新加载命令 | `GSit.Reload` |
| `/gspin` | 旋转命令 | `GSit.Spin` |

## 详细用法

### /gbellyflop

- **说明**：Bellyflop命令
- **用法**：`/&lt;command&gt;`
- **别名**：`/bellyflop`
- **权限**：`GSit.Bellyflop`

### /gcrawl

- **说明**：爬网命令
- **用法**：`/&lt;command&gt; [toggle]`
- **别名**：`/crawl`

### /glay

- **说明**：Lay命令
- **用法**：`/&lt;command&gt;`
- **别名**：`/lay`
- **权限**：`GSit.Lay`

### /glayback

- **说明**：Lay back命令
- **用法**：`/&lt;command&gt;`
- **别名**：`/layback`
- **权限**：`GSit.LayBack`

### /gsit

- **说明**：SIT命令
- **用法**：`/&lt;command&gt; [toggle|playertoggle]`
- **别名**：`/sit`

### /gsitreload

- **说明**：插件重新加载命令
- **用法**：`/&lt;command&gt;`
- **别名**：`/gsitrl`
- **权限**：`GSit.Reload`

### /gspin

- **说明**：旋转命令
- **用法**：`/&lt;command&gt;`
- **别名**：`/spin`
- **权限**：`GSit.Spin`

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
