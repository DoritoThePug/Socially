import { watch } from 'vue'
import { defineStore } from 'pinia'
import Cookies from 'js-cookie'

import User from '../interfaces/user'

export const useUserStore = defineStore("userStore", {
  state: () => ({
    isAuthenticated: false,
    user: {} as User,
  }),
  actions: {
    authenticate(token:string, user:User):void {
      this.isAuthenticated = true
      this.user = user
    },
    logoutUser():void {
      this.isAuthenticated = false
      this.user = {} as User
      Cookies.remove('token')
      Cookies.remove('csrftoken')
      Cookies.remove('sessionid')
    }
  },
  persist: true
})