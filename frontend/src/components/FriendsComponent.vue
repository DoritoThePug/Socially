<template>
  <div class="xl:w-full w-fit">
    <div class="pb-[8px]">
      <h4 class="text-black-75 pr-[8px] inline-block align-middle">Friends</h4>
    </div>

    <div
      class="flex flex-col bg-white rounded-[25px] dropShadow px-[16px] py-[18px] w-full space-y-[16px]"
    >
      <div class="flex flex-row items-center justify-between">
        <div
          class="bg-gray-600 h-[42px] w-[42px] rounded-full xl:mr-[16px] relative"
        >
          <div
            class="h-[10px] w-[10px] bg-success rounded-full absolute bottom-0 right-0"
          ></div>
        </div>
        <h5 class="hidden xl:block">Jamal baking</h5>
        <button class="ml-auto">
          <i
            class="hidden fa-solid fa-ellipsis text-[24px] xl:mr-[16px] xl:block"
          ></i>
        </button>
      </div>
      <div class="flex flex-row items-center justify-between">
        <div
          class="bg-gray-600 h-[42px] w-[42px] rounded-full xl:mr-[16px] relative"
        >
          <div
            class="h-[10px] w-[10px] bg-black-75 rounded-full absolute bottom-0 right-0"
          ></div>
        </div>
        <h5 class="hidden xl:block">Jamal baking</h5>
        <button class="ml-auto">
          <i
            class="hidden fa-solid fa-ellipsis text-[24px] mr-[16px] xl:block"
          ></i>
        </button>
      </div>
      <div class="flex flex-row items-center justify-between">
        <div
          class="bg-gray-600 h-[42px] w-[42px] rounded-full xl:mr-[16px] relative"
        >
          <div
            class="h-[10px] w-[10px] bg-error rounded-full absolute bottom-0 right-0"
          ></div>
        </div>
        <h5 class="hidden xl:block">Jamal baking</h5>
        <button class="ml-auto">
          <i
            class="hidden fa-solid fa-ellipsis text-[24px] mr-[16px] xl:block"
          ></i>
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "FriendsComponent",
});
</script>

<style scoped></style>
