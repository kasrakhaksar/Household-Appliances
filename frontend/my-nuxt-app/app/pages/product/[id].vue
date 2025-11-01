<template>
  <div class="min-h-screen bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 py-16">
    <div
      class="product-detail max-w-5xl mx-auto p-8 bg-gradient-to-b from-slate-800 via-slate-700 to-slate-800 text-white rounded-2xl shadow-xl animate-fadeIn">

      <div v-if="loading" class="flex flex-col items-center gap-4">
        <div class="w-full h-64 md:h-96 bg-slate-700 animate-pulse rounded-xl"></div>
        <div class="w-3/4 h-6 bg-slate-600 animate-pulse rounded"></div>
        <div class="w-1/2 h-4 bg-slate-600 animate-pulse rounded"></div>
      </div>

      <div v-else-if="product" class="product-container flex flex-wrap gap-8">
        
        <div class="image-section flex-1 min-w-[300px] h-[350px] md:h-auto text-center">
          <img
            :src="product.image"
            :alt="product.name"
            class="w-full h-full object-cover rounded-xl transition-transform duration-300 hover:scale-105"
          />
        </div>

        <div class="info-section flex-1 min-w-[400px] text-left">
          <h1 class="product-name text-3xl md:text-4xl font-extrabold mb-4">{{ product.name }}</h1>

          <div v-if="product.discount_price && product.discount_price > 0" class="mb-4">
            <span class="discount-badge inline-block bg-orange-500 text-white px-3 py-1 rounded-full text-sm font-bold mb-1 animate-pulse">
              🔥 Save {{ ((product.discount_price * 100) / product.price).toFixed(0) }}%
            </span>
            <p class="product-price text-lg mt-1">
              <del class="text-gray-400 mr-2">${{ product.price }}</del>
              <span class="discounted-price text-red-500 font-bold text-xl">
                ${{ (product.price - product.discount_price).toFixed(2) }}
              </span>
            </p>
          </div>
          <p v-else class="product-price text-blue-400 text-lg">${{ product.price }}</p>


          <p :class="stockClass" class="mt-2 font-medium">
            <strong>Stock:</strong>
            <span v-if="product.stock > 0">{{ product.stock }} item<span v-if="product.stock > 1">s</span> left</span>
            <span v-else>Out of stock ❌</span>
          </p>

          <p class="mt-2"><strong>Brand:</strong> {{ product.brand }}</p>
          <p class="mt-1"><strong>Category:</strong> {{ product.category }}</p>

          <p class="product-desc mt-4 text-gray-300 leading-relaxed">{{ product.description }}</p>
        </div>
      </div>

      <div v-else class="not-found text-center text-gray-300 text-xl py-12">
        <p>Product not found 😕</p>
      </div>
    </div>
  </div>
</template>

<script>
import ProductAPI from '../../../server/api/products';

export default {
  name: 'ProductDetail',
  data() {
    return {
      product: null,
      loading: true,
    };
  },
  computed: {
    stockClass() {
      if (!this.product) return '';
      if (this.product.stock === 0) return 'text-red-600 font-bold';
      if (this.product.stock < 5) return 'text-orange-400 font-bold';
      return '';
    },
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

<style>
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fadeIn {
  animation: fadeIn 0.5s ease-out forwards;
}
.animate-flash {
  animation: flash 1s infinite;
}
@keyframes flash {
  0%, 50%, 100% { opacity: 1; }
  25%, 75% { opacity: 0.5; }
}
</style>
