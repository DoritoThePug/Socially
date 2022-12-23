<template>
  <PostComponent />
</template>

<script>
import axios from 'axios'

import Post from '@/components/Post'
import CreatePost from '@/components/CreatePost'
import PostComponent from '@/components/PostComponent';

export default {
  name: "FeedView",
  data() {
    return {
      posts: []
    }
  },
  components: {
    Post,
    CreatePost,
    PostComponent,
  },
  mounted() {
    this.get_user_posts()
  },
  methods: {
    get_user_posts() {
      axios
          .get('/api/latest-posts/')
          .then(response => {
            this.posts = response.data
          })
    }
  },
};
</script>

<style scoped>

</style>