<template>
  <div>
    <HeaderSection v-if="$route?.meta?.layout !== 'auth'" />
    <router-view />
    <FooterSection v-if="$route?.meta?.layout !== 'auth'" />
  </div>
</template>



<script>
  import HeaderSection from './components/pages/layout/HeaderSection.vue';
  import FooterSection from './components/pages/layout/FooterSection.vue';

  export default {
      name: 'App',
      components: {
    HeaderSection,
    FooterSection
    
}}

</script>


<style scoped>


  @font-face {
    font-family: 'ny-font';
    src: url('@/assets/fonts/my-font.woff2') format('woff2');
    font-display: swap;
  }

  body {
    font-family: 'ny-font';
  }


</style>