import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

export interface ProductImage {
  id: number;
  url: string;
  alt_text: string;
}

export interface Product {
  id: number;
  name: string;
  price: string;
  discount_price?: string;
  stock: number;
  brand?: string;
  category: string;
  description?: string;
  image?: string;
  images?: ProductImage[];
  is_active?: boolean;
  created_at?: string;
  updated_at?: string;
  [key: string]: any;
}

export interface Category {
  label: string;
  value: string;
}

class ProductAPI {
  static async getAllProducts(): Promise<Product[]> {
    try {
      const response = await axios.get<Product[]>(`${BASE_URL}/product/`);
      return response.data;
    } catch (error) {
      console.error('❌ Error fetching all products:', error);
      throw error;
    }
  }

  static async getProductById(id: number): Promise<Product> {
    try {
      const response = await axios.get<Product>(`${BASE_URL}/product/${id}/`);
      return response.data;
    } catch (error) {
      console.error(`❌ Error fetching product ${id}:`, error);
      throw error;
    }
  }

  static async getProductsByCategory(category: string): Promise<Product[]> {
    try {
      const response = await axios.get<Product[]>(`${BASE_URL}/product/search/`, {
        params: { category },
      });
      return response.data;
    } catch (error) {
      console.error(`❌ Error fetching products for category ${category}:`, error);
      throw error;
    }
  }

  static async getHomeProducts(count: number): Promise<Product[]> {
    try {
      const response = await axios.get<Product[]>(`${BASE_URL}/product/`, {
        params: { count },
      });
      return response.data;
    } catch (error) {
      console.error('❌ Error fetching home products:', error);
      throw error;
    }
  }

  static async getRelatedProducts(productId: number): Promise<Product[]> {
    try {
      const response = await axios.get<Product[]>(`${BASE_URL}/product/${productId}/related/`)
      return response.data
    } catch (error) {
      console.error(`❌ Error fetching related products for product ${productId}:`, error)
      throw error
    }
  }

  static async getCategories(): Promise<Category[]> {
    try {
      const response = await axios.get<Category[]>(`${BASE_URL}/product/categories/`);
      return response.data;
    } catch (error) {
      console.error('❌ Error fetching categories:', error);
      throw error;
    }
  }

  static async searchProducts(params: {
    search?: string;
    category?: string;
    brand?: string;
    minPrice?: number;
    maxPrice?: number;
    stockStatus?: string;
  }): Promise<Product[]> {
    try {
      const response = await axios.get<Product[]>(`${BASE_URL}/product/search/`, {
        params,
      });
      return response.data;
    } catch (error) {
      console.error('❌ Error searching products:', error);
      throw error;
    }
  }
}

export default ProductAPI;