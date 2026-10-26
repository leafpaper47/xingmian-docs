---
title: InvSaver
createTime: 2026/10/24
---

# 背包快照 · InvSaver

> 分类 🧰 基础工具 · 版本 `1.0.1` · 指令 6 条 · api-version `1.20`

::: tip 背包快照保存与回滚工具
把玩家当下的背包整体存成一份快照，需要时再回滚回去，用来兜住误清包、误操作、异常物品这类不可逆事故。它不参与日常游戏玩法，主要给服主和管理员做运维兜底，通常和查号/封禁流程、活动发奖流程配合使用。
:::

## 什么时候会用到它

- 活动、发奖、批量调背包之前，先给关键玩家存一份快照，事后可回退
- 玩家申诉物品丢失或被误清包时，用备份记录核对并恢复原状
- 处罚、查号前先备份现场，保留玩家背包的实际内容作为证据
- 怀疑刷物品或出现异常物品时，先保存再处理，避免证据被覆盖

## 上手流程

1. 给执行人要权限：`invSaver.save`、`invSaver.restore`、`invSaver.list`、`invSaver.preview`、`invSaver.reload` 是五个独立节点，按需下发
2. 出事先存现场：`/invSaver save <玩家>`
3. 核对：`/invSaver list <玩家>` 找到要回滚的那份备份记录编号，再用 `/invSaver preview <玩家> <记录>` 看内容
4. 只想改几个格子：`/invSaver preview <玩家> <记录> -e` 打开可编辑预览，改完直接写回该记录
5. 整体回滚：给玩家当前背包再 save 一份，然后 `/invSaver restore <玩家> <记录>`
6. 改过配置文件后用 `/invSaver reload` 生效，不必重启服务器

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/invSaver` | 背包快照主命令，子功能见下方子指令速查 | `/invSaver <save｜restore｜list｜preview｜reload> ...` | — |
| `/invSaver save` | 保存玩家当前背包，生成一条备份记录 | `/invSaver save <玩家>` | `invSaver.save` |
| `/invSaver restore` | 把玩家背包整体恢复成某条备份记录的内容 | `/invSaver restore <玩家> <备份记录>` | `invSaver.restore` |
| `/invSaver list` | 列出该玩家的全部备份记录 | `/invSaver list <玩家>` | `invSaver.list` |
| `/invSaver preview` | 以箱子界面预览某条备份记录；加 -e 可直接编辑 | `/invSaver preview <玩家> <备份记录> [-e]` | `invSaver.preview` |
| `/invSaver reload` | 重新加载配置文件 | `/invSaver reload` | `invSaver.reload` |

## 指令详解

### `/invSaver` — 背包快照主命令，子功能见下方子指令速查

- **语法**：`/invSaver <save｜restore｜list｜preview｜reload> ...`

- **示例**：

```
/invSaver list Steve
```

- **备注**：不带子指令时只会提示用法；实际功能都在子指令里。

### `/invSaver save` — 保存玩家当前背包，生成一条备份记录

- **语法**：`/invSaver save <玩家>`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `玩家` | 必填 | 目标玩家名，备份的是这一瞬间的整个背包 |


- **示例**：

```
/invSaver save Steve
```

- **权限**：`invSaver.save`
- **备注**：任何不可逆操作（清包、发奖、改物品、封号处置）之前先执行一次；备份只反映保存那一刻的状态。

### `/invSaver restore` — 把玩家背包整体恢复成某条备份记录的内容

- **语法**：`/invSaver restore <玩家> <备份记录>`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `玩家` | 必填 | 要回滚的玩家 |
| `备份记录` | 必填 | 备份编号，先用 /invSaver list 玩家 查出可用编号 |


- **示例**：

```
/invSaver restore Steve 1
```

- **权限**：`invSaver.restore`
- **备注**：直接覆盖玩家当前背包，且不可反悔——执行前务必先 preview 核对，并给当前背包再 save 一份。

### `/invSaver list` — 列出该玩家的全部备份记录

- **语法**：`/invSaver list <玩家>`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `玩家` | 必填 | 要查看记录的玩家 |


- **示例**：

```
/invSaver list Steve
```

- **权限**：`invSaver.list`
- **备注**：记录里的编号就是 restore / preview 要填的「备份记录」参数。

### `/invSaver preview` — 以箱子界面预览某条备份记录；加 -e 可直接编辑

- **语法**：`/invSaver preview <玩家> <备份记录> [-e]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `玩家` | 必填 | 备份记录所属玩家 |
| `备份记录` | 必填 | 备份编号，来自 list |
| `-e` | 可选 | 加在末尾表示进入可编辑预览，改完直接写回该记录 |


- **示例**：

```
/invSaver preview Steve 1
/invSaver preview Steve 1 -e
```

- **权限**：`invSaver.preview`
- **备注**：只看不要加 -e；-e 是「就地改这份备份」，改错了得靠别的记录救回来。

### `/invSaver reload` — 重新加载配置文件

- **语法**：`/invSaver reload`

- **示例**：

```
/invSaver reload
```

- **权限**：`invSaver.reload`
- **备注**：只重载配置，不动已有备份记录。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/invSaver save <玩家>` | 保存玩家背包，生成一条备份记录 | `/invSaver save Steve` |
| `/invSaver list <玩家>` | 查看该玩家的备份记录列表（取编号） | `/invSaver list Steve` |
| `/invSaver preview <玩家> <备份记录> [-e]` | 预览指定记录内容，加 -e 可编辑 | `/invSaver preview Steve 1 -e` |
| `/invSaver restore <玩家> <备份记录>` | 把玩家背包恢复成该记录 | `/invSaver restore Steve 1` |
| `/invSaver reload` | 重载配置文件 | `/invSaver reload` |

## 注意事项

::: warning
- `restore` 会直接覆盖玩家当前背包，执行前先 `save` 一份当前的、再 `preview` 核对目标记录，否则可能二次损失
- `preview ... -e` 会直接修改那份备份记录，只想查看时千万别带 `-e`
- 五个权限默认只有 OP 拥有；下放时只给需要的那一个，`invSaver.restore` 与 `invSaver.preview` 尤其要收紧
- 备份只反映保存那一刻的状态，保存之后的物品变动不会同步，跨天的老问题别指望用很旧的记录解决
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `invSaver.list` | 查看玩家的备份记录列表 | op |
| `invSaver.preview` | 预览（或加 -e 编辑）玩家的备份记录 | op |
| `invSaver.reload` | 重载插件配置文件 | op |
| `invSaver.restore` | 恢复玩家背包到指定备份记录 | op |
| `invSaver.save` | 保存玩家背包快照 | op |

## 相关插件

[CoreProtect](/commands/audit/coreprotect.md)、[OpenInv](/commands/essentials/openinv.md)、[Essentials](/commands/essentials/essentials.md)
