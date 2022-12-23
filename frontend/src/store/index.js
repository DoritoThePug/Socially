import { createStore } from 'vuex'

import axios from 'axios'

export default createStore({
  state: {
    isAuthenticated: false,
    token: '',
    user: {},
  },
  getters: {
  },
  mutations: {
    initialize() {
      if ($cookies.get('token') && localStorage.getItem('user')) {
        this.state.user = $cookies.get('user')
        this.state.token = $cookies.get('token')
        axios.defaults.headers.common['Authorization'] = "Token " + this.state.token
        this.state.isAuthenticated = true
      } else {
        this.state.token = ''
        this.state.isAuthenticated = false
        $cookies.remove('user')
        $cookies.remove('token')
      }
    },
    setToken(token) {
      this.state.token = token
      this.state.isAuthenticated = true
    },
    setUserObject(user) {
      this.state.user = user
    },
    setUser(token, user) {
      this.state.token = token
      this.state.user = user

      localStorage.setItem('user', user)
      $cookies.set('token', token, '30d')

      axios.defaults.headers.common['Authorization'] = token

      this.state.isAuthenticated = true
    }
  },
  actions: {
  },
  modules: {
  }
})
