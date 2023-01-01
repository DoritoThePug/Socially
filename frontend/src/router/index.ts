import { createRouter, createWebHistory } from 'vue-router'

import FeedView from '../views/FeedView.vue';
import AccountView from "@/views/AccountView.vue";

const routes = [
  {
    path: '/',
    name: 'home',
    component: FeedView
  },
  {
    path: '/profile/:user_slug',
    name: 'profile',
    component: AccountView,
    props: true
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
