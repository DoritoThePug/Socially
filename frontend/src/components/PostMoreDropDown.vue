// Drop down menu for when you click the more optionals button on a post/comment

<template>
<!-- &ndash;&gt; <div class="p-[8px] rounded-[15px] bg-black-25">-->
<!--    <button class="flex no-wrap">-->
<!--      <i class="fa-solid fa-trash pr-[8px]"></i>-->
<!--      <p>Delete</p>-->
<!--    </button>-->
<!--&lt;!&ndash;  </div>-->

  <button @click="$parent.deletePost()">Delete</button>

</template>

<script>
export default {
  name: "PostMoreDropDown"
};
</script>

<style scoped>

</style>