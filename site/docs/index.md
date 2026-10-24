---
title: 星冕服务器 · 管理员指令手册
createTime: 2026/10/24
---

# 星冕服务器 · 管理员指令手册

给服内管理组用的插件指令速查站。全部内容由服务器 `plugins/` 目录下各插件的 `plugin.yml` 直接解析生成，**不是网上抄的通用文档**，所以指令名、别名、权限节点和这台服务器是对得上的。

## 怎么用

1. 左侧按 **功能分类** 找插件，或直接按 `Ctrl + K` 搜索指令名（例如 `co`、`lp`、`res`）。
2. 每个插件页分两层：**指令一览**（快速扫一遍）和 **详细用法**（用法格式、别名、权限节点）。
3. 只有权限节点对了，指令才会生效。查不到就去 [权限节点总表](/permissions.md)。

## 功能分类

| 分类 | 内容 |
| --- | --- |
| 🛡️ [基础与权限](/commands/core/) | LuckPerms、PlugManX、维护模式、Vault、VaultUnlocked |
| 🧰 [基础工具](/commands/essentials/) | Essentials 全系、物品/背包/装备编辑 |
| 🌀 [传送与出生点](/commands/teleport/) | EssentialsSpawn、BetterRTP |
| 🗺️ [世界与地图](/commands/world/) | BlueMap、ArtMap、xaero 坐标、天气与天象 |
| 🔒 [领地与保护](/commands/protect/) | Residence、容器锁、WorldGuard GUI、城长 |
| 🪙 [经济与商店](/commands/economy/) | 点券、商店、玩家交易、赞助充值 |
| ⚔️ [战斗与 RPG](/commands/rpg/) | MythicMobs、附魔、Boss、属性、自研 RPG |
| 🧟 [生物与展示](/commands/entity/) | 伪装、模型、NPC、实体编辑 |
| 💬 [聊天与社交](/commands/chat/) | 聊天格式、公告、邮件、称号、语音、计分板 |
| 🧩 [脚本与菜单](/commands/config/) | Skript、DeluxeMenus、PlaceholderAPI、菜单 |
| 📊 [记录与性能](/commands/audit/) | CoreProtect 回滚、spark 性能采样 |
| 🎲 [小游戏与娱乐](/commands/minigame/) | 自研玩法、麻将、AFK、玩家 |
| 📦 [其他](/commands/other/) | 未归类的插件 |

完整插件目录见 [全部指令](/commands/)。

## 三条常识

- **主指令 + 子指令**：很多插件只注册一个主指令（如 LuckPerms 的 `/lp`、CoreProtect 的 `/co`、MythicMobs 的 `/mm`），真正的功能在子指令里。本手册给出主指令，具体子指令请执行该指令的 `help`。
- **`<command>` 已替换**：插件 `plugin.yml` 里的用法格式写的是 `/<command> [args]`，本手册已替换成真实指令名。
- **颜色码已去掉**：原文里的 `§x` 颜色码在文档里被去除，避免复制到游戏里变成乱码。

::: warning 别外传
本手册包含服务器权限节点与内部指令结构，仅供服内管理组使用。
:::
