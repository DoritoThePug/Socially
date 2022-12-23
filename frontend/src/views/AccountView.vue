<template>
  <div class="page-feed pt-[64px]">
    <div class="grid grid-flow-col auto-cols-auto justify-center space-y-[32px]">
      <div class="mb-[32px] flex no-wrap">
        <div class="h-[128px] w-[128px] rounded-full overflow-hidden mr-[64px]">
          <img :src="this.user.get_profile_picture" alt="profile picture" class="object-cover h-full w-full">
        </div>
        <div><h3>{{ user.username }}</h3>
          <i class="fa-solid fa-users wrap"></i></div>
      </div>


    </div>
<!--    <div class="grid justify-center space-y-[32px]">-->
<!--      <Post v-for="post in posts"-->
<!--            :key="post.id"-->
<!--            :post="post"-->
<!--      />-->
<!--    </div>-->
  </div>
</template>

<script>
import axios from 'axios'

import Post from '@/components/Post'

export default {
  name: "AccountView",
  data() {
    return {
      user: {},
    }
  },
  mounted() {
    this.getUserDetails()
  },
  methods: {
    getUserDetails() {
      const user_slug = this.$route.params.user_slug

      axios
          .get(`/api/${user_slug}`)
          .then(response => {
            this.user = response.data
            console.log(this.user)
          })
    }
  },
  components: {
    Post
  }
};
</script>

<style scoped>

</style>