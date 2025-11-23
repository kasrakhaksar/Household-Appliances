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
        <div class="image-section flex-1 min-w-[300px]">
          <div class="main-image h-[350px] md:h-[400px] text-center mb-4">
            <img :src="selectedImage || product.image" :alt="product.name"
              class="w-full h-full object-cover rounded-xl transition-transform duration-300 hover:scale-105" />
          </div>

          <div v-if="allImages.length > 0" class="image-gallery flex gap-2 overflow-x-auto py-2">
            <div v-for="(img, index) in allImages" :key="img.id || index" @click="selectedImage = img.url" :class="[
              'thumbnail cursor-pointer border-2 rounded-lg transition-all duration-200 flex-shrink-0',
              selectedImage === img.url ? 'border-blue-500 scale-105' : 'border-transparent hover:border-gray-400'
            ]">
              <img :src="img.url" :alt="img.alt_text || product.name"
                class="w-16 h-16 md:w-20 md:h-20 object-cover rounded" />
            </div>
          </div>
        </div>

        <div class="info-section flex-1 min-w-[400px] text-left">
          <h1 class="product-name text-3xl md:text-4xl font-extrabold mb-4">{{ product.name }}</h1>

          <div v-if="product.discount_price && parseFloat(product.discount_price) > 0" class="mb-4">
            <span
              class="discount-badge inline-block bg-orange-500 text-white px-3 py-1 rounded-full text-sm font-bold mb-1 animate-pulse">
              🔥 Save {{ calculateDiscountPercentage() }}%
            </span>
            <p class="product-price text-lg mt-1">
              <del class="text-gray-400 mr-2">${{ product.price }}</del>
              <span class="discounted-price text-red-500 font-bold text-xl">
                ${{ calculateFinalPrice() }}
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

      <RelatedProducts v-if="product" :productId="product.id" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import ProductAPI, { type Product, type ProductImage } from '@/service/products';
import RelatedProducts from '@/components/pages/product/RelatedProducts.vue';

const route = useRoute();
const product = ref<Product | null>(null);
const loading = ref<boolean>(true);
const selectedImage = ref<string>('');

const allImages = computed((): ProductImage[] => {
  if (!product.value) return [];

  const images: ProductImage[] = [];

  if (product.value.images && Array.isArray(product.value.images)) {
    images.push(...product.value.images);
  }

  const mainImageUrl = product.value.image;
  const hasMainImageInGallery = images.some(img => img.url === mainImageUrl);

  if (mainImageUrl && !hasMainImageInGallery) {
    images.unshift({
      id: 0,
      url: mainImageUrl,
      alt_text: product.value.name
    });
  }

  return images;
});

const calculateDiscountPercentage = (): string => {
  if (!product.value || !product.value.discount_price) return '0';

  const price = parseFloat(product.value.price);
  const discount = parseFloat(product.value.discount_price);

  if (price <= 0 || discount <= 0) return '0';

  return ((discount * 100) / price).toFixed(0);
};

const calculateFinalPrice = (): string => {
  if (!product.value) return '0';

  const price = parseFloat(product.value.price);
  const discount = product.value.discount_price ? parseFloat(product.value.discount_price) : 0;

  return (price - discount).toFixed(2);
};

watch(product, (newProduct) => {
  if (newProduct) {
    selectedImage.value = newProduct.image || '';
  }
});

const stockClass = computed(() => {
  if (!product.value) return '';
  if (product.value.stock === 0) return 'text-red-600 font-bold';
  if (product.value.stock < 5) return 'text-orange-400 font-bold';
  return '';
});

onMounted(async () => {
  try {
    const id = Number(route.params.id);
    product.value = await ProductAPI.getProductById(id);
  } catch (error) {
    console.error('❌ Error fetching product:', error);
  } finally {
    loading.value = false;
  }
});
</script>

<style scoped>
.image-gallery {
  scrollbar-width: thin;
  scrollbar-color: #4a5568 #2d3748;
}

.image-gallery::-webkit-scrollbar {
  height: 6px;
}

.image-gallery::-webkit-scrollbar-track {
  background: #2d3748;
  border-radius: 3px;
}

.image-gallery::-webkit-scrollbar-thumb {
  background: #4a5568;
  border-radius: 3px;
}

.image-gallery::-webkit-scrollbar-thumb:hover {
  background: #718096;
}
</style>