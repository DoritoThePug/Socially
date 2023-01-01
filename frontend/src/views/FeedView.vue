<template>
  <div class="w-full">
    <div class="flex flex-col space-y-[32px]">
      <CreatePostComponent class="mb-[16px]" @reloadFeed="getLatestPosts"/>

      <PostComponent v-for="post in latestPosts" :post="post" :id="post.id"/>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import axios from 'axios'

import CreatePostComponent from '../components/CreatePostComponent.vue';
import PostComponent from '../components/PostComponent.vue';

import post from '@/interfaces/post'


export default defineComponent({
  name: "FeedView",
  components: {
    PostComponent,
    CreatePostComponent,
  },
  data() {
    return {
      latestPosts: [] as post[]
    }
  },
  methods: {
    async getLatestPosts() {
      await axios.get('/api/latest-posts/')
        .then((response) => {
          this.latestPosts = response.data;
        })
        .catch((error) => {
          console.log(error);
        })
    }
  },
  mounted() {
    this.getLatestPosts();
  }
});
</script>

<style scoped>

</style>