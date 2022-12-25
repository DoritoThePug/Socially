<template>
  <div class="w-full h-full mx-auto">
<!--    <AuthenticationOverlay v-if="authenticationPromptVisible" class="absolute z-20 overflow-hidden fixed"/>-->
<!--    <div class="w-full h-full fixed z-20 backdrop-blur-sm"></div>-->
    <AuthenticationOverlay v-if="authenticationPromptVisible" class="fixed z-20"/>

    <div class="bg-white rounded-[15px] dropShadow px-[32px] py-[20px] h-min sticky top-0">
      <NavBar />
    </div>
    <div class="flex">
      <div class="w-1/5">
        <div class="justify-between p-[32px] h-min sticky top-[74px]">
          <Sidebar/>
        </div>
      </div>
      <div class="w-3/5 p-[32px]">
        <router-view />
      </div>
      <div class="w-1/5 p-[32px] space-y-[32px] h-min sticky top-[74px]">
        <NotificationComponent />
        <FriendsComponent />
      </div>
    </div>



  </div>
</template>

<script>
  import HomeView from '@/views/HomeView'

  import Sidebar from '@/components/SidebarComponent'
  import AuthenticationOverlay from '@/components/AuthenticationOverlay'
  import CreatePostComponent from '@/components/CreatePostComponent';
  import NavBar from '@/components/NavBarComponent';
  import NotificationComponent from '@/components/NotificationComponent';
  import FriendsComponent from '@/components/FriendsComponent';

  export default {
    name: "App",
    components: {
      NotificationComponent,
      CreatePostComponent,
      HomeView,
      Sidebar,
      AuthenticationOverlay,
      NavBar,
      FriendsComponent,
    },
    methods: {
      toggleAuthenticationPrompt() {
        this.authenticationPromptVisible = !this.authenticationPromptVisible
      }
    },
    data() {
      return {
        authenticationPromptVisible: true,
      }
    },
    beforeCreate() {
      this.$store.commit('initialize')
    }
  }
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
