<script setup lang="ts">
  import {useAuthenticationComponentStore} from "@/stores/AuthenticationComponentStore";
  import {ref} from 'vue'
  import {vOnClickOutside} from "@vueuse/components";

  const formatter = Intl.NumberFormat('en', {notation: 'compact'})

  const authenticationStore = useAuthenticationComponentStore()

  const showDropDown = ref(false)
  function toggleDropDown() {
    showDropDown.value = !showDropDown.value
  }
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

            <button @click="toggleDropDown">
              <i class="fa-solid fa-ellipsis-vertical"></i>
            </button>

            <div v-if="showDropDown" v-on-click-outside="toggleDropDown" class="relative">
              <div class="rounded-[25px] absolute bg-white dropShadow top-[96px] right-[-32px] py-[24px] px-[32px] flex flex-col space-y-[16px]">
                <button @click="authenticationStore.toggleAccountInfoComponent()" class="flex flex-row items-center text-[18px] font-['roboto'] font-[500]">
                  <i class="fa-solid fa-pen-to-square fa-md mr-[16px]"></i>
                  Edit
                </button>
                <button class="flex flex-row items-center text-[18px] font-['roboto'] font-[500] text-error">
                  <i class="fa-solid fa-right-from-bracket fa-md mr-[16px]"></i>
                  Logout
                </button>
              </div>
            </div>
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
      isFollowing: false,
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
    },
    showDropDown() {

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