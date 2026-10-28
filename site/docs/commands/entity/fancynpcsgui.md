---
title: FancyNpcsGUI
createTime: 2026/10/24
---

# NPC界面 · FancyNpcsGUI

> 分类 🧟 生物与展示 · 版本 `1.1.0` · 指令 1 条 · api-version `1.21`

::: tip FancyNpcs 图形化 NPC 编辑
这是 FancyNpcs 的第三方非官方图形编辑器，把原本要敲命令才能完成的 NPC 增删改操作搬到界面里点。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 图形化编辑 NPC | /npcgui | 点选改外观与对话 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/npcgui` | 打开 FancyNpcs 图形编辑器主界面 | `/npcgui` | `fancynpcsgui.use` |

## 指令详解

### `/npcgui` — 打开 FancyNpcs 图形编辑器主界面

- **语法**：`/npcgui`

- **示例**：

```
/npcgui
```

- **权限**：`fancynpcsgui.use`
- **备注**：需要 fancynpcsgui.use 权限；实际能做什么取决于是否还拥有 create、edit、delete、actions 这几个分项权限。具体按钮与子指…

## 注意事项

::: warning
- 这是 FancyNpcs 的非官方编辑器，FancyNpcs 本体升级后界面可能失灵或报错，升级前先备份 NPC 数据
- 具体参数与子指令以游戏内 help 和界面实际显示为准，不要照搬网上别的版本教程
- fancynpcsgui.admin 会一次性给全部子权限，只让可信管理员持有；给普通管理员建议只发 use 加需要的分项
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `fancynpcsgui.actions` | — | op |
| `fancynpcsgui.admin` | 授予所有NPC GUI权限 | op |
| `fancynpcsgui.create` | — | op |
| `fancynpcsgui.delete` | — | op |
| `fancynpcsgui.edit` | — | op |
| `fancynpcsgui.use` | — | op |
