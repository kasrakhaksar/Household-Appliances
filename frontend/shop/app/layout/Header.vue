<template>
  <nav class="bg-gradient-to-r from-blue-900 via-slate-900 to-blue-800 text-white sticky top-0 z-50 shadow-xl">
    <div class="container mx-auto px-6 flex items-center justify-between py-4">

      <NuxtLink to="/" class="text-2xl font-bold tracking-tight text-blue-400 hover:text-blue-200">
        Household Appliances
      </NuxtLink>

      <ul class="hidden lg:flex items-center gap-10">
        <li class="relative group">
          <button class="flex items-center gap-1 font-semibold hover:text-blue-200 transition">
            Products
            <svg class="w-4 h-4 mt-1" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"></path>
            </svg>
          </button>

          <div class="absolute top-full left-1/2 -translate-x-1/2 w-screen max-w-6xl bg-white text-gray-800 rounded-xl shadow-2xl 
         opacity-0 invisible translate-y-6 group-hover:opacity-100 group-hover:visible group-hover:translate-y-0
         transition-all duration-500 ease-out p-8 grid grid-cols-4 gap-6 z-50">
            <div v-for="(category, idx) in categories" :key="idx">
              <h6 class="font-bold text-blue-600 mb-2">{{ category.label }}</h6>
              <ul class="space-y-1">
                <li>
                  <button @click="magaMenuGetCategory(category.value)" class="hover:text-blue-400 transition">
                    View All
                  </button>
                </li>
              </ul>
            </div>
          </div>
        </li>

        <li>
          <NuxtLink to="/" class="hover:text-blue-200 transition font-semibold">Home</NuxtLink>
        </li>
        <li>
          <NuxtLink to="/blog" class="hover:text-blue-200 transition font-semibold">Blog</NuxtLink>
        </li>
        <li>
          <NuxtLink to="/aboutus" class="hover:text-blue-200 transition font-semibold">About Us</NuxtLink>
        </li>
        <li>
          <NuxtLink to="/contactus" class="hover:text-blue-200 transition font-semibold">Contact Us</NuxtLink>
        </li>

        <li>
          <button v-if="isLoggedIn" @click="confirmLogout"
            class="flex items-center gap-2 hover:text-blue-200 transition font-semibold">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round"
                d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path>
            </svg>
            Logout
          </button>
          <NuxtLink v-else to="/auth" class="flex items-center gap-2 hover:text-blue-200 transition font-semibold">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round"
                d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"></path>
            </svg>
            Login
          </NuxtLink>
        </li>
      </ul>

    </div>
  </nav>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { fetchCategories, magaMenuProductRouter } from "@/service/header";
import Swal from 'sweetalert2';



const categories = ref<any[]>([]);
const router = useRouter();
const isLoggedIn = ref(false);

onMounted(async () => {
  categories.value = await fetchCategories();
  checkLoginStatus();
});

const checkLoginStatus = () => {
  isLoggedIn.value = !!localStorage.getItem("access_token");
};

const magaMenuGetCategory = (categoryValue: string) => {
  magaMenuProductRouter(router, categoryValue);
};

const confirmLogout = async () => {
  const result = await Swal.fire({
    title: 'Are you sure you want to logout?',
    icon: 'question',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, Logout',
    cancelButtonText: 'Cancel',
    reverseButtons: true
  });

  if (result.isConfirmed) {
    logout();
  }
};

const logout = () => {
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");
  isLoggedIn.value = false;

  Swal.fire({
    title: 'Logged out successfully!',
    icon: 'success',
    timer: 2000,
    showConfirmButton: false
  });

  router.push("/");
};
</script>