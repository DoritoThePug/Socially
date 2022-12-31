<script setup lang="ts">
  import { storeToRefs } from 'pinia'

  import { useUserStore } from '@/stores/UserStore'

  const { isAuthenticated } = storeToRefs(useUserStore())
  const { user } = storeToRefs(useUserStore())
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
      <button  v-if="isAuthenticated" @click="toggleDropDown">
        <img :src="user.get_profile_picture" alt="" class="w-[32px] h-[32px] rounded-full">
      </button>
      <button v-else class="hover:text-secondary-100" @click="$parent.toggleAuthenticationPrompt">
        <i class="fa-solid fa-right-to-bracket text-[24px]"></i>
      </button>

      <div v-if="showDropDown" class="relative">
        <div class="rounded-[25px] absolute bg-white dropShadow top-[32px] right-[8px] py-[24px] px-[32px] flex flex-col space-y-[16px]">
          <button class="flex flex-row items-center text-[18px] font-['brandon-grotesque'] font-[500]">
            <i class="fa-solid fa-user fa-md mr-[32px]"></i>
            Profile
          </button>
          <button class="flex flex-row items-center text-[18px] font-['brandon-grotesque'] font-[500]">
            <i class="fa-solid fa-gear fa-md mr-[32px]"></i>
            Settings
          </button>
          <button class="flex flex-row items-center text-[18px] font-['brandon-grotesque'] font-[500] text-error">
            <i class="fa-solid fa-right-from-bracket fa-md mr-[32px]"></i>
            Logout
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: "NavBarComponent",
  data() {
    return {
      showDropDown: false
    }
  },
  methods: {
    toggleDropDown() {
      this.showDropDown = !this.showDropDown
    }
  }
});
</script>

<style scoped>

</style>