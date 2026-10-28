---
title: XingmianElement
createTime: 2026/10/24
---

# 元素系统 · XingmianElement

> 分类 ⚔️ 战斗与成长 · 版本 `0.1.23` · 指令 2 条 · api-version `1.21`

::: tip 元素职业
星冕自研元素职业系统：10 级选元素发法杖、20 级转职，五种元素各有技能与护盾，RPG BOSS 也带元素属性。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 玩家选元素/转职 | /element | 界面里操作；10 级选元素、20 级可转职 |
| 查个人档案 | /element info | 等级、经验、元素、护盾都在这 |
| 给玩家补经验 | /element exp Steve 500 | 可填负数扣经验 |
| 清掉玩家元素数据 | /element reset Steve item | 加 item 连背包法杖/技能卡一起收 |
| 元素护盾没显示黄心 | /element shield 20 | 玩家自己跑，20 点=10 颗黄心 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/element` | 元素之力主入口：界面、选元素、转职、档案与管理员操作<br>别名 `/elem`、`/ys` | `/element [info｜list｜choose <元素>｜switch <元素>｜exp｜le…` | — |
| `/xmbe` | 元素 BOSS 调试：强制下一只 BOSS 带几个元素 | `/xmbe <next <1-5>｜next off｜info>` | `xingmianelement.admin` |

## 指令详解

### `/element` — 元素之力主入口：界面、选元素、转职、档案与管理员操作

- **语法**：`/element [info｜list｜choose <元素>｜switch <元素>｜exp｜level｜reset｜reload｜debug｜shield]`

- **示例**：

```
/element
/element list
```

- **别名**：`/elem`、`/ys`
- **备注**：别名 /elem、/ys；不带参数= 打开界面；管理类子指令要 xingmianelement.admin

### `/xmbe` — 元素 BOSS 调试：强制下一只 BOSS 带几个元素

- **语法**：`/xmbe <next <1-5>｜next off｜info>`

- **示例**：

```
/xmbe next 3
/xmbe info
```

- **权限**：`xingmianelement.admin`
- **备注**：只作用于「下一只 roll 出来的 BOSS」，不改全服概率

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/element choose <元素>` | 10 级起选择元素，成功发放对应法杖 | `/element choose 火` |
| `/element switch <元素>` | 20 级起转职，有冷却（默认 36 小时） | `/element switch 冰` |
| `/element bt` | 玩家自己突破元素等级上限，控制台不可用 | `/element bt` |
| `/element list` | 列出五种元素的定位与被动 | `/element list` |
| `/element info` | 打开个人档案界面（等级/经验/元素/护盾） | `/element info` |
| `/element exp <玩家> <数量>` | 调整元素经验，可为负数 | `/element exp Steve 500` |
| `/element level <玩家> <等级>` | 直接把元素等级设为指定值（别名 setlevel） | `/element level Steve 20` |
| `/element forceswitch <玩家> <元素>` | 管理员强制把某玩家转成指定元素（别名 强转） | `/element forceswitch Steve 雷` |
| `/element reset <玩家> [item]` | 清等级/经验/元素/冷却/领卡记录；加 item 连法杖与技能卡一起收（别名 clear、wipe、清档） | `/element reset Steve item` |
| `/element reload` | 重载配置与界面文案，不用重启 | `/element reload` |
| `/element debug` | 自检面板：事件数、认成法杖数、放出去数、最近一次（必须游戏内跑） | `/element debug` |
| `/element shield [数值]` | 手动测试元素护盾吸收，数值=护盾点数 | `/element shield 20` |
| `/xmbe next <1-5>` | 强制下一只刷出的 BOSS 带 N 种元素 | `/xmbe next 3` |
| `/xmbe next off` | 取消强制，恢复按权重抽 | `/xmbe next off` |
| `/xmbe info` | 查看元素数量权重与当前强制值 | `/xmbe info` |

## 注意事项

::: warning
- 转职有冷却（默认 36 小时），玩家「转不了」先查冷却再查权限；强转 /element forceswitch 是管理员旁路。
- level 只改元素等级，不动原版经验等级，两套等级体系别混。
- reset 会先写 playerdata-backup.yml；控制台报「写备份失败」先修 plugins 目录写权限，否则清档没备份。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `xingmianelement.admin` | 管理权限：exp / level / forceswitch / reset / reload / debug / xmbe | op |
