<template>
    <div class="min-h-screen bg-gradient-to-b from-slate-900 via-slate-800 to-slate-900 text-white py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h1 class="text-5xl font-extrabold text-center mb-12">Blog</h1>

            <div class="relative max-w-md mx-auto mb-12">
                <input v-model="searchTag" type="text" placeholder="Search by tag..." class="w-full px-5 py-3 rounded-full bg-slate-800/60 text-white placeholder-gray-400
                 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition-all duration-300 shadow-md" />
                <span
                    class="absolute right-4 top-1/2 -translate-y-1/2 text-indigo-400 pointer-events-none text-lg">#</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div v-for="post in filteredBlogs" :key="post.id"
                    class="bg-slate-800/70 rounded-xl shadow-xl backdrop-blur-md hover:scale-105 transition-transform duration-300 flex flex-col">
                    <div v-if="post.image" class="overflow-hidden rounded-t-xl">
                        <img :src="post.image" :alt="post.title"
                            class="w-full h-48 object-cover transition-transform duration-500 hover:scale-110" />
                    </div>

                    <div class="p-6 flex flex-col flex-1">
                        <h2 class="text-2xl font-bold mb-2">{{ post.title }}</h2>
                        <p class="text-gray-400 text-sm mb-4">🖊 {{ post.author.first_name }} {{ post.author.last_name
                            }}</p>
                        <p class="text-gray-300 mb-4 line-clamp-3">{{ post.content }}</p>

                        <div class="flex flex-wrap gap-2 mb-4">
                            <span v-for="tag in post.tags" :key="tag.id"
                                class="inline-block bg-gray-700 text-gray-200 px-2 py-1 rounded text-xs cursor-pointer hover:bg-indigo-500 hover:text-white transition-colors"
                                @click="searchTag = tag.name">
                                #{{ tag.name }}
                            </span>
                        </div>

                        <NuxtLink :to="`/blog/${post.id}`"
                            class="mt-auto inline-block text-indigo-400 hover:text-indigo-300 font-semibold">
                            Read More →
                        </NuxtLink>
                    </div>
                </div>
            </div>

            <div v-if="loading" class="text-center text-gray-400 text-lg mt-10 animate-pulse">Loading blogs...</div>
            <div v-else-if="!filteredBlogs.length && !loading" class="text-center text-red-500 text-lg mt-10">
                ⚠️ No blogs found for tag "<span class="text-indigo-400">{{ searchTag }}</span>"
            </div>
        </div>
    </div>
</template>




<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import BlogAPI from '@/service/blogs'

const route = useRoute()
const blogs = ref<any[]>([])
const loading = ref(true)
const searchTag = ref('')

watch(
    () => route.query.tag,
    (newTag) => {
        if (newTag) searchTag.value = String(newTag)
    },
    { immediate: true }
)

const filteredBlogs = computed(() => {
    if (!searchTag.value.trim()) return blogs.value
    return blogs.value.filter(blog =>
        blog.tags?.some((tag: any) =>
            tag.name.toLowerCase().includes(searchTag.value.toLowerCase())
        )
    )
})

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
