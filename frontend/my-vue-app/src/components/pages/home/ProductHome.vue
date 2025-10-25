<template>
  <div class="container py-5">
    <div v-if="loading" class="text-center">Loading...</div>
    <div v-else class="row g-4 justify-content-center">
      <div v-for="product in products" :key="product.id" class="col-sm-6 col-md-4 col-lg-3">
        <router-link :to="`/product/${product.id}`" class="text-decoration-none">
          <div class="card h-100 product-card shadow-sm text-center p-2">
            <img :src="product.image" :alt="product.name" class="card-img-top product-image mb-2" />
            <div class="card-body p-2">
              <h5 class="card-title text-dark">{{ product.name }}</h5>
              <p class="card-text text-secondary mb-1">Price: {{ product.price }} $</p>
              <p class="card-text text-secondary mb-1">Brand: {{ product.brand }}</p>
              <p class="card-text text-secondary mb-0">Category: {{ product.category }}</p>
            </div>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import ProductAPI from './api/ProductAPI';

export default {
  name: 'ProductList',
  data() {
    return {
      products: [],
      loading: true,
    };
  },
  async mounted() {
    try {
      this.products = await ProductAPI.getHomeProducts(4);
    } catch (error) {
      console.error('❌ error :', error);
    } finally {
      this.loading = false;
    }
  }
};
</script>

<style scoped>
.product-card {
  border-radius: 16px;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.product-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}

.product-image {
  object-fit: contain;
  height: 160px;
  background: #fff;
  padding: 0.5rem;
  border-radius: 8px;
}
</style>
