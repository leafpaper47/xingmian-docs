---
title: LobbyGames
createTime: 2026/10/24
---

# LobbyGames

> 版本 `2.6.1` · 指令 3 条 · api-version `1.13` · 文件 `LobbyGames-2.6.1.jar`

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/lgjoin help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/lgjoin` | Directly join a Lobby Game | — |
| `/lgjoinplayer` | Console command to send a player into a game | — |
| `/lobbygames` | LobbyGames plugin main command | — |

## 详细用法

### /lgjoin

- **说明**：Directly join a Lobby Game
- **别名**：`/clicker`、`/minesweeper`、`/snake`、`/soccer`、`/football`、`/spleef`、`/sudoku`、`/soduko`、`/2048`、`/tictactoe`、`/tic`、`/ttt`、`/pool`、`/minesw`、`/connect4`

### /lgjoinplayer

- **说明**：Console command to send a player into a game
- **别名**：`/lgforcejoin`

### /lobbygames

- **说明**：LobbyGames plugin main command
- **别名**：`/lg`、`/minigames`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `lobbygames.admin` | Access to /lg leaderboard, /lg create, and /lg delete | — |
| `lobbygames.command` | Access to /lg list, /lg tp | — |
| `lobbygames.forcejoin` | Access to /lgjoinplayer | — |
| `lobbygames.kickplayer` | Access to /lg kick | — |
