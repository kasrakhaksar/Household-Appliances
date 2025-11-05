<template>
    <div v-if="relatedProducts.length" class="mt-12">
        <h3 class="text-3xl font-bold mb-6">Related Products</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div v-for="product in relatedProducts" :key="product.id"
                class="bg-slate-800/70 rounded-xl shadow-md backdrop-blur-md hover:scale-105 transition-transform duration-300 flex flex-col">

                <div v-if="product.image" class="overflow-hidden rounded-t-xl">
                    <img :src="product.image" :alt="product.name"
                        class="w-full h-40 object-cover transition-transform duration-500 hover:scale-110" />
                </div>

                <div class="p-4 flex flex-col flex-1">
                    <h4 class="text-xl font-semibold mb-2">{{ product.name }}</h4>
                    <p class="text-gray-400 text-sm mb-2"><strong>Brand:</strong> {{ product.brand }}</p>
                    <p class="text-blue-400 font-bold mb-2">${{ product.price }}</p>

                    <NuxtLink :to="`/product/${product.id}`"
                        class="mt-auto inline-block text-indigo-400 hover:text-indigo-300 font-semibold">
                        View Details →
                    </NuxtLink>
                </div>
            </div>
        </div>
    </div>
</template>



<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import ProductAPI from '@/service/products'
import type { Product } from '@/service/products'

interface Props {
    productId: number
}

const props = defineProps<Props>()
const relatedProducts = ref<Product[]>([])
const loading = ref(true)

const fetchRelated = async () => {
    loading.value = true
    try {
        const response = await ProductAPI.getRelatedProducts(props.productId)
        relatedProducts.value = response
    } catch (error) {
        console.error('❌ Error fetching related products:', error)
        relatedProducts.value = []
    } finally {
        loading.value = false
    }
}

onMounted(fetchRelated)
watch(() => props.productId, fetchRelated)

</script>
