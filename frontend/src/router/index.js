import { createRouter, createWebHistory } from 'vue-router'

import store from '../store'

import HomeView from '@/views/HomeView'
import AccountView from '@/views/AccountView';
import FeedView from '@/views/FeedView';
import PostView from '@/views/PostView';

const routes = [
  {
    path: '/',
    name: 'home',
    component: FeedView
  },
  {
    path: '/favourites',
    name: 'favourites',
    component: FeedView
  },
  {
    path: '/account',
    name: 'account',
    component: AccountView
  },
  {
    path: '/:user_slug',
    name: 'user',
    component: AccountView
  },
  {
    path: '/posts/:post_id',
    name: 'post',
    component: PostView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
