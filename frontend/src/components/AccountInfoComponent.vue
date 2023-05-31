<script setup lang="ts">
import { useAuthenticationComponentStore } from "@/stores/AuthenticationComponentStore";

const authenticationStore = useAuthenticationComponentStore();
</script>

<template>
  <div class="w-full h-full backdrop-blur-md flex place-content-center">
    <div
      class="flex flex-col p-[32px] bg-white rounded-[25px] self-center dropShadow"
    >
      <div class="flex flex-row justify-between items-center mb-[16px]">
        <h2>Account Information</h2>
        <button
          class="ml-auto flex-none hover:text-secondary-100"
          @click="authenticationStore.toggleAuthenticationComponent()"
        >
          <i class="fa-solid fa-x"></i>
        </button>
      </div>

      <div class="flex flex-row">
        <div class="mr-[16px]">
          <h3 class="fieldHeading">Profile Picture</h3>
          <div class="h-[104px] w-[104px] bg-black-25 rounded-full"></div>
        </div>
        <div class="flex flex-col">
          <div class="flex flex-row">
            <div>
              <h3 class="fieldHeading">First Name</h3>
              <div
                class="min-w-[120px] rounded-[10px] p-[8px] border-[1px] mb-[8px] mr-[16px]"
                :class="{
                  // 'border-black-25': !passwordError,
                  // 'border-error': passwordError,
                }"
              >
                <input class="w-full bg-white focus:outline-none" type="text" />
              </div>
            </div>
            <div>
              <h3 class="fieldHeading">Last Name</h3>
              <div
                class="min-w-[120px] rounded-[10px] p-[8px] border-[1px] mb-[8px]"
                :class="{
                  // 'border-black-25': !passwordError,
                  // 'border-error': passwordError,
                }"
              >
                <input class="w-full bg-white focus:outline-none" type="text" />
              </div>
            </div>
          </div>
          <h3 class="fieldHeading">Bio</h3>
          <div
            class="min-w-[280px] min-h-[150px] rounded-[10px] p-[8px] border-[1px] mb-[8px]"
            :class="{
              // 'border-black-25': !passwordError,
              // 'border-error': passwordError,
            }"
          >
            <textarea
              class="resize-none overflow-hidden focus: outline-none w-full min-h-[16px]"
              ref="bioInputTextArea"
              @input="adjustTextareaHeight"
              maxlength="150"
            />
          </div>
          <button
            class="px-[32px] py-[4px] self-center rounded-[5px] bg-primary-100 hover:bg-primary-80 mb-[16px]"
          >
            <h4 class="text-white">Save</h4>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "AccountInfoComponent",
  props: {
    partOfSignUp: Boolean, // Used to show/not show the "Complete Later" button
  },
  methods: {
    adjustTextareaHeight() {
      const textarea = this.$refs.bioInputTextArea as HTMLTextAreaElement;

      textarea.style.height = "auto";
      textarea.style.height = textarea.scrollHeight + "px";
    },
  },
});
</script>

<style scoped>
.fieldHeading {
  @apply text-[16px] font-normal;
}
</style>
