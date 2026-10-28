---
title: BlockLocker
createTime: 2026/10/24
---

# 箱子锁 · BlockLocker

> 分类 🔒 领地与保护 · 版本 `1.14.1` · 指令 1 条 · api-version `1.20`

::: tip 用告示牌给箱子门做私有上锁
BlockLocker 让玩家把告示牌贴在箱子、熔炉、门等容器或方块上，写上标签就完成上锁与授权，不必依赖命令或额外 GUI。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 改完配置生效 | /blocklocker reload | 锁具与提示文案 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/blocklocker` | 插件管理命令，目前主要用于重载配置<br>别名 `/b`、`/l` | `/blocklocker reload` | `blocklocker.reload` |

## 指令详解

### `/blocklocker` — 插件管理命令，目前主要用于重载配置

- **语法**：`/blocklocker reload`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `reload` | 必填 | 重新读取配置文件与语言文件，改动后才需要执行 |


- **示例**：

```
/blocklocker reload
```

- **别名**：`/b`、`/l`
- **权限**：`blocklocker.reload`
- **备注**：输入 /blocklocker 不带参数会提示用法；别名可用 /bl 等短写。需要 blocklocker.reload 权限（默认仅 OP）。玩家侧上锁不靠命…

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `blocklocker reload` | 重载插件配置与语言文件 | `/blocklocker reload` |

## 注意事项

::: warning
- 别把 blocklocker.bypass 当日常权限发给管理组：它能直接打开他人容器，容易误操作或引发玩家纠纷；只想查看状态时更应慎用
- blocklocker.admin 可以改别人的保护标记甚至完全取消保护，属于破坏性操作，建议只给服主或极少数人，操作前先告知玩家
- 告示牌一旦被破坏或掉落，保护可能随之失效，配置里若有告示牌掉落/破坏相关开关请谨慎调整
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `blocklocker.admin` | 编辑某人的防护标志，或完全取消防护。 | op |
| `blocklocker.bypass` | 绕过他人的保护，但不要允许破坏它。 | op |
| `blocklocker.protect` | 保护容器和门。 | True |
| `blocklocker.reload` | 使用/blocklocker reload重新加载插件。 | op |
| `blocklocker.wilderness` | 在荒野中放置宝箱（在Towny领地之外） | True |
