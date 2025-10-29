import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

// Define a Product type
export interface Product {
  id: number;
  name: string;
  price: number;
  brand: string;
  category: string;
  image: string;
  [key: string]: any; 
}

class ProductAPI {
  static async getAllProducts(): Promise<Product[]> {
    try {
      const response = await axios.get<Product[]>(`${BASE_URL}/product/`);
      return response.data;
    } catch (error) {
      console.error('❌', error);
      throw error;
    }
  }

  static async getProductById(id: number): Promise<Product> {
    try {
      const response = await axios.get<Product>(`${BASE_URL}/product/${id}/`);
      return response.data;
    } catch (error) {
      console.error(`❌${id}:`, error);
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
      console.error('❌', error);
      throw error;
    }
  }
}

export default ProductAPI;
