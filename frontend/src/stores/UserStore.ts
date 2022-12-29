import { watch } from 'vue'
import { defineStore } from 'pinia'

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
    }
  },
  persist: true
})