---
title: PlaceholderAPI
createTime: 2026/10/24
---

# 变量占位符 · PlaceholderAPI

> 分类 🧩 脚本与菜单 · 版本 `2.12.3` · 指令 1 条 · api-version `1.13`

::: tip 全服统一的变量占位符引擎，供各插件取值
它本身不提供玩法，而是给全服插件提供统一的占位符解析：别的插件配置里写 %player_name% 这类变量，由 PAPI 向对应扩展要值再填回文本。计分板、聊天格式、菜单、TAB、称号这类展示型插件几乎都靠它把玩家数据拼进文字里。没有它，多数现代插件的变量会原样显示成一串百分号。
:::

## 什么时候会用到它

- 装了计分板、聊天格式、菜单或 TAB 之类的插件，但里面的变量原样显示成 %xxx% 时
- 想知道某个占位符此刻到底解析出什么值，排查变量为空或不生效
- 需要下载或更新扩展（比如 player、server、statistic）来支持想要的变量
- 新加了扩展或改了配置后，要重载 PAPI 让它生效

## 上手流程

1. 把 PlaceholderAPI 放进 plugins 目录重启服务器，确认控制台无报错
2. 游戏内输入 /papi list 查看已注册扩展，缺哪个就用 /papi ecloud download 扩展名 下载
3. 下载完执行 /papi reload，再用 /papi parse me 占位符 实测解析结果
4. 把验证通过的占位符填进其它插件的配置文件里

## 指令一览

| 指令 | 功能 | 用法 | 权限节点 |
| --- | --- | --- | --- |
| `/placeholderapi` | PAPI 主命令，用于管理扩展、下载云端扩展与调试占位符<br>别名 `/papi` | `/papi 子命令 参数` | — |

## 指令详解

### `/placeholderapi` — PAPI 主命令，用于管理扩展、下载云端扩展与调试占位符

- **语法**：`/papi 子命令 参数`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `子命令` | 必填 | 如 help、list、info、parse、ecloud、reload、version |


- **示例**：

```
/papi list
/papi parse me %player_name%
```

- **别名**：`/papi`
- **备注**：别名 /papi，日常几乎都用 /papi；每个子命令对应一个独立权限节点，给管理组授权时按需给

## 子指令速查

| 子指令 | 功能 | 示例 |
| --- | --- | --- |
| `help [页码]` | 列出 PAPI 全部子命令及对应权限 | `/papi help` |
| `info 扩展名` | 查看某个扩展的作者、版本与它提供的占位符 | `/papi info Player` |
| `list` | 列出服务器上已注册（当前可用）的扩展 | `/papi list` |
| `parse 玩家名 文本` | 以指定玩家为上下文解析一段占位符文本 | `/papi parse Steve %player_name%` |
| `parse me 文本` | 以自己为上下文解析，最常用的调试方式 | `/papi parse me %player_health%` |
| `parse --null 文本` | 不带玩家上下文解析，适合服务器类占位符 | `/papi parse --null %server_online%` |
| `reload` | 重载 PAPI 配置与已下载的扩展，下载后必做 | `/papi reload` |
| `version` | 查看当前 PAPI 版本号 | `/papi version` |
| `register 扩展名` | 手动注册本地扩展，多数情况会自动注册，非必要不用 | `/papi register Player` |
| `unregister 扩展名` | 取消注册某个扩展，让它暂时不起作用 | `/papi unregister Player` |
| `ecloud status` | 查看 eCloud 云扩展仓库的连接状态 | `/papi ecloud status` |
| `ecloud list all 页码` | 列出云端可用扩展，可指定页码翻页 | `/papi ecloud list all 1` |
| `ecloud info 扩展名` | 查看云端某个扩展的说明、作者与版本 | `/papi ecloud info player` |
| `ecloud download 扩展名` | 从云端下载扩展，下载完需 /papi reload | `/papi ecloud download Player` |
| `ecloud update 扩展名` | 更新已下载的云端扩展，写 all 表示全部更新 | `/papi ecloud update all` |
| `ecloud refresh` | 刷新本地 eCloud 扩展缓存，看不到新扩展时用 | `/papi ecloud refresh` |
| `ecloud clear` | 清空本地 eCloud 缓存文件 | `/papi ecloud clear` |
| `ecloud placeholders 扩展名` | 查看某个扩展提供的全部占位符清单 | `/papi ecloud placeholders player` |

## 注意事项

::: warning
- 没有玩家上下文时（控制台、异步任务）占位符会取到空值，要显式指定玩家或改用 --null 形式
- 刚下载的扩展必须 /papi reload 才生效，但扩展很多时 reload 会有短暂卡顿，尽量在低峰做
- 占位符前缀和大小写要照扩展文档写全，写错不会报错，只会原样输出一串百分号
- 扩展装太多会拖慢每次解析，计分板这种高频刷新的地方少用重计算的扩展
:::

## 权限节点

| 节点 | 说明 | 默认 |
| --- | --- | --- |
| `placeholderapi.*` | 能够使用所有PAPI命令 | — |
| `placeholderapi.admin` | 能够使用所有PAPI命令 | — |
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

## 相关插件

[TAB](/commands/chat/tab.md)、[DeluxeMenus](/commands/config/deluxemenus.md)、[LuckPerms](/commands/core/luckperms.md)、[Vault](/commands/core/vault.md)、[Skript](/commands/config/skript.md)
