import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

class BlogAPI {
  static async getAllBlogs() {
    try {
      const response = await axios.get(`${BASE_URL}/blog/`);
      return response.data;
    } catch (error) {
      console.error('❌', error);
      throw error;
    }
  }

  static async getBlogById(id) {
    try {
      const response = await axios.get(`${BASE_URL}/blog/${id}/`);
      return response.data;
    } catch (error) {
      console.error(`❌${id}:`, error);
      throw error;
    }
  }

  static async getHomeBlog(count) {
    try {
      const response = await axios.get(`${BASE_URL}/blog/`, { params: { count: count } })
      return response.data;
    } catch (error) {
      console.error('❌', error);
      throw error;
    }
  }
}

export default BlogAPI;
