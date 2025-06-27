<template>
  <div class="product-detail">
    <div v-if="loading" class="loading">Loading...</div>

    <div v-else-if="product" class="product-container">
      <div class="image-section">
        <img :src="product.image" :alt="product.name" class="product-image" />
      </div>
      <div class="info-section">
        <h1 class="product-name">{{ product.name }}</h1>

        <div v-if="product.discount_price && product.discount_price > 0" class="discount-wrapper">
          <span class="discount-badge">
            🔥 SALE – You save {{ ((product.discount_price * 100 / product.price )).toFixed(0) }}%
          </span>
          <p class="product-price">
            <del>${{ product.price }}</del>
            <span class="discounted-price">${{ (product.price - product.discount_price).toFixed(2) }}</span>
          </p>
        </div>

        <p v-else class="product-price">${{ product.price }}</p>
        <p :class="['stock-info', product.stock === 0 ? 'out-of-stock' : (product.stock < 5 ? 'low-stock' : '')]">
          <strong>Stock:</strong>
          <span v-if="product.stock > 0">{{ product.stock }} item<span v-if="product.stock > 1">s</span> left</span>
          <span v-else>Out of stock ❌</span>
        </p>

        <p><strong>Brand:</strong> {{ product.brand }}</p>
        <p><strong>Category:</strong> {{ product.category }}</p>
        <p class="product-desc">{{ product.description }}</p>
      </div>
    </div>

    <div v-else class="not-found">
      <p>Product not found 😕</p>
    </div>
  </div>
</template>

<script>
import ProductAPI from '../home/api/ProductAPI';

export default {
  name: 'ProductDetail',
  data() {
    return {
      product: null,
      loading: true,
    };
  },
  async created() {
    const id = this.$route.params.id;
    try {
      this.product = await ProductAPI.getProductById(id);
    } catch (error) {
      console.error('❌ Error fetching product:', error);
    } finally {
      this.loading = false;
    }
  },
};
</script>

<style scoped>

.product-detail {
  font-family: 'Vazirmatn', sans-serif;
  padding: 2rem;
  max-width: 1000px;
  margin: 2rem auto;
  background: #ffffff;
  border-radius: 15px;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.05);
  animation: fadeIn 0.6s ease;
}

.loading,
.not-found {
  text-align: center;
  font-size: 1.5rem;
  color: #555;
  padding: 3rem;
}

.product-container {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
}

.image-section {
  flex: 1 1 300px;
  text-align: center;
}

.product-image {
  width: 100%;
  max-height: 350px;
  object-fit: contain;
  border-radius: 12px;
  transition: transform 0.3s ease;
}

.product-image:hover {
  transform: scale(1.05);
}

.info-section {
  flex: 1 1 400px;
  text-align: left;
}

.product-name {
  font-size: 2rem;
  color: #222;
  margin-bottom: 1rem;
}

.product-price {
  font-size: 1.3rem;
  color: #003f88;
  margin: 0.5rem 0;
}

.product-price del {
  color: #999;
  margin-right: 0.5rem;
}

.discounted-price {
  color: #dc2626;
  font-weight: bold;
  font-size: 1.4rem;
}

.discount-wrapper {
  margin-bottom: 1rem;
}

.discount-badge {
  background: #f97316;
  color: #fff;
  padding: 0.3rem 0.7rem;
  border-radius: 999px;
  font-size: 0.9rem;
  font-weight: bold;
  display: inline-block;
  margin-bottom: 0.3rem;
  animation: flash 1.2s infinite;
}

.product-desc {
  margin-top: 1rem;
  line-height: 1.7;
  color: #444;
}


.stock-info {
  font-weight: 500;
  margin-top: 0.5rem;
}

.out-of-stock {
  color: #b91c1c;
  font-weight: bold;
}

.low-stock {
  color: #d97706;
  font-weight: bold;
}

@media (max-width: 768px) {
  .product-container {
    flex-direction: column;
    text-align: center;
  }

  .info-section {
    text-align: center;
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes flash {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.6; }
}
</style>
