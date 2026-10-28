---
title: KaleidoscopeCookeryPlugin
createTime: 2026/10/24
---

# 森罗厨房 · KaleidoscopeCookeryPlugin

> 分类 🧩 脚本与菜单 · 版本 `1.3.0` · 指令 1 条 · api-version `1.21`

::: tip 森罗厨房菜谱系统
森罗厨房（KaleidoscopeCookery）是把自定义食物与烹饪配方做成菜单的服务端插件，玩家在一个图形菜单里就能查到每道菜要什么材料、怎么做。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 看食谱菜单 | /kcrecipe | 加 edit 进编辑模式 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/kcrecipe` | 打开森罗厨房食谱菜单，加 edit 进入编辑模式<br>别名 `/kcfood` | `/kcrecipe [edit]` | — |

## 指令详解

### `/kcrecipe` — 打开森罗厨房食谱菜单，加 edit 进入编辑模式

- **语法**：`/kcrecipe [edit]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `edit` | 可选 | 可选参数，加上后进入食谱编辑模式，需要额外的编辑权限 |


- **示例**：

```
/kcrecipe
/kcrecipe edit
```

- **别名**：`/kcfood`
- **备注**：别名 /kcfood，效果相同。浏览菜单需要 kaleidoscopecookery.recipe.browse，进入编辑模式需要 kaleidoscopeco…

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `kcrecipe edit` | 进入食谱编辑模式，用于维护菜谱内容 | `/kcrecipe edit` |

## 注意事项

::: warning
- 浏览和编辑是两个独立权限，普通玩家只给 kaleidoscopecookery.recipe.browse，否则他能直接改你的菜谱
- 编辑模式里改完一定要按插件要求保存并重载，重载前先小退或提醒在线玩家，避免菜单读到半截数据
- 若菜单里出现空白图标或点了没反应，通常是配置里引用了不存在的物品或客户端资源包没装，先看服务端日志报错再改配置
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `kaleidoscopecookery.recipe.browse` | 允许玩家用 /kcrecipe 浏览全部食谱 | op |
| `kaleidoscopecookery.recipe.edit` | 允许用 /kcrecipe edit 编辑食谱 | op |
