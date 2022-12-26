<template>
  <div class="w-full">
    <div class="flex flex-col bg-white rounded-[25px] dropShadow px-[16px] py-[18px]">
      <div class="flex flex-row space-x-[8px] mb-[12px]">
        <div class="h-[42px] aspect-square pr-[8px] bg-gray-600 rounded-full"></div>
        <div>
          <p class="font-bold">Burrito Baby </p>
          <p>wants to becomes friends with you!</p>
        </div>
      </div>

      <div class="flex flex-row justify-center space-x-[16px]">
        <button class="bg-primary-100 rounded-[5px] py-[4px] px-[20px]">
          <h5 class="text-white">Accept</h5>
        </button>

        <button class="bg-black-50 rounded-[5px] py-[4px] px-[20px]">
          <h5 class="text-white">Ignore</h5>
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "NotificationPopupComponent"
});
</script>

<style scoped>

</style>