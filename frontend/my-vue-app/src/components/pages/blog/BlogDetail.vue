<template>
    <div class="blog-detail" v-if="!loading && blog">
      <div class="header">
        <h1 class="title">{{ blog.title }}</h1>
        <div class="meta">
            <span>🖊 {{ blog.author.first_name }} {{ blog.author.last_name }}</span>
            <span>🏷 {{ blog.category.name }}</span>
        </div>
      </div>
  
      <div v-if="blog.image" class="cover-image">
        <img :src="blog.image" :alt="blog.title" />
      </div>
  
      <div class="content" v-html="renderMarkdown(blog.content)"></div>
  
      <div class="tags" v-if="blog.tags && blog.tags.length">
        <strong>Tags:</strong>
        <span v-for="tag in blog.tags" :key="tag.id" class="tag">#{{ tag.name }}</span>
      </div>
    </div>
  
    <div v-else-if="loading" class="loading">Loading blog post...</div>
    <div v-else class="error">⚠️ Blog not found or failed to load.</div>
  </template>
  
  <script>
  import BlogAPI from '../home/api/BlogsApi';
  import { marked } from 'marked'; // ✨ اضافه شده
  
  export default {
    name: 'BlogDetail',
    data() {
      return {
        blog: null,
        loading: true,
      };
    },
    methods: {
      formatDate(dateStr) {
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        return new Date(dateStr).toLocaleDateString(undefined, options);
      },
      renderMarkdown(markdownText) {
        return marked.parse(markdownText || '');
      },
    },
    async created() {
      const slug = this.$route.params.slug;
      try {
        this.blog = await BlogAPI.getBlogById(slug);
      } catch (error) {
        console.error('❌ Error fetching blog:', error);
      } finally {
        this.loading = false;
      }
    },
  };
  </script>
  
  <style scoped>
  .blog-detail {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
    font-family: "Segoe UI", sans-serif;
  }
  .header .title {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
  }
  .meta span {
    margin-right: 1rem;
    font-size: 0.9rem;
    color: #666;
  }
  .cover-image img {
    max-width: 100%;
    margin: 1.5rem 0;
    border-radius: 12px;
  }
  .content {
    font-size: 1.1rem;
    line-height: 1.8;
    margin-top: 1rem;
  }
  .tags {
    margin-top: 2rem;
  }
  .tag {
    background-color: #eee;
    padding: 4px 8px;
    border-radius: 8px;
    margin-right: 0.5rem;
    font-size: 0.85rem;
  }
  .loading, .error {
    text-align: center;
    margin-top: 4rem;
    font-size: 1.2rem;
  }
  </style>
  