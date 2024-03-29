<template>
  <nav class="w-full">
    <div class="flex flex-row justify-between items-center">
      <button
        @click="goToHome"
        class="bg-gradient-to-r from-primary-100 to-secondary-100 text-transparent bg-clip-text font-bold text-[22px] leading-[31px]"
      >
        SOCIALLY
      </button>
      <div
        class="flex ml-auto w-[400px] bg-black-10 h-[32px] rounded-[10px] mr-[16px] py-[8px] px-[16px] content-center hover:drop-shadow"
      >
        <input
          class="bg-black-10 w-full overflow-hidden focus: outline-none font-['roboto'] text-[14px]"
          type="text"
          placeholder="Search"
        />
        <i
          class="fa-solid fa-magnifying-glass text-primary-100 text-black-50"
        ></i>
      </div>
      <button class="mr-[32px] text-[20px]">
        <i class="fa-solid fa-sun"></i>
      </button>
      <button
        v-if="isAuthenticated"
        @click="showDropDown = !showDropDown"
        class="z-[50px]"
      >
        <img
          :src="user.get_profile_picture"
          alt="https://192.168.88.122:8000/media/default-user-image.png"
          class="w-[32px] h-[32px] rounded-full"
        />
      </button>
      <button v-else class="hover:text-secondary-100" @click="navBarToggle">
        <i class="fa-solid fa-right-to-bracket text-[24px]"></i>
      </button>

      <div v-if="showDropDown" class="relative">
        <div
          class="rounded-[25px] absolute bg-white dropShadow top-[32px] right-[8px] py-[24px] px-[32px] flex flex-col space-y-[16px]"
        >
          <button @click="goToProfile" class="navbarPopup text-[18px] font-['roboto'] font-[500]">
            <i class="fa-solid fa-user fa-md mr-[16px]"></i>
            Profile
          </button>
          <button class="navbarPopup text-[18px] font-['roboto'] font-[500]">
            <i class="fa-solid fa-gear fa-md mr-[16px]"></i>
            Settings
          </button>
          <button @click="logout" class="navbarPopup text-error text-[18px] font-['roboto'] font-[500]">
            <i class="fa-solid fa-right-from-bracket fa-md mr-[16px]"></i>
            Logout
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapState, mapActions } from "pinia";
import axios from "axios";

import { useUserStore } from "@/stores/UserStore";
import { useAuthenticationComponentStore } from "@/stores/AuthenticationComponentStore";

export default defineComponent({
  name: "NavBarComponent",
  computed: {
    ...mapState(useUserStore, ["isAuthenticated", "user"]),
    ...mapActions(useAuthenticationComponentStore, ["navBarToggle"]),
    ...mapActions(useUserStore, ["logoutUser"]),
  },
  data() {
    return {
      showDropDown: false as boolean,
    };
  },
  methods: {
    goToProfile() {
      this.$router.push(`/profile/${this.user.username}`);
    },
    goToHome() {
      this.$router.push("/");
    },
    logout() {
      axios
        .post("/api/logout/", {}, { withCredentials: true })
        .then((response) => {
          this.logoutUser;
          this.goToHome();
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
});
</script>

<style scoped>
.navbarPopup {
  @apply flex flex-row items-center text-[18px] font-['lato'] font-[500];
}
</style>
