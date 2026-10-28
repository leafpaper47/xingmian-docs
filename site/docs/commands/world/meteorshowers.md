---
title: MeteorShowers
createTime: 2026/10/24
---

# 流星雨 · MeteorShowers

> 分类 🗺️ 世界与地图 · 版本 `1.0.0` · 指令 1 条 · api-version `1.21`

::: tip 随机流星雨事件与预警
MeteorShowers 为生存服提供随机流星雨事件，触发时会有警告提示，陨石落地后留下陨石坑并散落战利品，形成风险与收益并存的资源机会。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 开关自动流星雨 | /meteorshowers toggle | — |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/meteorshowers` | 管理流星雨事件：开关自动触发、重载配置、手动召唤<br>别名 `/ms`、`/meteor` | `/meteorshowers toggle｜reload｜summon [player]` | `meteorshowers.admin` |

## 指令详解

### `/meteorshowers` — 管理流星雨事件：开关自动触发、重载配置、手动召唤

- **语法**：`/meteorshowers toggle｜reload｜summon [player]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `toggle｜reload｜summon` | 必填 | 必填动作：toggle 切换事件开关，reload 重新加载配置，summon 立刻召唤一次流星雨 |
| `player` | 可选 | 可选参数，通常用于指定这次召唤所针对的玩家；留空时按插件默认规则处理 |


- **示例**：

```
/meteorshowers toggle
/meteorshowers reload
```

- **别名**：`/ms`、`/meteor`
- **权限**：`meteorshowers.admin`
- **备注**：别名 /ms 与 /meteor；需要 meteorshowers.admin 权限（默认仅 OP）。三个动作的细节行为与是否接受更多参数，以游戏内 help …

## 注意事项

::: warning
- 本插件属小众/自研类，toggle、reload、summon 之外是否还有别的参数或用法，具体参数以游戏内 help 为准。
- 陨石坑会真实破坏地形，开自动触发前务必确认已有 CoreProtect 之类的回滚手段。
- 手动 summon 在人多时可能砸到玩家或建筑，建议先广播提醒并自行挑好位置。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `meteorshowers.admin` | 访问所有MeteorShowers管理命令 | op |
