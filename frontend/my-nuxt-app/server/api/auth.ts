import axios from 'axios'

const API_URL = 'http://localhost:8000/api'

export interface LoginData {
  username: string
  password: string
}

export interface SignupData {
  name: string
  email: string
  password: string
}

export interface AuthResponse {
  access: string
  refresh: string
}

/**
 * Login function
 * @param data {LoginData}
 * @returns {Promise<AuthResponse>}
 */
export const login = async (data: LoginData): Promise<AuthResponse> => {
  try {
    const response = await axios.post(`${API_URL}/token/`, data)
    return response.data
  } catch (err: any) {
    if (err.response?.data?.detail) {
      throw new Error(err.response.data.detail)
    } else {
      throw new Error('Server connection error')
    }
  }
}

/**
 * Signup function
 * @param data {SignupData}
 * @returns {Promise<AuthResponse>}
 */
export const signup = async (data: SignupData): Promise<AuthResponse> => {
  try {
    const response = await axios.post(`${API_URL}/signup/`, data)
    return response.data
  } catch (err: any) {
    if (err.response?.data) {
      const resp = err.response.data
      if (typeof resp === 'object') {
        const messages: string[] = []
        for (const key in resp) {
          const val = resp[key]
          if (Array.isArray(val)) messages.push(...val)
          else messages.push(val)
        }
        throw new Error(messages.join(', '))
      } else {
        throw new Error('Unknown error occurred')
      }
    } else {
      throw new Error('Server connection error')
    }
  }
}
