import { createApp } from 'vue'

// import fs from 'fs'
// import https from 'https'
import axios from 'axios'
import https from 'https'
import {createPinia} from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import Cookie from 'js-cookie'

import App from './App.vue'
import router from './router'

import {useAuthenticationComponentStore} from "@/stores/AuthenticationComponentStore";

// const httpsAgent = new https.Agent({
//   rejectUnauthorized: false, // (NOTE: this will disable client verification)
//   cert: fs.readFileSync("./certs/cert.pem"),
//   key: fs.readFileSync("./certs/key.pem"),
//   passphrase: "Jadenjin904119"
// })

// const instance = axios.create({ httpsAgent })

axios.defaults.baseURL = "https://192.168.88.121:8000"
axios.defaults.withCredentials = true

const agent = new https.Agent({
    rejectUnauthorized: false
})

axios.defaults.httpsAgent = agent

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

const app = createApp(App)
app.use(router)

app.use(pinia)
app.mount('#app')




axios.interceptors.request.use(function (config) {
    const csrftoken = Cookie.get("csrftoken")

    config.headers = {
        ...config.headers,
        "X-CSRFToken": `${csrftoken}`
    }

    return config
}, function (error) {
    return Promise.reject(error)
})


axios.interceptors.response.use(function (config) {
    return config
}, function (error) {
  if (error.response.status == 401) {
      useAuthenticationComponentStore().toggleAuthenticationComponent()

      return Promise.reject(error)
  }

    return Promise.reject(error);
})

app.directive('click-outside', {
  mounted(el, binding, vnode) {
    el.clickOutsideEvent = function(event:any) {
      if (!(el === event.target || el.contains(event.target))) {
        binding.value(event, el);
      }
    };
    document.body.addEventListener('click', el.clickOutsideEvent);
  },
  unmounted(el) {
    document.body.removeEventListener('click', el.clickOutsideEvent);
  }
});
