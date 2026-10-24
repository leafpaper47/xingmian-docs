---
title: ArtMap
createTime: 2026/10/24
---

# ArtMap

> 版本 `3.9.26` · 指令 1 条 · api-version `1.13` · 文件 `ArtMap-JDK21-3.9.26.jar`

制作像素艺术！

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/art help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/art` | — | — |

## 详细用法

### /art

- **用法**：`&lt;command&gt; save &lt;title&gt; : Save your artwork`<br>`&lt;command&gt; clear : Reset the artwork on an easel`<br>`&lt;command&gt; delete &lt;title&gt; : Remove your artwork`<br>`&lt;command&gt; preview &lt;title&gt; : Preview an artwork`<br>`&lt;command&gt; help : Display help`<br>`&lt;command&gt; reload : Reloads the config`<br>`&lt;command&gt; give &lt;player&gt; &lt;easel|canvas|artwork:&lt;title&gt;&gt; &lt;amount&gt; : Give a player ArtMap item(s)`
- **别名**：`/a`、`/r`、`/t`、`/m`、`/a`、`/p`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `artmap.admin` | Allows administrative commands | op |
| `artmap.artist` | Allows players to paint, and place/break easels in any region they own, or are a member of. | op |
| `artmap.artkit` | Gives players a kit of art supplies while they use an easel | op |
| `artmap.menu` | Allows players to open the ArtMap menu | True |
| `artmap.prevent.afk` | Player will not be kicked for being AFK at easel. Supports Eseentials and CMI. | — |
| `artmap.region.member` | Allows players to place/break easels in regions that they are a member of, but DO NOT own. | op |
