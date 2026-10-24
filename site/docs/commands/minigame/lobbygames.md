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
| `/lgjoin` | 直接加入大堂游戏 | — |
| `/lgjoinplayer` | 将玩家送入游戏的控制台命令 | — |
| `/lobbygames` | LobbyGames插件主命令 | — |

## 详细用法

### /lgjoin

- **说明**：直接加入大堂游戏
- **别名**：`/clicker`、`/minesweeper`、`/snake`、`/soccer`、`/football`、`/spleef`、`/sudoku`、`/soduko`、`/2048`、`/tictactoe`、`/tic`、`/ttt`、`/pool`、`/minesw`、`/connect4`

### /lgjoinplayer

- **说明**：将玩家送入游戏的控制台命令
- **别名**：`/lgforcejoin`

### /lobbygames

- **说明**：LobbyGames插件主命令
- **别名**：`/lg`、`/minigames`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `lobbygames.admin` | 访问/lg排行榜、/lg创建和/lg删除 | — |
| `lobbygames.command` | 访问/lg列表，/lg tp | — |
| `lobbygames.forcejoin` | 访问/lgjoinplayer | — |
| `lobbygames.kickplayer` | 进入/lg kick | — |
