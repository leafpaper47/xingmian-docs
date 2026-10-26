---
title: ModelEngine
createTime: 2026/10/24
---

# 模型引擎 · ModelEngine

> 分类 🧟 生物与展示 · 版本 `R4.1.1` · 指令 1 条 · api-version `1.19`

::: tip 让服务器用自定义 3D 模型替换生物外观并播放动画
ModelEngine 是自定义模型引擎，把 Blockbench 导出的模型做成可动的服务器实体，用来替换原版生物外观或摆出纯装饰的模型。它本身只负责生成模型和播动画，实际玩法一般交给 MythicMobs、DeluxeMenus 之类去调用，配合资源包下发模型文件才能被客户端看见。
:::

## 什么时候会用到它

- 想把原版僵尸、苦力怕换成自制 BOSS 或宠物外观
- 需要摆一个会动的装饰模型，比如雕像、坐骑、NPC
- 排查模型显示不出来、材质发白、动画不播放的问题
- 给 MythicMobs 的技能或副本准备模型与动画

## 上手流程

1. 先把模型文件夹放进 plugins/ModelEngine/blueprints，并确保服务器资源包已下发对应贴图与模型文件
2. 执行 /meg reload 让引擎重新加载所有模型，观察控制台有没有加载报错
3. 用 /meg model list 确认模型已被识别，再用 /meg spawn 生成一只测试并检查外观与动画
4. 确认无误后再交给 MythicMobs 等插件在技能里正式调用模型

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/meg` | 模型引擎主指令，下面所有操作都通过它的子指令完成 | `/meg` | — |

## 指令详解

### `/meg` — 模型引擎主指令，下面所有操作都通过它的子指令完成

- **语法**：`/meg`

- **示例**：

```
/meg help
/meg reload
/meg model list
```

- **备注**：需要权限 modelengine.command（默认仅 OP）。控制台也可直接执行，但生成类子指令依赖具体坐标，通常还是游戏内用。

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `help` | 列出全部可用子指令与用法 | `/meg help` |
| `reload` | 重新加载所有模型与配置，改完模型文件后用 | `/meg reload` |
| `model list` | 列出当前已加载的全部模型名 | `/meg model list` |
| `model info 模型名` | 查看某个模型的详细信息，含动画、骨骼、贴图等 | `/meg model info example_model` |
| `spawn 模型名` | 在指定坐标生成一个模型实体，可附加朝向参数 | `/meg spawn example_model 0 64 0` |
| `remove` | 移除已生成的模型实体，用于清理测试模型 | `/meg remove` |
| `status` | 查看引擎当前状态，包括已生成的模型数量等信息 | `/meg status` |

## 注意事项

::: warning
- 模型要先在客户端资源包里存在，只装插件不会有外观；玩家没拿到资源包时会看到隐形或原版生物
- 改完模型文件必须 /meg reload，但重载后已经生成的实体可能外观错乱，建议清掉重新生成
- 子指令在不同 R4 小版本间略有差异，具体参数以游戏内 /meg help 的输出为准
- 模型数量多时重载会卡顿几秒，尽量在低峰期操作
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `modelengine.command` | 访问所有模型引擎命令。 | op |

## 相关插件

[MythicMobs](/commands/rpg/mythicmobs.md)、[PlaceholderAPI](/commands/config/placeholderapi.md)、[DeluxeMenus](/commands/config/deluxemenus.md)
