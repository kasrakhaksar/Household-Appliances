<template>
    <div class="product-list">
      <h1>Products</h1>
      <div v-if="loading">loading</div>
      <div v-else>
        <div v-for="product in products" :key="product.id" class="product-card">
          <img :src="product.image" :alt="product.name" class="product-image" />
          <h2>{{ product.name }}</h2>
          <p>{{ product.description.slice(0, 50) }}{{ product.description.length > 50 ? '...' : '' }}</p>
          <p>price: {{ product.price }} $</p>
          <p>stock: {{ product.stock }}</p>
          <p>brand: {{ product.brand }}</p>
          <p>category: {{ product.category }}</p>
        </div>
      </div>
    </div>
</template>
  



<script>
  import axios from 'axios';
  
  export default {
    name: 'ProductList',
    data() {
      return {
        products: [],
        loading: true,
      };
    },
    mounted() {
      axios
        .get('http://localhost:8000/product/')
        .then((response) => {
          this.products = response.data;
        })
        .catch((error) => {
          console.error('خطا در دریافت اطلاعات محصولات:', error);
        })
        .finally(() => {
          this.loading = false;
        });
    },
  };
</script>
  



<style scoped>
.product-list {
  padding: 40px 20px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 30px;
  background-color: #f0f6fc; 
  min-height: 100vh;
}

h1 {
  grid-column: 1 / -1;
  text-align: center;
  font-size: 2.2rem;
  color: #003f88; 
  margin-bottom: 30px;
  font-weight: bold;
}

.product-card {
  background-color: #ffffff;
  border-radius: 14px;
  box-shadow: 0 6px 16px rgba(0, 63, 136, 0.1); /* Soft navy shadow */
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  border: 1px solid #cbe2ff;
}

.product-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 8px 20px rgba(0, 63, 136, 0.15);
}

.product-image {
  width: 100%;
  height: 170px;
  object-fit: cover;
  border-bottom: 2px solid #e0f0ff;
}

.product-card h2 {
  font-size: 1.3rem;
  color: #002b5b;
  margin: 15px 15px 5px;
  font-weight: 600;
}

.product-card p {
  font-size: 0.95rem;
  color: #0a2540;
  margin: 4px 15px;
  line-height: 1.4;
}

.product-card p:last-of-type {
  margin-bottom: 15px;
}

@media (max-width: 600px) {
  h1 {
    font-size: 1.6rem;
  }
  .product-card h2 {
    font-size: 1.1rem;
  }
  .product-card p {
    font-size: 0.88rem;
  }
}

</style>
  
  