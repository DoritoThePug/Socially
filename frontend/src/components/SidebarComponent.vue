<template>
  <div
    class="2xl:w-full xl:w-full lg:w-[64px] md:w-[64px] sm:w-[64px] flex flex-col"
  >
    <nav class="bg-white rounded-[25px] py-[32px] space-y-[8px] dropShadow">
      <router-link
        to="/"
        :class="{ dropShadow: $route.name === 'home' }"
        class="sidebarItem"
      >
        <div v-if="$route.name === 'home'" class="highlightBar"></div>
        <i class="fa-solid fa-house icon"></i>
        <h1 class="sidebarText">Home</h1>
      </router-link>
      <router-link
        to="/favourites"
        :class="{ dropShadow: $route.name === 'favourites' }"
        class="sidebarItem"
      >
        <div v-if="$route.name === 'favourites'" class="highlightBar"></div>
        <i class="fa-solid fa-star icon"></i>
        <h1 class="sidebarText">Favourites</h1>
      </router-link>
      <router-link
        to="/messages"
        :class="{ dropShadow: $route.name === 'messages' }"
        class="sidebarItem"
      >
        <div v-if="$route.name === 'messages'" class="highlightBar"></div>
        <i class="fa-solid fa-message icon"></i>
        <h1 class="sidebarText">Messages</h1>
      </router-link>
      <router-link
        to="/friends"
        :class="{ dropShadow: $route.name === 'friends' }"
        class="sidebarItem"
      >
        <div v-if="$route.name === 'friends'" class="highlightBar"></div>
        <i class="fa-solid fa-user-group text-[24px] mr-[8px]"></i>
        <h1 class="sidebarText">Friends</h1>
      </router-link>
      <router-link
        to="/notifications"
        :class="{ dropShadow: $route.name === 'notifications' }"
        class="sidebarItem"
      >
        <div v-if="$route.name === 'notifications'" class="highlightBar"></div>
        <i class="fa-solid fa-bell icon"></i>
        <h1 class="sidebarText">Notifications</h1>
      </router-link>
      <router-link
        to="/settings"
        :class="{ dropShadow: $route.name === 'settings' }"
        class="sidebarItem"
      >
        <div v-if="$route.name === 'settings'" class="highlightBar"></div>
        <i class="fa-solid fa-gear icon"></i>
        <h1 class="sidebarText">Settings</h1>
      </router-link>
    </nav>

    <div
      class="rounded-full bg-primary-100 h-[48px] w-[48px] xl:hidden mt-[32px] flex justify-center items-center self-center"
    >
      <i class="fa-solid fa-plus text-[24px] text-white"></i>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "SidebarComponent",
});
</script>

<style scoped>
@tailwind components;

@layer components {
  .sidebarItem {
    @apply flex w-full py-[12px] px-[16px] hover:bg-black-10 rounded-[10px] items-center overflow-hidden;
  }

  .highlightBar {
    @apply h-[28px] w-[3px] ml-[-16px] mr-[13px] bg-primary-100 rounded-full;
  }

  .icon {
    @apply text-[24px] 2xl:mr-[16px] xl:mr-[16px];
  }

  .sidebarText {
    font-family: "Lato", sans-serif;
    @apply font-[400] text-black-100 text-[28px] leading-none hidden 2xl:block xl:block;
  }
}
</style>
