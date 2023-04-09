import { createRouter, createWebHistory } from 'vue-router'

import FeedView from '../views/FeedView.vue';
import AccountView from "@/views/AccountView.vue";
import PostView from "@/views/PostView.vue";

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
  },
  {
    path: '/post/:user_slug/:post_id',
    name: 'post',
    component: PostView,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
