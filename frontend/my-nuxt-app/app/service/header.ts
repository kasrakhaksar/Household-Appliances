import axios from "axios";


const BASE_URL = "http://localhost:8000";



export const fetchCategories = async () => {
  try {
    const response = await axios.get(`${BASE_URL}/products/categories/`);
    return response.data;
  } catch (error) {
    console.error("Error fetching categories:", error);
    return [];
  }
};


export const magaMenuProductRouter = (router: Router, category: string) => {
  router.push({ path: "/product", query: { category } });
};