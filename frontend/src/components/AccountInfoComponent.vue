<template>
  <div class="w-full h-full backdrop-blur-md flex place-content-center">
    <div
      class="flex flex-col p-[32px] bg-white rounded-[25px] self-center dropShadow"
    >
      <div class="flex flex-row justify-between items-center mb-[16px]">
        <h2>Account Information</h2>
        <button
          class="ml-auto flex-none hover:text-secondary-100"
          @click="toggleAuthenticationComponent"
        >
          <i class="fa-solid fa-x"></i>
        </button>
      </div>

      <form class="flex flex-row" @submit.prevent="submitAccountInfoChanges">
        <div class="mr-[16px]">
          <h3 class="fieldHeading">Profile Picture</h3>
          <div
            class="h-[104px] w-[104px] bg-black-25 rounded-full group relative"
          >
            <img
              class="rounded-full h-full w-full object-none"
              :src="user.get_profile_picture"
            />
            <div
              class="hidden group-hover:block absolute backdrop-blur-sm rounded-full top-0 left-0 h-full w-full flex place-content-center"
            >
              <label
                for="pfpFile"
                class="flex h-full w-full justify-center items-center"
              >
                <i class="fa-solid fa-arrow-up-from-bracket text-[24px]"></i>
              </label>
              <input
                class="invisible"
                type="file"
                id="pfpFile"
                accept="image/*"
                ref="profileImageFile"
                @change="submitAccountInfoChanges"
              />
            </div>
          </div>
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
                <input
                  class="w-full bg-white focus:outline-none"
                  type="text"
                  maxlength="30"
                  v-model="firstName"
                />
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
                <input
                  class="w-full bg-white focus:outline-none"
                  type="text"
                  maxlength="30"
                  v-model="lastName"
                />
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
              maxlength="255"
              v-model="bio"
            />
          </div>
          <button
            class="px-[32px] py-[4px] self-center rounded-[5px] bg-primary-100 hover:bg-primary-80 mb-[16px]"
          >
            <h4 class="text-white">Save</h4>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import axios from "axios";
import User from "@/interfaces/user";
import { mapState, mapActions } from "pinia";

import { useUserStore } from "@/stores/UserStore";
import { useAuthenticationComponentStore } from "@/stores/AuthenticationComponentStore";

export default defineComponent({
  name: "AccountInfoComponent",
  props: {
    partOfSignUp: Boolean, // Used to show/not show the "Complete Later" button
  },
  computed: {
    ...mapState(useUserStore, ["user"]),
    ...mapActions(useAuthenticationComponentStore, ["toggleAccountInfoComponent"])
  },
  data() {
    return {
      profilePicture: "",
      firstName: "",
      lastName: "",
      bio: "",
    };
  },
  mounted() {
    this.profilePicture = this.user.get_profile_picture;
    this.firstName = this.user.first_name;
    this.lastName = this.user.last_name;
    this.bio = this.user.bio;
  },
  methods: {
    adjustTextareaHeight() {
      const textarea = this.$refs.bioInputTextArea as HTMLTextAreaElement;

      textarea.style.height = "auto";
      textarea.style.height = textarea.scrollHeight + "px";
    },
    async submitAccountInfoChanges() {
      var formData = new FormData();
      this.profilePicture = (this.$refs.profileImageFile as any).files[0];

      console.log(this.profilePicture);

      if (this.profilePicture != undefined) {
        formData.append("profile_picture", this.profilePicture);
      }

      formData.append("first_name", this.firstName);
      formData.append("last_name", this.lastName);
      formData.append("bio", this.bio);

      await axios
        .patch("/api/update-user/", formData)
        .then(async (response) => {
          useUserStore().upadteUser(response.data);
        });
    },
  },
});
</script>

<style scoped>
.fieldHeading {
  @apply text-[16px] font-normal;
}
</style>
