<template>
    <nav class="fixed bottom-0 left-0 w-full z-50">
        <div
            class="relative bg-slate-900/70 backdrop-blur-2xl backdrop-saturate-150 border-t border-white/10 overflow-hidden shadow-2xl shadow-black/20">
            <div
                class="absolute w-32 h-32 bg-gradient-to-br from-blue-500 to-purple-500 rounded-full blur-2xl opacity-30 -bottom-10 left-1/4 animate-float">
            </div>
            <div
                class="absolute w-28 h-28 bg-gradient-to-br from-cyan-500 to-blue-500 rounded-full blur-2xl opacity-30 -bottom-8 left-1/2 animate-float animation-delay-2000">
            </div>
            <div
                class="absolute w-24 h-24 bg-gradient-to-br from-purple-500 to-pink-500 rounded-full blur-2xl opacity-30 -bottom-6 right-1/4 animate-float animation-delay-4000">
            </div>

            <ul class="flex justify-around items-center py-2 relative z-10">
                <li>
                    <NuxtLink to="/"
                        class="flex flex-col items-center text-sm transition-all duration-300 text-white/70 hover:text-white group px-2 py-1 rounded-xl">
                        <div
                            class="w-10 h-10 flex items-center justify-center rounded-xl bg-white/5 group-hover:bg-blue-500/20 group-hover:translate-y-[-2px] group-hover:shadow-lg group-hover:shadow-blue-500/30 transition-all duration-300 mb-1">
                            <svg xmlns="http://www.w3.org/2000/svg"
                                class="w-6 h-6 transition-all duration-300 group-hover:scale-110" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M3 12l2-2m0 0l7-7 7 7M13 5v6h6" />
                            </svg>
                        </div>
                        <span
                            class="text-xs font-medium transition-all duration-300 group-hover:font-semibold">Home</span>
                    </NuxtLink>
                </li>

                <li>
                    <NuxtLink to="/product"
                        class="flex flex-col items-center text-sm transition-all duration-300 text-white/70 hover:text-white group px-2 py-1 rounded-xl">
                        <div
                            class="w-10 h-10 flex items-center justify-center rounded-xl bg-white/5 group-hover:bg-blue-500/20 group-hover:translate-y-[-2px] group-hover:shadow-lg group-hover:shadow-blue-500/30 transition-all duration-300 mb-1">
                            <svg xmlns="http://www.w3.org/2000/svg"
                                class="w-6 h-6 transition-all duration-300 group-hover:scale-110" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M3 7h18M3 12h18M3 17h18" />
                            </svg>
                        </div>
                        <span
                            class="text-xs font-medium transition-all duration-300 group-hover:font-semibold">Products</span>
                    </NuxtLink>
                </li>

                <li>
                    <NuxtLink to="/blog"
                        class="flex flex-col items-center text-sm transition-all duration-300 text-white/70 hover:text-white group px-2 py-1 rounded-xl">
                        <div
                            class="w-10 h-10 flex items-center justify-center rounded-xl bg-white/5 group-hover:bg-blue-500/20 group-hover:translate-y-[-2px] group-hover:shadow-lg group-hover:shadow-blue-500/30 transition-all duration-300 mb-1">
                            <svg xmlns="http://www.w3.org/2000/svg"
                                class="w-6 h-6 transition-all duration-300 group-hover:scale-110" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M12 8c.667 0 1.333.667 1.333 1.333S12.667 10.667 12 10.667 10.667 10 10.667 9.333 11.333 8 12 8zm0 0v8" />
                            </svg>
                        </div>
                        <span
                            class="text-xs font-medium transition-all duration-300 group-hover:font-semibold">Blog</span>
                    </NuxtLink>
                </li>

                <li>
                    <NuxtLink to="/aboutus"
                        class="flex flex-col items-center text-sm transition-all duration-300 text-white/70 hover:text-white group px-2 py-1 rounded-xl">
                        <div
                            class="w-10 h-10 flex items-center justify-center rounded-xl bg-white/5 group-hover:bg-blue-500/20 group-hover:translate-y-[-2px] group-hover:shadow-lg group-hover:shadow-blue-500/30 transition-all duration-300 mb-1">
                            <svg xmlns="http://www.w3.org/2000/svg"
                                class="w-6 h-6 transition-all duration-300 group-hover:scale-110" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
                            </svg>
                        </div>
                        <span class="text-xs font-medium transition-all duration-300 group-hover:font-semibold">About
                            Us</span>
                    </NuxtLink>
                </li>

                <li>
                    <button v-if="isLoggedIn" @click="confirmLogout"
                        class="flex flex-col items-center text-sm transition-all duration-300 text-white/70 hover:text-white group px-2 py-1 rounded-xl w-full">
                        <div
                            class="w-10 h-10 flex items-center justify-center rounded-xl bg-white/5 group-hover:bg-red-500/20 group-hover:translate-y-[-2px] group-hover:shadow-lg group-hover:shadow-red-500/30 transition-all duration-300 mb-1">
                            <svg xmlns="http://www.w3.org/2000/svg"
                                class="w-6 h-6 transition-all duration-300 group-hover:scale-110" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                            </svg>
                        </div>
                        <span
                            class="text-xs font-medium transition-all duration-300 group-hover:font-semibold">Logout</span>
                    </button>
                    <NuxtLink v-else to="/auth"
                        class="flex flex-col items-center text-sm transition-all duration-300 text-white/70 hover:text-white group px-2 py-1 rounded-xl">
                        <div
                            class="w-10 h-10 flex items-center justify-center rounded-xl bg-white/5 group-hover:bg-blue-500/20 group-hover:translate-y-[-2px] group-hover:shadow-lg group-hover:shadow-blue-500/30 transition-all duration-300 mb-1">
                            <svg xmlns="http://www.w3.org/2000/svg"
                                class="w-6 h-6 transition-all duration-300 group-hover:scale-110" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1" />
                            </svg>
                        </div>
                        <span
                            class="text-xs font-medium transition-all duration-300 group-hover:font-semibold">Login</span>
                    </NuxtLink>
                </li>
            </ul>
        </div>
    </nav>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import Swal from 'sweetalert2';

const router = useRouter();
const isLoggedIn = ref(false);

onMounted(() => {
    checkLoginStatus();
});

const checkLoginStatus = () => {
    isLoggedIn.value = !!localStorage.getItem("access_token");
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