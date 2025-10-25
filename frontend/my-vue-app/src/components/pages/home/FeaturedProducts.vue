<template>
  <section class="py-5 text-center">
    <div class="container">
      <h2 class="text-primary mb-3">Featured Products</h2>
      <p class="text-secondary mb-4">Explore our top-rated appliances selected just for you.</p>
      <ProductHome />
    </div>
  </section>
</template>

<script>
import ProductHome from './ProductHome.vue';

export default {
  name: 'FeaturedProducts',
  components: {
    ProductHome,
  },
};
</script>

