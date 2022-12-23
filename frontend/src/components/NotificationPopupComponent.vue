<template>
  <div class="w-full">
    <div class="flex bg-white rounded-[25px] dropShadow overflow-x-hidden px-[16px] py-[18px] w-auto ">
      <div class="w-[15%]">
        <div class="h-[42px] w-[42px] pr-[8px] bg-gray-600 rounded-full inline-block"></div>
      </div>

      <div class="flex flex-col w-[85%] pl-[8px] w-auto justify-between">
        <p class="font-bold">Burrito Baby </p><p>wants to becomes friends with you!</p>

        <div class="space-x-[16px] pt-[8px]">
          <button class="w-auto bg-primary-100 rounded-[5px] inline-block py-[4px] px-[25px]">
            <h5 class="text-white w-auto">Accept</h5>
          </button>

          <button class="bg-black-50 rounded-[5px] inline-block py-[4px] px-[25px]">
            <h5 class="text-white w-auto">Ignore</h5>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NotificationPopupComponent"
};
</script>

<style scoped>

</style>