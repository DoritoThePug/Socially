<script setup lang="ts">
  const formatter = Intl.NumberFormat('en', {notation: 'compact'})
</script>

<template>
  <div class="w-full space-y-[32px]">
    <div class="px-[288px]">
      <div class="w-full flex flex-col relative bg-white rounded-[25px] h-[320px] dropShadow mb-[32px]">
        <div class="absolute h-[55%] rounded-t-[25px] w-full dropShadow"></div>
        <div class="p-[24px] pt-[128px] z-10">
          <div class="flex flex-row justify-between">
            <div>
              <img :src="user.get_profile_picture" class="z-50 w-[112px] aspect-square rounded-full bg-black-50 mb-[8px]"/>
              <h5 class="leading-none">{{ user.username }}</h5>
              <div>
                <p class="text-[10px] text-black-50 inline mr-[8px]"><b>{{ formatter.format(user.followers) }}</b>
                  Followers</p>
                <p class="text-[10px] text-black-50 inline"><b>{{ formatter.format(user.following) }}</b> Following</p>
              </div>
            </div>

            <button v-if="!isFollowing" @click="followUser" class="bg-primary-100 text-white font-[500] px-[8px] rounded-[8px] self-center ml-auto mr-[16px]">
              Follow
            </button>
            <button v-else @click="followUser" class="bg-black-50 text-white font-[500] px-[8px] rounded-[8px] self-center ml-auto mr-[16px]">
              Following
            </button>

            <button>
              <i class="fa-solid fa-ellipsis-vertical"></i>
            </button>
          </div>
        </div>
      </div>
    </div>

    <PostComponent v-for="post in posts" :post="post" id="post.id"/>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import axios from 'axios'

import User from '@/interfaces/user'
import Post from '@/interfaces/post'

import PostComponent from '@/components/PostComponent.vue'

export default defineComponent({
  name: "ProfileComponent",
  components: {
    PostComponent
  },
  props: {
    toggleAuthenticationPrompt: Function,
    toggleSignUpPrompt: Function
  },
  data() {
    return {
      user: {} as User,
      posts: [] as Post[],
      isFollowing: false
    }
  },
  methods: {
    async getUserInfo() {
      await axios.get(`/api/${this.$route.params.user_slug}/`)
        .then((response) => {
          this.user = response.data.user
          this.isFollowing = response.data.is_following
        })
        .catch((error) => {
          console.log(error)
        })
    },
    async getUserPosts() {
      await axios.get(`/api/posts/${this.$route.params.user_slug}/`)
        .then((response) => {
          this.posts = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    async followUser() {
      await axios.patch(`/api/${this.$route.params.user_slug}/follow/`)
        .then((response) => {
          this.user = response.data.user
          this.isFollowing = response.data.is_following
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  mounted() {
    this.getUserInfo()
    this.getUserPosts()
  }
});
</script>

<style scoped>

</style>