<template>
  <div class="container">

    <ProductHome/>

  </div>
</template>



<script>

import ProductHome from './components/ProductHome.vue';

export default {
    name: 'App',
    components: {
      ProductHome
}}

</script>

<style scoped>
.container {
  padding: 20px;
}
</style>
