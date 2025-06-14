<template>
    <section class="extra-section">
      <h2>Latest Blog Posts</h2>
      <p>Check out our latest tips and tricks for home appliance care and maintenance.</p>

      <section class="latest-blogs">
        <h2>Latest Blogs</h2>
        <div v-if="blogs.length > 0" class="blog-list">
          <div v-for="blog in blogs" :key="blog.id" class="blog-card">
            <h3>{{ blog.title }}</h3>
            <p class="excerpt">{{ blog.excerpt }}</p>
            <router-link :to="`/blog/${blog.slug}`" class="read-more">Read More</router-link>
          </div>
        </div>
        <p v-else>Loading...</p>
      </section>
    </section>
  </template>
  


  
  
  <script setup>
    import { ref, onMounted } from 'vue'
    import axios from 'axios'
  
    const blogs = ref([])
  
    const fetchLatestBlogs = async () => {
      try {
        const response = await axios.get('http://localhost:8000/blog/latest/')
        blogs.value = response.data
      } catch (error) {
        console.error('Error fetching blogs:', error)
      }
    }
  
    onMounted(() => {
      fetchLatestBlogs()
    })
  </script>
  
  
  
  <style scoped>
  
  .extra-section {
    padding: 2rem 1rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    text-align: center;
  }
  
  .extra-section h2 {
    color: #003f88;
    margin-bottom: 1rem;
  }
  
  .extra-section p {
    color: #0a2540;
    margin-bottom: 1rem;
  }
  
  .latest-blogs {
  padding: 2rem;
  max-width: 900px;
  margin: 0 auto;
}

.blog-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
}

.blog-card {
  background: linear-gradient(145deg, #f0f7ff, #d9e9ff);
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow:
    0 8px 24px rgba(0, 63, 136, 0.15),
    inset 0 0 10px rgba(255, 255, 255, 0.8);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
}

.blog-card:hover {
  transform: translateY(-8px);
  box-shadow:
    0 16px 40px rgba(0, 63, 136, 0.25),
    inset 0 0 15px rgba(255, 255, 255, 0.9);
}

.blog-card h3 {
  color: #003f88;
  font-weight: 700;
  font-size: 1.4rem;
  margin-bottom: 0.75rem;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.blog-card .excerpt {
  color: #1a2e5b;
  font-size: 1rem;
  line-height: 1.5;
  margin-bottom: 1.25rem;
  min-height: 60px;
}

.read-more {
  display: inline-block;
  font-weight: 600;
  color: #0077cc;
  text-decoration: none;
  border-bottom: 2px solid transparent;
  transition: border-color 0.3s ease, color 0.3s ease;
}

.read-more:hover {
  color: #004a99;
  border-color: #004a99;
}

@media (max-width: 480px) {
  .blog-card {
    padding: 1rem;
  }

  .blog-card h3 {
    font-size: 1.2rem;
  }

  .blog-card .excerpt {
    font-size: 0.9rem;
    min-height: auto;
  }
}
  
</style>