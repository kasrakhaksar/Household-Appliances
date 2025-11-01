<template>
  <nav class="bg-gradient-to-r from-blue-900 via-slate-900 to-blue-800 text-white sticky top-0 z-50 shadow-xl">
    <div class="container mx-auto px-6 flex items-center justify-between py-4">

      <!-- Logo -->
      <router-link to="/" class="text-2xl font-bold tracking-tight text-blue-400 hover:text-blue-200">
        Household Appliances
      </router-link>

      <!-- Desktop Menu -->
      <ul class="hidden lg:flex items-center gap-10">
        <!-- Products Mega Menu -->
        <li class="relative group">
          <button class="flex items-center gap-1 font-semibold hover:text-blue-200 transition">
            Products
            <svg class="w-4 h-4 mt-1" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"></path>
            </svg>
          </button>

          <!-- Mega Menu -->
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
                <li><a href="#" class="hover:text-blue-400 transition">Best Sellers</a></li>
                <li><a href="#" class="hover:text-blue-400 transition">New Arrivals</a></li>
              </ul>

            </div>
          </div>

        </li>


        <li>
          <router-link to="/" class="hover:text-blue-200 transition font-semibold">Home</router-link>
        </li>
        <li>
          <router-link to="/blog" class="hover:text-blue-200 transition font-semibold">Blog</router-link>
        </li>
        <li>
          <router-link to="/aboutus" class="hover:text-blue-200 transition font-semibold">About Us</router-link>
        </li>
        <li>
          <router-link to="/contactus" class="hover:text-blue-200 transition font-semibold">Contact Us</router-link>
        </li>
      </ul>

      <!-- Icons -->
      <div class="flex items-center gap-5">
        <button class="hover:text-blue-200 transition text-xl">🔍</button>
        <button class="hover:text-blue-200 transition text-xl">🛒</button>

        <span>
          <router-link v-if="!isLoggedIn" to="/auth"
            class="text-blue-400 hover:text-blue-200 text-xl transition">👤</router-link>
          <button v-else @click="logout" class="text-red-400 hover:text-red-600 text-xl transition">🚪</button>
        </span>

        <!-- Mobile Menu Button -->
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

    <!-- Mobile Menu -->
    <div v-if="mobileOpen" class="lg:hidden bg-slate-900 text-white">
      <ul class="flex flex-col px-6 py-4 gap-4">
        <li>
          <router-link to="/" class="hover:text-blue-400 transition">Home</router-link>
        </li>
        <li>
          <router-link to="/aboutus" class="hover:text-blue-400 transition">About Us</router-link>
        </li>
        <li>
          <router-link to="/contactus" class="hover:text-blue-400 transition">Contact Us</router-link>
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
import { fetchCategories, magaMenuProductRouter } from "../../server/api/header";

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