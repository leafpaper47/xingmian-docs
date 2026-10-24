---
title: ALCERecipeViewer
createTime: 2026/10/24
---

# ALCERecipeViewer

> 版本 `1.0.8` · 指令 1 条 · api-version `1.21` · 文件 `ALCERecipeViewer-1.0.8-subcategory.jar`

AL合成表查看器 - 按分类浏览合成配方，支持搜索与用途查看

::: tip 用法提示
本页数据由服务器上该插件 jar 内的 `plugin.yml` 自动解析生成，只包含**指令名、说明、用法格式、别名与权限节点**。
具体子参数可以执行 `/alcerecipes help` 或该插件对应子命令的 `help` 查看。
:::

## 指令一览

| 指令 | 说明 | 权限节点 |
| --- | --- | --- |
| `/alcerecipes` | 打开AL合成表查看器，按分类浏览合成配方 | `alcerecipeviewer.use` |

## 详细用法

### /alcerecipes

- **说明**：打开AL合成表查看器，按分类浏览合成配方
- **用法**：`/&lt;command&gt; [search|usage|reload] [物品ID]`
- **别名**：`/alcer`、`/alcebook`、`/alcerecipe`
- **权限**：`alcerecipeviewer.use`

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `alcerecipeviewer.admin` | 允许使用管理命令（重载数据） | op |
| `alcerecipeviewer.use` | 允许使用 /alcerecipes 查看合成配方 | True |
