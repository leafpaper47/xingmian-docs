---
title: Images
createTime: 2026/10/24
---

# Images

> 分类 📦 其他 · 版本 `2.5.12` · 指令 1 条 · api-version `1.13`

::: tip 自定义图片
把图片文件变成游戏内可放置/可显示的图片方块与地图画：导入图片、创建画框、批量清理附近图片、调整尺寸。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 导入一张图 | /img import &lt;文件名&gt; | 先把 png 放进 plugins/Images/images/ |
| 把图贴到墙上 | /img create &lt;文件名&gt; | 对着墙面执行，按视线方向生成 |
| 列出已导入的图 | /img list | 确认文件名拼写 |
| 清理附近的图 | /img deletenear 5 | 半径内所有自定义图片一并删除 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/image` | 自定义图片管理（导入/创建/删除/缩放）<br>别名 `/customimage`、`/images`、`/img` | `/image <create｜delete｜deletenear｜import｜list｜resiz…` | — |

## 指令详解

### `/image` — 自定义图片管理（导入/创建/删除/缩放）

- **语法**：`/image <create｜delete｜deletenear｜import｜list｜resize｜size｜transfer>`

- **示例**：

```
/img import logo.png
/img create logo.png
```

- **别名**：`/customimage`、`/images`、`/img`
- **备注**：别名 img、images、customimage

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/img create <文件名>` | 在当前位置/朝向前生成图片（地图画或方块） | `/img create logo.png` |
| `/img delete` | 删除准星指向的图片 | `/img delete` |
| `/img deletenear <半径>` | 删除半径内所有自定义图片 | `/img deletenear 5` |
| `/img list` | 列出 images 目录下已导入的文件 | `/img list` |
| `/img import <文件名>` | 把图片导入为可用资源 | `/img import logo.png` |
| `/img resize <宽> <高>` | 调整图片尺寸（重新生成） | `/img resize 4 2` |
| `/img size <宽> <高>` | 设置创建时的默认尺寸 | `/img size 2 2` |
| `/img transfer <玩家>` | 把图片数据转交给指定玩家 | `/img transfer Steve` |

## 注意事项

::: warning
- deletenear 会把半径内所有自定义图片一起删掉，执行前确认周围没有装饰画。
- 图片尺寸过大（单边 &gt; 8 张地图）会明显卡顿并占用地图 id，建议先在外部压缩。
- create 依赖玩家朝向与站位，贴歪了先 delete 再重贴。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `images.admin` | 使用 /image 全部子指令 | — |
