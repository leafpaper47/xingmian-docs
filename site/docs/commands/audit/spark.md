---
title: spark
createTime: 2026/10/24
---

# 性能分析 · spark

> 分类 📊 记录与性能 · 版本 `1.10.175` · 指令 1 条 · api-version `1.13`

::: tip 性能剖析
卡服时先开它：采样火焰图定位是哪个插件/哪段代码在吃 CPU，还能看 TPS、内存与 GC、堆转储。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 卡了，先看整体 | /spark tps | TPS 与内存概览，最轻量 |
| 找出吃 CPU 的插件 | /spark profiler start | 跑 30 秒后 /spark profiler stop 拿链接 |
| 看单次卡顿尖峰 | /spark tickmonitor --threshold 100 | 只报超过阈值的 tick |
| 内存异常/疑似泄漏 | /spark heapsummary | 生成堆摘要，链接在控制台 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/spark` | 性能剖析主指令 | `/spark <tps｜profiler｜tickmonitor｜health｜heapsummar…` | — |

## 指令详解

### `/spark` — 性能剖析主指令

- **语法**：`/spark <tps｜profiler｜tickmonitor｜health｜heapsummary｜gc｜activitylog｜help>`

- **示例**：

```
/spark tps
```

- **备注**：命令名 spark，别名 /spark

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/spark tps` | 查看 TPS / MSPT / CPU 与内存概况 | `/spark tps` |
| `/spark profiler start` | 开始 CPU 采样（默认 30 秒后自动停） | `/spark profiler start --timeout 60` |
| `/spark profiler stop` | 停止采样并输出分析链接 | `/spark profiler stop` |
| `/spark profiler open` | 直接打开上次采样的网页结果 | `/spark profiler open` |
| `/spark tickmonitor` | 监控超时 tick，定位卡顿尖峰 | `/spark tickmonitor --threshold 100` |
| `/spark health` | 查看服务器健康报告（采样/内存/线程） | `/spark health` |
| `/spark heapsummary` | 生成堆内存摘要（查内存泄漏） | `/spark heapsummary` |
| `/spark gc` | 查看 GC 频率与停顿情况 | `/spark gc` |
| `/spark activitylog` | 按时间段查看服务器活动日志统计 | `/spark activitylog` |

## 注意事项

::: warning
- profiler 采样本身有开销，别在高峰期长时间开着；一般 30–60 秒足够定位。
- 采样结果是「谁吃 CPU」，不等于「谁引起卡顿」，低 CPU 卡顿要看 tickmonitor 与 GC。
- 结果链接是公开的 spark 网页，别在里面暴露玩家隐私信息（聊天内容不会进去，但插件名/世界名会）。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `spark` | 使用 spark 全部指令 | — |
| `spark.heapsummary` | 生成堆摘要 | — |
| `spark.profiler` | 使用 profiler | — |
