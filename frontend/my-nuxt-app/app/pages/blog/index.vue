<template>
    <div class="min-h-screen bg-gradient-to-b from-slate-900 via-slate-800 to-slate-900 text-white py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

            <h1 class="text-5xl font-extrabold text-center mb-12">Blog</h1>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div v-for="post in blogs" :key="post.id"
                    class="bg-slate-800/70 rounded-xl shadow-xl backdrop-blur-md hover:scale-105 transition-transform duration-300 flex flex-col">
                    <div v-if="post.image" class="overflow-hidden rounded-t-xl">
                        <img :src="post.image" :alt="post.title"
                            class="w-full h-48 object-cover transition-transform duration-500 hover:scale-110" />
                    </div>

                    <div class="p-6 flex flex-col flex-1">
                        <h2 class="text-2xl font-bold mb-2">{{ post.title }}</h2>
                        <p class="text-gray-400 text-sm mb-4">🖊 {{ post.author.first_name }} {{ post.author.last_name}}</p>
                        <p class="text-gray-300 mb-4 line-clamp-3">{{ post.content }}</p>

                        <div class="flex flex-wrap gap-2 mb-4">
                            <span v-for="tag in post.tags" :key="tag.id"
                                class="inline-block bg-gray-700 text-gray-200 px-2 py-1 rounded text-xs">
                                #{{ tag.name }}
                            </span>
                        </div>

                        <router-link :to="`/blog/${post.id}`"
                            class="mt-auto inline-block text-indigo-400 hover:text-indigo-300 font-semibold">
                            Read More →
                        </router-link>
                    </div>
                </div>

            </div>

            <div v-if="loading" class="text-center text-gray-400 text-lg mt-10">Loading blogs...</div>
            <div v-else-if="!blogs.length" class="text-center text-red-500 text-lg mt-10">⚠️ No blogs found.</div>

        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import BlogAPI from '../../../server/api/blogs'

const blogs = ref<any[]>([])
const loading = ref(true)

onMounted(async () => {
    try {
        blogs.value = await BlogAPI.getAllBlogs()
    } catch (error) {
        console.error('❌ Error fetching blogs:', error)
    } finally {
        loading.value = false
    }
})
</script>
