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
    ['link', { rel: 'icon', href: `${BASE}logo.svg`, type: 'image/svg+xml' }],
    ['meta', { name: 'theme-color', content: '#3b6cf6' }],
  ],
  theme: plumeTheme({
    logo: `${BASE}logo.svg`,
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
