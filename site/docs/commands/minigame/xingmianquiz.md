---
title: XingmianQuiz
createTime: 2026/10/24
---

# 知识问答 · XingmianQuiz

> 分类 🎲 休闲与小游戏 · 版本 `1.0.0` · 指令 4 条 · api-version `1.21`

::: tip 定时全服答题
按固定间隔向全服广播一道百科题，第一个在聊天框答对的玩家拿星点；题库在 questions.yml，节奏、时限与奖励都在 config.yml。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 看当前题目与倒计时 | /quiz info | 含标准答案与距下一题秒数 |
| 手动换一题 | /quiz now | 公布本题答案并立刻换题，会打断节奏 |
| 改完题库生效 | /quiz reload | 回显题目总数，改 questions.yml 后必做 |
| 调奖励与时限 | /quiz reload | 改 config.yml 的 reward-points、answer-time-seconds |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/quiz` | 答题管理总入口，玩家侧只需在聊天框打出答案 | `/quiz <reload｜now｜info>` | `xingmian.quiz.admin` |
| `/quiz info` | 查看当前题目、标准答案与距离下一题的倒计时 | — | — |
| `/quiz now` | 公布当前题目的答案并立刻换下一题 | — | — |
| `/quiz reload` | 重新载入题库与配置 | — | — |

## 指令详解

### `/quiz` — 答题管理总入口，玩家侧只需在聊天框打出答案

- **语法**：`/quiz <reload｜now｜info>`

- **示例**：

```
/quiz info
```

- **权限**：`xingmian.quiz.admin`
- **备注**：无别名；三条子指令都要 xingmian.quiz.admin（默认 OP）

### `/quiz info` — 查看当前题目、标准答案与距离下一题的倒计时


- **示例**：

```
/quiz info
```

- **备注**：状态分答题中/已答对/已超时/暂无题目；空服时暂停出题，每 30 秒检查一次

### `/quiz now` — 公布当前题目的答案并立刻换下一题


- **示例**：

```
/quiz now
```

- **备注**：会打断 30 分钟固定节奏，活动暖场用完记得对一下 /quiz info

### `/quiz reload` — 重新载入题库与配置


- **示例**：

```
/quiz reload
```

- **备注**：回显「题库已重新载入，共 N 题」；改 config.yml 或 questions.yml 后都要执行

## 注意事项

::: warning
- plugin.yml 里写的「每 15 分钟一道」是旧文案，真实节奏看 config.yml 的 interval-seconds，当前为 1800 秒（30 分钟）；答题情况不影响下一题时间，除非把 answer-then-wait-seconds 从 -1 改成具体秒数。
- 奖励走 Vault 经济的星点（reward-points 当前 50）；Vault 没就绪时会广播「经济系统不可用」且不扣不发，排查先看 Vault 是否正常启用。
- 答案比对由插件自动归一：忽略空格标点大小写，阿拉伯数字与中文数字、全角与半角、繁体与简体互通，所以 alts 只填「意思不同也正确」的写法；改完题库务必 /quiz reload，不重载等于没改。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `xingmian.quiz.admin` | 星冕答题管理员 | op |
