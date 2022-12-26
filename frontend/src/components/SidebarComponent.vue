<template>
  <div class="w-full">
    <nav class="bg-white rounded-[25px] py-[32px] space-y-[8px] dropShadow">
      <router-link to="/" :class="{dropShadow: $route.name==='home'}" class="sidebarItem">
        <div v-if="$route.name === 'home'" class="highlightBar"></div>
        <i class="fa-solid fa-house text-[24px] mr-[16px]"></i>
        Home
      </router-link>
      <router-link to="/favourites" :class="{dropShadow: $route.name==='favourites'}" class="sidebarItem">
        <div v-if="$route.name === 'favourites'" class="highlightBar"></div>
        <i class="fa-solid fa-star text-[24px] mr-[16px]"></i>
        Favourites
      </router-link>
      <router-link to="/messages" :class="{dropShadow: $route.name==='messages'}" class="sidebarItem">
        <div v-if="$route.name === 'messages'" class="highlightBar"></div>
        <i class="fa-solid fa-message text-[24px] mr-[16px]"></i>
        Messages
      </router-link>
      <router-link to="/friends" :class="{dropShadow: $route.name==='friends'}" class="sidebarItem">
        <div v-if="$route.name === 'friends'" class="highlightBar"></div>
        <i class="fa-solid fa-user-group text-[24px] mr-[8px]"></i>
        Friends
      </router-link>
      <router-link to="/notifications" :class="{dropShadow: $route.name==='notifications'}" class="sidebarItem">
        <div v-if="$route.name === 'notifications'" class="highlightBar"></div>
        <i class="fa-solid fa-bell text-[24px] mr-[16px]"></i>
        Notifications
      </router-link>
      <router-link to="/settings" :class="{dropShadow: $route.name==='settings'}" class="sidebarItem">
        <div v-if="$route.name === 'settings'" class="highlightBar"></div>
        <i class="fa-solid fa-gear text-[24px] mr-[16px]"></i>
        Settings
      </router-link>
    </nav>
  </div>
</template>

<script lang="ts">
import {defineComponent} from "vue";

export default defineComponent({
  name: "SidebarComponent",
});
</script>

<style scoped>
@tailwind components;

@layer components {
  .sidebarItem {
    @apply flex w-full py-[12px] px-[16px] font-['brandon-grotesque'] font-[500] text-black-100 leading-[0px] text-[28px] hover:bg-black-10 rounded-[10px] items-center
  }

  .highlightBar {
    @apply h-[28px] w-[3px] ml-[-16px] mr-[13px] bg-primary-100 rounded-full
  }
}
</style>