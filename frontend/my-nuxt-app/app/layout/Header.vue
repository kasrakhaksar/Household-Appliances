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
      </ul>

      <div class="flex items-center gap-5">
        <button class="hover:text-blue-200 transition text-xl">🔍</button>
        <button class="hover:text-blue-200 transition text-xl">🛒</button>

        <span>
          <NuxtLink v-if="!isLoggedIn" to="/auth"
            class="text-blue-400 hover:text-blue-200 text-xl transition cursor-pointer">👤</NuxtLink>
          <button v-else @click="logout"
            class="text-red-400 hover:text-red-600 text-xl transition cursor-pointer">🚪</button>
        </span>


        <button @click="mobileOpen = !mobileOpen" class="lg:hidden text-2xl">
          <svg v-if="!mobileOpen" class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2"
            viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
          <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>
      </div>
    </div>

    <div v-if="mobileOpen" class="lg:hidden bg-slate-900 text-white">
      <ul class="flex flex-col px-6 py-4 gap-4">
        <li>
          <NuxtLink to="/" class="hover:text-blue-400 transition">Home</NuxtLink>
        </li>
        <li>
          <NuxtLink to="/aboutus" class="hover:text-blue-400 transition">About Us</NuxtLink>
        </li>
        <li>
          <NuxtLink to="/contactus" class="hover:text-blue-400 transition">Contact Us</NuxtLink>
        </li>
        <li v-if="categories.length">
          <span class="font-semibold mb-2 block">Products</span>
          <ul class="pl-4 space-y-1">
            <li v-for="(category, idx) in categories" :key="idx" class="hover:text-blue-400 transition">{{
              category.label }}</li>
          </ul>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { fetchCategories, magaMenuProductRouter } from "../service/header";

const categories = ref<any[]>([]);
const router = useRouter();
const isLoggedIn = ref(false);
const mobileOpen = ref(false);

onMounted(async () => {
  categories.value = await fetchCategories();
  isLoggedIn.value = !!localStorage.getItem("access_token");
});

const magaMenuGetCategory = (categoryValue: string) => {
  magaMenuProductRouter(router, categoryValue);
};

const logout = () => {
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");
  isLoggedIn.value = false;
  router.push("/auth");
};
</script>