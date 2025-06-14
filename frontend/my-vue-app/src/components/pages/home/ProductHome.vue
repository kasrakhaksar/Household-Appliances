<template>
    <div class="product-list">
      <div v-if="loading">loading</div>
      <div v-else>
        <div v-for="product in products" :key="product.id" class="product-card">
          <img :src="product.image" :alt="product.name" class="product-image" />
          <h2>{{ product.name }}</h2>
          <p>price: {{ product.price }} $</p>
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
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem;
}



.product-card {
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 1rem;
  margin: 1rem;
  flex: 1 1 300px;
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: transform 0.2s ease;
}

.product-card:hover {
  transform: translateY(-5px);
}

.product-image {
  max-width: 100%;
  height: 200px;
  object-fit: contain;
  margin-bottom: 1rem;
}

.product-list > div {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
}

.product-card h2 {
  font-size: 15px;
  margin-bottom: 0.5rem;
  text-align: center;
}

.product-card p {
  font-size: 1rem;
  margin: 0.25rem 0;
  text-align: center;
}

/* Responsive Design */
@media (max-width: 768px) {
  .product-card {
    flex: 1 1 100%;
  }
}

</style>
  
  