---
title: PlayerTask
createTime: 2026/10/24
---

# 玩家任务 · PlayerTask

> 分类 🧰 基础工具 · 版本 `2.12.4` · 指令 1 条 · api-version `1.13`

::: tip 任务系统
每日任务 + NPC 任务的整套玩法：按挖掘/击杀/合成等目标派任务，完成后领奖励并用任务币在商城换东西，稀有权重按权限分档。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 玩家看今天任务 | /plk open | 默认玩家入口，别名 /playerTask |
| 开任务币商城 | /plk shop | 奖励货币在这里花 |
| 手动刷新今日任务 | /plk getToday | 管理用；配合 /plk delToday 先删再刷 |
| 改完配置生效 | /plk reload | 改目标/奖励/稀有度都要重载 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/playerTask` | 玩家任务主指令：任务界面、商城与管理子指令<br>别名 `/plk` | `/plk <子指令>` | — |

## 指令详解

### `/playerTask` — 玩家任务主指令：任务界面、商城与管理子指令

- **语法**：`/plk <子指令>`

- **示例**：

```
/plk open
```

- **别名**：`/plk`
- **备注**：别名 /plk；管理类子指令名与权限后缀一一对应（见下表与权限页）

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/plk open` | 打开玩家任务界面（玩家入口，默认有权限） | `/plk open` |
| `/plk shop` | 打开任务币商城（默认有权限） | `/plk shop` |
| `/plk openMeNpcTask` | 查看自己已领取的 NPC 任务 | `/plk openMeNpcTask` |
| `/plk create` | 创建任务 | `/plk create` |
| `/plk view` | 任务管理总表：查看/编辑/删除已有任务 | `/plk view` |
| `/plk addDemand` | 给任务新增目标（挖多少、杀几只、合成几次） | `/plk addDemand` |
| `/plk addReward` | 给任务新增奖励（物品/命令/任务币） | `/plk addReward` |
| `/plk addShop` | 新增任务币商城商品 | `/plk addShop` |
| `/plk addNpcTask` | 新增 NPC 任务 | `/plk addNpcTask` |
| `/plk edit` | 编辑任务的名称、描述、稀有度等字段 | `/plk edit` |
| `/plk setRarity` | 设置任务稀有度（普通/高级/稀有/罕见/史诗/神话） | `/plk setRarity` |
| `/plk setDescription` | 设置任务描述文本 | `/plk setDescription` |
| `/plk changeItem` | 把某个任务 ID 转成可发放的物品 | `/plk changeItem` |
| `/plk coin` | 任务币处理：给玩家加减任务币 | `/plk coin` |
| `/plk getToday` | 立即生成今日任务 | `/plk getToday` |
| `/plk delToday` | 删除今日已生成的任务 | `/plk delToday` |
| `/plk openNpc` | 打开 NPC 任务菜单 | `/plk openNpc` |
| `/plk setEnableCommand` | 设置领取 NPC 任务时执行的命令 | `/plk setEnableCommand` |
| `/plk import` | 从配置文件批量导入任务 | `/plk import` |
| `/plk convert` | 转换数据源（换存档方式时用，先备份） | `/plk convert` |
| `/plk reload` | 重载配置与任务数据 | `/plk reload` |

## 注意事项

::: warning
- convert 会搬迁数据源，操作前先整目录备份 plugins/PlayerTask/。
- 稀有度是按权限 playerTask.rarity.&lt;稀有度&gt;.&lt;类型&gt; 分档的，玩家抽不到史诗通常是没给权限。
- getToday / delToday 直接影响当天任务，误删后玩家当天进度会一起没。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `playerTask.*` | 玩家任务插件 | — |
| `playerTask.addDemand` | 新增任务目标 | op |
| `playerTask.addNpcTask` | 新增NPC任务 | op |
| `playerTask.addReward` | 新增任务奖励 | op |
| `playerTask.addShop` | 新增任务币商品 | op |
| `playerTask.changeItem` | 将对应id的任务转化成物品 | op |
| `playerTask.coin` | 处理任务币 | op |
| `playerTask.convert` | 转换数据源 | op |
| `playerTask.create` | 创建任务 | op |
| `playerTask.delToday` | 删除今日任务 | op |
| `playerTask.edit` | 编辑任务 | op |
| `playerTask.getToday` | 立即生成今日任务 | op |
| `playerTask.import` | 从配置文件导入任务 | op |
| `playerTask.open` | 查看任务（默认开启） | True |
| `playerTask.openMeNpcTask` | 打开自己领取的的NPC任务列表 | op |
| `playerTask.openNpc` | 打开NPC菜单 | op |
| `playerTask.reload` | 重载配置 | op |
| `playerTask.setDescription` | 设置任务描述 | op |
| `playerTask.setEnableCommand` | 设置领取npc任务执行的命令 | op |
| `playerTask.setRarity` | 设置稀有度 | op |
| `playerTask.shop` | 查看任务币商城（默认开启） | True |
| `playerTask.view` | 管理任务 | op |
