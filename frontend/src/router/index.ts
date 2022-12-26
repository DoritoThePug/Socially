import { createRouter, createWebHistory } from 'vue-router'

import FeedView from '../views/FeedView.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: FeedView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
