---
title: PlaceholderAPI
createTime: 2026/10/24
---

# 变量占位符 · PlaceholderAPI

> 分类 🧩 脚本与菜单 · 版本 `2.12.3` · 指令 1 条 · api-version `1.13`

::: tip 变量占位符
全服变量中转站：把等级/经济/在线人数等数据变成 %xxx% 占位符，供计分板、聊天、菜单等插件引用，并可从云端下载扩展包。
:::

## 常用用法

| 场景 | 指令 | 说明 |
| --- | --- | --- |
| 看装了哪些扩展 | /papi list | 显示已加载的扩展与作者 |
| 测变量能不能出值 | /papi parse me %player_level% | 最常用的排错手段 |
| 下载扩展包 | /papi ecloud download Player | 下载后必须 /papi reload |
| 改完配置生效 | /papi reload | 重载所有扩展与配置 |

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/placeholderapi` | PlaceholderAPI命令<br>别名 `/papi` | — | — |

## 指令详解

### `/placeholderapi` — PlaceholderAPI命令

- **别名**：`/papi`

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `/papi list` | 列出已安装的扩展（含版本与作者） | `/papi list` |
| `/papi info <扩展>` | 查看某扩展的详细信息与占用情况 | `/papi info Player` |
| `/papi parse <玩家> <文本>` | 用指定玩家上下文解析占位符，直接看到替换结果 | `/papi parse Steve %player_level%` |
| `/papi parse me <文本>` | 以自己为上下文解析（玩家最常用） | `/papi parse me %server_online%` |
| `/papi reload` | 重载配置并重新注册全部扩展 | `/papi reload` |
| `/papi version` | 查看 PAPI 版本与更新状态 | `/papi version` |
| `/papi dump` | 导出诊断信息（反馈问题用） | `/papi dump` |
| `/papi ecloud download <扩展>` | 从云端下载扩展 jar | `/papi ecloud download Player` |
| `/papi ecloud update <扩展｜all>` | 更新云端扩展 | `/papi ecloud update all` |
| `/papi ecloud refresh` | 刷新云端扩展列表缓存 | `/papi ecloud refresh` |
| `/papi ecloud status` | 查看云端可用性与本地缓存状态 | `/papi ecloud status` |
| `/papi ecloud list <all｜installed｜作者>` | 列出云端扩展 | `/papi ecloud list installed` |
| `/papi ecloud placeholders <扩展>` | 查看某扩展提供的全部占位符 | `/papi ecloud placeholders Player` |
| `/papi ecloud clear` | 清空本地云端缓存 | `/papi ecloud clear` |
| `/papi register <jar 名>` | 手动注册一个本地扩展 jar | `/papi register MyExpansion.jar` |
| `/papi unregister <扩展>` | 卸载某个扩展 | `/papi unregister Player` |

## 注意事项

::: warning
- 占位符解析失败时先 `/papi parse me %xxx%` 单测，再怀疑引用方插件——90% 的「计分板不显示」是变量名写错或扩展没加载。
- ecloud download 之后必须 /papi reload 才生效，很多人以为下载完就完事了。
- PAPI 本身不产出数据，`%xxx%` 全靠扩展；没装对应扩展的占位符会原样显示。
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `placeholderapi.*` | 能够使用所有PAPI命令 | — |
| `placeholderapi.admin` | 使用 /papi 管理类子指令 | — |
| `placeholderapi.ecloud` | 允许您访问PAPI eCloud | op |
| `placeholderapi.ecloud.*` | 能够使用所有PAPI ecloud命令 | — |
| `placeholderapi.ecloud.clear` | 允许您清除本地eCloud扩展缓存 | op |
| `placeholderapi.ecloud.download` | 允许您从eCloud下载扩展 | op |
| `placeholderapi.ecloud.info` | 允许您查看云扩展信息 | op |
| `placeholderapi.ecloud.list` | 允许您列出eCloud扩展 | op |
| `placeholderapi.ecloud.placeholders` | 允许您查看eCloud扩展的占位符 | op |
| `placeholderapi.ecloud.refresh` | 允许您刷新本地eCloud扩展缓存 | op |
| `placeholderapi.ecloud.status` | 允许您查看eCloud扩展的状态 | op |
| `placeholderapi.ecloud.update` | 允许您更新已注册的eCloud扩展 | op |
| `placeholderapi.help` | 允许您查看PAPI命令列表 | op |
| `placeholderapi.info` | 允许您查看扩展信息 | op |
| `placeholderapi.list` | 允许您列出活动扩展 | op |
| `placeholderapi.parse` | 允许您分析占位符 | op |
| `placeholderapi.register` | 允许您注册扩展 | op |
| `placeholderapi.reload` | 允许您重新加载PAPI及其配置 | op |
| `placeholderapi.unregister` | 允许您取消注册扩展 | op |
| `placeholderapi.updatenotify` | 当有PAPI更新时通知您 | op |
| `placeholderapi.version` | 允许您查看已安装的PAPI版本 | op |
