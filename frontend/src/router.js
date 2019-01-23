import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Builder from './views/Builder.vue'
import HelloWorld from '@/components/HelloWorld.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  linkExactActiveClass: 'is-active',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/guides/builder',
      component: Builder,
      name: 'guide-builder'
    },
    {
      path: '/guides/detail/:slug',
      component: HelloWorld, // TODO: Guide Detail Component
      name: 'guide-detail'
    },
    {
      path: '/search',
      name: 'search',
      component: HelloWorld // TODO: Search Page Component
    },
    {
      path: '/search-result',
      name: 'search-result',
      component: HelloWorld // TODO: Search Result Component
    },
    {
      path: '/login',
      name: 'login',
      component: HelloWorld // TODO: Login Page Component
    },
    {
      path: '/about',
      name: 'about',
      component: HelloWorld
    }
  ]
})
