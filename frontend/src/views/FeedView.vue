<template>
  <div class="w-full">
    <div class="flex flex-col space-y-[32px]">
      <CreatePostComponent class="mb-[16px]"/>

      <PostComponent />
      <PostComponent />
      <PostComponent />
      <PostComponent />
      <PostComponent />
    </div>
  </div>
</template>

<script>
import axios from 'axios'

// import Post from '@/components/Post'
// import CreatePost from '@/components/CreatePost'
import CreatePostComponent from '@/components/CreatePostComponent';
import PostComponent from '@/components/PostComponent';



export default {
  name: "FeedView",
  data() {
    return {
      posts: []
    }
  },
  components: {
    // Post,
    // CreatePost,
    PostComponent,
    CreatePostComponent,
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