---
title: Vault
createTime: 2026/10/24
---

# 经济前置 · Vault

> 分类 🛡️ 基础与权限 · 版本 `2.20.2` · 指令 2 条 · api-version `1.13`

::: tip 经济与权限接口前置库，插件间的通用桥梁
Vault 本身不是经济插件，它只提供一套统一接口，让商店、任务、地皮、签到等插件不必各自去适配每一种经济或权限系统。装上 Vault 后，再装一个真正的经济插件（如 EssentialsX 经济、CMI、PlayerPoints 等），其它插件就能通过 Vault 统一读写玩家余额。很多第三方插件把 Vault 列为必需前置，缺了它会直接无法启用。
:::

## 什么时候会用到它

- 新开服搭基础环境，先装 Vault 再装经济插件，让商店/地皮/任务类插件能正常扣钱发钱
- 从旧经济插件迁移到新经济插件时，用它的转换指令把余额数据搬过去
- 排查某插件为什么报 Vault 相关错误，确认 Vault 是否启用、是否已挂上经济 provider
- 确认当前 Vault 版本与已注册的经济/权限 provider，写进运维记录

## 上手流程

1. 把 Vault 的 jar 放进 plugins 目录并重启服务器，不要只用 reload
2. 再安装一个真正的经济插件（例如 EssentialsX 经济模块），同样重启
3. 进游戏或用控制台执行 vault-info，检查版本信息与已注册的 provider 是否正常
4. 到商店/任务等插件里测试一次扣款或查询余额，确认整条链路通了

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/vault-convert` | 把余额数据从一个经济插件转换导入到另一个经济插件 | `/vault-convert [economy1] [economy2]` | `vault.admin.convert` |
| `/vault-info` | 显示 Vault 版本信息与当前已注册的各类服务提供者 | `/vault-info` | `vault.admin.info` |

## 指令详解

### `/vault-convert` — 把余额数据从一个经济插件转换导入到另一个经济插件

- **语法**：`/vault-convert [economy1] [economy2]`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `economy1` | 必填 | 数据来源的经济插件名，写它在 Vault 里注册的名字，如 Essentials |
| `economy2` | 必填 | 数据目标的经济插件名，即要写入的那个经济插件 |


- **示例**：

```
/vault-convert Essentials CMI
/vault-convert EssentialsX PlayerPoints
```

- **权限**：`vault.admin.convert`
- **备注**：两个经济插件必须都已安装并成功注册到 Vault，否则会提示找不到对应经济。执行前务必备份双方的经济数据文件，转换属于写操作，出错回滚很麻烦。

### `/vault-info` — 显示 Vault 版本信息与当前已注册的各类服务提供者

- **语法**：`/vault-info`

- **示例**：

```
/vault-info
```

- **权限**：`vault.admin.info`
- **备注**：排查前置问题的第一站：能看到版本号以及哪些插件注册了经济、权限、聊天等服务。如果经济一栏是空的，说明没装经济插件或没注册成功。

## 注意事项

::: warning
- Vault 只是接口，不装经济插件的话它没有任何余额功能，报错时先查经济插件而不是 Vault
- 只允许装一个 Vault 同类前置（如 Vault 与 VaultUnlocked 不要并存），重复会导致注册冲突和插件报错
- 升级或更换 Vault 版本后要整服重启，热重载容易让依赖它的插件丢失 provider 引用
- 具体参数与子指令以游戏内 help 为准，不同分支版本（Vault 与 VaultUnlocked）指令细节可能有差异
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `vault.admin` | 授予对管理工具的访问权限。 | op |
| `vault.update` | 当避难所需要更新时通知玩家。 | op |

## 相关插件

EssentialsX、[PlaceholderAPI](/commands/config/placeholderapi.md)、[LuckPerms](/commands/core/luckperms.md)、CMI、PlayerPoints
