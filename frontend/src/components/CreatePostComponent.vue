<template>
  <div class="w-full">
    <div class="flex bg-white rounded-[25px] dropShadow overflow-x-hidden">
      <div class="w-[8%] pl-[16px] py-[16px]">
        <div class="h-[42px] w-[42px] bg-gray-600 rounded-full inline-block"></div>
      </div>

      <div class="flex flex-col w-[92%] pt-[24px] pb-[16px] pb-[16px] pr-[24px] ">
        <textarea class="resize-none overflow-hidden focus: outline-none w-full min-h-[16px] flex-grow-1" ref="postInputTextArea" v-model="postContent"></textarea>
        <div class="flex justify-between mt-[16px]">
          <div class="self-center inline-block">
            <button>
              <i class="fa-solid fa-image text-[24px] mr-[16px]"></i>
            </button>
            <button>
              <i class="fa-solid fa-video text-[24px] mr-[16px]"></i>
            </button>
            <button>
              <i class="fa-solid fa-square-poll-vertical text-[24px] mr-[16px]"></i>
            </button>
            <button>
              <i class="fa-solid fa-smile text-[24px] mr-[16px]"></i>
            </button>
          </div>
          <button class="bg-primary-100 h-[39px] w-[140px] rounded-[5px] inline-block" @click="submitPost">
            <h5 class="text-white">Post</h5>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import axios from 'axios'

export default defineComponent({
  name: "PostComponent",
  data() {
    return {
      postContent: "" as string
    }
  },
  methods: {
    reloadFeed() {
      this.$emit('reloadFeed')
    },
    submitPost() {
      if (!this.postContent) {
        return
      }

      axios.post('/api/post/', {
        content: this.postContent
      }, {withCredentials: true}).then(response => {
        this.reloadFeed()
      }).catch(error => {
        console.log(error)
      })
    }
  }
});
</script>

<style scoped>

</style>