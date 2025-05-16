<template>
    <div class="product-list">
      <h1>لیست محصولات</h1>
      <div v-if="loading">در حال بارگذاری...</div>
      <div v-else>
        <div v-for="product in products" :key="product.id" class="product-card">
          <img :src="product.image" :alt="product.name" class="product-image" />
          <h2>{{ product.name }}</h2>
          <p>{{ product.description }}</p>
          <p>قیمت: {{ product.price }} دلار</p>
          <p>موجودی: {{ product.stock }}</p>
          <p>برند: {{ product.brand }}</p>
          <p>دسته‌بندی: {{ product.category }}</p>
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
    padding: 20px;
    display: grid;
    gap: 20px;
  }
  
  .product-card {
    border: 1px solid #ccc;
    padding: 15px;
    border-radius: 10px;
    max-width: 400px;
  }
  
  .product-image {
    width: 100%;
    max-height: 200px;
    object-fit: cover;
  }
  </style>
  