<template>
  <div class="w-[600px] h-auto p-[16px] bg-white rounded-[10px]">
    <form @submit.prevent="submitCreatePostForm">
      <textarea class="focus:outline-0 w-full bg-inherit resize-none min-h-[100px] text-black-100" v-model="content"
                                placeholder="Say something!" />
      <hr class="mb-[8px]">
      <button
          class="float-right flex self-start text-white h-[32px] px-[24px] py-[6px] items-center bg-gradient-to-r from-primary-100 to-secondary-100 rounded-full hover:from-primary-80 hover:to-secondary-80 active:from-primary-100 active:to-primary-100">
        <h6>Post</h6>
      </button>
    </form>
    <button class="mr-[8px] mt-[8px]">
      <i class="fa-solid fa-image text-primary-100"></i>
    </button>
    <button class="mr-[8px] mt-[8px]">
      <i class="fa-solid fa-camera text-primary-100"></i>
    </button>
    <button class="mr-[8px] mt-[8px]">
      <i class="fa-solid fa-poll text-primary-100"></i>
    </button>
    <button class="mt-[8px]">
      <i class="fa-solid fa-smile text-primary-100"></i>
    </button>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "CreatePost",
  data() {
    return {
      content: '',
    }
  },
  methods: {
    submitCreatePostForm() {
      const formData = {
        content: this.content
      }

      axios
          .post('/api/post/', formData)
          .then(response => {
            this.content = ''
            this.$parent.get_user_posts()
          })
    }
  }
};
</script>

<style scoped>

</style>