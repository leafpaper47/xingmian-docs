---
title: MahjongPlay
createTime: 2026/10/24
---

# 麻将 · MahjongPlay

> 分类 🎲 小游戏与娱乐 · 版本 `1.5` · 指令 1 条 · api-version `26.2`

::: tip 在服务器里打日本立直麻将的小游戏
把日式立直麻将搬进 Minecraft，玩家可以在服内开桌、凑人、完整打完一局，不用跳到外部平台。主要解决休闲区没牌打、临时凑不齐人的问题，配合各子指令的权限节点可以控制谁能开桌、加机器人和踢人。适合作为大厅或休闲区的常驻小游戏，和其他小游戏插件并列使用。
:::

## 什么时候会用到它

- 玩家想在大厅或休闲区打一局日式立直麻将，需要开桌并拉人加入时
- 在线人数不够四个人，想加机器人补位做演示或陪玩时
- 管理员要查看现有麻将桌、清理没人用的残留桌子时

## 上手流程

1. 先确认玩家有基础权限（join、leave、ready、unready、action、list、info 默认开启），开桌权限要单独给
2. 用 /mahjong create 开一张麻将桌，其他玩家用 /mahjong join 加入
3. 各自 /mahjong ready 准备，人齐后由有权限的人 /mahjong start 开始
4. 牌局中用 /mahjong action 执行摸打、吃碰杠等操作
5. 散场后玩家 /mahjong leave 退出，桌主用 /mahjong destroy 销毁桌子

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/mahjong` | 麻将游戏主指令，开桌、加入、准备、开始与牌局操作都走它<br>别名 `/mj`、`/majiang` | `/mahjong create｜join｜leave｜ready｜start｜bot｜destroy…` | — |

## 指令详解

### `/mahjong` — 麻将游戏主指令，开桌、加入、准备、开始与牌局操作都走它

- **语法**：`/mahjong create｜join｜leave｜ready｜start｜bot｜destroy｜info｜list｜action`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子指令` | 必填 | create 开桌、join 加入、leave 离开、ready 准备、start 强制开始、bot 加机器人、destroy 销毁桌子、info 查看桌子信息、list 列出麻将桌、action 执行牌局操作 |


- **示例**：

```
/mahjong create
/mahjong join
/mahjong list
```

- **别名**：`/mj`、`/majiang`
- **备注**：别名 /mj、/majiang 等价；权限按子指令拆分，节点为 mahjongplay.command 开头（如 mahjongplay.command.create），create、start、bot、kick、destroy 类管理子指令默认只给 OP，其余默认所有人可用。

## 注意事项

::: warning
- create、start、bot、kick、destroy 默认只发 OP，普通玩家不额外授权就开不了桌、也踢不了人和清桌。
- 取消准备（unready）和踢人（kick）在权限节点里存在，但指令用法串里没列全，具体参数与子指令以游戏内 help 为准。
- 别随便放开开桌权限，玩家开出的桌子会占位；建议在大厅用领地或区域圈出专门的麻将区。
- 玩家卡在半局或掉线时桌子不会自己消失，需要管理员用 list 找出来再 destroy 清掉。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `mahjongplay.command.action` | 允许执行麻将操作 | True |
| `mahjongplay.command.bot` | 允许添加机器人 | — |
| `mahjongplay.command.create` | 允许创建麻将桌 | — |
| `mahjongplay.command.destroy` | 允许销毁麻将桌 | — |
| `mahjongplay.command.info` | 允许查看麻将桌信息 | True |
| `mahjongplay.command.join` | 允许加入麻将桌 | True |
| `mahjongplay.command.kick` | 允许踢出玩家 | — |
| `mahjongplay.command.leave` | 允许离开麻将桌 | True |
| `mahjongplay.command.list` | 允许查看麻将桌列表 | True |
| `mahjongplay.command.ready` | 允许准备 | True |
| `mahjongplay.command.start` | 允许强制开始游戏 | — |
| `mahjongplay.command.unready` | 允许取消准备 | True |
