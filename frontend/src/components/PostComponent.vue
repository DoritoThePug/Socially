<template>
  <div class="w-full">
    <div class="flex flex-col space-y-[16px] bg-white rounded-[25px] p-[24px] dropShadow">
      <div class="flex flex-row items-center justify-between">
        <div class="h-[42px] w-[42px] bg-black-50 rounded-full mr-[16px]"></div>
        <div>
          <h4 class="leading-none">Jamal Baking</h4>
          <p class="text-[9px] text-black-50">10 days ago</p>
        </div>
        <button class="ml-auto">
          <i class="fa-solid fa-ellipsis text-[24px] text-black-75"></i>
        </button>
      </div>

      <p>Guys check out my cookies!</p>

      <div class="w-full h-[400px] bg-black-25 rounded-[25px]"></div>

      <div class="h-[1px] w-full bg-black-25"></div>

      <div class="flex flex-row justify-between items center">
        <button class="flex items-center space-x-[8px]">
          <i class="fa-solid fa-heart text-[24px] inline"></i>
          <p class="inline">17k likes</p>
        </button>
        <button class="flex items-center space-x-[8px]">
          <i class="fa-solid fa-comment text-[24px]"></i>
          <p>7k comments</p>
        </button>
        <button class="flex items-center space-x-[8px]">
          <i class="fa-solid fa-share text-[24px]"></i>
          <p>1k shares</p>
        </button>
        <button class="flex items-center space-x-[8px]">
          <i class="fa-solid fa-bookmark text-[24px]"></i>
          <p>500 bookmarks</p>
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "PostComponent"
});
</script>

<style scoped>

</style>