import type { ThemeNavItem, ThemeSidebarMulti } from 'vuepress-theme-plume'

export const navbar: ThemeNavItem[] = [
  { text: '首页', link: '/' },
  { text: '指令总览', link: '/commands/' },
  { text: '权限总表', link: '/permissions.md' },
  { text: '使用说明', link: '/about.md' },
]

export const sidebar: ThemeSidebarMulti = {
  '/commands/': [
    { text: '指令总览', link: '/commands/' },
    {
      text: '🛡️ 基础与权限',
      collapsed: false,
      items: [
        { text: 'ConsoleSpamFixReborn', link: '/commands/core/consolespamfixreborn.md' },
        { text: 'LuckPerms', link: '/commands/core/luckperms.md' },
        { text: 'MaintenanceMode', link: '/commands/core/maintenancemode.md' },
        { text: 'PlugManX', link: '/commands/core/plugmanx.md' },
        { text: 'Vault', link: '/commands/core/vault.md' },
        { text: 'WebBridge', link: '/commands/core/webbridge.md' },
      ],
    },
    {
      text: '🧰 基础工具',
      collapsed: false,
      items: [
        { text: 'ALCERecipeViewer', link: '/commands/essentials/alcerecipeviewer.md' },
        { text: 'ArmoredElytra', link: '/commands/essentials/armoredelytra.md' },
        { text: 'ArmorUnbreaking', link: '/commands/essentials/armorunbreaking.md' },
        { text: 'BookEdit', link: '/commands/essentials/bookedit.md' },
        { text: 'CMILib', link: '/commands/essentials/cmilib.md' },
        { text: 'CraftBench', link: '/commands/essentials/craftbench.md' },
        { text: 'Essentials', link: '/commands/essentials/essentials.md' },
        { text: 'InBlock', link: '/commands/essentials/inblock.md' },
        { text: 'InfiniteFuel', link: '/commands/essentials/infinitefuel.md' },
        { text: 'InvSaver', link: '/commands/essentials/invsaver.md' },
        { text: 'ItemEdit', link: '/commands/essentials/itemedit.md' },
        { text: 'LeafHat', link: '/commands/essentials/leafhat.md' },
        { text: 'OpenInv', link: '/commands/essentials/openinv.md' },
        { text: 'PlayerSignIn', link: '/commands/essentials/playersignin.md' },
        { text: 'PlayerTask', link: '/commands/essentials/playertask.md' },
        { text: 'StarAFK', link: '/commands/essentials/starafk.md' },
      ],
    },
    {
      text: '🌀 传送与出生点',
      collapsed: false,
      items: [
        { text: 'BetterRTP', link: '/commands/teleport/betterrtp.md' },
        { text: 'EssentialsSpawn', link: '/commands/teleport/essentialsspawn.md' },
      ],
    },
    {
      text: '🗺️ 世界与地图',
      collapsed: false,
      items: [
        { text: 'ArtMap', link: '/commands/world/artmap.md' },
        { text: 'MeteorShowers', link: '/commands/world/meteorshowers.md' },
        { text: 'Mirrora', link: '/commands/world/mirrora.md' },
        { text: 'WeatherCard', link: '/commands/world/weathercard.md' },
        { text: 'XaeroTracker', link: '/commands/world/xaerotracker.md' },
      ],
    },
    {
      text: '🔒 领地与保护',
      collapsed: false,
      items: [
        { text: 'BlockLocker', link: '/commands/protect/blocklocker.md' },
        { text: 'Residence', link: '/commands/protect/residence.md' },
        { text: 'TownPlugin', link: '/commands/protect/townplugin.md' },
        { text: 'WorldGuardGUI', link: '/commands/protect/worldguardgui.md' },
      ],
    },
    {
      text: '🪙 经济与商店',
      collapsed: false,
      items: [
        { text: 'AfDianPay', link: '/commands/economy/afdianpay.md' },
        { text: 'DummyPool', link: '/commands/economy/dummypool.md' },
        { text: 'MagicPointsLog', link: '/commands/economy/magicpointslog.md' },
        { text: 'SenluoBuyer', link: '/commands/economy/senluobuyer.md' },
        { text: 'Shopkeepers', link: '/commands/economy/shopkeepers.md' },
        { text: 'WineSuite', link: '/commands/economy/winesuite.md' },
      ],
    },
    {
      text: '⚔️ 战斗与 RPG',
      collapsed: false,
      items: [
        { text: 'EcoEnchants', link: '/commands/rpg/ecoenchants.md' },
        { text: 'EliteMobs', link: '/commands/rpg/elitemobs.md' },
        { text: 'EnchantInfuser', link: '/commands/rpg/enchantinfuser.md' },
        { text: 'FoMiningComp', link: '/commands/rpg/fominingcomp.md' },
        { text: 'KaoguGuide', link: '/commands/rpg/kaoguguide.md' },
        { text: 'KaoguPlugin', link: '/commands/rpg/kaoguplugin.md' },
        { text: 'MythicMobs', link: '/commands/rpg/mythicmobs.md' },
        { text: 'MythicTools', link: '/commands/rpg/mythictools.md' },
        { text: 'PVPPlugin', link: '/commands/rpg/pvpplugin.md' },
        { text: 'StarPact', link: '/commands/rpg/starpact.md' },
        { text: 'XingmianElement', link: '/commands/rpg/xingmianelement.md' },
        { text: 'XingmianRPG', link: '/commands/rpg/xingmianrpg.md' },
      ],
    },
    {
      text: '🧟 生物与展示',
      collapsed: false,
      items: [
        { text: 'BossBarHealth', link: '/commands/entity/bossbarhealth.md' },
        { text: 'EditableStands', link: '/commands/entity/editablestands.md' },
        { text: 'FancyNpcsGUI', link: '/commands/entity/fancynpcsgui.md' },
        { text: 'LibsDisguises', link: '/commands/entity/libsdisguises.md' },
        { text: 'ModelEngine', link: '/commands/entity/modelengine.md' },
        { text: 'YiyunCEskin', link: '/commands/entity/yiyunceskin.md' },
      ],
    },
    {
      text: '💬 聊天与社交',
      collapsed: false,
      items: [
        { text: 'BroadcastPlusPlus', link: '/commands/chat/broadcastplusplus.md' },
        { text: 'LeafChat', link: '/commands/chat/leafchat.md' },
        { text: 'PlayerTitle', link: '/commands/chat/playertitle.md' },
        { text: 'SweetMail', link: '/commands/chat/sweetmail.md' },
        { text: 'TAB', link: '/commands/chat/tab.md' },
        { text: 'vcm', link: '/commands/chat/vcm.md' },
        { text: 'voicechat', link: '/commands/chat/voicechat.md' },
        { text: 'YaoqingPlugin', link: '/commands/chat/yaoqingplugin.md' },
      ],
    },
    {
      text: '🧩 脚本与菜单',
      collapsed: false,
      items: [
        { text: 'DeluxeMenus', link: '/commands/config/deluxemenus.md' },
        { text: 'KaleidoscopeCookeryPlugin', link: '/commands/config/kaleidoscopecookeryplugin.md' },
        { text: 'PlaceholderAPI', link: '/commands/config/placeholderapi.md' },
        { text: 'Skript', link: '/commands/config/skript.md' },
      ],
    },
    {
      text: '📊 记录与性能',
      collapsed: false,
      items: [
        { text: 'CoreProtect', link: '/commands/audit/coreprotect.md' },
        { text: 'spark', link: '/commands/audit/spark.md' },
      ],
    },
    {
      text: '🎲 小游戏与娱乐',
      collapsed: false,
      items: [
        { text: 'Ah-Toy-1.0', link: '/commands/minigame/ah-toy-1-0.md' },
        { text: 'Ah-WolfmanKill-1.0', link: '/commands/minigame/ah-wolfmankill-1-0.md' },
        { text: 'allmusic', link: '/commands/minigame/allmusic.md' },
        { text: 'GSit', link: '/commands/minigame/gsit.md' },
        { text: 'LeashPlayers', link: '/commands/minigame/leashplayers.md' },
        { text: 'LobbyGames', link: '/commands/minigame/lobbygames.md' },
        { text: 'MahjongPlay', link: '/commands/minigame/mahjongplay.md' },
        { text: 'XingmianQuiz', link: '/commands/minigame/xingmianquiz.md' },
      ],
    },
    {
      text: '📦 其他',
      collapsed: false,
      items: [
        { text: 'ArchitectPlugin', link: '/commands/other/architectplugin.md' },
      ],
    },
  ],
  '/': [
    { text: '指令总览', link: '/commands/' },
    { text: '权限节点总表', link: '/permissions.md' },
    { text: '使用说明', link: '/about.md' },
  ],
}