import type { AxiosResponse } from "axios";
import axios from "axios";

const BASE_URL = 'http://localhost:8000';

interface Author {
  first_name: string;
  last_name: string;
}

interface Category {
  name: string;
}

interface Tag {
  id: number;
  name: string;
}

export interface Blog {
  id: number;
  title: string;
  content: string;
  image?: string;
  author: Author;
  category: Category;
  tags?: Tag[];
}

class BlogAPI {
  static async getAllBlogs(): Promise<Blog[]> {
    try {
      const response: AxiosResponse<Blog[]> = await axios.get(`${BASE_URL}/blog/`);
      return response.data;
    } catch (error) {
      console.error('❌', error);
      throw error;
    }
  }

  static async getBlogById(id: string | number): Promise<Blog> {
    try {
      const response: AxiosResponse<Blog> = await axios.get(`${BASE_URL}/blog/${id}/`);
      return response.data;
    } catch (error) {
      console.error(`❌ Blog ID ${id}:`, error);
      throw error;
    }
  }

  static async getHomeBlog(count: number): Promise<Blog[]> {
    try {
      const response: AxiosResponse<Blog[]> = await axios.get(`${BASE_URL}/blog/`, {
        params: { count }
      });
      return response.data;
    } catch (error) {
      console.error('❌', error);
      throw error;
    }
  }


  static async getBlogsByTag(tag: string): Promise<Blog[]> {
    try {
      const response = await axios.get<Blog[]>(`${BASE_URL}/blog/`, { params: { tag } });
      return response.data;
    } catch (error) {
      console.error('❌ Error fetching blogs by tag:', error);
      throw error;
    }
  }

  static async getRelatedBlogs(blogId: number): Promise<Blog[]> {
    try {
      const response = await axios.get<Blog[]>(`${BASE_URL}/blog/${blogId}/related/`);
      return response.data;
    } catch (error) {
      console.error(`❌ Error fetching related blogs for blog ${blogId}:`, error);
      throw error;
    }
  }

}

export default BlogAPI;