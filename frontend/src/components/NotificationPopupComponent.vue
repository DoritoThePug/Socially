<template>
  <div class="w-full">
    <div
      class="flex flex-col bg-white rounded-[25px] dropShadow px-[16px] py-[18px]"
    >
      <div class="flex flex-row space-x-[8px] mb-[12px]">
        <div
          class="h-[42px] aspect-square pr-[8px] bg-gray-600 rounded-full"
        ></div>
        <div>
          <p class="font-bold">Burrito Baby</p>
          <p>wants to becomes friends with you!</p>
        </div>
      </div>

      <div class="flex flex-row justify-center space-x-[16px]">
        <button
          class="bg-primary-100 rounded-[5px] py-[4px] 2xl:px-[20px] xl:px-[12px] xl:w-fit xl:h-fit lg:w-[28px] lg:h-[28px]"
        >
          <h5 class="hidden 2xl:block xl:block text-white">Accept</h5>
          <i
            class="fa-solid fa-check text-white text-[16-px] 2xl:hidden xl:hidden"
          ></i>
        </button>

        <button
          class="bg-black-50 rounded-[5px] py-[4px] 2xl:px-[20px] xl:px-[12px] xl:w-fit xl:h-fit lg:w-[28px] lg:h-[28px]"
        >
          <h5 class="hidden 2xl:block xl:block text-white">Ignore</h5>
          <i
            class="fa-solid fa-x text-white text-[16-px] 2xl:hidden xl:hidden"
          ></i>
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "NotificationPopupComponent",
});
</script>

<style scoped></style>
