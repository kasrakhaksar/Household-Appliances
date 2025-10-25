<template>
  <section class="py-5 text-center">
    <div class="container">
      <h2 class="text-primary mb-3">Latest Blog Posts</h2>
      <p class="text-secondary mb-4">Check out our latest tips and tricks for home appliance care and maintenance.</p>

      <div v-if="blogs.length > 0" class="row g-4 justify-content-center">
        <div v-for="blog in blogs" :key="blog.id" class="col-sm-6 col-md-4">
          <div class="card blog-card h-100 p-3">
            <h3 class="h5 text-primary">{{ blog.title }}</h3>
            <p class="text-dark excerpt">{{ blog.excerpt }}</p>
            <router-link :to="`/blog/${blog.id}/`" class="read-more">Read More</router-link>
          </div>
        </div>
      </div>

      <p v-else>Loading...</p>
    </div>
  </section>
</template>

<script>
import BlogAPI from './api/BlogsApi'

export default {
  name: 'BlogList',
  data() {
    return {
      blogs: [],
    };
  },
  async mounted() {
    try {
      this.blogs = await BlogAPI.getHomeBlog(1);
      console.log(this.blogs);
    } catch (error) {
      console.error('❌ error:', error);
    }
  },
};
</script>

<style scoped>
.blog-card {
  background: linear-gradient(145deg, #f0f7ff, #d9e9ff);
  border-radius: 16px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
}

.blog-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 16px 40px rgba(0, 63, 136, 0.25),
              inset 0 0 15px rgba(255, 255, 255, 0.9);
}

.blog-card h3 {
  font-weight: 700;
  margin-bottom: 0.75rem;
}

.blog-card .excerpt {
  font-size: 0.95rem;
  line-height: 1.5;
  min-height: 60px;
  margin-bottom: 1rem;
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
</style>
