---
title: StarPact
createTime: 2026/10/24
---

# 星契社交 · StarPact

> 分类 ⚔️ 战斗与 RPG · 版本 `0.6.0` · 指令 16 条 · api-version `1.21`

::: tip 关系契约社交
星冕自研社交核心：结契（恋人/死党/闺蜜等）、亲密度分级解锁专属频道、单向传送、双人传送点、濒死救助，全在 GUI 内操作；本页含全部管理子指令。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 打开契约主界面 | /xzqy | 别名 /pact、/starpact |
| 选性别 | /gender | 别名 /xb、/xingbie，/xzqyxb 也同效 |
| 改完 config.yml 生效 | /xzqy admin reload | 立即回显「已重载 config.yml」 |
| 补发喜糖 | /xzqy admin candy Steve 5 | 数量默认 1，上限 64 |
| 给玩家发求婚戒指 | /xzqy admin ring Steve star_ring | 第三段填戒指 id，不是序号 |
| 清空全服羁绊数据 | /xzqy admin wipedata confirm | 必须带 confirm，且是全服不是单人 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/gender` | 打开性别选择界面，选完自动关闭<br>别名 `/xb`、`/xingbie` | `/gender` | — |
| `/xzqy` | 打开星之契约主界面（结契、关系列表、亲密度、默契题）<br>别名 `/pact`、`/starpact` | `/xzqy` | — |
| `/xzqy admin` | 打印全部管理子指令用法 | — | — |
| `/xzqy admin reload` | 重载 config.yml（席位价、亲密度阈值、冷却、文案全生效） | — | — |
| `/xzqy admin save` | 把内存里的羁绊数据立即写进 data.yml | — | — |
| `/xzqy admin worlds` | 打印服务器真实世界名，用来填两份禁用名单 | — | — |
| `/xzqy admin info` | 查看某玩家的羁绊列表（含认证伴侣）与星点余额 | `/xzqy admin info <玩家>` | — |
| `/xzqy admin candy` | 发喜糖道具（右键随机开奖：20% 星钻 1-10，否则星点 1-100） | `/xzqy admin candy [玩家] [数量]` | — |
| `/xzqy admin ring` | 发一枚求婚戒指到玩家背包 | `/xzqy admin ring <玩家> <戒指 id>` | — |
| `/xzqy admin gift` | 往玩家「我的礼物」收件箱补一份礼物 | `/xzqy admin gift <赠送人> <收件人> <礼物 id>` | — |
| `/xzqy admin marry` | 把已有羁绊的两人直接认证为伴侣 | `/xzqy admin marry <玩家A> <玩家B>` | — |
| `/xzqy admin card` | 打印该玩家的聊天卡片原文（%starpact_card% 解析结果） | `/xzqy admin card <玩家>` | — |
| `/xzqy admin quiz` | 打印今天抽到的 3 道默契题 | — | — |
| `/xzqy admin setrescuehome` | 把「濒死下线回归点」设到脚下并写入 config.yml | — | — |
| `/xzqy admin wipedata` | 清空全服羁绊/缔结请求，并把关系位重置为 1 | `/xzqy admin wipedata confirm` | — |
| `/xzqyxb` | /gender 的备用同义入口 | `/xzqyxb` | — |

## 指令详解

### `/gender` — 打开性别选择界面，选完自动关闭

- **语法**：`/gender`

- **示例**：

```
/gender
```

- **别名**：`/xb`、`/xingbie`
- **备注**：别名 /xb、/xingbie；界面里点「我的性别」可改回未知

### `/xzqy` — 打开星之契约主界面（结契、关系列表、亲密度、默契题）

- **语法**：`/xzqy`

- **示例**：

```
/xzqy
```

- **别名**：`/pact`、`/starpact`
- **备注**：别名 /pact、/starpact；控制台执行只提示「只有玩家可以打开界面」

### `/xzqy admin` — 打印全部管理子指令用法


- **示例**：

```
/xzqy admin
```

- **备注**：需 starpact.admin 或 OP；忘了子指令就敲这条看清单

### `/xzqy admin reload` — 重载 config.yml（席位价、亲密度阈值、冷却、文案全生效）


- **示例**：

```
/xzqy admin reload
```

- **备注**：改配置后必做，回显「已重载 config.yml」

### `/xzqy admin save` — 把内存里的羁绊数据立即写进 data.yml


- **示例**：

```
/xzqy admin save
```

- **备注**：手动改 data.yml 前先停服或先 save，否则被内存数据覆盖

### `/xzqy admin worlds` — 打印服务器真实世界名，用来填两份禁用名单


- **示例**：

```
/xzqy admin worlds
```

- **备注**：填 teleport.blocked-worlds 与 rescue.blocked-worlds，两份互相独立（rpg 可救助、竞技场禁救助）

### `/xzqy admin info` — 查看某玩家的羁绊列表（含认证伴侣）与星点余额

- **语法**：`/xzqy admin info <玩家>`

- **示例**：

```
/xzqy admin info Steve
```

- **备注**：玩家名必填，缺了回显「缺少玩家名」

### `/xzqy admin candy` — 发喜糖道具（右键随机开奖：20% 星钻 1-10，否则星点 1-100）

- **语法**：`/xzqy admin candy [玩家] [数量]`

- **示例**：

```
/xzqy admin candy Steve 5
```

- **备注**：省略玩家=发给自己（控制台必须写玩家）；数量默认 1，超过 64 按 64

### `/xzqy admin ring` — 发一枚求婚戒指到玩家背包

- **语法**：`/xzqy admin ring <玩家> <戒指 id>`

- **示例**：

```
/xzqy admin ring Steve star_ring
```

- **备注**：第三段填 id 不是序号：star_ring 紫耀5200 / galaxy_ring 星河13140 / eternal_ring 誓约之翼52000；背包满会掉脚下

### `/xzqy admin gift` — 往玩家「我的礼物」收件箱补一份礼物

- **语法**：`/xzqy admin gift <赠送人> <收件人> <礼物 id>`

- **示例**：

```
/xzqy admin gift Alex Steve star_bouquet
```

- **备注**：id 取自 gift.items：star_bouquet/star_watch/star_stamp/eternal_core；两人不能同一人；不扣星点

### `/xzqy admin marry` — 把已有羁绊的两人直接认证为伴侣

- **语法**：`/xzqy admin marry <玩家A> <玩家B>`

- **示例**：

```
/xzqy admin marry Alex Steve
```

- **备注**：不会新建关系，先有羁绊才行，否则回显「这两人之间没有羁绊」；支持离线玩家名；每人上限 marry.partner-max=1

### `/xzqy admin card` — 打印该玩家的聊天卡片原文（%starpact_card% 解析结果）

- **语法**：`/xzqy admin card <玩家>`

- **示例**：

```
/xzqy admin card Steve
```

- **备注**：必须装 PlaceholderAPI，否则回显「不可用」；卡片里的 &lt;newline&gt; 就是换行

### `/xzqy admin quiz` — 打印今天抽到的 3 道默契题


- **示例**：

```
/xzqy admin quiz
```

- **备注**：无参数；题库在 config.yml 的 intimacy.quiz.questions，格式 问题｜选项A｜选项B

### `/xzqy admin setrescuehome` — 把「濒死下线回归点」设到脚下并写入 config.yml


- **示例**：

```
/xzqy admin setrescuehome
```

- **备注**：必须站在主城、用游戏内账号执行；即写即生效，不用重启

### `/xzqy admin wipedata` — 清空全服羁绊/缔结请求，并把关系位重置为 1

- **语法**：`/xzqy admin wipedata confirm`

- **示例**：

```
/xzqy admin wipedata confirm
```

- **备注**：不带 confirm 只打印警告不执行；保留性别/游戏时长/首次进服时间，其余全删并立即落盘

### `/xzqyxb` — /gender 的备用同义入口

- **语法**：`/xzqyxb`

- **示例**：

```
/xzqyxb
```

- **备注**：功能与 /gender 完全一致

## 注意事项

::: warning
- 改完 config.yml 必须 /xzqy admin reload；动亲密度阈值或席位价格会立刻影响全服已有关系，别在高峰期改。
- /xzqy admin wipedata 是**全服**清空（不是单人），执行前把 plugins/StarPact/data.yml 备份一份。
- 亲密度只增不减，且 /kiss 与「蹲下+右键摸头」由 Skript 脚本触发、本插件只旁听：摸头不涨点先查 Skript，不是插件坏了。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `starpact.admin` | 星之契约管理权限（/xzqy admin 全部子指令，未给则默认 OP） | op |
