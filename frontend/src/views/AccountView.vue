<template>
  <div class="w-full">
    <div class="flex flex-col space-y-[32px]">
      <ProfileComponent :toggleAuthenticationPrompt="toggleAuthenticationPrompt" :toggleSignUpPrompt="toggleSignUpPrompt"/>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

import ProfileComponent from '../components/ProfileComponent.vue';

export default defineComponent({
  name: "AccountView",
  components: {
    ProfileComponent
  },
  props: {
    toggleAuthenticationPrompt: Function,
    toggleSignUpPrompt: Function
  }
});
</script>

<style scoped>

</style>