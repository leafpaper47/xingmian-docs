---
title: EssentialsSpawn
createTime: 2026/10/24
---

# 出生点 · EssentialsSpawn

> 分类 🌀 移动与传送 · 版本 `2.22.1-dev+12-776f709` · 指令 2 条 · api-version `1.13`

::: tip 出生点传送
Essentials 的出生点模块：按组存出生点，玩家用 /spawn 回城，可配登录自动传送。必须和 Essentials 一起装，单人装它不生效。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 站好位置设默认出生点 | /setspawn default | 参数是组名，default 就是所有人默认走这个点 |
| 回出生点 | /spawn | 上一次的位置会被 /back 记住 |
| 给 VIP 单独出生点 | /setspawn vip | 组名要和玩家所在组一致，否则仍走 default |
| 登录自动传送 | /ess reload | 先把 config.yml 的 spawn-on-join 改 true 再重载 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/setspawn` | 把你当前站的位置和朝向设为某个组的出生点<br>别名 `/esetspawn` | `/setspawn <组名>` | — |
| `/spawn` | 传送到出生点<br>别名 `/espawn` | `/spawn [玩家]` | — |

## 指令详解

### `/setspawn` — 把你当前站的位置和朝向设为某个组的出生点

- **语法**：`/setspawn <组名>`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `组名` | 必填 | default 为默认组，其它写自定义组名，如 vip |


- **示例**：

```
/setspawn default
/setspawn vip
```

- **别名**：`/esetspawn`
- **备注**：组名与 Essentials 配置里的组不一致时，玩家 /spawn 仍走 default；改完立即生效，不用重启

### `/spawn` — 传送到出生点

- **语法**：`/spawn [玩家]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `玩家` | 可选 | 把别人送回出生点，需要 others 权限 |


- **示例**：

```
/spawn
/spawn Steve
```

- **别名**：`/espawn`
- **备注**：传送到该玩家所属组的出生点，该组没设过就退回 default

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/spawn <玩家>` | 把指定玩家送回他的出生点（需 essentials.spawn.others） | `/spawn Steve` |

## 注意事项

::: warning
- 出生点按组存：玩家换组后 /spawn 会去新组的点，排查「回城地点变了」先看他的 LuckPerms 主组。
- config.yml 的 spawn-on-join 打开后登录会强制传送，不想被拉走的玩家给 essentials.spawn-on-join.exempt。
- 出生点在未加载区块时会传送失败，公共出生点建议常驻加载。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `essentials.setspawn` | 允许使用 /setspawn | — |
| `essentials.spawn` | 允许使用 /spawn | — |
| `essentials.spawn-on-join.exempt` | 开启登录传送到出生点后被豁免 | — |
| `essentials.spawn.others` | 允许把其他玩家传送到出生点 | — |
