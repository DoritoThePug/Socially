<template>
<div class="w-full">
  <div class="pb-[8px]">
    <h4 class="text-black-75 pr-[8px] inline-block align-middle">Friends</h4>
  </div>

  <div class="flex flex-col bg-white rounded-[25px] dropShadow px-[16px] py-[18px] w-full space-y-[16px]">
    <div class="flex flex-row items-center justify-between">
      <div class="bg-gray-600 h-[42px] w-[42px] rounded-full mr-[16px] relative">
        <div class="h-[10px] w-[10px] bg-success rounded-full absolute bottom-0 right-0"></div>
      </div>
      <h5>Jamal baking</h5>
      <button class="ml-auto">
        <i class="fa-solid fa-ellipsis text-[24px] mr-[16px]"></i>
      </button>
    </div>
    <div class="flex flex-row items-center justify-between">
      <div class="bg-gray-600 h-[42px] w-[42px] rounded-full mr-[16px] relative">
        <div class="h-[10px] w-[10px] bg-black-75 rounded-full absolute bottom-0 right-0"></div>
      </div>
      <h5>Jamal baking</h5>
      <button class="ml-auto">
        <i class="fa-solid fa-ellipsis text-[24px] mr-[16px]"></i>
      </button>
    </div>
    <div class="flex flex-row items-center justify-between">
      <div class="bg-gray-600 h-[42px] w-[42px] rounded-full mr-[16px] relative">
        <div class="h-[10px] w-[10px] bg-error rounded-full absolute bottom-0 right-0"></div>
      </div>
      <h5>Jamal baking</h5>
      <button class="ml-auto">
        <i class="fa-solid fa-ellipsis text-[24px] mr-[16px]"></i>
      </button>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: "FriendsComponent",
};
</script>

<style scoped>

</style>