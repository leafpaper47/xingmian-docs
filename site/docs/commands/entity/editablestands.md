---
title: EditableStands
createTime: 2026/10/24
---

# EditableStands

> 版本 `1.0.0` · 指令 1 条 · api-version `1.21` · 文件 `EditableStands-1.0.0.jar`

Sneak right-click an armor stand with tools to toggle arms, size, base plate, visibility and gravity.

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/editablestands help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/editablestands` | EditableStands 主命令（info / reload） | `op` |

## 详细用法

### /editablestands

- **说明**：EditableStands 主命令（info / reload）
- **用法**：`正确用法: /editablestands [info/reload]`
- **别名**：`/es`
- **权限**：`op`

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
