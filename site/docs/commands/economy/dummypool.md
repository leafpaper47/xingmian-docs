---
title: DummyPool
createTime: 2026/10/24
---

# 台球 · DummyPool

> 分类 🪙 经济与商店 · 版本 `1.1.1-leaf` · 指令 2 条 · api-version `1.21`

::: tip 服务器里的台球玩法插件
DummyPool 给服务器加了一套可以自己摆台、自己开局的台球玩法：管理员先建好球台，玩家拿到球物品后就能开球对局。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 开一桌台球 | /dummypool | 所有子指令挂在这下面 |
| 同上，短别名 | /dump | — |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/dummypool` | DummyPool 台球插件主命令，所有子指令都挂在它下面<br>别名 `/dump` | `/dummypool 子指令 ...` | — |
| `/dump` | 主命令 dummypool 的短别名，功能完全相同 | `/dump 子指令 ...` | — |

## 指令详解

### `/dummypool` — DummyPool 台球插件主命令，所有子指令都挂在它下面

- **语法**：`/dummypool 子指令 ...`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子指令` | 必填 | 具体可用的子指令（建台、删台、领球、重载配置等）以游戏内 help 输出为准 |


- **示例**：

```
/dummypool
```

- **别名**：`/dump`
- **备注**：只输入主命令一般会列出可用子指令和当前版本信息；权限要求随子指令不同，建台删台要 dummypool.create / dummypool.remove，重载配…

### `/dump` — 主命令 dummypool 的短别名，功能完全相同

- **语法**：`/dump 子指令 ...`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子指令` | 必填 | 与 /dummypool 共用同一套子指令和同一套权限节点 |


- **示例**：

```
/dump
```

- **备注**：别名走的是同一条命令处理逻辑，权限节点也是同一套，不存在「别名权限更松」的情况；如果 /dummypool 能用而 /dump 报未知命令，说明别名被别的插件抢…

## 注意事项

::: warning
- 这是服务器自研/分支版本插件，具体参数与子指令以游戏内 help 为准，不要凭记忆敲网上的原版教程
- dummypool.ball 默认只给 OP，是为了防止普通玩家刷球；确实要给玩家时按人单独下发，别整组放开
- 删台前先确认台面上没人在对局，避免把正在打的玩家卡在半局状态
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `dummypool.admin` | 执行管理命令（reloadconfig / reloadmessages） | op |
| `dummypool.ball` | 领取球物品（/dummypool ball get）——默认仅 OP，防止普通玩家刷球 | op |
| `dummypool.create` | 创建球台 | op |
| `dummypool.remove` | 删除球台 | op |
| `dummypool.use` | 使用 DummyPool 的基础功能（打开界面、参与对局、查看球台列表） | True |
