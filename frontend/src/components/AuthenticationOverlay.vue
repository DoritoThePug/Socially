<template>
  <div class="w-full h-full backdrop-blur-md flex place-content-center">
    <div class="flex flex-col p-[32px] bg-white rounded-[25px] self-center">
      <div class="flex flex-row justify-between items-center">
        <h2 class="self-center align-middle">Log In</h2>
        <button class="ml-auto flex-none hover:text-secondary-100" @click="$parent.toggleAuthenticationPrompt">
          <i class="fa-solid fa-x"></i>
        </button>
      </div>

      <h6 class="font-normal text-black-75 mr-[8px]">Email</h6>
      <div class="min-w-[280px] rounded-[10px] p-[8px] border-[1px] border-black-25 mb-[16px]">
        <input class="w-full bg-white focus:outline-none font-['roboto'] text-[14px]" type="email">
      </div>

      <h6 class="font-normal text-black-75 mr-[8px]">Password</h6>
      <div class="min-w-[280px] rounded-[10px] p-[8px] border-[1px] border-black-25 mb-[8px]">
        <input class="w-full bg-white focus:outline-none" type="password">
      </div>

      <div class="flex flex-row items-center justify-between mb-[16px]">
        <input class="mr-[4px] w-[12px] h-[12px] appearance-none border-[1px] border-black-25 rounded-[2px] checked:bg-secondary-100 hover:border-black-50" type="checkbox">
        <p class="text-[12px] text-black-50">Remember me</p>

        <router-link to="" class="ml-auto text-[12px] text-secondary-100 hover:text-secondary-80">Forgot Password?</router-link>
      </div>

      <button class="px-[38px] py-[8px] self-center rounded-[5px] bg-primary-100 hover:bg-primary-80 mb-[16px]">
        <h4 class="text-white">Log In</h4>
      </button>

      <div class="h-[2px] bg-black-10 mb-[16px]"></div>

      <div class="flex flex-row justify-center space-x-[32px] mb-[16px]">
        <div class="authenticationIcon">
          <i class="fa-brands fa-google text-[24px]"></i>
        </div>
        <div class="authenticationIcon">
          <i class="fa-brands fa-github text-[24px]"></i>
        </div>
        <div class="authenticationIcon">
          <i class="fa-brands fa-apple text-[24px]"></i>
        </div>
      </div>

      <div class="self-center">
        <p class="inline">Don't have an account? </p>
        <router-link class="text-secondary-100 hover:text-secondary-80 inline" to="">Sign up</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "AuthenticationOverlay",
  data() {
    return {
      showAccountPrompt: false,
      showLogInPrompt: true,
      email: '',
      username: '',
      password: '',
      password2: '',
      bio: '',
      profile_picture: ''
    }
  },
  methods: {
    submitLogInForm() {
      axios.defaults.headers.common["Authorization"] = ''

      const formData = {
        email: this.email,
        password: this.password
      }

      axios
          .post('/api/log-in/', formData)
          .then(response => {
            const token = response.data.token
            const user = response.data.user

            console.log(response)

            this.$store.commit('setToken', token)
            this.$store.commit('setUserObject', user)

            axios.defaults.headers.common["Authorization"] = `Token ${token}`

            this.$cookies.set('token', token, '30d', '','',true, 'Strict')
            localStorage.setItem('user')

            this.$router.go()
          }).catch(error => {
            console.log(error)
      })
    },
    submitSignUpForm() {
      let formData = new FormData()

      formData.append('email', this.email)
      formData.append('username', this.username)
      formData.append('password', this.password)
      formData.append('bio', this.bio)
      formData.append('profile_picture', this.profile_picture)
      formData.append('slug', this.username)

      axios.defaults.headers.common["Authorization"] = ""

      axios
          .post('/api/create-user/', formData, {headers:{'Content-Type': 'multipart/form-data'}})
          .then(response => {
            this.switchPrompt()
          })
    },
    switchPrompt() {
      this.showLogInPrmpt = !this.showLogInPrmpt
      console.log(this.showLogInPrmpt)
    },
    handleFileUpload() {
      this.profile_picture = this.$refs.file.files[0]
    }
  },
  computed: {
    isDisableSubmitButton() {
      if (this.showLogInPrompt) {
        return (this.password.length === 0 || this.username.length === 0)
      } else {
        return (this.password.length === 0 || this.username.length === 0 || this.password2.length === 0 || !(this.password === this.password2))
      }
    }
  }
};
</script>

<style scoped>
.authenticationIcon {
  @apply flex place-items-center px-[10px] py-[6px] rounded-[5px] border-[1px] border-black-25;
}
</style>