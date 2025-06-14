<template>
    <section class="extra-section">
      <h2>Featured Products</h2>
      <p>Explore our top-rated appliances selected just for you.</p>
      <ProductHome />
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
  
  <style scoped>
  .extra-section {
    padding: 2rem 1rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    text-align: center;
  }
  
  .extra-section h2 {
    color: #003f88;
    margin-bottom: 1rem;
  }
  
  .extra-section p {
    color: #0a2540;
    margin-bottom: 1rem;
  }
  </style>
  