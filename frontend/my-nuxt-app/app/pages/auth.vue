<template>
    <div
        class="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 overflow-hidden relative">
        <!-- Background glows -->
        <div
            class="absolute top-[-15%] left-[-10%] w-[500px] h-[500px] bg-blue-500/20 rounded-full blur-3xl animate-float">
        </div>
        <div
            class="absolute bottom-[-15%] right-[-10%] w-[400px] h-[400px] bg-purple-500/20 rounded-full blur-3xl animate-float-delayed">
        </div>

        <!-- Flip Card -->
        <div class="relative w-[90%] max-w-5xl h-[600px] perspective">
            <div class="relative w-full h-full transition-transform duration-[1s] transform-style-preserve"
                :class="{ 'rotate-y-180': !isLogin }">
                <!-- LOGIN SIDE -->
                <div
                    class="card-face front absolute inset-0 flex flex-col lg:flex-row bg-slate-800/70 rounded-3xl backdrop-blur-xl border border-white/10 shadow-2xl overflow-hidden">
                    <!-- Left image section -->
                    <div class="hidden lg:flex flex-1 bg-cover bg-center relative bg-login">
                        <div class="absolute inset-0 bg-gradient-to-r from-slate-900/70 to-slate-800/50"></div>
                        <div class="absolute bottom-10 left-10 text-white">
                            <h2 class="text-4xl font-extrabold mb-2">Welcome Back 👋</h2>
                            <p class="text-gray-300 text-sm">Log in to access your account</p>
                        </div>
                    </div>

                    <!-- Login form -->
                    <div class="flex-1 flex justify-center items-center">
                        <div class="w-full max-w-md p-8 text-white">
                            <h2 class="text-3xl font-bold mb-6 text-center">Login</h2>
                            <form @submit.prevent="handleLogin" class="flex flex-col gap-5">
                                <input v-model="email" type="email" placeholder="Email" class="input" required />
                                <input v-model="password" type="password" placeholder="Password" class="input"
                                    required />
                                <button class="btn-primary mt-2">Login</button>
                            </form>

                            <p class="text-center text-gray-400 text-sm mt-4">
                                Don’t have an account?
                                <button class="text-blue-400 hover:underline font-semibold" @click="isLogin = false">
                                    Sign Up
                                </button>
                            </p>

                            <div v-if="errorMessages.length" class="mt-4 text-red-400 text-sm">
                                <ul>
                                    <li v-for="(err, i) in errorMessages" :key="i">{{ err }}</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- SIGNUP SIDE -->
                <div
                    class="card-face back absolute inset-0 flex flex-col lg:flex-row bg-slate-800/70 rounded-3xl backdrop-blur-xl border border-white/10 shadow-2xl overflow-hidden rotate-y-180">
                    <!-- Left image section -->
                    <div class="hidden lg:flex flex-1 bg-cover bg-center relative bg-signup">
                        <div class="absolute inset-0 bg-gradient-to-r from-slate-900/70 to-slate-800/50"></div>
                        <div class="absolute bottom-10 left-10 text-white">
                            <h2 class="text-4xl font-extrabold mb-2">Join Us ✨</h2>
                            <p class="text-gray-300 text-sm">Create an account and start exploring</p>
                        </div>
                    </div>

                    <!-- Signup form -->
                    <div class="flex-1 flex justify-center items-center">
                        <div class="w-full max-w-md p-8 text-white">
                            <h2 class="text-3xl font-bold mb-6 text-center">Sign Up</h2>
                            <form @submit.prevent="handleSignup" class="flex flex-col gap-5">
                                <input v-model="name" type="text" placeholder="Name" class="input" required />
                                <input v-model="email" type="email" placeholder="Email" class="input" required />
                                <input v-model="password" type="password" placeholder="Password" class="input"
                                    required />
                                <button class="btn-success mt-2">Create Account</button>
                            </form>

                            <p class="text-center text-gray-400 text-sm mt-4">
                                Already have an account?
                                <button class="text-emerald-400 hover:underline font-semibold" @click="isLogin = true">
                                    Login
                                </button>
                            </p>

                            <div v-if="errorMessages.length" class="mt-4 text-red-400 text-sm">
                                <ul>
                                    <li v-for="(err, i) in errorMessages" :key="i">{{ err }}</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import Swal from 'sweetalert2'
import { useRouter } from 'vue-router'

const router = useRouter()

const isLogin = ref(true)
const email = ref('')
const password = ref('')
const name = ref('')
const errorMessages = ref<string[]>([])

const API_URL = 'http://localhost:8000/api'

const handleLogin = async () => {
  errorMessages.value = []
  try {
    const { data } = await axios.post(`${API_URL}/token/`, {
      username: email.value,
      password: password.value,
    })

    localStorage.setItem('access_token', data.access)
    localStorage.setItem('refresh_token', data.refresh)

    await Swal.fire({
      icon: 'success',
      title: 'Login Successful!',
      text: 'You are now logged in.',
      confirmButtonText: 'OK',
    })

    // redirect after success
    router.push('/')
  } catch (err: any) {
    console.error(err)
    if (err.response?.data?.detail) {
      errorMessages.value.push(err.response.data.detail)
    } else {
      errorMessages.value.push('Server connection error')
    }
  }
}

const handleSignup = async () => {
  errorMessages.value = []
  try {
    const { data } = await axios.post(`${API_URL}/signup/`, {
      name: name.value,
      email: email.value,
      password: password.value,
    })

    localStorage.setItem('access_token', data.access)
    localStorage.setItem('refresh_token', data.refresh)

    await Swal.fire({
      icon: 'success',
      title: 'Signup Successful!',
      text: 'Your account has been created.',
      confirmButtonText: 'OK',
    })

    // redirect after success
    router.push('/')
  } catch (err: any) {
    console.error(err)
    if (err.response?.data) {
      const resp = err.response.data
      if (typeof resp === 'object') {
        for (const key in resp) {
          const val = resp[key]
          if (Array.isArray(val)) errorMessages.value.push(...val)
          else errorMessages.value.push(val)
        }
      } else {
        errorMessages.value.push('Unknown error occurred')
      }
    } else {
      errorMessages.value.push('Server connection error')
    }
  }
}
</script>





<style scoped>
.bg-login {
    background-image: url('../assets/auth/login.jpg');
}

.bg-signup {
    background-image: url('../assets/auth/signup.jpg');
}


.perspective {
    perspective: 2000px;
}

.transform-style-preserve {
    transform-style: preserve-3d;
}

.rotate-y-180 {
    transform: rotateY(180deg);
}

.card-face {
    backface-visibility: hidden;
    transform-style: preserve-3d;
}

.card-face.back {
    transform: rotateY(180deg);
}

.input {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 12px 14px;
    border-radius: 10px;
    color: white;
    outline: none;
    transition: all 0.3s ease;
}

.input:focus {
    border-color: #3b82f6;
    box-shadow: 0 0 10px rgba(59, 130, 246, 0.3);
}

.btn-primary {
    background-color: #3b82f6;
    padding: 12px;
    border-radius: 10px;
    font-weight: 600;
    transition: all 0.3s ease;
}

.btn-primary:hover {
    background-color: #2563eb;
}

.btn-success {
    background-color: #10b981;
    padding: 12px;
    border-radius: 10px;
    font-weight: 600;
    transition: all 0.3s ease;
}

.btn-success:hover {
    background-color: #059669;
}

@keyframes float {

    0%,
    100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-25px);
    }
}

.animate-float {
    animation: float 8s ease-in-out infinite;
}

.animate-float-delayed {
    animation: float 10s ease-in-out infinite 2s;
}
</style>
