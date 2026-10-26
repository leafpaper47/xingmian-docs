---
title: spark
createTime: 2026/10/24
---

# 性能分析 · spark

> 分类 📊 记录与性能 · 版本 `1.10.175` · 指令 1 条 · api-version `1.13`

::: tip 服务器卡顿排查与性能采样工具
spark 是给服主和管理员用的性能诊断插件，能在不关服的情况下采集 CPU 占用、TPS、单个线程的调用火焰图，定位到底是哪个插件或哪个实体在拖慢服务器。它输出的是一份可以网页打开的火焰图报告，比老版 Timings 更细，是目前主流服默认装的排查工具。和 Paper 服务端自带诊断、以及权限插件配合使用即可。
:::

## 什么时候会用到它

- 玩家反馈服务器一阵一阵卡顿、TPS 掉到 15 以下，需要找出真凶插件
- 想知道某个红石/刷怪塔/实体农场是不是主要的性能开销来源
- 排查内存吃紧、怀疑有内存泄漏时查看堆内存占用情况
- 优化前后对比：改完配置或删插件后再采样一次，看耗时占比有没有下降

## 上手流程

1. 确认玩家有 spark 权限（管理员一般给 spark 或 op），先在控制台或游戏内执行 /spark tps 看当前 TPS 与每刻耗时是否异常
2. 卡顿复现时执行 /spark profiler start 开始采样，让服务器在高负载状态下跑 30 秒到 1 分钟
3. 执行 /spark profiler stop 结束采样，它会自动上传并返回一个网页链接，用浏览器打开看火焰图
4. 在火焰图里按耗时排序找最粗的那条调用链，判断是哪个插件、哪个事件或哪类实体，再针对性地改配置或报给插件作者

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/spark` | 性能分析主命令，所有诊断功能都通过它的子指令调用 | `/spark` | — |

## 指令详解

### `/spark` — 性能分析主命令，所有诊断功能都通过它的子指令调用

- **语法**：`/spark`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子指令` | 必填 | 要执行的功能，如 profiler 采样、tps 看刻率、health 看健康报告、ping 看延迟等 |


- **示例**：

```
/spark tps
/spark profiler start
/spark profiler stop
/spark health
```

- **备注**：不带参数直接输入会列出所有子指令和用法。profiler 的结果会上传到 spark 官方网页，生成链接后需要自己保存。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `profiler start` | 开始采样服务器性能，默认采到手动 stop 为止 | `/spark profiler start` |
| `profiler start --timeout 60` | 开始采样并在 60 秒后自动结束，适合卡顿持续时无人值守 | `/spark profiler start --timeout 60` |
| `profiler start --timeout 60 --only-ticks-over 100` | 只记录单刻耗时超过 100 毫秒的慢刻，抓卡顿峰值更精准 | `/spark profiler start --timeout 60 --only-ticks-over 100` |
| `profiler start --thread 服务器主线程名` | 只采指定线程，例如只看主线程 World 线程的调用 | `/spark profiler start --thread Server thread` |
| `profiler start --alloc` | 改为采样内存分配，用来查谁在疯狂创建对象导致 GC 频繁 | `/spark profiler start --alloc --timeout 30` |
| `profiler stop` | 结束采样并上传，返回网页版火焰图链接 | `/spark profiler stop` |
| `profiler info` | 查看当前正在进行的采样状态和已运行时长 | `/spark profiler info` |
| `profiler cancel` | 取消当前采样且不上传结果 | `/spark profiler cancel` |
| `profiler check` | 查询某个采样任务的进度或结果状态 | `/spark profiler check` |
| `tps` | 查看当前 TPS、每刻耗时和最近一段时间的波动 | `/spark tps` |
| `health` | 生成一份服务器健康报告，汇总 TPS、CPU、内存与磁盘占用 | `/spark health` |
| `health --memory` | 健康报告附带堆内存细分，便于判断是否内存吃紧 | `/spark health --memory` |
| `tickmonitor` | 持续监控每一刻的耗时，实时打印慢刻的日志 | `/spark tickmonitor` |
| `tickmonitor --threshold 50` | 只报告耗时超过 50 毫秒的刻，过滤掉正常波动 | `/spark tickmonitor --threshold 50` |
| `ping` | 查看玩家与服务器的网络延迟情况 | `/spark ping` |
| `ping --interval 10` | 每 10 秒输出一次延迟采样结果 | `/spark ping --interval 10` |
| `gc` | 手动触发一次垃圾回收，观察内存是否能被正常释放 | `/spark gc` |
| `heap` | 导出堆内存快照文件，用于分析内存泄漏 | `/spark heap` |
| `heap --live` | 导出前先做一次全量 GC，只保留存活对象，快照更干净 | `/spark heap --live` |
| `heapsummary` | 输出一份堆内存占用汇总，比完整快照轻量很多 | `/spark heapsummary` |
| `viewer` | 查看或打开 spark 网页查看器的地址 | `/spark viewer` |

## 注意事项

::: warning
- profiler 采样本身有开销，建议只在卡顿复现时开 30 到 60 秒，别长期挂着；线上高峰期采样会让卡顿更明显
- 采样结果默认上传到第三方网站生成链接，如果服务器有保密要求，注意不要把含敏感插件名、玩家名的链接公开分享
- 看火焰图不要只盯绝对值最大的那一项，很多是原版世界运算或区块加载，要先区分开原版开销和插件开销再动手
- 权限是按子指令细分的（如 spark.profiler、spark.tps），只想给管理员看 TPS 就单独给对应节点，不要一律给 spark
:::

## 相关插件

[PlaceholderAPI](/commands/config/placeholderapi.md)、[LuckPerms](/commands/core/luckperms.md)
