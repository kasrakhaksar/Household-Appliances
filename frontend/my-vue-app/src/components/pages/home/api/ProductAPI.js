import axios from 'axios';

const BASE_URL = 'http://localhost:8000';


class ProductAPI {
  static async getAllProducts() {
    try {
      const response = await axios.get(`${BASE_URL}/product/`);
      return response.data;
    } catch (error) {
      console.error('❌', error);
      throw error;
    }
  }

  static async getProductById(id) {
    try {
      const response = await axios.get(`${BASE_URL}/product/${id}/`);
      return response.data;
    } catch (error) {
      console.error(`❌${id}:`, error);
      throw error;
    }
  }

}

export default ProductAPI;