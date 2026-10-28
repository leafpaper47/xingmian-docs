---
title: CraftBench
createTime: 2026/10/24
---

# 随身工作台 · CraftBench

> 分类 🧰 基础工具 · 版本 `1.1.14` · 指令 2 条 · api-version `1.21`

::: tip 随身 5×5 合成台与配
给玩家一个随时可开的 5×5 大工作台，配方不限形状、不消耗经济，方便在野外或副本地图里直接合成。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 随时打开合成台 | /craftbench | 5×5 随身界面 |
| 增删自定义配方 | /craftbenchadmin | 改完让玩家重开界面 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/craftbench` | 打开 5×5 随身合成台界面 | `/craftbench` | `craftbench.use` |
| `/craftbenchadmin` | 打开配方编辑界面，增删自定义配方 | `/craftbenchadmin` | `craftbench.admin` |

## 指令详解

### `/craftbench` — 打开 5×5 随身合成台界面

- **语法**：`/craftbench`

- **示例**：

```
/craftbench
```

- **权限**：`craftbench.use`
- **备注**：默认权限 craftbench.use 对所有人开放；若关掉该权限，玩家执行会提示无权限。合成台为纯界面，关闭界面时请注意材料是否已取出。

### `/craftbenchadmin` — 打开配方编辑界面，增删自定义配方

- **语法**：`/craftbenchadmin`

- **示例**：

```
/craftbenchadmin
```

- **权限**：`craftbench.admin`
- **备注**：需要 craftbench.admin（默认仅 OP）。这是纯 GUI 操作，不需要手写配置；改完配方后最好让玩家测一次实际合成结果，确认产物与数量正确。

## 注意事项

::: warning
- 配方改动属于服务端数据，改完后建议重载插件或重启服务器，避免只改了界面、合成判定没更新
- 只给信任的管理员 craftbench.admin：能改配方就等于能定义任意物品产出，权限外泄会导致刷物品
- 涉及 CraftEngine 等自定义物品的配方，需确认对应物品已正确注册，否则合成会失败或产出异常
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `craftbench.admin` | 允许管理配方 | op |
| `craftbench.use` | 允许使用合成台 | True |
