---
title: AfDianPay
createTime: 2026/10/24
---

# 爱发电支付 · AfDianPay

> 分类 🪙 经济与商店 · 版本 `1.1.7` · 指令 1 条 · api-version `1.13`

::: tip 爱发电对接
把爱发电（afdian）的赞助订单同步进服：玩家发电后自动或手动发放奖励，支持订单核对、补发与配置重载。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 看玩家有没有未发奖励 | /afdianpay look Steve | 按玩家查订单与发放状态 |
| 补发奖励 | /afdianpay reward Steve | 玩家说没收到时先查再补 |
| 手动拉取订单 | /afdianpay send | 不走自动轮询时手动同步一次 |
| 改完配置生效 | /afdianpay reload | 改了 token/套餐映射必须重载 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/afDianPay` | 爱发电支付<br>别名 `/afdian` | — | — |

## 指令详解

### `/afDianPay` — 爱发电支付

- **别名**：`/afdian`

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/afdianpay send` | 手动同步一次订单（拉取最新赞助） | `/afdianpay send` |
| `/afdianpay look <玩家>` | 查看玩家的赞助订单与奖励发放状态 | `/afdianpay look Steve` |
| `/afdianpay done <订单号>` | 把订单标记为已处理（不再自动发） | `/afdianpay done 202510280001` |
| `/afdianpay reward <玩家>` | 对玩家手动发放/补发奖励 | `/afdianpay reward Steve` |
| `/afdianpay convert` | 转换历史订单数据格式（升级后跑一次） | `/afdianpay convert` |
| `/afdianpay reload` | 重载配置（token、套餐与奖励映射） | `/afdianpay reload` |

## 注意事项

::: warning
- 重复执行 reward 会重复发奖，补发前先用 look 确认状态并记下订单号。
- token 与 user_id 属敏感信息，别把 config.yml 贴到群里或文档里。
- convert 是数据升级操作，跑之前备份 plugins/AfDianPay/。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `afDianPay.*` | 爱发电支付 | — |
| `afDianPay.convert` | 转化数据库 | op |
| `afDianPay.done` | 完成订单 | op |
| `afDianPay.look` | 查看订单信息 | op |
| `afDianPay.reload` | 重载插件 | op |
| `afDianPay.reward` | 根据订单号发送奖励 | op |
| `afDianPay.send` | 发送赞助链接 | True |
| `afdianpay.admin` | 使用 /afdianpay 全部子指令 | — |
