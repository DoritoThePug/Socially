<template>
  <div class="page-home">
    <h1>Home Page</h1>
  </div>
</template>

<script>
  import Sidebar from '@/components/SidebarComponent';
  import FeedView from '@/views/FeedView';
  import AuthenticationOverlay from '@/components/AuthenticationOverlay';

  export default {
    name: "App",
    components: {
      AuthenticationOverlay,
      Sidebar,
      FeedView
    },

  }
</script>