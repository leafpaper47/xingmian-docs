---
title: WineSuite
createTime: 2026/10/24
---

# 酿酒图鉴 · WineSuite

> 分类 🍳 烹饪与采集 · 版本 `1.2.0` · 指令 2 条 · api-version `1.21`

::: tip 酿酒图鉴
把酿酒配方变成可查的图鉴、把玩家酿的酒变成可收购的商品；配方数据自动跟随主酿造插件，无需手动维护。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 玩家查自己酿过什么 | /winebook | 别名 /酒鉴 |
| 卖酒换钱 | /winebuyer | 别名 /收酒 |
| 改了配方价格 | /winebuyer reload | 图鉴侧用 /winebook reload |
| 看收购清单 | /winebuyer list | 列出当前可收购的配方与价格 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/winebook` | 打开酿酒图鉴（已酿出的配方会打勾）<br>别名 `/酒鉴`、`/酿酒图鉴`、`/图鉴`、`/wbk` | `/winebook [reload]` | — |
| `/winebuyer` | 打开酒水收购界面（玩家卖酒）<br>别名 `/wb`、`/收酒`、`/酒收` | `/winebuyer [list｜reload｜reset]` | — |

## 指令详解

### `/winebook` — 打开酿酒图鉴（已酿出的配方会打勾）

- **语法**：`/winebook [reload]`

- **示例**：

```
/winebook
```

- **别名**：`/酒鉴`、`/酿酒图鉴`、`/图鉴`、`/wbk`
- **备注**：别名 /酒鉴 /酿酒图鉴 /图鉴 /wbk；reload 需 winebook.admin

### `/winebuyer` — 打开酒水收购界面（玩家卖酒）

- **语法**：`/winebuyer [list｜reload｜reset]`

- **示例**：

```
/winebuyer
```

- **别名**：`/wb`、`/收酒`、`/酒收`
- **备注**：别名 /wb /收酒 /酒收；reload、reset 需 winebuyer.admin

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/winebook reload` | 重载图鉴配置与配方同步 | `/winebook reload` |
| `/winebuyer list` | 文本列出可收购配方与价格 | `/winebuyer list` |
| `/winebuyer reload` | 重载收购配置 | `/winebuyer reload` |
| `/winebuyer reset` | 重置收购相关计数/配额（把配置恢复默认统计） | `/winebuyer reset` |

## 注意事项

::: warning
- 收购价格与图鉴内容自动跟随主酿造插件的 recipes.yml（每 30 秒检测一次），别在本插件里硬改配方。
- reset 会清掉收购侧的记录，跑之前先备份 `plugins/WineSuite/` 下的配置。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `winebook.admin` | 重载图鉴 | op |
| `winebook.use` | 使用酿酒图鉴（默认开启） | True |
| `winebuyer.admin` | 重载/重置收购配置 | op |
| `winebuyer.use` | 使用酒水收购（默认开启） | True |
