<template>
  <div class="min-h-screen bg-gradient-to-b from-slate-900 via-slate-800 to-slate-900 text-white py-16">
    <div class="max-w-3xl mx-auto p-8 bg-slate-800/70 rounded-xl shadow-xl backdrop-blur-md">

      <!-- Loading/Error -->
      <div v-if="loading" class="text-center text-gray-400 text-lg mt-10">Loading blog post...</div>
      <div v-else-if="!blog" class="text-center text-red-500 text-lg mt-10">⚠️ Blog not found or failed to load.</div>

      <!-- Blog Content -->
      <div v-else>
        <header class="mb-6">
          <h1 class="text-4xl font-extrabold mb-2">{{ blog.title }}</h1>
          <div class="flex flex-wrap gap-4 text-gray-400 text-sm">
            <span class="flex items-center gap-1">🖊 {{ blog.author.first_name }} {{ blog.author.last_name }}</span>
            <span class="flex items-center gap-1">🏷 {{ blog.category.name }}</span>
          </div>
        </header>

        <div v-if="blog.image" class="mb-6">
          <img :src="blog.image" :alt="blog.title" class="w-full rounded-xl shadow-lg" />
        </div>

        <article class="prose prose-invert max-w-none mb-6" v-html="renderMarkdown(blog.content)"></article>

        <div v-if="blog.tags && blog.tags.length" class="mt-6">
          <span class="font-semibold">Tags:</span>
          <span v-for="tag in blog.tags" :key="tag.id" class="inline-block bg-gray-700 text-gray-200 px-2 py-1 rounded mr-2 mb-2 text-sm">
            #{{ tag.name }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import BlogAPI from '../../../server/api/blogs'
import { marked } from 'marked'

const route = useRoute()
const blog = ref<any>(null)
const loading = ref(true)

const renderMarkdown = (md: string) => marked.parse(md || '')

onMounted(async () => {
  const id = route.params.id
  try {
    blog.value = await BlogAPI.getBlogById(id)
  } catch (error) {
    console.error('❌ Error fetching blog:', error)
  } finally {
    loading.value = false
  }
})
</script>
