import { createApp } from 'vue'

import axios from 'axios'
import {createPinia} from 'pinia'


import VueCookies from 'vue-cookies'
import App from './App.vue'
import router from './router'



axios.defaults.baseURL = "http://127.0.0.1:8000"

const pinia = createPinia()

const app = createApp(App)

app.use(VueCookies)

app.use(router)

app.use(pinia)
app.mount('#app')
