import { createApp } from 'vue'

import axios from 'axios'
import {createPinia} from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import VueCookies from 'vue-cookies'

import App from './App.vue'
import router from './router'



axios.defaults.baseURL = "http://192.168.88.105:8000"
axios.defaults.withCredentials = true

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

const app = createApp(App)

app.use(VueCookies)

app.use(router)

app.use(pinia)
app.mount('#app')
