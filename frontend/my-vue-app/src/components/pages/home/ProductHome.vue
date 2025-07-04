<template>
  <div class="product-list">
    <div v-if="loading">loading</div>
    <div v-else>
      <div v-for="product in products" :key="product.id" class="product-card">
        <router-link :to="`/product/${product.id}`" class="card-link">
          <img :src="product.image" :alt="product.name" class="product-image" />
          <h2>{{ product.name }}</h2>
          <p>price: {{ product.price }} $</p>
          <p>brand: {{ product.brand }}</p>
          <p>category: {{ product.category }}</p>
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
      console.error('❌ دریافت اطلاعات محصولات با خطا مواجه شد:', error);
    } finally {
      this.loading = false;
    }
  }
  };
</script>
  



<style scoped>
.product-list {
  max-width: 1100px;
  margin: 0 auto;
  padding: 2rem 1rem;
}

.product-list > div {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.5rem;
}

.product-card {
  background: linear-gradient(135deg, #ffffff, #f3f3f3);
  border-radius: 16px;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08);
  padding: 1rem;
  margin: 0.5rem;
  flex: 1 1 220px;
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
  max-width: 250px;
}

.product-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}

.product-image {
  width: 100%;
  height: 160px;
  object-fit: contain;
  margin-bottom: 0.75rem;
  border-radius: 8px;
  background: #fff;
  padding: 0.5rem;
}

.product-card h2 {
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 0.4rem;
  text-align: center;
  color: #333;
}

.product-card p {
  font-size: 0.875rem;
  margin: 0.25rem 0;
  text-align: center;
  color: #555;
}



.card-link {
  text-decoration: none;
  color: inherit;
  display: block;
  width: 100%;
  height: 100%;
}

@media (max-width: 768px) {
  .product-card {
    flex: 1 1 100%;
    max-width: 90%;
  }
}



</style>

  
  