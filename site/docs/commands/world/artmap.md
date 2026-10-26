---
title: ArtMap
createTime: 2026/10/24
---

# 画板地图 · ArtMap

> 分类 🗺️ 世界与地图 · 版本 `3.9.26` · 指令 1 条 · api-version `1.13`

::: tip 把画架变成像素画板，作画、存作、发放作品
ArtMap 给服务器加了一套可交互的像素绘画玩法：玩家放下画架，用调色盘在画布上一格一格上色，画完保存成自己的作品。作品可以预览、导出成物品发给别人当装饰画，也能当收藏与展示内容。管理侧主要靠 art 指令完成发放、清理和重载配置。
:::

## 什么时候会用到它

- 想让玩家在服里画像素画、做地图画
- 举办绘画活动并发放画架与画布道具
- 把玩家作品做成物品奖励或装饰挂件
- 在领地或地皮里和朋友合作画画

## 上手流程

1. 给玩家 artmap.artkit 或管理员发放画架，玩家放下画架开始作画
2. 画完用 art save 保存成带标题的作品
3. 用 art preview 检查效果，用 art give 把作品或画架发给目标玩家
4. 画错了用 art clear 清空当前画架，不需要的作品用 art delete 删除

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/art` | 画架作品主指令：保存、清空、删除、预览、发放与管理<br>别名 `/a`、`/r`、`/t`、`/m`、`/a`、`/p` | `/art save 作品名` | — |

## 指令详解

### `/art` — 画架作品主指令：保存、清空、删除、预览、发放与管理

- **语法**：`/art save 作品名`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子指令` | 必填 | save / clear / delete / preview / help / reload / give 之一 |
| `作品名` | 可选 | save、delete、preview 需要，用作品标题字符串 |
| `玩家` | 可选 | give 时指定目标玩家 |
| `物品类型` | 可选 | give 时为 easel 画架、canvas 画布或 artwork:作品名 |
| `数量` | 可选 | give 时发放的个数 |


- **示例**：

```
/art save 星冕日落
/art preview 星冕日落
/art give Steve easel 1
/art give Steve artwork:星冕日落 1
```

- **别名**：`/a`、`/r`、`/t`、`/m`、`/a`、`/p`
- **备注**：管理类子指令（give、reload 等）需要 artmap.admin；绘画与保存需要 artmap.artist；在别人领地内还需 artmap.region.member。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `save 作品名` | 把当前画架上的画保存为作品 | `/art save 星冕日落` |
| `clear` | 清空当前画架上的画，重新开始 | `/art clear` |
| `delete 作品名` | 删除自己的某个作品 | `/art delete 星冕日落` |
| `preview 作品名` | 预览某个作品的效果 | `/art preview 星冕日落` |
| `give 玩家 easel 数量` | 给玩家发放画架 | `/art give Steve easel 1` |
| `give 玩家 canvas 数量` | 给玩家发放画布 | `/art give Steve canvas 1` |
| `give 玩家 artwork:作品名 数量` | 把指定作品当作物件发给玩家 | `/art give Steve artwork:星冕日落 1` |
| `help` | 显示指令帮助与可用子指令列表 | `/art help` |
| `reload` | 重载 ArtMap 的配置文件 | `/art reload` |

## 注意事项

::: warning
- art give 的 artwork 写法是 artwork:作品名，冒号别漏，作品名要和保存时完全一致
- 绘画、放置和敲掉画架受领地插件限制，普通玩家需要 artmap.artist，非自己领地还需 artmap.region.member
- art reload 只重配置不重载作品数据，删掉的画作一般找不回来，动手前提醒玩家备份重要作品
- artmap.prevent.afk 可让玩家画画时不被 AFK 踢出，装 Essentials 或 CMI 的服建议开启
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `artmap.admin` | 允许管理命令 | op |
| `artmap.artist` | 允许玩家在他们拥有或是其成员的任何区域中绘画和放置/打破画架。 | op |
| `artmap.artkit` | 使用画架时为玩家提供一套艺术用品 | op |
| `artmap.menu` | 允许玩家打开ArtMap菜单 | True |
| `artmap.prevent.afk` | 在画架上，玩家不会因为是AFK而被踢出。支持Eseentials和CMI。 | — |
| `artmap.region.member` | 允许玩家在他们是成员但不拥有的地区放置/打破画架。 | op |

## 相关插件

[PlaceholderAPI](/commands/config/placeholderapi.md)、[Essentials](/commands/essentials/essentials.md)、[WorldGuardGUI](/commands/protect/worldguardgui.md)
