<template>
  <div class="min-h-screen bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 text-white py-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 class="text-5xl font-extrabold text-center mb-12">Products</h1>


      <div class="bg-slate-800/50 backdrop-blur-md rounded-2xl p-6 mb-10 border border-slate-700/50 shadow-2xl">
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-6 mb-6">
          <h2 class="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-500">
            Filter Products
          </h2>

          <button @click="resetFilters"
            class="px-4 py-2 bg-slate-700/50 hover:bg-slate-600/70 rounded-lg transition-all duration-300 border border-slate-600/50 text-sm font-medium flex items-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd"
                d="M4 2a1 1 0 011 1v2.101a7.002 7.002 0 0111.601 2.566 1 1 0 11-1.885.666A5.002 5.002 0 005.999 7H9a1 1 0 010 2H4a1 1 0 01-1-1V3a1 1 0 011-1zm.008 9.057a1 1 0 011.276.61A5.002 5.002 0 0014.001 13H11a1 1 0 110-2h5a1 1 0 011 1v5a1 1 0 11-2 0v-2.101a7.002 7.002 0 01-11.601-2.566 1 1 0 01.61-1.276z"
                clip-rule="evenodd" />
            </svg>
            Reset Filters
          </button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" viewBox="0 0 20 20"
                fill="currentColor">
                <path fill-rule="evenodd"
                  d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                  clip-rule="evenodd" />
              </svg>
            </div>
            <input v-model="filters.search" type="text" placeholder="Search products..."
              class="w-full pl-10 pr-4 py-3 bg-slate-800/70 border border-slate-600/50 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all duration-300 text-white placeholder-gray-400" />
          </div>

          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" viewBox="0 0 20 20"
                fill="currentColor">
                <path
                  d="M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
              </svg>
            </div>
            <select v-model="filters.category"
              class="w-full pl-10 pr-4 py-3 bg-slate-800/70 border border-slate-600/50 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all duration-300 text-white appearance-none">
              <option value="">All Categories</option>
              <option v-for="cat in categories" :key="cat.value" :value="cat.value">
                {{ cat.label }}
              </option>
            </select>
            <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" viewBox="0 0 20 20"
                fill="currentColor">
                <path fill-rule="evenodd"
                  d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                  clip-rule="evenodd" />
              </svg>
            </div>
          </div>

          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" viewBox="0 0 20 20"
                fill="currentColor">
                <path fill-rule="evenodd"
                  d="M12.316 3.051a1 1 0 01.633 1.265l-4 12a1 1 0 11-1.898-.632l4-12a1 1 0 011.265-.633zM5.707 6.293a1 1 0 010 1.414L3.414 10l2.293 2.293a1 1 0 11-1.414 1.414l-3-3a1 1 0 010-1.414l3-3a1 1 0 011.414 0zm8.586 0a1 1 0 011.414 0l3 3a1 1 0 010 1.414l-3 3a1 1 0 11-1.414-1.414L16.586 10l-2.293-2.293a1 1 0 010-1.414z"
                  clip-rule="evenodd" />
              </svg>
            </div>
            <select v-model="filters.brand"
              class="w-full pl-10 pr-4 py-3 bg-slate-800/70 border border-slate-600/50 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all duration-300 text-white appearance-none">
              <option value="">All Brands</option>
              <option v-for="brand in brands" :key="brand" :value="brand">{{ brand }}</option>
            </select>
            <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" viewBox="0 0 20 20"
                fill="currentColor">
                <path fill-rule="evenodd"
                  d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                  clip-rule="evenodd" />
              </svg>
            </div>
          </div>

          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" viewBox="0 0 20 20"
                fill="currentColor">
                <path fill-rule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                  clip-rule="evenodd" />
              </svg>
            </div>
            <select v-model="filters.stockStatus"
              class="w-full pl-10 pr-4 py-3 bg-slate-800/70 border border-slate-600/50 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all duration-300 text-white appearance-none">
              <option value="all">All Statuses</option>
              <option value="in-stock">In Stock Only</option>
              <option value="low-stock">Low Stock</option>
              <option value="out-of-stock">Out of Stock</option>
            </select>
            <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" viewBox="0 0 20 20"
                fill="currentColor">
                <path fill-rule="evenodd"
                  d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                  clip-rule="evenodd" />
              </svg>
            </div>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div class="md:col-span-2">
            <div class="flex items-center justify-between mb-2">
              <span class="text-sm font-medium text-gray-300">Price Range</span>
              <span class="text-sm font-medium text-blue-400">${{ filters.minPrice }} - ${{ filters.maxPrice }}</span>
            </div>
            <div class="relative pt-1">
              <div class="flex justify-between mb-2">
                <input v-model.number="filters.minPrice" type="range" min="0" :max="maxPrice" step="10"
                  class="w-full h-2 bg-slate-700 rounded-lg appearance-none cursor-pointer slider-thumb" />
              </div>
              <div class="flex justify-between">
                <span class="text-xs text-gray-400">$0</span>
                <span class="text-xs text-gray-400">${{ maxPrice }}</span>
              </div>
            </div>
          </div>

          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" viewBox="0 0 20 20"
                fill="currentColor">
                <path
                  d="M3 3a1 1 0 000 2h11a1 1 0 100-2H3zM3 7a1 1 0 000 2h5a1 1 0 000-2H3zM3 11a1 1 0 100 2h4a1 1 0 100-2H3zM13 16a1 1 0 102 0v-5.586l1.293 1.293a1 1 0 001.414-1.414l-3-3a1 1 0 00-1.414 0l-3 3a1 1 0 101.414 1.414L13 10.414V16z" />
              </svg>
            </div>
            <select v-model="sortOption"
              class="w-full pl-10 pr-4 py-3 bg-slate-800/70 border border-slate-600/50 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all duration-300 text-white appearance-none">
              <option value="default">Default Sorting</option>
              <option value="price-low">Price: Low to High</option>
              <option value="price-high">Price: High to Low</option>
              <option value="name">Name: A to Z</option>
              <option value="stock">Stock: High to Low</option>
            </select>
            <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" viewBox="0 0 20 20"
                fill="currentColor">
                <path fill-rule="evenodd"
                  d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                  clip-rule="evenodd" />
              </svg>
            </div>
          </div>
        </div>
      </div>

      <div class="mb-6 flex justify-between items-center">
        <p class="text-gray-400">
          Showing
          <span class="font-bold text-white">{{ filteredProducts.length }}</span>
          products out of
          <span class="font-bold text-white">{{ products.length }}</span>
        </p>

        <div v-if="activeFiltersCount > 0" class="flex items-center gap-2 text-sm">
          <span class="text-gray-400">Active Filters:</span>
          <span class="px-2 py-1 bg-blue-500/20 text-blue-400 rounded-lg text-xs">
            {{ activeFiltersCount }}
          </span>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div v-for="product in filteredProducts" :key="product.id"
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

            <NuxtLink :to="`/product/${product.id}`"
              class="mt-auto inline-block text-indigo-400 hover:text-indigo-300 font-semibold">
              View Details →
            </NuxtLink>
          </div>
        </div>
      </div>

      <div v-if="loading" class="text-center text-gray-400 text-lg mt-10">Loading products...</div>
      <div v-else-if="!filteredProducts.length" class="text-center text-red-500 text-lg mt-10">⚠️ No products found.
      </div>
    </div>
  </div>
