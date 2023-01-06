<script setup lang="ts">
import {useAuthenticationComponentStore} from "@/stores/AuthenticationComponentStore";

const authenticationStore = useAuthenticationComponentStore()
</script>

<template>
  <div class="w-full h-full backdrop-blur-md flex place-content-center">
    <div class="flex flex-col p-[32px] bg-white rounded-[25px] self-center">
      <div class="flex flex-row justify-between items-center">
        <h2 class="self-center align-middle">WIP</h2>
        <button class="ml-auto flex-none hover:text-secondary-100" @click="authenticationStore.toggleAccountDetailsComponent()">
          <i class="fa-solid fa-x"></i>
        </button>
      </div>

      <form @submit.prevent="submitAccountDetailsForm" class="flex flex-col justify-center">
        <h6 class="font-normal text-black-75 mr-[8px]">Email</h6>
        <div class="min-w-[280px] rounded-[10px] p-[8px] border-[1px] border-black-25 mb-[16px]" :class="{ 'border-black-25': !emailError, 'border-error': emailError }">
          <input class="w-full bg-white focus:outline-none font-['roboto'] text-[14px]" type="email" v-model="email">
        </div>
         <p v-if="emailError" class="text-[9px] text-error mt-[-8px] mb-[8px]">{{ this.emailError }}</p>

        <h6 class="font-normal text-black-75 mr-[8px]">Password</h6>
        <div class="min-w-[280px] rounded-[10px] p-[8px] border-[1px] mb-[8px]" :class="{ 'border-black-25': !passwordError, 'border-error': passwordError }">
          <input class="w-full bg-white focus:outline-none" type="password" v-model="password">
        </div>
        <p v-if="passwordError" class="text-[9px] text-error mt-[-8px] mb-[8px]">{{ this.passwordError }}</p>

        <div class="flex flex-row items-center justify-between mb-[16px]">
          <input
              class="mr-[4px] w-[12px] h-[12px] appearance-none border-[1px] border-black-25 rounded-[2px] checked:bg-secondary-100 hover:border-black-50"
              type="checkbox"
              v-model="rememberMe">
          <p class="text-[12px] text-black-50">Remember me</p>

          <router-link to="" class="ml-auto text-[12px] text-secondary-100 hover:text-secondary-80">Forgot Password?
          </router-link>
        </div>

        <button type="submit" class="px-[38px] py-[8px] self-center rounded-[5px] bg-primary-100 hover:bg-primary-80 mb-[16px]" formnovalidate="formnovalidate">
          <h4 class="text-white">Log In</h4>
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

      <button class="self-center" @click="authenticationStore.toggleSignUpComponent()" >
        <p class="inline">Don't have an account? </p>
        <p class="text-secondary-100 hover:text-secondary-80 inline">Sign up</p>
      </button>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  name: "AccountDetailsComponent",
  methods: {
    submitAccountDetailsForm(){

    }
  }
};
</script>

<style scoped>

</style>