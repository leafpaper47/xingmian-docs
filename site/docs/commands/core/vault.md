---
title: Vault
createTime: 2026/10/24
---

# Vault

> 版本 `2.20.2` · 指令 2 条 · api-version `1.13` · 文件 `VaultUnlocked-2.20.2.jar`

A PR-friendly version of Vault; Where PRs are actually accepted.

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/vault-convert help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/vault-convert` | Converts all data in economy1 and dumps it into economy2 | `vault.admin.convert` |
| `/vault-info` | Displays information about VaultUnlocked | `vault.admin.info` |

## 详细用法

### /vault-convert

- **说明**：Converts all data in economy1 and dumps it into economy2
- **用法**：`/&lt;command&gt; [economy1] [economy2]`
- **权限**：`vault.admin.convert`

### /vault-info

- **说明**：Displays information about VaultUnlocked
- **用法**：`/&lt;command&gt; - Displays VaultUnlocked information`
- **权限**：`vault.admin.info`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `vault.admin` | Grants access to the administrative tools. | op |
| `vault.update` | Notifies the player when Vault is in need of an update. | op |