</template>



<script setup lang="ts">
import { ref, onMounted, watch, computed, nextTick } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import ProductAPI, { type Product, type Category } from '@/service/products'

useHead({
  title: 'Product'
})

const products = ref<Product[]>([])
const filteredProducts = ref<Product[]>([])
const loading = ref(true)

const route = useRoute()
const router = useRouter()

const filters = ref({
  search: '',
  category: '',
  brand: '',
  stockStatus: 'all',
  minPrice: 0,
  maxPrice: 1000
})

const sortOption = ref('default')

const categories = ref<Category[]>([])
const brands = ref<string[]>([])

const maxPrice = computed(() => {
  if (products.value.length === 0) return 1000
  return Math.max(...products.value.map(p => parseFloat(p.price)))
})

const activeFiltersCount = computed(() => {
  let count = 0
  if (filters.value.search) count++
  if (filters.value.category) count++
  if (filters.value.brand) count++
  if (filters.value.stockStatus !== 'all') count++
  if (filters.value.minPrice > 0 || filters.value.maxPrice < maxPrice.value) count++
  if (sortOption.value !== 'default') count++
  return count
})

const updateURL = () => {
  const query: any = {}

  if (filters.value.search) query.search = filters.value.search
  if (filters.value.category) query.category = filters.value.category
  if (filters.value.brand) query.brand = filters.value.brand
  if (filters.value.stockStatus !== 'all') query.stock = filters.value.stockStatus
  if (filters.value.minPrice > 0) query.minPrice = filters.value.minPrice
  if (filters.value.maxPrice < maxPrice.value) query.maxPrice = filters.value.maxPrice
  if (sortOption.value !== 'default') query.sort = sortOption.value

  router.replace({
    path: route.path,
    query
  })
}

