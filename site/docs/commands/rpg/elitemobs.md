---
title: EliteMobs
createTime: 2026/10/24
---

# 精英怪物 · EliteMobs

> 分类 ⚔️ 战斗与成长 · 版本 `1.0.0` · 指令 1 条 · api-version `1.21`

::: tip 精英怪物
按配置生成带技能与血条的精英怪/自定义 BOSS，配套地牢、战利品与等级缩放，是 PVE 内容的主要来源。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 看当前精英怪状态 | /elitemobs status | 开关状态、活跃数量与版本 |
| 临时关掉精英怪 | /elitemobs off | 维护/活动时用，不影响已生成的 |
| 手动刷一只 | /elitemobs spawn &lt;怪物id&gt; | 怪物 id 来自 mobs 配置 |
| 改完配置生效 | /elitemobs reload | 重载不会重建已存在的怪 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/elitemobs` | 精英怪主指令：开关、状态、刷怪与重载<br>别名 `/elite`、`/em` | `/elitemobs <on｜off｜toggle｜status｜reload｜spawn>` | `elitemobs.admin` |

## 指令详解

### `/elitemobs` — 精英怪主指令：开关、状态、刷怪与重载

- **语法**：`/elitemobs <on｜off｜toggle｜status｜reload｜spawn>`

- **示例**：

```
/elitemobs status
```

- **别名**：`/elite`、`/em`
- **权限**：`elitemobs.admin`
- **备注**：别名 /elite、/em

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/elitemobs status` | 查看精英怪系统状态（开关、数量、版本） | `/elitemobs status` |
| `/elitemobs on` | 开启精英怪生成 | `/elitemobs on` |
| `/elitemobs off` | 关闭精英怪生成（已存在的不受影响） | `/elitemobs off` |
| `/elitemobs toggle` | 在开/关之间切换 | `/elitemobs toggle` |
| `/elitemobs spawn <怪物id> [等级]` | 在当前位置刷出指定精英怪 | `/elitemobs spawn zombie_boss 50` |
| `/elitemobs reload` | 重载配置、怪物与战利品表 | `/elitemobs reload` |

## 注意事项

::: warning
- off 只停「新生成」，场上已有的精英怪会继续活动，活动结束要连同已生成的怪一起清。
- reload 不会替换已存在的怪，改了怪物属性要让它重新生成才生效。
- 怪物 id 写错时不会报错，只是什么都不刷——排错先 /elitemobs status 看配置是否加载成功。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `elitemobs.admin` | 使用 /elitemobs 全部子指令 | op |
