import { createApp } from 'vue'

import axios from 'axios'
import {createPinia} from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

import App from './App.vue'
import router from './router'

import {useAuthenticationComponentStore} from "@/stores/AuthenticationComponentStore";



axios.defaults.baseURL = "http://192.168.88.109:8000"
axios.defaults.withCredentials = true

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

export const app = createApp(App)
app.use(router)

app.use(pinia)
app.mount('#app')

axios.interceptors.response.use(function (config) {
    return config;
}, function (error) {
  if (error.response.status == 401) {
      useAuthenticationComponentStore().toggleAuthenticationComponent()

      return Promise.reject(error)
  }

    return Promise.reject(error);
})