const readURLParams = () => {
  const { query } = route

  if (query.search) filters.value.search = query.search as string
  if (query.category) filters.value.category = query.category as string
  if (query.brand) filters.value.brand = query.brand as string
  if (query.stock) filters.value.stockStatus = query.stock as string
  if (query.minPrice) filters.value.minPrice = Number(query.minPrice)
  if (query.maxPrice) filters.value.maxPrice = Number(query.maxPrice)
  if (query.sort) sortOption.value = query.sort as string
}

const applyFilters = () => {
  if (products.value.length === 0) return

  let result = [...products.value]

  if (filters.value.search) {
    const searchTerm = filters.value.search.toLowerCase()
    result = result.filter(product =>
      product.name.toLowerCase().includes(searchTerm) ||
      (product.brand && product.brand.toLowerCase().includes(searchTerm)) ||
      product.category.toLowerCase().includes(searchTerm)
    )
  }

  if (filters.value.category) {
    result = result.filter(product => product.category === filters.value.category)
  }

  if (filters.value.brand) {
    result = result.filter(product => product.brand === filters.value.brand)
  }

  if (filters.value.stockStatus !== 'all') {
    if (filters.value.stockStatus === 'in-stock') {
      result = result.filter(product => product.stock > 0)
    } else if (filters.value.stockStatus === 'low-stock') {
      result = result.filter(product => product.stock > 0 && product.stock < 5)
    } else if (filters.value.stockStatus === 'out-of-stock') {
      result = result.filter(product => product.stock === 0)
    }
  }

  result = result.filter(product => {
    const price = parseFloat(product.price)
    return price >= filters.value.minPrice && price <= filters.value.maxPrice
  })

  if (sortOption.value !== 'default') {
    result.sort((a, b) => {
      const priceA = parseFloat(a.price)
      const priceB = parseFloat(b.price)

      switch (sortOption.value) {
        case 'price-low':
          return priceA - priceB
        case 'price-high':
          return priceB - priceA
        case 'name':
          return a.name.localeCompare(b.name)
        case 'stock':
          return b.stock - a.stock
        default:
          return 0
      }
    })
  }

  filteredProducts.value = result
  updateURL()
}

const resetFilters = () => {
  filters.value = {
    search: '',
    category: '',
    brand: '',
    stockStatus: 'all',
    minPrice: 0,
    maxPrice: maxPrice.value
  }
  sortOption.value = 'default'

  router.replace({ path: route.path })
}

const fetchCategories = async () => {
  try {
    const categoriesData = await ProductAPI.getCategories()
    categories.value = categoriesData
  } catch (error) {
    console.error('❌ Error fetching categories:', error)
  }
}

const extractBrands = (products: Product[]) => {
  const brandSet = new Set<string>()
  products.forEach(product => {
    if (product.brand) {
      brandSet.add(product.brand)
    }
  })
  brands.value = Array.from(brandSet)
}

const fetchProducts = async () => {
  loading.value = true
  try {
    const allProducts = await ProductAPI.getAllProducts()
    products.value = allProducts
    extractBrands(allProducts)

    filters.value.maxPrice = maxPrice.value

    readURLParams()

    applyFilters()

  } catch (error) {
    console.error('❌ Error fetching products:', error)
    products.value = []
    filteredProducts.value = []
  } finally {
    loading.value = false
  }
}



onMounted(async () => {

  await fetchCategories()
  await fetchProducts()

})

watch([
  () => filters.value.search,
  () => filters.value.category,
  () => filters.value.brand,
  () => filters.value.stockStatus,
  () => filters.value.minPrice,
  () => filters.value.maxPrice,
  sortOption
], () => {
  applyFilters()
}, { deep: true })

watch(() => route.query, (newQuery) => {

  readURLParams()

  applyFilters()
})
</script>