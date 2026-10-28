import { defineUserConfig } from 'vuepress'
import { viteBundler } from '@vuepress/bundler-vite'
import { plumeTheme } from 'vuepress-theme-plume'
import { navbar, sidebar } from './sidebar.js'

// GitHub Pages 项目站点的路径：https://<用户名>.github.io/<仓库名>/
// 仓库名不是 xingmian-docs 时，只改这一行（末尾斜杠必须有）
const BASE = '/xingmian-docs/'
// 站点完整地址，只影响 sitemap/SEO，改成 https://<用户名>.github.io/
const HOSTNAME = 'https://xingmian.github.io/'

export default defineUserConfig({
  lang: 'zh-CN',
  title: '星冕服务器 · 管理员指令手册',
  description: '星冕服务器插件管理指令、用法与权限节点速查手册',
  base: BASE,
  bundler: viteBundler(),
  head: [
    // 站点图标：public/logo.png（512×512，由用户提供的像素图缩放而来）
    // 32px 小图给地址栏，apple-touch-icon 给 iOS 收藏
    ['link', { rel: 'icon', href: `${BASE}favicon-32.png`, type: 'image/png', sizes: '32x32' }],
    ['link', { rel: 'icon', href: `${BASE}logo.png`, type: 'image/png', sizes: '512x512' }],
    ['link', { rel: 'apple-touch-icon', href: `${BASE}apple-touch-icon.png`, sizes: '180x180' }],
    ['meta', { name: 'theme-color', content: '#1b1b4b' }],
  ],
  theme: plumeTheme({
    // 注意：这里不要再手动拼 BASE，VuePress 会自动加 base 前缀，
    // 之前写成 `${BASE}logo.svg` 导致产物里出现 /xingmian-docs/xingmian-docs/logo.svg（图标 404、标题错位）
    logo: '/logo.png',
    hostname: HOSTNAME,
    navbar,
    sidebar,
    outline: { level: [2, 3] },
    search: { provider: 'local' },
    editLink: false,
    // 只关掉随机 permalink（保留 title/createTime 自动注入），否则页面会变成 /xxxxxx/ 这种 URL
    autoFrontmatter: { permalink: false },
    contributors: false,
    changelog: false,
    lastUpdated: false,
    footer: {
      message: '星冕服务器 · 管理员指令手册',
      copyright: '仅供服内管理使用，请勿外传',
    },
    markdown: {
      icon: { provider: 'iconify' },
    },
  }),
})
