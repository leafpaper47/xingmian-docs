---
title: PlayerTask
createTime: 2026/10/24
---

# 玩家任务 · PlayerTask

> 分类 🧰 基础工具 · 版本 `2.12.4` · 指令 1 条 · api-version `1.13`

::: tip 每日任务、任务目标与任务币商城系统
PlayerTask 给服务器加一套任务玩法：管理员建好任务，玩家按任务目标去完成，交任务拿奖励和任务币，再用任务币到商城兑换。任务目标、奖励、商品和 NPC 任务都由管理员在后台配置，玩家只需要开界面查看和领取。它属于养成/日常向的粘性插件，常和权限组、经济、NPC 插件一起用，用来给在线时长和重复劳动找点目标。
:::

## 什么时候会用到它

- 想给玩家一套每日/周期任务，让上线有事可做，避免只会刷怪挂机
- 需要一条任务币经济线：完成任务得币，币在任务商城换物品或奖励
- 想让 NPC 发布任务，玩家找 NPC 领任务、交任务，做成一条任务线
- 服里已有任务类插件不好用，想换一套支持自定义目标与稀有度分级的方案

## 上手流程

1. 把插件放进 plugins 目录启动，先用 playerTask.reload 权限确认配置能正常加载
2. 用管理员账号打开插件主界面或执行 /playerTask，按提示进入任务管理相关的菜单
3. 在管理侧先建任务本体，再给它加任务目标与奖励，必要时设置稀有度和任务描述
4. 配置任务币商城商品，确定完成一次任务大致给多少币、商品定多少钱
5. 给玩家侧账号配好查看任务和查看商城的权限，自己用小号实测一遍领任务到交任务的完整流程

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/playerTask` | PlayerTask 主指令，玩家查看任务、管理员进入任务管理<br>别名 `/plk` | `/playerTask` | — |

## 指令详解

### `/playerTask` — PlayerTask 主指令，玩家查看任务、管理员进入任务管理

- **语法**：`/playerTask`

- **示例**：

```
/playerTask
```

- **别名**：`/plk`
- **备注**：别名 plk，可简写为 /plk。这个指令不带参数时通常直接打开界面，具体子指令、参数和菜单路径以游戏内 help 与插件配置文件为准；玩家侧需要 playerTask.open，管理员侧各项操作分别对应 create、view、edit、addDemand、addReward、addShop 等权限节点。

## 注意事项

::: warning
- 具体参数与子指令以游戏内 help 为准，本手册只记录了主指令，不要凭猜测敲子指令
- 权限节点分得很细：查看类默认对玩家开放，创建/编辑/加目标/加奖励/加商品/发任务币等默认仅 OP，给普通管理组授权时按需逐条给，别直接给 playerTask.*
- 改完任务配置后记得用 playerTask.reload 对应的操作重新加载，部分任务数据改动可能需要玩家重新获取今日任务才生效
- 涉及任务币发放、删除今日任务、转换数据源这类操作影响面较大，先在测试服验证再上正式服
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
| `playerTask.coin` | 任务币处理 | op |
| `playerTask.convert` | 转换数据源 | op |
| `playerTask.create` | 创建任务 | op |
| `playerTask.delToday` | 删除今日的任务 | op |
| `playerTask.edit` | 编辑任务 | op |
| `playerTask.getToday` | 立即获取今日任务 | op |
| `playerTask.import` | 从配置文件导入任务 | op |
| `playerTask.open` | 查看任务 | True |
| `playerTask.openMeNpcTask` | 打开自己领取的的NPC任务列表 | op |
| `playerTask.openNpc` | 打开NPC菜单 | op |
| `playerTask.reload` | 重新加载配置 | op |
| `playerTask.setDescription` | 设置任务描述 | op |
| `playerTask.setEnableCommand` | 设置领取npc任务执行的命令 | op |
| `playerTask.setRarity` | 设置稀有度 | op |
| `playerTask.shop` | 查看任务币商城 | True |
| `playerTask.view` | 管理任务 | op |

## 相关插件

[PlaceholderAPI](/commands/config/placeholderapi.md)、[Vault](/commands/core/vault.md)
