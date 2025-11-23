<template>
    <div class="min-h-screen bg-gradient-to-b from-slate-900 via-slate-800 to-slate-900 text-white py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h1 class="text-5xl font-extrabold text-center mb-12">Blog</h1>

            <div class="bg-slate-800/50 backdrop-blur-md rounded-2xl p-6 mb-10 border border-slate-700/50 shadow-2xl">
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-6 mb-6">
                    <h2
                        class="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-500">
                        Filter Blogs
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

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-6">
                    <div class="relative">
                        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" viewBox="0 0 20 20"
                                fill="currentColor">
                                <path fill-rule="evenodd"
                                    d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                                    clip-rule="evenodd" />
                            </svg>
                        </div>
                        <input v-model="filters.search" type="text" placeholder="Search blog posts..."
                            class="w-full pl-10 pr-4 py-3 bg-slate-800/70 border border-slate-600/50 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all duration-300 text-white placeholder-gray-400" />
                    </div>

                    <div class="relative">
                        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" viewBox="0 0 20 20"
                                fill="currentColor">
                                <path fill-rule="evenodd"
                                    d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z"
                                    clip-rule="evenodd" />
                            </svg>
                        </div>
                        <input v-model="filters.tag" type="text" placeholder="Filter by tag..."
                            class="w-full pl-10 pr-4 py-3 bg-slate-800/70 border border-slate-600/50 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all duration-300 text-white placeholder-gray-400" />
                    </div>

                    <div class="relative">
                        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" viewBox="0 0 20 20"
                                fill="currentColor">
                                <path fill-rule="evenodd"
                                    d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
                                    clip-rule="evenodd" />
                            </svg>
                        </div>
                        <select v-model="filters.contentLength"
                            class="w-full pl-10 pr-4 py-3 bg-slate-800/70 border border-slate-600/50 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all duration-300 text-white appearance-none">
                            <option value="all">All Content Lengths</option>
                            <option value="short">Short Reads</option>
                            <option value="medium">Medium Reads</option>
                            <option value="long">Long Reads</option>
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

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
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
                            <option value="newest">Newest First</option>
                            <option value="oldest">Oldest First</option>
                            <option value="title-asc">Title: A to Z</option>
                            <option value="title-desc">Title: Z to A</option>
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
                    <span class="font-bold text-white">{{ filteredBlogs.length }}</span>
                    posts out of
                    <span class="font-bold text-white">{{ blogs.length }}</span>
                </p>

                <div v-if="activeFiltersCount > 0" class="flex items-center gap-2 text-sm">
                    <span class="text-gray-400">Active Filters:</span>
                    <span class="px-2 py-1 bg-blue-500/20 text-blue-400 rounded-lg text-xs">
                        {{ activeFiltersCount }}
                    </span>
                </div>
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
                                @click="filters.tag = tag.name">
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
                ⚠️ No blogs found matching your filters
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import BlogAPI from '@/service/blogs'

useHead({
    title: 'Blog'
})

const route = useRoute()
const router = useRouter()
const blogs = ref<any[]>([])
const loading = ref(true)

const filters = ref({
    search: '',
    tag: '',
    contentLength: 'all'
})

const sortOption = ref('default')

const updateURL = () => {
    const query: any = {}

    if (filters.value.search) query.search = filters.value.search
    if (filters.value.tag) query.tag = filters.value.tag
    if (filters.value.contentLength !== 'all') query.contentLength = filters.value.contentLength
    if (sortOption.value !== 'default') query.sort = sortOption.value

    router.replace({
        path: route.path,
        query
    })
}

const readURLParams = () => {
    const { query } = route

    if (query.search) filters.value.search = query.search as string
    if (query.tag) filters.value.tag = query.tag as string
    if (query.contentLength) filters.value.contentLength = query.contentLength as string
    if (query.sort) sortOption.value = query.sort as string
}

const applyFilters = () => {
    updateURL()
}

const filteredBlogs = computed(() => {
    let filtered = blogs.value.filter(blog => {
        const matchesSearch = !filters.value.search ||
            blog.title.toLowerCase().includes(filters.value.search.toLowerCase()) ||
            blog.content.toLowerCase().includes(filters.value.search.toLowerCase())

        const matchesTag = !filters.value.tag ||
            blog.tags?.some((tag: any) =>
                tag.name.toLowerCase().includes(filters.value.tag.toLowerCase())
            )

        const matchesContentLength = filters.value.contentLength === 'all' ||
            (filters.value.contentLength === 'short' && blog.content.length < 500) ||
            (filters.value.contentLength === 'medium' && blog.content.length >= 500 && blog.content.length < 1500) ||
            (filters.value.contentLength === 'long' && blog.content.length >= 1500)

        return matchesSearch && matchesTag && matchesContentLength
    })

    switch (sortOption.value) {
        case 'newest':
            filtered.sort((a, b) => new Date(b.created_at).getTime() - new Date(a.created_at).getTime())
            break
        case 'oldest':
            filtered.sort((a, b) => new Date(a.created_at).getTime() - new Date(b.created_at).getTime())
            break
        case 'title-asc':
            filtered.sort((a, b) => a.title.localeCompare(b.title))
            break
        case 'title-desc':
            filtered.sort((a, b) => b.title.localeCompare(a.title))
            break
        default:
            break
    }

    return filtered
})

const activeFiltersCount = computed(() => {
    return Object.values(filters.value).filter(value =>
        value !== '' && value !== 'all'
    ).length + (sortOption.value !== 'default' ? 1 : 0)
})

const resetFilters = () => {
    filters.value = {
        search: '',
        tag: '',
        contentLength: 'all'
    }
    sortOption.value = 'default'

    router.replace({ path: route.path })
}

watch([filters, sortOption], applyFilters, { deep: true })

watch(() => route.query, () => {
    readURLParams()
})

onMounted(async () => {
    try {
        readURLParams()

        blogs.value = await BlogAPI.getAllBlogs()
    } catch (error) {
        console.error('❌ Error fetching blogs:', error)
    } finally {
        loading.value = false
    }
})
</script>