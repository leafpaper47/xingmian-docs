---
title: MahjongPlay
createTime: 2026/10/24
---

# 麻将 · MahjongPlay

> 分类 🎲 小游戏与娱乐 · 版本 `1.5` · 指令 1 条 · api-version `26.2`

::: tip 麻将小游戏
服内四人麻将：开桌、入座就绪、机器人补位、出牌与结算，带权限细分到每个子指令。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 开一桌 | /mj create | 创建牌桌并拿到桌号 |
| 加入牌桌 | /mj join &lt;桌号&gt; | 提示桌号无效时先 /mj list |
| 人不够，补机器人 | /mj bot | 机器人补位后再 start |
| 开始牌局 | /mj start | 全员 ready 才能开始 |
| 打出一张牌 | /mj action &lt;操作&gt; | 摸/打/吃/碰/杠/胡 都在 action 下 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/mahjong` | 麻将主指令（开桌/入座/出牌/结算）<br>别名 `/mj`、`/majiang` | `/mahjong <create｜join｜leave｜ready｜unready｜start｜bo…` | — |

## 指令详解

### `/mahjong` — 麻将主指令（开桌/入座/出牌/结算）

- **语法**：`/mahjong <create｜join｜leave｜ready｜unready｜start｜bot｜kick｜destroy｜info｜list｜action>`

- **示例**：

```
/mj create
/mj join 1
/mj start
```

- **别名**：`/mj`、`/majiang`
- **备注**：别名 mj、majiang；权限按子指令细分

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/mj create` | 创建牌桌（返回桌号） | `/mj create` |
| `/mj join <桌号>` | 加入指定牌桌 | `/mj join 1` |
| `/mj leave` | 离开当前牌桌 | `/mj leave` |
| `/mj ready` | 标记自己已准备 | `/mj ready` |
| `/mj unready` | 取消准备状态 | `/mj unready` |
| `/mj start` | 开始牌局（需全员准备） | `/mj start` |
| `/mj bot` | 用机器人补位 | `/mj bot` |
| `/mj kick <玩家>` | 把玩家移出牌桌（桌主/管理） | `/mj kick Steve` |
| `/mj destroy` | 解散当前牌桌 | `/mj destroy` |
| `/mj info [桌号]` | 查看牌桌状态 | `/mj info 1` |
| `/mj list` | 列出所有牌桌 | `/mj list` |
| `/mj action <摸｜打｜吃｜碰｜杠｜胡>` | 牌局内执行操作 | `/mj action 打 3万` |

## 注意事项

::: warning
- 玩家中途下线会占座，人不在时用 /mj kick 或 /mj destroy 清桌，否则桌号会一直被占用。
- 牌面依赖客户端资源包，没装包的玩家看到的是方块占位图标，不是数据错误。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `mahjongplay.command.action` | 牌局内操作（摸打吃碰杠胡） | True |
| `mahjongplay.command.bot` | 机器人补位 | — |
| `mahjongplay.command.create` | 创建牌桌 | — |
| `mahjongplay.command.destroy` | 解散牌桌 | — |
| `mahjongplay.command.info` | 查看牌桌状态 | True |
| `mahjongplay.command.join` | 加入牌桌 | True |
| `mahjongplay.command.kick` | 踢人出桌 | — |
| `mahjongplay.command.leave` | 离开牌桌 | True |
| `mahjongplay.command.list` | 列出牌桌 | True |
| `mahjongplay.command.ready` | 准备 / 取消准备 | True |
| `mahjongplay.command.start` | 开始牌局 | — |
| `mahjongplay.command.unready` | 允许取消准备 | True |
