---
title: Vault
createTime: 2026/10/24
---

# 经济前置 · Vault

> 分类 🛡️ 基础与权限 · 版本 `2.20.2` · 指令 2 条 · api-version `1.13`

::: tip 经济与权限接口层
给插件之间提供统一接口：扣钱、查权限、发聊天前缀都走它，自己不带任何玩法。商店、地皮、任务类插件大多把它列为必需前置。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 确认经济挂上了没 | /vault-info | 经济那一栏为空 = 没有经济插件注册，扣钱类插件全会报错 |
| 换经济插件后搬余额 | /vault-convert Essentials CMI | 把前一个经济插件的数据倒进后一个，先备份两边数据 |
| 开管理权限 | /lp group admin permission set vault.admin true | 否则 info 与 convert 都会提示无权限 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/vault-convert` | 把一个经济插件的余额数据整体倒入另一个经济插件 | `/vault-convert <源经济> <目标经济>` | `vault.admin.convert` |
| `/vault-info` | 显示 Vault 版本与已接入的经济、权限、聊天实现 | `/vault-info` | `vault.admin.info` |

## 指令详解

### `/vault-convert` — 把一个经济插件的余额数据整体倒入另一个经济插件

- **语法**：`/vault-convert <源经济> <目标经济>`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `源经济` | 必填 | 经济插件在 Vault 里注册的名字，如 Essentials |
| `目标经济` | 必填 | 要接管的那个，如 CMI |


- **示例**：

```
/vault-convert Essentials CMI
```

- **权限**：`vault.admin.convert`
- **备注**：两边都必须已安装并注册到 Vault；目标里同名玩家的余额会被覆盖，跑之前备份数据库

### `/vault-info` — 显示 Vault 版本与已接入的经济、权限、聊天实现

- **语法**：`/vault-info`

- **示例**：

```
/vault-info
```

- **权限**：`vault.admin.info`
- **备注**：「商店能打开但结账报错」先跑这条，经济一栏为空就是没装经济插件或没注册成功

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/vault-info` | 排查前置问题第一站：看版本与各 provider 是否注册成功 | `/vault-info` |

## 注意事项

::: warning
- Vault 不给玩家任何指令，玩家侧的 /bal、/pay 来自 Essentials；Vault 出问题的表现是第三方插件报 Vault 相关错误。
- 同时装两个经济插件（Essentials 经济 + CMI 经济）时以最后注册的为准，余额会分叉，只留一个。
- vault-convert 不可撤销，迁移前把两边的经济数据文件都备份一份。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `vault.admin` | Vault 管理工具总权限（含 info、convert） | op |
| `vault.update` | 有新版本时收到提示 | op |
