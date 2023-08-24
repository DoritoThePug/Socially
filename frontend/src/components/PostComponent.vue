<script setup lang="ts">
  const formatter = Intl.NumberFormat('en', {notation: 'compact'})
</script>

<template>
  <div class="w-full">
    <CommentModalComponent v-if="commentModalOpen" class="fixed z-20 inset-0" @close-modal="toggleCommentModal"/>

    <div class="flex flex-col space-y-[16px] bg-white rounded-[25px] p-[24px] dropShadow " :class="{ 'hover:bg-black-5': $route.name != 'post', 'cursor-pointer': $route.name != 'post' }" @click="goToPostDetailPage">
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
        <button class="flex items-center space-x-[8px] p-[8px] rounded-full group" @click="likePost">
          <i class="fa-solid fa-heart text-[24px] inline group-hover:text-secondary-100" :class="{
            'text-primary-100': isLiked,
            'text-black-75': !isLiked
          }"></i>
          <p class="inline group-hover:text-secondary-100">{{ formatter.format(post.likes.length) }} likes</p>
        </button>
        <button class="flex items-center space-x-[8px] group" @click="toggleCommentModal">
          <i class="fa-solid fa-comment text-[24px] text-black-75 group-hover:text-secondary-100"></i>
          <p class="group-hover:text-secondary-100">7k comments</p>
        </button>
        <button class="flex items-center space-x-[8px] group" @click="sharePost">
          <i class="fa-solid fa-share text-[24px] text-black-75 group-hover:text-secondary-100"></i>
          <p class="group-hover:text-secondary-100">1k shares</p>
        </button>
        <button class="flex items-center space-x-[8px] group">
          <i class="fa-solid fa-bookmark text-[24px] text-black-75 group-hover:text-secondary-100"></i>
          <p class="group-hover:text-secondary-100">500 bookmarks</p>
        </button>
      </div>
    </div>

    <h2 class="text-black-75 mt-[32px] mb-[8px]">Comments</h2>

    <div class="bg-white p-[24px] dropShadow rounded-[25px]">
      <CommentComponent/>

      <div class="h-[1px] w-full bg-black-25 my-[16px]"></div>

      <CommentComponent/>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import axios from 'axios'
import { mapState } from 'pinia'

import { useUserStore } from "@/stores/UserStore";
import Post from '@/interfaces/post'
import CommentComponent from "./CommentComponent.vue";
import CommentModalComponent from "./CommentModalComponent.vue"

export default defineComponent({
  name: "PostComponent",
  props: ["post"],
  data() {
    return {
      isLiked: false,
      localPost: this.post as Post,
      postUrl: '',
      commentModalOpen: false
    }
  },
  components: {
      CommentComponent,
      CommentModalComponent
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
    },
    goToPostDetailPage() {
      if (this.$route.name !== 'post') {
          this.$router.push({
              name: 'post',
              params: {
                  user_slug: this.post.author.username,
                  post_id: this.post.id
              }
          })
      }
    },
    toggleCommentModal() {
        this.commentModalOpen = !this.commentModalOpen
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