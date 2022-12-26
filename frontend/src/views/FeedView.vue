<template>
  <div class="w-full">
    <div class="flex flex-col space-y-[32px]">
      <CreatePostComponent class="mb-[16px]"/>

      <PostComponent />
      <PostComponent />
      <PostComponent />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

import CreatePostComponent from '../components/CreatePostComponent.vue';
import PostComponent from '../components/PostComponent.vue';



export default defineComponent({
  name: "FeedView",
  components: {
    PostComponent,
    CreatePostComponent,
  },
});
</script>

<style scoped>

</style>