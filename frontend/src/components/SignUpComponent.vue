<script setup lang="ts">
  import { useAuthenticationComponentStore } from "@/stores/AuthenticationComponentStore";

  const authenticationStore = useAuthenticationComponentStore();
</script>

<template>
<div class="w-full h-full backdrop-blur-md flex place-content-center">
    <div class="flex flex-col p-[32px] bg-white rounded-[25px] self-center">
      <div class="flex flex-row justify-between items-center">
        <h2 class="self-center align-middle">Sign Up</h2>
        <button class="ml-auto flex-none hover:text-secondary-100" @click="authenticationStore.toggleSignUpComponent()">
          <i class="fa-solid fa-x"></i>
        </button>
      </div>

      <form @submit.prevent="submitSignUpForm" class="flex flex-col justify-center">
        <h6 class="font-normal text-black-75 mr-[8px]">Email</h6>
        <div class="min-w-[280px] rounded-[10px] p-[8px] border-[1px] border-black-25 mb-[16px]" :class="{ 'border-black-25': !emailError, 'border-error': emailError }">
          <input class="w-full bg-white focus:outline-none font-['roboto'] text-[14px]" type="email" v-model="email">
        </div>
         <p v-if="emailError" class="text-[9px] text-error mt-[-8px] mb-[8px]">{{ this.emailError }}</p>

        <h6 class="font-normal text-black-75 mr-[8px]">Username</h6>
        <div class="min-w-[280px] rounded-[10px] p-[8px] border-[1px] border-black-25 mb-[16px]" :class="{ 'border-black-25': !usernameError, 'border-error': usernameError }">
          <input class="w-full bg-white focus:outline-none font-['roboto'] text-[14px]" type="email" v-model="username">
        </div>
         <p v-if="usernameError" class="text-[9px] text-error mt-[-8px] mb-[8px]">{{ this.usernameError }}</p>

        <h6 class="font-normal text-black-75 mr-[8px]">Password</h6>
        <div class="min-w-[280px] rounded-[10px] p-[8px] border-[1px] mb-[8px]" :class="{ 'border-black-25': !passwordError, 'border-error': passwordError }">
          <input class="w-full bg-white focus:outline-none" type="password" v-model="password">
        </div>
        <p v-if="passwordError" class="text-[9px] text-error mt-[-8px] mb-[8px]">{{ this.passwordError }}</p>

        <h6 class="font-normal text-black-75 mr-[8px]">Repeat Password</h6>
        <div class="min-w-[280px] rounded-[10px] p-[8px] border-[1px] mb-[8px]" :class="{ 'border-black-25': !repeatPasswordError, 'border-error': repeatPasswordError }">
          <input class="w-full bg-white focus:outline-none" type="password" v-model="repeatPassword">
        </div>
        <p v-if="repeatPasswordError" class="text-[9px] text-error mt-[-8px] mb-[8px]">{{ this.repeatPasswordError }}</p>

        <div class="flex flex-row items-center justify-between mb-[16px]">
          <input
              class="mr-[4px] w-[12px] h-[12px] appearance-none border-[1px] border-black-25 rounded-[2px] checked:bg-secondary-100 hover:border-black-50"
              type="checkbox"
              v-model="rememberMe">
          <p class="text-[12px] text-black-50">Remember me</p>
        </div>

        <button class="px-[38px] py-[8px] self-center rounded-[5px] bg-primary-100 hover:bg-primary-80 mb-[16px]" formnovalidate="formnovalidate">
          <h4 class="text-white">Sign Up</h4>
        </button>
      </form>

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

      <button class="self-center" @click="authenticationStore.toggleAuthenticationComponent()">
        <p class="inline">Already have an account? </p>
        <p class="text-secondary-100 hover:text-secondary-80 inline">Log In</p>
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios'

export default defineComponent({
  name: "SignUpComponent",
  data() {
    return {
      email: '',
      username: '',
      password: '',
      repeatPassword: '',

      emailError: '',
      usernameError: '',
      passwordError: '',
      repeatPasswordError: '',
    }
  },
  methods: {
    validateAuthenticationForm(): boolean { // makes sure inputs are valid for authentication form
      if (this.email === "") {
        this.emailError = "Email is required"
      } else if (this.email.length > 255 || !this.email.includes("@") || !this.email.includes(".")) {
        this.emailError = "Please enter a valid email"
      } else {
        this.emailError = ""
      }

      if (this.password === "") {
        this.passwordError = "Password is required"
      } else {
        this.passwordError = ""
      }

      if (this.repeatPassword === "") {
        this.repeatPasswordError = "Please repeat your password"
      } else if (!(this.password === this.repeatPassword)) {
        this.repeatPasswordError = "Passwords do not match"
      }
      else {
        this.repeatPasswordError = ""
      }

      if (this.username=== "") {
        this.usernameError = "Username is required"
      } else if (this.username.length > 255) {
        this.usernameError = "Username must be less than 255 characters"
      } else {
        this.usernameError = ""
      }

      return !(this.emailError || this.passwordError || this.repeatPasswordError || this.usernameError)
    },

    async submitSignUpForm() {
      if (this.validateAuthenticationForm()) {
        await axios.post('/api/create-user/', {
          email: this.email,
          username: this.username,
          password: this.password,
        }).then(response => {
          console.log(response)
        }).catch(error => {
          console.log(error)
        })
      }
    }
  }
});
</script>

<style scoped>
.authenticationIcon {
  @apply flex place-items-center px-[10px] py-[6px] rounded-[5px] border-[1px] border-black-25;
}
</style>