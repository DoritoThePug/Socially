<template>
  <div class="grid">
    <div class="grid absolute py-[32px] px-[64px] w-[704px] bg-white place-self-center z-10 rounded-[10px]">
      <button @click="$parent.toggleLogInPrompt()" class="place-self-start ml-[-48px] mt-[-16px]"><i class="fa-solid fa-x"></i></button>

      <form v-if="showLogInPrompt" @submit.prevent="submitLogInForm" class="grid">
        <h1 class="text-black-100 border-box justify-self-center">Log In</h1>
        <hr class="bg-black-50 box-border mt-[8px] mb-[16px] mx-[128px]">

        <div class="h-[64px] bg-[#EFEFEF] rounded-[10px] px-[16px] mb-[8px]">
          <h6 class="bg-gradient-to-r from-primary-100 to-secondary-100 text-transparent bg-clip-text">Email</h6>
          <input type="text" class="focus:outline-0 w-full bg-inherit" v-model="email">
        </div>
        <div class="h-[64px] bg-[#EFEFEF] rounded-[10px] px-[16px] mb-[8px]">
          <h6 class="bg-gradient-to-r from-primary-100 to-secondary-100 text-transparent bg-clip-text">Password</h6>
          <input type="password" class="focus:outline-0 w-full bg-inherit" v-model="password">
        </div>

        <a href="/password-reset/"><p class="text-primary-100 hover:underline active:text-primary-80">Forgot password?</p></a>

        <button class="bg-gradient-to-r from-primary-100 to-secondary-100 px-[64px] py-[16px] rounded-full mt-[16px] text-center place-self-center mb-[16px] hover:from-primary-80 hover:to-secondary-80 active:from-primary-100 active:to-primary-100"><h4 class="text-white">Log In</h4></button>

        <p @click="showLogInPrompt = false" class="text-primary-100 hover:underline active:text-primary-80">Don't have an account? Sign up instead.</p>
      </form>

      <form v-else @submit.prevent="submitSignUpForm" class="grid">
        <h1 class="text-black-100 border-box justify-self-center">Sign Up</h1>
        <hr class="bg-black-50 box-border mt-[8px] mb-[16px] mx-[128px]">

        <div class="h-[64px] bg-[#EFEFEF] rounded-[10px] px-[16px] mb-[8px]">
          <h6 class="bg-gradient-to-r from-primary-100 to-secondary-100 text-transparent bg-clip-text">Email</h6>
          <input type="email" class="focus:outline-0 w-full bg-inherit" v-model="email">
        </div>

        <div class="h-[64px] bg-[#EFEFEF] rounded-[10px] px-[16px] mb-[8px]">
          <h6 class="bg-gradient-to-r from-primary-100 to-secondary-100 text-transparent bg-clip-text">Username</h6>
          <input type="text" class="focus:outline-0 w-full bg-inherit" v-model="username">
        </div>

        <div class="h-[64px] bg-[#EFEFEF] rounded-[10px] px-[16px] mb-[8px]">
          <h6 class="bg-gradient-to-r from-primary-100 to-secondary-100 text-transparent bg-clip-text">Password</h6>
          <input type="password" class="focus:outline-0 w-full bg-inherit" v-model="password">
        </div>

        <div class="h-[64px] bg-[#EFEFEF] rounded-[10px] px-[16px] mb-[8px]">
          <h6 class="bg-gradient-to-r from-primary-100 to-secondary-100 text-transparent bg-clip-text">Repeat password</h6>
          <input type="password" class="focus:outline-0 w-full bg-inherit" v-model="password2">
        </div>

        <div class="h-[64px] bg-[#EFEFEF] rounded-[10px] px-[16px] mb-[8px]">
          <h6 class="bg-gradient-to-r from-primary-100 to-secondary-100 text-transparent bg-clip-text">Bio</h6>
          <input type="text" class="focus:outline-0 w-full bg-inherit" v-model="bio">
        </div>

        <div class="h-[64px] bg-[#EFEFEF] rounded-[10px] px-[16px] mb-[8px]">
          <h6 class="bg-gradient-to-r from-primary-100 to-secondary-100 text-transparent bg-clip-text">Profile Picture</h6>
          <input type="file" ref="file" class="focus:outline-0 w-full bg-inherit" @change="handleFileUpload()">
        </div>


        <button class="bg-gradient-to-r from-primary-100 to-secondary-100 px-[64px] py-[16px] rounded-full mt-[16px] text-center place-self-center mb-[16px] hover:from-primary-80 hover:to-secondary-80 active:from-primary-100 active:to-primary-100"><h4 class="text-white">Sign Up</h4></button>

        <p @click="showLogInPrompt = true" class="text-primary-100 hover:underline active:text-primary-80">Already have an account? Log in instead.</p>
      </form>
    </div>

    <div class="h-screen w-screen bg-black-25 opacity-25"></div>
  </div>
</template>

<script>
import axios from 'axios';
import {toast} from 'bulma-toast';

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

</style>