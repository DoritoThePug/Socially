

<template>
  <div class="w-full">
    <div class="flex bg-white rounded-[25px] dropShadow overflow-x-hidden">
      <div class="w-[8%] pl-[16px] py-[16px]">
        <div class="h-[42px] w-[42px] bg-gray-600 rounded-full inline-block"></div>
      </div>

      <div class="flex flex-col w-[92%] pt-[24px] pb-[16px] pb-[16px] pr-[24px] ">
        <textarea class="resize-none overflow-hidden focus: outline-none w-full min-h-[16px]" placeholder="What's poppin'?" ref="postInputTextArea" v-model="postContent" @input="adjustTextareaHeight" maxlength="280"></textarea>
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
import { mapState, mapActions } from "pinia";

import {useAuthenticationComponentStore} from "@/stores/AuthenticationComponentStore";
import {useUserStore} from "@/stores/UserStore";

export default defineComponent({
  name: "PostComponent",
  data() {
    return {
      postContent: "" as string
    }
  },
  computed: {
    ...mapState(useUserStore, ["isAuthenticated"]),

  },
  methods: {
    ...mapActions(useAuthenticationComponentStore, ["toggleAuthenticationComponent"]),
    reloadFeed() {
      this.$emit('reloadFeed')
    },
    async submitPost() {
      if (!this.isAuthenticated) {
        this.toggleAuthenticationComponent()
        return
      }

      if (!this.postContent) {
        return
      }

      await axios.post('/api/post/', {
        content: this.postContent
      }, {withCredentials: true}).then(response => {
        this.reloadFeed()
      }).catch(error => {
        console.log(error)
      })
    },
      adjustTextareaHeight() {
            const textarea = this.$refs.postInputTextArea as HTMLTextAreaElement;

            textarea.style.height = 'auto';
            textarea.style.height = textarea.scrollHeight + 'px';
        },
  },
});
</script>

<style scoped>

</style>