---
title: CMILib
createTime: 2026/10/24
---

# CMI前置库 · CMILib

> 分类 🛡️ 权限与底座 · 版本 `1.5.9.9` · 指令 1 条 · api-version `1.13`

::: tip 库前置
CMI 系列的公共库，本身没有玩法，只负责给依赖它的插件提供工具类与缓存；出问题基本只在 reload 与缓存层面。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 依赖插件报错 | /cmil compatibility | 先看兼容性检查结果 |
| 缓存异常/数据不刷新 | /cmil clearcache | 清缓存后相关插件需重新加载 |
| 改了 CMILib 配置 | /cmil reload | 重载本身配置 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/cmil` | CMILib 管理指令（只有维护类子指令） | `/cmil <reload｜clearcache｜compatibility>` | — |

## 指令详解

### `/cmil` — CMILib 管理指令（只有维护类子指令）

- **语法**：`/cmil <reload｜clearcache｜compatibility>`

- **示例**：

```
/cmil compatibility
```

- **备注**：命令名 cmil；不要给普通玩家

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/cmil reload` | 重载 CMILib 自身配置 | `/cmil reload` |
| `/cmil clearcache` | 清空内部缓存（玩家数据、材质映射等） | `/cmil clearcache` |
| `/cmil compatibility` | 输出与服务端/其它插件的兼容性检查 | `/cmil compatibility` |

## 注意事项

::: warning
- clearcache 会让依赖它的插件（CMI/CMILib 生态）出现一次数据重读，建议低峰执行。
- CMILib 版本与依赖插件必须匹配，升级时两边一起升，只升一个会出现 NoSuchMethodError。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `cmilib.admin` | 使用 /cmil 维护指令 | — |
