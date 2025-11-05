<template>
  <div v-if="relatedBlogs.length" class="mt-12">
    <h3 class="text-3xl font-bold mb-6">Related Blogs</h3>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="blog in relatedBlogs" :key="blog.id"
           class="bg-slate-800/70 rounded-xl shadow-md backdrop-blur-md hover:scale-105 transition-transform duration-300 p-4 flex flex-col">
        
        <div v-if="blog.image" class="overflow-hidden rounded-t-xl mb-4">
          <img :src="blog.image" :alt="blog.title"
               class="w-full h-40 object-cover transition-transform duration-500 hover:scale-110 rounded-lg" />
        </div>

        <h4 class="text-xl font-semibold mb-2">{{ blog.title }}</h4>
        <p class="text-gray-400 text-sm mb-2">
          🖊 {{ blog.author.first_name }} {{ blog.author.last_name }}
        </p>
        <p class="text-gray-400 text-sm mb-4">
          🏷 {{ blog.category.name }}
        </p>

        <NuxtLink :to="`/blog/${blog.id}`"
                  class="mt-auto inline-block text-indigo-400 hover:text-indigo-300 font-semibold">
          Read More →
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import type { Blog } from '@/service/blogs'
import BlogAPI from '@/service/blogs'

interface Props {
  blogId: number
}

const props = defineProps<Props>()
const relatedBlogs = ref<Blog[]>([])
const loading = ref(true)

const fetchRelatedBlogs = async () => {
  loading.value = true
  try {
    relatedBlogs.value = await BlogAPI.getRelatedBlogs(props.blogId)
  } catch (error) {
    console.error('❌ Error fetching related blogs:', error)
    relatedBlogs.value = []
  } finally {
    loading.value = false
  }
}

onMounted(fetchRelatedBlogs)
watch(() => props.blogId, fetchRelatedBlogs)
</script>
