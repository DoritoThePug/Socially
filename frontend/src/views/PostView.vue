<template>
  <div class="page-post grid justify-center pt-[64px]">
    <Post v-if="showPost" :post="post"/>
  </div>
</template>

<script>
import axios from 'axios'

import Post from '@/components/Post'

export default {
  name: "PostView",
  components: {
    Post
  },
  data() {
    return {
      post: {},
      showPost: false, // This is a flag to show the post only when data is fetched
    }
  },
  mounted() {
    this.getPostDetail()
  },
  methods: {
    async getPostDetail() {
      const post_id = this.$route.params.post_id

      await axios
          .get(`/api/posts/${post_id}`)
          .then(response => {
            this.post = response.data
            console.log(response.data)
          })

      this.showPost = true
    }
  },
};
</script>

<style scoped>

</style>