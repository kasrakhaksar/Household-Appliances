import axios from "axios";

const BASE_URL = "http://localhost:8000";



export const subscribeEmail = async (email: string) => {
  try {
    const response = await axios.post(`${BASE_URL}/subscribe/`, { email });
    return { success: true, message: response.data.message };
  } catch (error: any) {
    const message =
      error.response?.data?.email?.[0] ||
      error.response?.data?.message ||
      "Something went wrong!";
    return { success: false, message };
  }
};
