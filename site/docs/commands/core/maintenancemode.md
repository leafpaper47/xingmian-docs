---
title: MaintenanceMode
createTime: 2026/10/24
---

# 维护模式 · MaintenanceMode

> 分类 🛡️ 权限与底座 · 版本 `1.0.0` · 指令 1 条 · api-version `1.21`

::: tip 开服维护期间的封服开关
给服务器加了一个「维护模式」总闸。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 开维护模式 | /maintenance on | 先广播再开，避免踢人 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/maintenance` | 开启、关闭或查询维护模式 | `/maintenance on｜off｜status` | `maintenance.use` |

## 指令详解

### `/maintenance` — 开启、关闭或查询维护模式

- **语法**：`/maintenance on｜off｜status`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `on｜off｜status` | 必填 | on 开启维护、off 关闭维护、status 查看当前状态 |


- **示例**：

```
/maintenance on
/maintenance status
```

- **权限**：`maintenance.use`
- **备注**：常用于更新/回档前封服。开启后记得确认自己有 maintenance.bypass，否则可能把自己也挡在外面。

## 注意事项

::: warning
- 开启维护前务必确认自己的账号有 maintenance.bypass 权限，否则可能连自己都进不去，只能改配置文件或控制台处理
- 维护模式通常只拦进服，不保证在线玩家被立即踢出；需要清场时配合 /kick 手动踢人
- 重启或重载插件后维护状态是否保留取决于配置，重载后先用 /maintenance status 复核一次
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `maintenance.bypass` | 免除维护模式限制（不被踢、可进服） | op |
| `maintenance.use` | 允许使用维护模式指令 | op |
