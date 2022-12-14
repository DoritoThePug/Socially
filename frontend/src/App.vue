<script setup lang="ts">
import { storeToRefs } from "pinia";

import { useAuthenticationComponentStore } from "@/stores/AuthenticationComponentStore";

const authenticationStore = useAuthenticationComponentStore();

const { isAuthenticationComponentOpen, isSignUpComponentOpen, isAccountDetailsComponentOpen } = storeToRefs(
  useAuthenticationComponentStore()
);
</script>

<template>
  <div class="w-full h-full mx-auto">
    <AuthenticationComponent v-if="isAuthenticationComponentOpen" class="fixed z-20"/>
    <SignUpComponent v-if="isSignUpComponentOpen" class="fixed z-20"/>
    <AccountDetailsComponent v-if="isAccountDetailsComponentOpen" class="fixed z-20"/>


    <div class="bg-white rounded-[15px] dropShadow px-[32px] py-[20px] h-min sticky top-0 z-50">
      <NavBarComponent />
    </div>
    <div class="flex">
      <div class="w-[22%]">
        <div class="justify-between p-[32px] pl-[64px] h-min sticky top-[74px]">
          <SidebarComponent />
        </div>
      </div>
      <div class="w-[56%] p-[32px]">
        <router-view/>
      </div>
      <div class="w-[22%] p-[32px] pr-[64px] space-y-[32px] h-min sticky top-[74px]">
        <NotificationComponent />
        <FriendsComponent />
      </div>
    </div>



  </div>
</template>

<script lang="ts">
  import { defineComponent } from "vue";

  import NavBarComponent from './components/NavBarComponent.vue';
  import NotificationComponent from './components/NotificationComponent.vue';
  import FriendsComponent from './components/FriendsComponent.vue';
  import SidebarComponent from './components/SidebarComponent.vue';
  import AuthenticationComponent from './components/AuthenticationComponent.vue'
  import SignUpComponent from './components/SignUpComponent.vue';
  import AccountDetailsComponent from "@/components/AccountDetailsComponent.vue";



  export default defineComponent({
    name: "App",
    components: {
      SidebarComponent,
      NavBarComponent,
      NotificationComponent,
      FriendsComponent,

      AuthenticationComponent,
      SignUpComponent,
      AccountDetailsComponent
    },
  })
</script>

<style lang="scss">
@tailwind base;
@tailwind components;
@tailwind utilities;


.dropShadow {
  box-shadow: 0px 26px 80px rgba(26, 34, 35, 0.07), 0px 10.8622px 33.4221px rgba(26, 34, 35, 0.0503198), 0px 5.80744px 17.869px rgba(26, 34, 35, 0.0417275), 0px 3.2556px 10.0172px rgba(26, 34, 35, 0.035), 0px 1.72903px 5.32008px rgba(26, 34, 35, 0.0282725), 0px 0.719487px 2.21381px rgba(26, 34, 35, 0.0196802);
}

@layer base{
  p {
    font-family: Roboto, sans-serif;
    @apply font-normal text-[14px] leading-[17px] text-black-100;
  }

  textarea {
    font-family: Roboto, sans-serif;
    @apply font-normal text-[16px] leading-[17px] text-black-100;
  }

  h1 {
    font-family: Brandon Grotesque, sans-serif;
    @apply font-bold text-[43px] leading-[61px] text-black-100;
  }

  h2 {
    font-family: Brandon Grotesque, sans-serif;
    @apply font-bold text-[34px] leading-[49px] text-black-100;
  }

  h3 {
    font-family: Brandon Grotesque, sans-serif;
    @apply font-bold text-[27px] leading-[39px] text-black-100;
  }

  h4 {
    font-family: Brandon Grotesque, sans-serif;
    @apply font-bold text-[22px] leading-[31px] text-black-100;
  }

  h5 {
    font-family: Brandon Grotesque, sans-serif;
    @apply font-bold text-[18px] leading-[26px] text-black-100;
  }

  h6 {
    font-family: Brandon Grotesque, sans-serif;
    @apply font-bold text-[14px] leading-[20px] text-black-100;
  }
};
</style>
