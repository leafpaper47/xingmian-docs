---
title: MeteorShowers
createTime: 2026/10/24
---

# 流星雨 · MeteorShowers

> 分类 🗺️ 世界与地图 · 版本 `1.0.0` · 指令 1 条 · api-version `1.21`

::: tip 生存向随机流星雨事件：预警、陨石坑、战利品
MeteorShowers 为生存服提供随机流星雨事件，触发时会有警告提示，陨石落地后留下陨石坑并散落战利品，形成风险与收益并存的资源机会。管理端只有一条主命令，用来开关自动触发、热重载配置和手动召唤一次事件，适合当作长期生存服的随机惊喜活动。该插件属小众/自研类，除命令里列出的动作外不要假设有更多能力。
:::

## 什么时候会用到它

- 给长期生存服增加随机可期的资源事件
- 在活动时段手动召唤流星雨制造话题
- 建造期或活动期临时关闭自动触发
- 改完配置后热重载生效，不必重启服务器

## 上手流程

1. 确认插件已正常加载，用拥有 meteorshowers.admin 权限的账号做测试
2. 查看配置文件中的触发间隔、陨石坑范围与战利品表，按服务器节奏调整
3. 执行重载让改动生效，再手动召唤一次确认警告与陨石坑都正常
4. 确认无误后才放开自动触发；有大型建造或活动时先临时关闭

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
/meteorshowers summon
```

- **别名**：`/ms`、`/meteor`
- **权限**：`meteorshowers.admin`
- **备注**：别名 /ms 与 /meteor；需要 meteorshowers.admin 权限（默认仅 OP）。三个动作的细节行为与是否接受更多参数，以游戏内 help 为准。

## 注意事项

::: warning
- 本插件属小众/自研类，toggle、reload、summon 之外是否还有别的参数或用法，具体参数以游戏内 help 为准。
- 陨石坑会真实破坏地形，开自动触发前务必确认已有 CoreProtect 之类的回滚手段。
- 手动 summon 在人多时可能砸到玩家或建筑，建议先广播提醒并自行挑好位置。
- 重载配置不一定重置正在进行的倒计时，改完建议观察一轮日志再放自动触发。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `meteorshowers.admin` | 访问所有MeteorShowers管理命令 | op |

## 相关插件

[CoreProtect](/commands/audit/coreprotect.md)
