<template>
  <footer class="bg-gradient-to-t from-slate-900 via-slate-800 to-slate-900 text-white py-16 relative overflow-hidden">
    <div class="absolute -top-32 -left-32 w-96 h-96 bg-blue-500 opacity-20 rounded-full blur-3xl animate-pulse-slow">
    </div>
    <div
      class="absolute -bottom-32 -right-32 w-96 h-96 bg-pink-500 opacity-20 rounded-full blur-3xl animate-pulse-slow">
    </div>

    <div class="container mx-auto px-6 relative z-10 grid lg:grid-cols-4 gap-10">
      <div>
        <h2 class="text-2xl font-bold text-blue-400 mb-4">Household Appliances</h2>
        <p class="text-gray-300">
          Your trusted partner in home appliances, delivering premium products with style and performance.
        </p>
      </div>

      <div>
        <h5 class="font-semibold text-white mb-4">Quick Links</h5>
        <ul class="space-y-2">
          <li>
            <NuxtLink to="/blog" class="hover:text-blue-400 transition">Blog</NuxtLink>
          </li>
          <li>
            <NuxtLink to="/aboutus" class="hover:text-blue-400 transition">About Us</NuxtLink>
          </li>
          <li>
            <NuxtLink to="/contactus" class="hover:text-blue-400 transition">Contact Us</NuxtLink>
          </li>
        </ul>
      </div>

      <div>
        <h5 class="font-semibold text-white mb-4">Contact</h5>
        <p class="text-gray-300 mb-1">📍 123 Blue Street, Tech City</p>
        <p class="text-gray-300 mb-1">📞 +1 (800) 123-4567</p>
        <p class="text-gray-300">📧 support@coolhome.com</p>
      </div>

      <div>
        <h5 class="font-semibold text-white mb-4">Subscribe to Our Newsletter</h5>
        <p class="text-gray-300 mb-3">
          Stay updated with the latest offers and news. Enter your email below:
        </p>
        <form @submit.prevent="handleSubscribe" class="flex gap-2 flex-wrap">
          <input v-model="email" type="email" placeholder="Your email address" required
            class="flex-grow px-4 py-3 rounded-lg text-gray-900 bg-gray-100 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-400" />
          <CustomButton :label="'Subscribe'" size="md"
            class="bg-gradient-to-r from-blue-400 to-pink-500 text-white px-6 py-3 rounded-lg font-semibold shadow-lg hover:scale-105 transition-transform w-auto"
            @click="handleSubscribe" />
        </form>
      </div>
    </div>

    <div class="mt-12 border-t border-gray-700 pt-6 text-center text-gray-400 text-sm">
      &copy; 2025 Household Appliances. All rights reserved.
    </div>
  </footer>
</template>

<script setup lang="ts">
import { ref } from "vue";
import Swal from "sweetalert2";
import CustomButton from '@/components/common/CustomButton.vue'
import { subscribeEmail } from '@/service/footer'

const email = ref("");

const handleSubscribe = async (): Promise<void> => {
  if (!email.value) return;

  const { success, message } = await subscribeEmail(email.value);

  Swal.fire({
    title: success ? "Subscribed!" : "Oops!",
    text: message,
    icon: success ? "success" : "error",
    confirmButtonText: "OK",
    confirmButtonColor: success ? "#4f46e5" : "#dc2626",
    background: "#1e293b",
    color: "#f8fafc",
  });

  if (success) email.value = "";
};
</script>
