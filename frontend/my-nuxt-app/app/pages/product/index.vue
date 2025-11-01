<template>
  <div class="min-h-screen bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 text-white py-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 class="text-5xl font-extrabold text-center mb-12">Products</h1>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div v-for="product in products" :key="product.id"
             class="bg-slate-800/70 rounded-xl shadow-xl backdrop-blur-md hover:scale-105 transition-transform duration-300 flex flex-col">

          <div v-if="product.image" class="overflow-hidden rounded-t-xl">
            <img :src="product.image" :alt="product.name"
                 class="w-full h-48 object-cover transition-transform duration-500 hover:scale-110" />
          </div>

          <div class="p-6 flex flex-col flex-1">
            <h2 class="text-2xl font-bold mb-2">{{ product.name }}</h2>
            <p class="text-gray-400 text-sm mb-2"><strong>Brand:</strong> {{ product.brand }}</p>
            <p class="text-gray-400 text-sm mb-2"><strong>Category:</strong> {{ product.category }}</p>

            <p class="text-blue-400 font-bold mb-4">${{ product.price }}</p>

            <p :class="[
              'text-sm mb-4',
              product.stock === 0 ? 'text-red-600 font-bold' : product.stock < 5 ? 'text-orange-400 font-bold' : 'text-gray-300'
            ]">
              <strong>Stock:</strong>
              <span v-if="product.stock > 0">{{ product.stock }} item<span v-if="product.stock > 1">s</span> left</span>
              <span v-else>Out of stock ❌</span>
            </p>

            <router-link :to="`/product/${product.id}`"
                         class="mt-auto inline-block text-indigo-400 hover:text-indigo-300 font-semibold">
              View Details →
            </router-link>
          </div>
        </div>
      </div>

      <div v-if="loading" class="text-center text-gray-400 text-lg mt-10">Loading products...</div>
      <div v-else-if="!products.length" class="text-center text-red-500 text-lg mt-10">⚠️ No products found.</div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import ProductAPI from '../../../server/api/products'

const products = ref<any[]>([])
const loading = ref(true)

const route = useRoute()

const fetchProducts = async () => {
  loading.value = true
  try {
    const category = route.query.category as string | undefined
    if (category) {
      // اگر category در query بود، فقط همان دسته
      products.value = await ProductAPI.getProductsByCategory(category)
    } else {
      // اگر category نبود، همه محصولات
      products.value = await ProductAPI.getAllProducts()
    }
  } catch (error) {
    console.error('❌ Error fetching products:', error)
    products.value = []
  } finally {
    loading.value = false
  }
}

onMounted(fetchProducts)
watch(() => route.query.category, fetchProducts)
</script>
