<template>
  <div>
    <HeaderSection v-if="$route?.meta?.layout !== 'auth'" />
    <router-view />

    <FooterSection
      v-if="$route?.meta?.layout !== 'auth' && !isMobile"
    />

    <MobileBottomNav
      v-if="$route?.meta?.layout !== 'auth' && isMobile"
    />
  </div>
</template>

<script>
import HeaderSection from './components/pages/layout/HeaderSection.vue';
import FooterSection from './components/pages/layout/FooterSection.vue';
import MobileBottomNav from './components/pages/layout/MobileBottomNav.vue';

export default {
  name: 'App',
  components: {
    HeaderSection,
    FooterSection,
    MobileBottomNav
  },
  data() {
    return {
      isMobile: false
    };
  },
  mounted() {
    this.checkIfMobile();
    window.addEventListener('resize', this.checkIfMobile);
  },
  beforeUnmount() {
    window.removeEventListener('resize', this.checkIfMobile);
  },
  methods: {
    checkIfMobile() {
      this.isMobile = window.innerWidth <= 768;
    }
  }
};
</script>


<style scoped>
@font-face {
  font-family: 'ny-font';
  src: url('@/assets/fonts/my-font.woff2') format('woff2');
  font-display: swap;
}

div {
  font-family: 'ny-font';
}
</style>
