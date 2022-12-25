<script setup>
  import { storeToRefs } from 'pinia'

  import { useUserStore } from '@/stores/UserStore'

  const { isAuthenticated } = storeToRefs(useUserStore())
</script>

<template>
  <nav class="w-full">
    <div class="flex flex-row justify-between items-center">
      <h4 class="bg-gradient-to-r from-primary-100 to-secondary-100 text-transparent bg-clip-text">SOCIALLY</h4>
      <div class="flex ml-auto w-[400px] bg-black-10 h-[32px] rounded-[10px] mr-[16px] py-[8px] px-[16px] content-center">
        <input class="bg-black-10 w-full overflow-hidden focus: outline-none font-['roboto'] text-[14px]" type="text" placeholder="Search"/>
        <i class="fa-solid fa-magnifying-glass text-primary-100 text-black-50"></i>
      </div>
      <button class="mr-[32px] text-[20px]">
        <i class="fa-solid fa-sun"></i>
      </button>
      <div  v-if="isAuthenticated" class="w-[32px] h-[32px] bg-black-50 rounded-full"></div>
      <button v-else class="hover:text-secondary-100" @click="$parent.toggleAuthenticationPrompt">
        <i class="fa-solid fa-right-to-bracket text-[24px]"></i>
      </button>
    </div>
  </nav>
</template>

<script>


export default {
  name: "NavBar"
};
</script>

<style scoped>

</style>