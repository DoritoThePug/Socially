<script setup lang="ts">
  const formatter = Intl.NumberFormat('en', {notation: 'compact'})
</script>

<template>
  <div class="w-full">
    <div class="flex flex-col space-y-[16px] bg-white rounded-[25px] p-[24px] dropShadow">
      <div class="flex flex-row items-center justify-between">
        <img :src="localPost.author.get_profile_picture" class="h-[42px] w-[42px] rounded-full mr-[16px]" />
        <div>
          <h4 class="leading-none">{{ localPost.author.username }}</h4>
          <p class="text-[9px] text-black-50">{{ localPost.date_created }}</p>
        </div>
        <button class="ml-auto">
          <i class="fa-solid fa-ellipsis text-[24px] text-black-75"></i>
        </button>
      </div>

      <p>{{ localPost.content }}</p>

      <div class="w-full h-[400px] bg-black-25 rounded-[25px]"></div>

      <div class="h-[1px] w-full bg-black-25"></div>

      <div class="flex flex-row justify-between items center">
        <button class="flex items-center space-x-[8px]" @click="likePost">
          <i class="fa-solid fa-heart text-[24px] inline" :class="{
            'text-primary-100': isLiked,
            'text-black-75': !isLiked
          }"></i>
          <p class="inline">{{ formatter.format(post.likes.length) }} likes</p>
        </button>
        <button class="flex items-center space-x-[8px]">
          <i class="fa-solid fa-comment text-[24px] text-black-75"></i>
          <p>7k comments</p>
        </button>
        <button class="flex items-center space-x-[8px]" @click="sharePost">
          <i class="fa-solid fa-share text-[24px] text-black-75"></i>
          <p>1k shares</p>
        </button>
        <button class="flex items-center space-x-[8px]">
          <i class="fa-solid fa-bookmark text-[24px] text-black-75"></i>
          <p>500 bookmarks</p>
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import axios from 'axios'
import { mapState } from 'pinia'

import { useUserStore } from "@/stores/UserStore";
import Post from '@/interfaces/post'

export default defineComponent({
  name: "PostComponent",
  props: ["post"],
  data() {
    return {
      isLiked: false,
      localPost: this.post as Post,
      postUrl: ''
    }
  },
  computed: {
    ...mapState(useUserStore, ['isAuthenticated'])
  },
  methods: {
    async likePost() {
      await axios.patch(`/api/posts/${this.post.id}/like/`).then(response => {
        this.isLiked = !this.isLiked
        this.localPost.likes = response.data.likes
      }).catch(error => {
        console.log(error)
      })
    },
    async isPostLiked() {
      await axios.get(`/api/posts/${this.post.id}/like/`).then(response => {
        this.isLiked = response.data.isLiked
        this.localPost.likes = response.data.post.likes
      }).catch(error => {
        console.log(error)
      })
    },
    getPostUrl() {
      this.postUrl = `${window.location.origin}/${this.post.author.username}/post/${this.post.id}`
    },
    sharePost() {
      navigator.share({
        title: 'Share Post',
        text: this.post.content,
        url: this.postUrl
      }).then(() => {
        console.log('Thanks for sharing!')
      }).catch(console.error)
    }
  },
  mounted() {
    if (this.isAuthenticated) {
      this.isPostLiked()
    }

    this.getPostUrl()
  }
});
</script>

<style scoped>

</style>