---
title: DummyPool
createTime: 2026/10/24
---

# DummyPool

> 版本 `1.1.1-leaf` · 指令 2 条 · api-version `1.21` · 文件 `DummyPool-1.1.1-leaf.jar`

DummyPool 台球插件（LeafPaper 分支：补齐权限门控、跨台串扰与实体泄漏修复）

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/dummypool help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/dummypool` | DummyPool 台球插件主命令 | — |
| `/dump` | DummyPool 台球插件主命令（别名） | — |

## 详细用法

### /dummypool

- **说明**：DummyPool 台球插件主命令
- **用法**：`/&lt;command&gt; &lt;subcommand&gt; ...`
- **别名**：`/dump`

### /dump

- **说明**：DummyPool 台球插件主命令（别名）
- **用法**：`/&lt;command&gt; &lt;subcommand&gt; ...`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `dummypool.admin` | 执行管理命令（reloadconfig / reloadmessages） | op |
| `dummypool.ball` | 领取球物品（/dummypool ball get）——默认仅 OP，防止普通玩家刷球 | op |
| `dummypool.create` | 创建球台 | op |
| `dummypool.remove` | 删除球台 | op |
| `dummypool.use` | 使用 DummyPool 的基础功能（打开界面、参与对局、查看球台列表） | True |
