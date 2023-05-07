<template>
  <div class="w-full">
    <div class="flex flex-col">
      <PostComponent v-if="!loadingData" :post="post"/>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import axios from "axios";

import PostComponent from "../components/PostComponent.vue";

import post from '../interfaces/post'

export default defineComponent({
  name: "PostView",
  components: {
    PostComponent
  },
  data() {
    return {
      post: {} as post,
      loadingData: true
    }
  },
  methods: {
    async getPost() {
      await axios.get(`/api/posts/${this.$route.params.user_slug}/${this.$route.params.post_id}/`)
        .then((response) => {
          this.post = response.data;
          console.log(this.post)
        })
        .catch((error) => {
          console.log(error);
        })

        console.log(this.post)
    }

  },
  created() {
    this.getPost().then(() => {
      this.loadingData = false
    })
  }
});
</script>

<style scoped>

</style>