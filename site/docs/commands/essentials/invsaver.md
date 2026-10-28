---
title: InvSaver
createTime: 2026/10/24
---

# 背包快照 · InvSaver

> 分类 🧰 基础工具 · 版本 `1.0.1` · 指令 6 条 · api-version `1.20`

::: tip 背包快照
给玩家背包拍快照并按记录回滚，处理误删、误销毁、盗号补偿时的救命工具。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 出事前先备份 | /invSaver save Steve | 补偿/回滚前一定先存一份当前的 |
| 看有哪些备份 | /invSaver list Steve | 编号就是 restore/preview 要填的参数 |
| 回滚背包 | /invSaver restore Steve 3 | 直接覆盖当前背包，不可反悔 |
| 只查看不回滚 | /invSaver preview Steve 3 | 别加 -e，加了会就地改写那份备份 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/invSaver` | 背包快照主指令，含保存/回滚/列表/预览/重载 | `/invSaver <save｜restore｜list｜preview｜reload> [参数]` | — |
| `/invSaver save` | 给指定玩家的当前背包拍快照 | `/invSaver save <玩家>` | `invSaver.save` |
| `/invSaver list` | 列出该玩家的备份记录与编号 | `/invSaver list <玩家>` | `invSaver.list` |
| `/invSaver preview` | 以只读方式查看某个备份的内容 | `/invSaver preview <玩家> <备份记录> [-e]` | `invSaver.preview` |
| `/invSaver restore` | 把玩家背包恢复成某个备份 | `/invSaver restore <玩家> <备份记录>` | `invSaver.restore` |
| `/invSaver reload` | 重载配置文件 | `/invSaver reload` | `invSaver.reload` |

## 指令详解

### `/invSaver` — 背包快照主指令，含保存/回滚/列表/预览/重载

- **语法**：`/invSaver <save｜restore｜list｜preview｜reload> [参数]`

- **示例**：

```
/invSaver list Steve
```

- **备注**：只会用到这一个入口，子指令见下表

### `/invSaver save` — 给指定玩家的当前背包拍快照

- **语法**：`/invSaver save <玩家>`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `玩家` | 必填 | 在线离线都能存，离线取最近一次登录的数据 |


- **示例**：

```
/invSaver save Steve
```

- **权限**：`invSaver.save`
- **备注**：只记录保存那一刻的状态，之后的变动不会被自动追踪

### `/invSaver list` — 列出该玩家的备份记录与编号

- **语法**：`/invSaver list <玩家>`

- **示例**：

```
/invSaver list Steve
```

- **权限**：`invSaver.list`

### `/invSaver preview` — 以只读方式查看某个备份的内容

- **语法**：`/invSaver preview <玩家> <备份记录> [-e]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `备份记录` | 必填 | 先用 /invSaver list 查编号 |


- **示例**：

```
/invSaver preview Steve 3
```

- **权限**：`invSaver.preview`
- **备注**：带 -e 是「就地编辑这份备份」，只想看千万别加

### `/invSaver restore` — 把玩家背包恢复成某个备份

- **语法**：`/invSaver restore <玩家> <备份记录>`

- **示例**：

```
/invSaver restore Steve 3
```

- **权限**：`invSaver.restore`
- **备注**：直接覆盖当前背包且不可撤销；建议先 save 一份当前的再 restore

### `/invSaver reload` — 重载配置文件

- **语法**：`/invSaver reload`

- **示例**：

```
/invSaver reload
```

- **权限**：`invSaver.reload`

## 注意事项

::: warning
- restore 会覆盖背包且没有二次确认，顺序永远是：save 当前 → preview 核对 → restore。
- preview 加 -e 会把改动写回那份备份，之后 restore 出来的就是被改过的内容。
- 5 个权限节点默认全是 op，别整组发出去——等于给了全服背包改写的权力。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `invSaver.list` | 查看玩家的备份记录列表 | op |
| `invSaver.preview` | 预览（或带 -e 编辑）备份内容 | op |
| `invSaver.reload` | 重载插件配置文件 | op |
| `invSaver.restore` | 把玩家背包回滚到指定备份 | op |
| `invSaver.save` | 为玩家保存背包快照 | op |
