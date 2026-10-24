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
| `artmap.admin` | 允许管理命令 | op |
| `artmap.artist` | 允许玩家在他们拥有或是其成员的任何区域中绘画和放置/打破画架。 | op |
| `artmap.artkit` | 使用画架时为玩家提供一套艺术用品 | op |
| `artmap.menu` | 允许玩家打开ArtMap菜单 | True |
| `artmap.prevent.afk` | 在画架上，玩家不会因为是AFK而被踢出。支持Eseentials和CMI。 | — |
| `artmap.region.member` | 允许玩家在他们是成员但不拥有的地区放置/打破画架。 | op |
