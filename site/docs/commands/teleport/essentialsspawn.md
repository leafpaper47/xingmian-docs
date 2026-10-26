---
title: EssentialsSpawn
createTime: 2026/10/24
---

# 出生点 · EssentialsSpawn

> 分类 🌀 传送与出生点 · 版本 `2.22.1-dev+12-776f709` · 指令 2 条 · api-version `1.13`

::: tip 管理服务器出生点的传送与设置
EssentialsSpawn 是 Essentials 官方拆出的配套插件，专门管一件事：设置出生点、把玩家传回出生点。它必须装在已装 Essentials 的服上，出生点数据存在 Essentials 的配置文件里。日常配合 Essentials 的传送、家园、登录出生等功能一起用。
:::

## 什么时候会用到它

- 新玩家第一次进服或重生后要落在主城指定位置
- 玩家在主城跑远了、卡在野外想一键回主城出生点
- 为不同身份组（如 vip、builder）分别设置不同的出生点
- 管理员把某位玩家直接拉回出生点，用于处理卡图或违规流放

## 上手流程

1. 确认服里已经装了 Essentials，再放 EssentialsSpawn 的 jar 并重启
2. 自己站到想当出生点的位置，执行 /setspawn 写入出生点
3. 用 /spawn 自己测一次，确认落地位置和朝向没问题
4. 按需在 EssentialsSpawn 的 config 里打开多组出生点或加入时传送到出生点

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/setspawn` | 把当前站的位置设为出生点<br>别名 `/esetspawn` | `/setspawn 组名（组名可省略）` | — |
| `/spawn` | 把你自己或指定玩家传送回出生点<br>别名 `/espawn` | `/spawn（可选：玩家名 或 组名）` | — |

## 指令详解

### `/setspawn` — 把当前站的位置设为出生点

- **语法**：`/setspawn 组名（组名可省略）`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `组名` | 可选 | 多组出生点开启后用于指定给哪个组设置，省略则设全局出生点 |


- **示例**：

```
/setspawn
/setspawn vip
```

- **别名**：`/esetspawn`
- **备注**：设置的是你当前坐标和视线方向，所以要先站好再敲。别名 esetspawn。只有配置里开启了多组出生点，组名参数才有意义。

### `/spawn` — 把你自己或指定玩家传送回出生点

- **语法**：`/spawn（可选：玩家名 或 组名）`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `玩家名` | 可选 | 把别人传回出生点，需要 essentials.spawn.others 权限 |


- **示例**：

```
/spawn
/spawn Steve
/spawn vip
```

- **别名**：`/espawn`
- **备注**：别名 espawn。传送别人需要额外权限。多组出生点开启时也可以把组名当参数，把玩家送到该组的出生点。

## 注意事项

::: warning
- 本插件依赖 Essentials，单独装它不会生效，必须先有 Essentials 且版本匹配
- 多组出生点、加入时传送到出生点都在配置里开关，默认可能没开，别以为敲了组名就自动分好
- essentials.spawn-on-join.exempt 只对普通玩家开放出生点传送，管理员组通常要加这条豁免，否则每次进服都被拉走
- 出生点会被水、岩浆或后建建筑影响，改完地形记得重新 /setspawn 并实测一次落脚点
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `essentials.setspawn` | 允许访问/setspawn命令 | — |
| `essentials.spawn` | 允许访问/spawn命令 | — |
| `essentials.spawn-on-join.exempt` | 当spawn-on-join为true时，在加入时绕过spawn传送 | — |
| `essentials.spawn.others` | 允许其他玩家访问/spawn命令 | — |

## 相关插件

[Essentials](/commands/essentials/essentials.md)、[LuckPerms](/commands/core/luckperms.md)、[Vault](/commands/core/vault.md)
