import axios from "axios";
import { Router } from "vue-router";


const API_BASE = "http://localhost:8000";



export const fetchCategories = async () => {
  try {
    const response = await axios.get(`${API_BASE}/products/categories/`);
    return response.data;
  } catch (error) {
    console.error("Error fetching categories:", error);
    return [];
  }
};


export const magaMenuProductRouter = (router: Router, category: string) => {
  router.push({ path: "/product", query: { category } });
};