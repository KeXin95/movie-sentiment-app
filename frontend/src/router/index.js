import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Hashtag from '../views/sentiment.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/sentiment',
    name: 'sentiment',
    component: Hashtag
  }
]

const router = new VueRouter({
  routes
})

export default router
