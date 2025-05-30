<template>

<body>
  <HeaderSection/>
  <router-view />

  <FooterSection/>

</body>
  
</template>



<script>
  import HeaderSection from './components/pages/header/HeaderSection.vue';
  import FooterSection from './components/pages/footer/FooterSection.vue';

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