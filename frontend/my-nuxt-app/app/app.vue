<!-- app.vue -->
<template>
  <header v-if="!isAuthRoute">
    <Header />
  </header>

  <main>
    <NuxtPage />
  </main>

  <footer v-if="!isAuthRoute">
    <Footer />
  </footer>
</template>

<script setup lang="ts">

import Footer from './layout/Footer.vue';
import Header from './layout/Header.vue';
import { useRoute } from 'vue-router';

const route = useRoute();

const isAuthRoute = computed(() => route.path.startsWith('/auth'));

</script>