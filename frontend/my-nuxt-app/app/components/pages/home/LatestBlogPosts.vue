<template>
  <section class="py-12 bg-gradient-to-b from-slate-900 via-slate-800 to-slate-900 text-white">
    <div class="container mx-auto px-4 text-center">

      <h4 class="text-3xl md:text-4xl font-extrabold mb-4">Latest Blog Posts</h4>
      <p class="text-gray-300 mb-8 text-lg md:text-xl">
        Check out our latest tips and tricks for home appliance care and maintenance.
      </p>

      <div v-if="blogs.length > 0" class="grid gap-6 sm:grid-cols-2 md:grid-cols-3 justify-items-center">
        <div v-for="blog in blogs" :key="blog.id" class="w-full max-w-sm">
          <div
            class="bg-slate-800/70 rounded-xl p-5 shadow-md hover:shadow-xl hover:translate-y-1 transition-all duration-300 cursor-pointer h-full flex flex-col"
          >
            <h3 class="text-xl font-bold text-white mb-3">{{ blog.title }}</h3>
            <p class="text-gray-300 text-sm mb-4 flex-1">{{ blog.excerpt }}</p>
            <NuxtLink
              :to="`/blog/${blog.id}/`"
              class="mt-auto inline-block text-blue-400 font-semibold hover:text-blue-600 hover:border-b-2 border-blue-600 transition-all"
            >
              Read More
            </NuxtLink>
          </div>
        </div>
      </div>

      <p v-else class="text-gray-400">Loading...</p>
    </div>
  </section>
</template>

<script>
import BlogAPI from '@/service/blogs'

export default {
  name: 'BlogList',
  data() {
    return {
      blogs: [],
    }
  },
  async mounted() {
    try {
      this.blogs = await BlogAPI.getHomeBlog(3)
      console.log(this.blogs)
    } catch (error) {
      console.error('❌ error:', error)
    }
  },
}
</script>
