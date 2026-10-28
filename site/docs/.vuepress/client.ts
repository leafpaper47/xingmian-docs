import { defineClientConfig, resolvers } from 'vuepress/client'
import './styles/index.scss'

// 首页标签页标题：去掉「指令总览 | 」前缀，直接显示站点名。
// VuePress 默认标题为 `[页面标题, 站点标题].join(' | ')`，
// 这里覆写官方 resolver（SSR 与客户端都用它，所以产物里的 <title> 也会一起变）。
const defaultResolvePageHeadTitle = resolvers.resolvePageHeadTitle

resolvers.resolvePageHeadTitle = (pageData, siteLocaleData) => {
  const isHome =
    pageData.pathRelative === 'index.md' ||
    pageData.path === '/' ||
    pageData.path === '/index.html'
  return isHome ? siteLocaleData.title : defaultResolvePageHeadTitle(pageData, siteLocaleData)
}

export default defineClientConfig({})
