<template>
  <div class="container mx-auto px-6 py-16 relative z-10">
    <div v-if="loading" class="text-center text-gray-400 text-lg">Loading...</div>

    <div v-else class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
      <NuxtLink v-for="product in products" :key="product.id" :to="`/product/${product.id}`"
        class="block transform transition-all hover:-translate-y-2 hover:shadow-lg">
        <div class="group relative bg-slate-900 border border-slate-700
                 rounded-2xl shadow-xl p-4 flex flex-col items-center text-center
                 hover:shadow-blue-400/30 transition-shadow duration-300 w-full h-full">
          <div class="w-full h-72 rounded-2xl mb-4 overflow-hidden">
            <img :src="product.image" :alt="product.name"
              class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105" />
          </div>

          <h5 class="font-bold text-white text-lg mb-2 break-words">
            {{ product.name }}
          </h5>

          <p class="text-blue-400 font-semibold text-lg mb-1">Price: ${{ product.price }}</p>
          <p class="text-gray-300 text-sm mb-1">Brand: {{ product.brand }}</p>
          <p class="text-gray-300 text-sm">Category: {{ product.category }}</p>
        </div>
      </NuxtLink>
    </div>

    <div class="absolute top-[-10%] left-[-10%] w-96 h-96 bg-blue-500/20 rounded-full blur-3xl animate-float-slow">
    </div>
    <div class="absolute bottom-[-10%] right-[-10%] w-72 h-72 bg-pink-400/20 rounded-full blur-2xl animate-float-slow">
    </div>
  </div>
</template>



<script setup>
import { ref, onMounted } from 'vue'
import ProductAPI from '../../../service/products'

const products = ref([])
const loading = ref(true)

onMounted(async () => {
  try {
    products.value = await ProductAPI.getHomeProducts(4)
  } catch (error) {
    console.error(error)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
@keyframes floating {

  0%,
  100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-6px);
  }
}

.animate-floating {
  animation: floating 3.5s ease-in-out infinite;
}

@keyframes float-slow {

  0%,
  100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-12px);
  }
}

.animate-float-slow {
  animation: float-slow 12s ease-in-out infinite;
}
</style>
