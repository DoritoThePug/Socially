<template>
  <div class="w-full flex flex-col">
    <div class="pb-[8px]">
      <h4 class="text-black-75 pr-[8px] inline-block align-middle">Notifications</h4>
      <h6 class="bg-secondary-100 rounded-[5px] py-[5.5px] px-[8px] inline-block leading-[14px] text-white">2</h6>
    </div>

    <div class="space-y-[16px]">
      <NotificationPopupComponent/>
      <NotificationPopupComponent/>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

import NotificationPopupComponent from './NotificationPopupComponent.vue';

export default defineComponent({
  name: "NotificationComponent",
  components: {NotificationPopupComponent}
});
</script>

<style scoped>

</style>