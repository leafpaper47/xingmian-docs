---
title: LobbyGames
createTime: 2026/10/24
---

# 大厅小游戏 · LobbyGames

> 分类 🎲 休闲与小游戏 · 版本 `2.6.1` · 指令 3 条 · api-version `1.13`

::: tip 小游戏汇总
大厅里的成套小游戏（2048/扫雷/贪吃蛇/井字棋/数独/桌球/四子棋/足球/雪球战），玩家一条命令进游戏，服务器侧无需额外状态。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 看有哪些小游戏 | /lg join | 不带游戏名会列出可玩清单 |
| 直接进 2048 | /lgjoin 2048 | 别名也可直接当命令：/2048 |
| 把人踢出游戏 | /lg kick Steve | 需 lobbygames.kickplayer |
| 清排行榜 | /lg clearleaderboard | 不可撤销，活动结算后再清 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/lgjoin` | 直接进入指定小游戏<br>别名 `/clicker`、`/minesweeper`、`/snake`、`/soccer`、`/football`、`/spleef`、`/sudoku`、`/soduko`、`/2048`、`/tictactoe`、`/tic`、`/ttt`、`/pool`、`/minesw`、`/connect4` | `/lgjoin <游戏>` | — |
| `/lgjoinplayer` | 把指定玩家送进某局游戏（控制台可用）<br>别名 `/lgforcejoin` | `/lgjoinplayer <玩家> <游戏>` | — |
| `/lobbygames` | 小游戏主指令：进入、管理、排行、传送<br>别名 `/lg`、`/minigames` | `/lg <join｜list｜tp｜kick｜create｜delete｜leaderboard｜r…` | — |

## 指令详解

### `/lgjoin` — 直接进入指定小游戏

- **语法**：`/lgjoin <游戏>`

- **示例**：

```
/lgjoin snake
```

- **别名**：`/clicker`、`/minesweeper`、`/snake`、`/soccer`、`/football`、`/spleef`、`/sudoku`、`/soduko`、`/2048`、`/tictactoe`、`/tic`、`/ttt`、`/pool`、`/minesw`、`/connect4`
- **备注**：每个游戏还有独立别名（/snake、/ttt、/connect4…）

### `/lgjoinplayer` — 把指定玩家送进某局游戏（控制台可用）

- **语法**：`/lgjoinplayer <玩家> <游戏>`

- **示例**：

```
/lgjoinplayer Steve minesweeper
```

- **别名**：`/lgforcejoin`
- **备注**：别名 /lgforcejoin；需 lobbygames.forcejoin

### `/lobbygames` — 小游戏主指令：进入、管理、排行、传送

- **语法**：`/lg <join｜list｜tp｜kick｜create｜delete｜leaderboard｜reload｜help>`

- **示例**：

```
/lg help
```

- **别名**：`/lg`、`/minigames`
- **备注**：别名 /lg、/minigames

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/lg join` | 查看可玩小游戏并进入 | `/lg join` |
| `/lg list` | 列出进行中的游戏与所在服务器 | `/lg list` |
| `/lg tp <玩家>` | 传送到某玩家正在玩的对局 | `/lg tp Steve` |
| `/lg kick <玩家>` | 把玩家踢出对局 | `/lg kick Steve` |
| `/lg leaderboard` | 查看排行榜（别名 /lg lb） | `/lg lb` |
| `/lg clearleaderboard` | 清空排行榜 | `/lg clearleaderboard` |
| `/lg create <游戏>` | 创建一局游戏 | `/lg create tictactoe` |
| `/lg delete <游戏>` | 删除一局游戏 | `/lg delete tictactoe` |
| `/lg reload` | 重载配置与别名开关 | `/lg reload` |

## 注意事项

::: warning
- 小游戏对局在内存里，重启服务器会全部丢失，活动前别重启。
- clearleaderboard 没有二次确认，赛季结算前先导出排行榜。
- 关掉 lg-join-command-enabled 后 /lgjoin 失效，玩家只能靠告示牌或控制台送达。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `lobbygames.admin` | 使用 /lg leaderboard、/lg create、/lg delete | — |
| `lobbygames.command` | 使用 /lg list 与 /lg tp | — |
| `lobbygames.forcejoin` | 使用 /lgjoinplayer | — |
| `lobbygames.kickplayer` | 使用 /lg kick | — |
