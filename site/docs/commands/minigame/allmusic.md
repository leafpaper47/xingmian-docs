---
title: allmusic
createTime: 2026/10/24
---

# 全服音乐 · allmusic

> 分类 🎲 小游戏与娱乐 · 版本 `4.0.2` · 指令 1 条 · api-version `1.13`

::: tip 点歌/音乐
全服音乐播放：玩家点歌投票、按歌单播放、支持 HUD 歌词显示与禁歌名单；管理员通过 /music 管理歌单、封禁与重载。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 玩家点歌 | /music select 千本桜 | 按关键词搜索后确认选择 |
| 看当前歌曲列表 | /music list | 列出已加载曲库 |
| 跳过当前歌 | /music next | 需要投票或管理员权限 |
| 禁掉某首歌 | /music ban &lt;歌曲id&gt; | 被禁的歌不再进入随机池 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/music` | 音乐系统主指令（点歌/投票/歌单/管理） | `/music <list｜search｜select｜next｜vote｜hud｜join｜push…` | — |

## 指令详解

### `/music` — 音乐系统主指令（点歌/投票/歌单/管理）

- **语法**：`/music <list｜search｜select｜next｜vote｜hud｜join｜push｜cancel｜stop｜ban｜unban｜addlist｜clearlist｜delete｜reload｜test>`

- **示例**：

```
/music search 千本桜
/music list
```

- **备注**：命令名 music；普通玩家可用点歌类子指令，管理类需权限

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/music list` | 列出曲库中的歌曲（分页） | `/music list` |
| `/music search <关键词>` | 按歌名/作者搜索曲库 | `/music search 千本桜` |
| `/music select <编号｜歌名>` | 选定要播放的歌曲 | `/music select 12` |
| `/music next` | 切换到下一首（投票或权限） | `/music next` |
| `/music vote` | 为跳歌/切歌投票 | `/music vote` |
| `/music hud [on｜off]` | 开关歌词 HUD 显示 | `/music hud on` |
| `/music join` | 加入当前音乐房间/跟随播放 | `/music join` |
| `/music cancel` | 取消自己的点歌/投票 | `/music cancel` |
| `/music stop` | 停止当前播放（管理） | `/music stop` |
| `/music push <玩家> <歌曲>` | 直接给指定玩家推一首歌（管理） | `/music push Steve 千本桜` |
| `/music ban [玩家｜歌曲]` | 禁歌或禁某玩家点歌 | `/music ban 12` |
| `/music unban [玩家｜歌曲]` | 解除禁歌/禁点 | `/music unban 12` |
| `/music addlist <歌曲>` | 把歌曲加入指定歌单/收藏列表 | `/music addlist 千本桜` |
| `/music clearlist` | 清空当前歌单 | `/music clearlist` |
| `/music delete <歌曲>` | 从曲库删除歌曲 | `/music delete 12` |
| `/music reload` | 重载曲库与配置（新加的歌才出现） | `/music reload` |
| `/music test <歌曲>` | 试听/测试播放（排查卡顿时用） | `/music test 12` |

## 注意事项

::: warning
- 歌名或编号写错不会报错，只会静默不播放，先 /music list 拿到准确编号。
- HUD 歌词与计分板/TAB 可能重叠，玩家反馈「字叠在一起」时先关 hud 排查。
- 新放入的音乐文件必须 /music reload 才会出现在曲库，reload 期间正在播放的歌会中断。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `music.admin` | 管理类子指令（ban/unban/delete/reload/push/stop） | — |
| `music.use` | 使用点歌、列表、搜索等基础子指令 | — |
