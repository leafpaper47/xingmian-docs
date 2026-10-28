---
title: YccHongBao
createTime: 2026/10/24
---

# 红包 · YccHongBao

> 分类 🪙 经济与商店 · 版本 `1.0.0` · 指令 1 条 · api-version `1.20`

::: tip 红包发放与领取记录查询
GUI and chat red packet economy plugin for Bukkit, Spigot, Paper, Purpur, and Folia cores.
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 发一个红包 | /ycch 100 5 | 金额 100、份数 5 |
| 看自己领到的红包 | /ycch list | 查发放与领取记录 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/ycch` | YccHongBao 红包主命令<br>别名 `/ycchongbao`、`/ycchb` | `/ycch help` | — |

## 指令详解

### `/ycch` — YccHongBao 红包主命令

- **语法**：`/ycch help`

- **示例**：

```
/ycch help
```

- **别名**：`/ycchongbao`、`/ycchb`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `ycch.admin` | 打开管理员红包 GUI、发送红包和重载配置 | op |
| `ycch.claim` | 领取红包 | True |
| `ycch.reload` | 重载红包配置 | op |
| `ycch.send` | 发送红包 | — |
