import { createApp } from 'vue'
import VueCookies from 'vue-cookies'
import App from './App.vue'
import router from './router'
import store from './store'
import './main.css'


import axios from 'axios'

axios.defaults.baseURL = "http://127.0.0.1:8000"

const app = createApp(App)

app.use(VueCookies)

app.use(store)
app.use(router)

app.mount('#app')
