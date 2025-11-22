<template>
  <div
    class="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 overflow-hidden relative">

    <div class="absolute -top-[15%] -left-[10%] w-[500px] h-[500px] bg-blue-500/20 rounded-full blur-3xl animate-float">
    </div>
    <div
      class="absolute -bottom-[15%] -right-[10%] w-[400px] h-[400px] bg-purple-500/20 rounded-full blur-3xl animate-float-delayed">
    </div>

    <div class="relative w-[90%] max-w-5xl h-[600px] perspective">
      <div class="relative w-full h-full transition-transform duration-1000 transform-style-preserve"
        :class="{ 'rotate-y-180': !isLogin }">

        <div
          class="card-face front absolute inset-0 flex flex-col lg:flex-row bg-slate-800/70 rounded-3xl backdrop-blur-xl border border-white/10 shadow-2xl overflow-hidden">

          <button @click="$router.push('/')"
            class="absolute top-4 left-4 z-20 w-10 h-10 flex items-center justify-center rounded-xl bg-white/5 hover:bg-blue-500/20 hover:translate-y-[-2px] hover:shadow-lg hover:shadow-blue-500/30 transition-all duration-300 group">
            <svg xmlns="http://www.w3.org/2000/svg"
              class="w-5 h-5 text-white/70 group-hover:text-white transition-all duration-300 group-hover:scale-110"
              viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
              stroke-linejoin="round">
              <path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" />
              <polyline points="9 22 9 12 15 12 15 22" />
            </svg>
          </button>

          <div class="hidden lg:flex flex-1 relative bg-cover bg-center bg-login">
            <div class="absolute inset-0 bg-gradient-to-r from-slate-900/70 to-slate-800/50"></div>
            <div class="absolute bottom-10 left-10 text-white">
              <h2 class="text-4xl font-extrabold mb-2">Welcome Back 👋</h2>
              <p class="text-gray-300 text-sm">Log in to access your account</p>
            </div>
          </div>

          <div class="flex-1 flex justify-center items-center">
            <div class="w-full max-w-md p-8 text-white">
              <h2 class="text-3xl font-bold mb-6 text-center">Login</h2>
              <form @submit.prevent="handleLogin" class="flex flex-col gap-5">
                <input v-model="email" type="email" placeholder="Email"
                  class="bg-white/8 border border-white/15 rounded-xl px-4 py-3 text-white outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-500 transition-all"
                  required />
                <input v-model="password" type="password" placeholder="Password"
                  class="bg-white/8 border border-white/15 rounded-xl px-4 py-3 text-white outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-500 transition-all"
                  required />

                <CustomButton :label="'Login'" size="md" color="blue"
                  class="mt-2 w-full px-4 py-3 rounded-xl font-semibold shadow-lg hover:bg-blue-700 transition-all"
                  @click="handleLogin" />
              </form>

              <p class="text-center text-gray-400 text-sm mt-4">
                Don't have an account?
                <button class="text-blue-400 hover:underline font-semibold" @click="isLogin = false">Sign Up</button>
              </p>

              <div v-if="errorMessages.length" class="mt-4 text-red-400 text-sm">
                <ul>
                  <li v-for="(err, i) in errorMessages" :key="i">{{ err }}</li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <div
          class="card-face back absolute inset-0 flex flex-col lg:flex-row bg-slate-800/70 rounded-3xl backdrop-blur-xl border border-white/10 shadow-2xl overflow-hidden rotate-y-180">

          <button @click="$router.push('/')"
            class="absolute top-4 left-4 z-20 w-10 h-10 flex items-center justify-center rounded-xl bg-white/5 hover:bg-emerald-500/20 hover:translate-y-[-2px] hover:shadow-lg hover:shadow-emerald-500/30 transition-all duration-300 group">
            <svg xmlns="http://www.w3.org/2000/svg"
              class="w-5 h-5 text-white/70 group-hover:text-white transition-all duration-300 group-hover:scale-110"
              viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
              stroke-linejoin="round">
              <path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" />
              <polyline points="9 22 9 12 15 12 15 22" />
            </svg>
          </button>

          <div class="hidden lg:flex flex-1 relative bg-cover bg-center bg-signup">
            <div class="absolute inset-0 bg-gradient-to-r from-slate-900/70 to-slate-800/50"></div>
            <div class="absolute bottom-10 left-10 text-white">
              <h2 class="text-4xl font-extrabold mb-2">Join Us ✨</h2>
              <p class="text-gray-300 text-sm">Create an account and start exploring</p>
            </div>
          </div>

          <div class="flex-1 flex justify-center items-center">
            <div class="w-full max-w-md p-8 text-white">
              <h2 class="text-3xl font-bold mb-6 text-center">Sign Up</h2>
              <form @submit.prevent="handleSignup" class="flex flex-col gap-5">
                <input v-model="name" type="text" placeholder="Name"
                  class="bg-white/8 border border-white/15 rounded-xl px-4 py-3 text-white outline-none focus:border-emerald-500 focus:ring-2 focus:ring-emerald-500 transition-all"
                  required />
                <input v-model="email" type="email" placeholder="Email"
                  class="bg-white/8 border border-white/15 rounded-xl px-4 py-3 text-white outline-none focus:border-emerald-500 focus:ring-2 focus:ring-emerald-500 transition-all"
                  required />
                <input v-model="password" type="password" placeholder="Password"
                  class="bg-white/8 border border-white/15 rounded-xl px-4 py-3 text-white outline-none focus:border-emerald-500 focus:ring-2 focus:ring-emerald-500 transition-all"
                  required />

                <CustomButton :label="'Create Account'" size="md" color="green"
                  class="mt-2 w-full px-4 py-3 rounded-xl font-semibold shadow-lg hover:bg-emerald-600 transition-all"
                  @click="handleSignup" />
              </form>

              <p class="text-center text-gray-400 text-sm mt-4">
                Already have an account?
                <button class="text-emerald-400 hover:underline font-semibold" @click="isLogin = true">Login</button>
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
import Swal from 'sweetalert2'
import { useRouter } from 'vue-router'
import { login, signup } from '@/service/auth'
import CustomButton from '@/components/common/CustomButton.vue'

const router = useRouter()

const isLogin = ref(true)
const email = ref('')
const password = ref('')
const name = ref('')
const errorMessages = ref<string[]>([])

const handleLogin = async () => {
  errorMessages.value = []
  try {
    const data = await login({ username: email.value, password: password.value })
    localStorage.setItem('access_token', data.access)
    localStorage.setItem('refresh_token', data.refresh)

    Swal.fire({
      icon: 'success',
      title: 'Login Successful!',
      text: 'You are now logged in.',
      timer: 2000,
      showConfirmButton: false,
      willClose: () => {
        window.location.href = '/'
      }
    })

  } catch (err: any) {
    errorMessages.value.push(err.message)
  }
}



const handleSignup = async () => {
  errorMessages.value = []
  try {
    const data = await signup({ name: name.value, email: email.value, password: password.value })
    localStorage.setItem('access_token', data.access)
    localStorage.setItem('refresh_token', data.refresh)

    Swal.fire({
      icon: 'success',
      title: 'Signup Successful!',
      text: 'Your account has been created.',
      timer: 2000,
      showConfirmButton: true,
      willClose: () => {
        window.location.href = '/'
      }
    })

  } catch (err: any) {
    errorMessages.value.push(err.message)
  }
}

</script>

<style scoped>
.bg-login {
  background-image: url('@/assets/auth/login.jpg');
}

.bg-signup {
  background-image: url('@/assets/auth/signup.jpg');
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
