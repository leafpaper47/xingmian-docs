---
title: ALCERecipeViewer
createTime: 2026/10/24
---

# 配方查询 · ALCERecipeViewer

> 分类 🧰 基础工具 · 版本 `1.0.8` · 指令 1 条 · api-version `1.21`

::: tip 按分类浏览和搜索合成配方的合成表查看器
ALCERecipeViewer 提供一个游戏内的合成表界面，让玩家不用查网页就能按分类翻看合成配方，并能搜索某个物品的配方或反查它的用途。它常和自定义物品、自定义合成类插件搭配使用，用来把服里新增的配方直观地展示给玩家。管理员需要维护配方数据时，可用管理权限触发重载。
:::

## 什么时候会用到它

- 玩家问某个物品怎么做，管理员让他自己打开合成表查看，减少反复答疑
- 新玩家上手时想快速了解服里改过或新增的合成配方
- 想反查某个材料都能用来做什么，判断材料价值或规划产出
- 调整或新增配方后，用管理权限重载，让界面显示最新内容

## 上手流程

1. 先确认玩家拥有 alcerecipeviewer.use 权限（该权限默认开启，一般无需额外配置）
2. 让玩家输入 /alcerecipes 打开合成表界面，按分类逐页浏览
3. 需要找特定物品时，用搜索参数带上物品ID，或用用途参数反查该物品能做什么
4. 改了配方数据之后，由管理员执行带 reload 的命令重载，再让玩家重新打开界面确认

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/alcerecipes` | 打开合成表查看器，或按搜索、反查用途、重载数据操作<br>别名 `/alcer`、`/alcebook`、`/alcerecipe` | `/alcerecipes [search｜usage｜reload] [物品ID]` | `alcerecipeviewer.use` |

## 指令详解

### `/alcerecipes` — 打开合成表查看器，或按搜索、反查用途、重载数据操作

- **语法**：`/alcerecipes [search｜usage｜reload] [物品ID]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `search｜usage｜reload` | 可选 | 可选模式：搜索配方、反查物品用途、重载数据；不带则直接打开分类浏览界面，reload 需管理权限 |
| `物品ID` | 可选 | 配合 search 或 usage 使用，指定要查询的物品ID |


- **示例**：

```
/alcerecipes
/alcerecipes search diamond
/alcerecipes usage diamond
/alcerecipes reload
```

- **别名**：`/alcer`、`/alcebook`、`/alcerecipe`
- **权限**：`alcerecipeviewer.use`
- **备注**：别名 alcer、alcebook、alcerecipe 用法完全相同；物品ID 的具体写法以插件配置为准，可用游戏内 help 或界面搜索确认

## 注意事项

::: warning
- 本插件为服内自研/小众插件，具体参数与子指令以游戏内 help 和实际界面为准，不要凭猜测输入参数
- reload 属管理操作，需要 alcerecipeviewer.admin（默认仅 OP），重载会临时占用主线程，建议在无人或少人的时候执行
- 普通玩家权限 alcerecipeviewer.use 默认就是开启的，若玩家打不开界面，先查是不是被权限组显式收回了
- 物品ID 拼写错误时多半不会报错而是查不到结果，先确认ID再判断配方是否缺失
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `alcerecipeviewer.admin` | 允许使用管理命令（重载数据） | op |
| `alcerecipeviewer.use` | 允许使用 /alcerecipes 查看合成配方 | True |
