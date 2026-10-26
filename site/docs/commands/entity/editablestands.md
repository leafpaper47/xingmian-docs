---
title: EditableStands
createTime: 2026/10/24
---

# 盔甲架编辑 · EditableStands

> 分类 🧟 生物与展示 · 版本 `1.0.0` · 指令 1 条 · api-version `1.21`

::: tip 拿物品右键盔甲架，直接改形态的轻量工具
它把盔甲架的编辑动作从指令换成了手持物品右键：加手臂、去底盘、改大小、名字常显、隐身、关重力都能一键切换。默认权限节点几乎都是对所有玩家开放的，所以配权限插件才能精确控制谁能改。适合展示区、摆摊、建筑装饰里那些需要临时调整形态的盔甲架。
:::

## 什么时候会用到它

- 摆盔甲架做展示或装饰，想临时加手臂、换大小、加底盘时
- 想让盔甲架上的名字一直可见，或让盔甲架隐身当纯浮空展示时
- 想做悬浮/悬空展示，需要把盔甲架的重力关掉时
- 想把盔甲架编辑能力收回到只有管理员能用的范围时

## 上手流程

1. 把插件 jar 放进 plugins 目录，重启服务端让它生成 config
2. 执行 /editablestands info 确认插件已正常启用，再按需改 config 里的数量上限等选项
3. 手持对应物品右键盔甲架试一次（木棍、剪刀、斧、平滑石台阶、镐、荧光墨囊、隐身药水、奶桶、羽毛、铁锭）
4. 用权限插件把 editablestands.arms.add 这类节点按需开放给玩家组，改完执行 /editablestands reload

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/editablestands` | 插件主命令，查看插件信息或重载配置文件<br>别名 `/es` | `/editablestands [info/reload]` | `op` |

## 指令详解

### `/editablestands` — 插件主命令，查看插件信息或重载配置文件

- **语法**：`/editablestands [info/reload]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `info 或 reload` | 可选 | 填 info 查看插件状态与版本信息；填 reload 重载 config 配置；不填则提示用法 |


- **示例**：

```
/editablestands info
/editablestands reload
```

- **别名**：`/es`
- **权限**：`op`
- **备注**：别名 es，需要 op 权限。日常真正的「编辑」是拿物品右键盔甲架，不经过这条指令。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `info` | 查看插件信息，确认插件已正常载入 | `/editablestands info` |
| `reload` | 重载插件配置，改完 config 后用 | `/editablestands reload` |

## 注意事项

::: warning
- 具体参数与子指令以游戏内 help 为准；本页只覆盖输入资料里明确出现的 info 和 reload。
- 所有编辑动作都靠手持物品右键盔甲架完成，不是靠指令；物品拿错不会生效，先对照权限节点说明里写的物品。
- 隐身和无重力盔甲架对普通玩家默认限 1 个，要放宽得给 editablestands.limit.invisible 或 editablestands.limit.nogravity（默认 op），或改 config 的 limitUnlimited。
- 改完 config 要执行 /editablestands reload，改权限节点后玩家可能需要重新进服才同步。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `editablestands.arms.add` | 允许用木棍给盔甲架添加手臂 | True |
| `editablestands.arms.remove` | 允许用剪刀移除盔甲架的手臂 | True |
| `editablestands.feather.nogravity` | 允许用羽毛让盔甲架失去重力 | True |
| `editablestands.ingot.gravity` | 允许用铁锭让盔甲架恢复重力 | True |
| `editablestands.limit.invisible` | 放宽隐身盔甲架的数量上限（普通玩家限 1 个，详见 config 的 limitUnlimited） | op |
| `editablestands.limit.nogravity` | 放宽无重力盔甲架的数量上限（普通玩家限 1 个，详见 config 的 limitUnlimited） | op |
| `editablestands.milk.show` | 允许用奶桶让盔甲架恢复显示 | True |
| `editablestands.name.visible` | 允许用荧光墨囊让盔甲架的名字变为常显 | True |
| `editablestands.plate.add` | 允许用平滑石台阶给盔甲架添加底盘 | True |
| `editablestands.plate.remove` | 允许用镐移除盔甲架的底盘 | True |
| `editablestands.potion.hide` | 允许用隐身药水让盔甲架隐形 | True |
| `editablestands.size.big` | 允许用木棍把盔甲架变回大型 | True |
| `editablestands.size.small` | 允许用斧把盔甲架变为小型 | True |

## 相关插件

[LuckPerms](/commands/core/luckperms.md)、WorldGuard
