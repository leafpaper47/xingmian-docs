---
title: FancyNpcsGUI
createTime: 2026/10/24
---

# NPC界面 · FancyNpcsGUI

> 分类 🧟 生物与展示 · 版本 `1.1.0` · 指令 1 条 · api-version `1.21`

::: tip FancyNpcs 的图形化 NPC 编辑器
这是 FancyNpcs 的第三方非官方图形编辑器，把原本要敲命令才能完成的 NPC 增删改操作搬到界面里点。它本身不实现 NPC 功能，所有 NPC 的生成、皮肤与动作仍由 FancyNpcs 负责，它只是给管理员套了一层更好上手的外壳。适合不想记 FancyNpcs 命令、想边看边改的服主使用。
:::

## 什么时候会用到它

- 刚接手服务器，不熟悉 FancyNpcs 的命令语法，想直接在界面里建一个 NPC
- 想给已有 NPC 换皮肤、改名字、调朝向，但懒得翻官方指令文档
- 整理活动地图或主城时，需要快速找出并删掉多余的 NPC
- 给建筑组或活动组临时开权限，让他们自己摆 NPC 而不必给全套管理权限

## 上手流程

1. 先在服务端装好 FancyNpcs 本体并确认它能正常用，再装 FancyNpcsGUI
2. 给自己或管理组加上 fancynpcsgui.admin 权限（或一次给全 fancynpcsgui.use、create、edit、delete、actions）
3. 进游戏执行 /npcgui 打开编辑器界面
4. 在界面里选择新建或选中已有 NPC，按界面按钮完成编辑，最后保存

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
- **备注**：需要 fancynpcsgui.use 权限；实际能做什么取决于是否还拥有 create、edit、delete、actions 这几个分项权限。具体按钮与子指令以游戏内界面和 help 为准。

## 注意事项

::: warning
- 这是 FancyNpcs 的非官方编辑器，FancyNpcs 本体升级后界面可能失灵或报错，升级前先备份 NPC 数据
- 具体参数与子指令以游戏内 help 和界面实际显示为准，不要照搬网上别的版本教程
- fancynpcsgui.admin 会一次性给全部子权限，只让可信管理员持有；给普通管理员建议只发 use 加需要的分项
- 删 NPC 权限 fancynpcsgui.delete 建议单独控制，误删的 NPC 需要重新配置皮肤和动作
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

## 相关插件

FancyNpcs、[PlaceholderAPI](/commands/config/placeholderapi.md)、[LuckPerms](/commands/core/luckperms.md)
