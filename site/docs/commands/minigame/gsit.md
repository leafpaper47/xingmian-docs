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
| `GSit.*` | GSit \| Permissions | op |
| `GSit.BellyFlop` | BellyFlop command \| Permission | True |
| `GSit.ByPass.*` | ByPass \| Permissions | op |
| `GSit.ByPass.Command` | ByPass command \| Permission | op |
| `GSit.ByPass.Region` | ByPass region \| Permission | op |
| `GSit.ByPass.World` | ByPass world \| Permission | op |
| `GSit.Crawl` | Crawl command \| Permission | True |
| `GSit.Crawl.*` | Crawl \| Permissions | op |
| `GSit.CrawlSneak` | Crawl sneak \| Permission | True |
| `GSit.CrawlToggle` | Toggle crawl ability \| Permission | True |
| `GSit.Kick.*` | Kick \| Permissions | op |
| `GSit.Kick.Pose` | Kick pose \| Permission | op |
| `GSit.Kick.Sit` | Kick sit \| Permission | op |
| `GSit.Lay` | Lay command \| Permission | True |
| `GSit.LayBack` | LayBack command \| Permission | True |
| `GSit.PlayerSit` | PlayerSit click \| Permission | True |
| `GSit.PlayerSit.*` | PlayerSit \| Permissions | op |
| `GSit.PlayerSitToggle` | Toggle PlayerSit ability \| Permission | True |
| `GSit.Pose.*` | Pose \| Permissions | op |
| `GSit.Reload` | Plugin reload command \| Permission | op |
| `GSit.Sit` | Sit command \| Permission | True |
| `GSit.Sit.*` | Sit \| Permissions | op |
| `GSit.SitClick` | Sit click \| Permission | True |
| `GSit.SitToggle` | Toggle sit ability \| Permission | True |
| `GSit.Spin` | Spin command \| Permission | True |
| `GSit.Update` | Update notification \| Permission | op |
