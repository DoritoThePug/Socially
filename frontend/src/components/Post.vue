<template>
  <div class="w-[600px] p-[16px] bg-white rounded-[10px]">

    <button @click="showDropDown = !showDropDown" class="float-right">
      <i class="fa-solid fa-ellipsis text-primary-100"></i>
      <div class="relative inline-block flex justify-center">
        <div class="absolute block min-w-[100px] flex justify-center">
          <PostMoreDropDown v-if="showDropDown"/>
        </div>
      </div>
    </button>

    <div class="flex no-wrap mb-[16px]">
      <div class="w-[45px] h-[45px] rounded-full overflow-hidden mr-[16px]">
        <img :src="post.author.get_profile_picture" alt="profile picture">
      </div>
      <h6 class="self-center">{{ this.post.author.username }}</h6>

      <button>
        <i @click="followAuthor" class="fa-solid fa-plus text-primary-100 pl-[8px]"></i>
      </button>
    </div>

    <p>{{this.post.content}}</p>
    <hr class="my-[16px]">
    <button @click="likePost">
      <i v-if="!liked" class="fa-solid fa-heart text-primary-100"></i>
      <i v-else class="fa-solid fa-heart text-secondary-100"></i>
    </button>
    <button class="mx-[16px]">
      <i class="fa-solid fa-comment text-primary-100"></i>
    </button>
    <button>
      <i class="fa-solid fa-star text-primary-100"></i>
    </button>
    <button class="float-right">
      <i class="fa-solid fa-flag text-primary-100"></i>
    </button>
  </div>
</template>

<script>
import axios from 'axios'

import PostMoreDropDown from '@/components/PostMoreDropDown';

export default {
  name: "Post",
  props: {
    post: Object
  },
  components: {
    PostMoreDropDown
  },
  data() {
    return {
      liked: false,
      favourited: false,
      showDropDown: false, // PostMoreDropDown.vue
    }
  },
  mounted() {
    if (this.$store.state.isAuthenticated) {
      this.getPostInfo()
    }
  },
  methods: {
    likePost() {
      axios
          .patch(`/api/posts/${this.post.id}/like/`,{})
          .then(response => {
            this.liked = response.data === "Post liked";
          }).catch(error => {
        console.log(error)
      })
    },
    getPostInfo() {
      // Get the post info (is it liked, favourited, etc)

      axios
          .get(`/api/posts/${this.post.id}/like/`)
          .then(response => {
            this.liked = response.data === "Post liked"
      })
    },
    deletePost() { // Called by PostMoreDropDown
      axios
          .delete(`/api/posts/${this.post.id}/delete/`)
          .then(response => {
          this.$router.go()
      })
    },
    followAuthor() {
      axios
          .patch(`/api/${this.post.author.slug}/follow/`)
          .then(response => {
            console.log(response)
      }).catch(error => {
        console.log(error)
      })
    }
  },
};
</script>

<style scoped>

</style>