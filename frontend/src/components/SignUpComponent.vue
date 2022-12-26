<template>
<div class="w-full h-full backdrop-blur-md flex place-content-center">
    <div class="flex flex-col p-[32px] bg-white rounded-[25px] self-center">
      <div class="flex flex-row justify-between items-center">
        <h2 class="self-center align-middle">Sign Up</h2>
        <button class="ml-auto flex-none hover:text-secondary-100" @click="$parent.toggleSignUpPrompt">
          <i class="fa-solid fa-x"></i>
        </button>
      </div>

      <h6 class="font-normal text-black-75 mr-[8px]">Email</h6>
      <div class="min-w-[280px] rounded-[10px] p-[8px] border-[1px] border-black-25 mb-[16px]">
        <input class="w-full bg-white focus:outline-none font-['roboto'] text-[14px]" type="email">
      </div>

      <h6 class="font-normal text-black-75 mr-[8px]">Username</h6>
      <div class="min-w-[280px] rounded-[10px] p-[8px] border-[1px] border-black-25 mb-[16px]">
        <input class="w-full bg-white focus:outline-none font-['roboto'] text-[14px]" type="text">
      </div>

      <h6 class="font-normal text-black-75 mr-[8px]">Password</h6>
      <div class="min-w-[280px] rounded-[10px] p-[8px] border-[1px] border-black-25 mb-[16px]">
        <input class="w-full bg-white focus:outline-none" type="password">
      </div>

      <h6 class="font-normal text-black-75 mr-[8px]">Repeat Password</h6>
      <div class="min-w-[280px] rounded-[10px] p-[8px] border-[1px] border-error mb-[8px]">
        <input class="w-full bg-white focus:outline-none" type="password">
      </div>
     <p class="text-[9px] text-error mt-[-8px] mb-[8px]">Passwords do not match</p>

      <div class="flex flex-row items-center justify-between mb-[16px]">
        <input class="mr-[4px] w-[12px] h-[12px] appearance-none border-[1px] border-black-25 rounded-[2px] checked:bg-secondary-100 hover:border-black-50" type="checkbox">
        <p class="text-[12px] text-black-50">Remember me</p>

        <router-link to="" class="ml-auto text-[12px] text-secondary-100 hover:text-secondary-80">Forgot Password?</router-link>
      </div>

      <button class="px-[38px] py-[8px] self-center rounded-[5px] bg-primary-100 hover:bg-primary-80 mb-[16px]">
        <h4 class="text-white">Sign Up</h4>
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

      <button class="self-center" @click="$parent.toggleAuthenticationPrompt">
        <p class="inline">Already have an account? </p>
        <p class="text-secondary-100 hover:text-secondary-80 inline">Log In</p>
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: "SignUpComponent",
});
</script>

<style scoped>
.authenticationIcon {
  @apply flex place-items-center px-[10px] py-[6px] rounded-[5px] border-[1px] border-black-25;
}
</style>