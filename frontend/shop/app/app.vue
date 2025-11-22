<template>
  <div v-if="!isAuthRoute">
    <header>
      <Header />
    </header>

    <main>
      <NuxtPage />
    </main>

    <footer v-if="!isMobileOrTablet">
      <Footer />
    </footer>
    <div v-else>
      <MobileNavigation />
    </div>

  </div>

  <div v-else>
    <NuxtPage />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount, computed } from 'vue';
import { useRoute } from 'vue-router';
import Header from '@/layout/Header.vue';
import MobileNavigation from '@/layout/MobileNavigation.vue';
import Footer from '@/layout/Footer.vue';

const isMobileOrTablet = ref(false);

const updateScreen = () => {
  isMobileOrTablet.value = window.innerWidth < 1024;
};

onMounted(() => {
  updateScreen();
  window.addEventListener('resize', updateScreen);
});

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateScreen);
});

const route = useRoute();
const isAuthRoute = computed(() => route.path.startsWith('/auth'));
</script>

<style>
html,
body {
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}
</style>
