import Vue from 'vue'
import VueRouter from 'vue-router'

import MainComponent from '@/components/pages/Home.vue'

const routes = [
  {path: '/', name: 'root', component: MainComponent, default:true},
]

Vue.use(VueRouter)
const router = new VueRouter({
  scrollBehavior (to, from, savedPosition) { return {x: 0, y: 0} },
  mode: 'history',
  routes
})

export default router
