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
                        class="flex flex-col items-center text-sm transition-all duration-300 text-white/70 hover:text-white group px-2 py-1 rounded-xl"
                        :class="{
                            'text-white font-semibold': $route.path === '/',
                            'text-white/70': $route.path !== '/'
                        }">
                        <div class="w-10 h-10 flex items-center justify-center rounded-xl transition-all duration-300 mb-1"
                            :class="{
                                'bg-blue-500/30 translate-y-[-2px] shadow-lg shadow-blue-500/30': $route.path === '/',
                                'bg-white/5 group-hover:bg-blue-500/20 group-hover:translate-y-[-2px] group-hover:shadow-lg group-hover:shadow-blue-500/30': $route.path !== '/'
                            }">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 transition-all duration-300" :class="{
                                'scale-110': $route.path === '/',
                                'group-hover:scale-110': $route.path !== '/'
                            }" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                stroke-linecap="round" stroke-linejoin="round">
                                <path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" />
                                <polyline points="9 22 9 12 15 12 15 22" />
                            </svg>
                        </div>
                        <span class="text-xs transition-all duration-300" :class="{
                            'font-semibold': $route.path === '/',
                            'font-medium group-hover:font-semibold': $route.path !== '/'
                        }">Home</span>
                    </NuxtLink>
                </li>

                <li>
                    <NuxtLink to="/product"
                        class="flex flex-col items-center text-sm transition-all duration-300 text-white/70 hover:text-white group px-2 py-1 rounded-xl"
                        :class="{
                            'text-white font-semibold': $route.path === '/product',
                            'text-white/70': $route.path !== '/product'
                        }">
                        <div class="w-10 h-10 flex items-center justify-center rounded-xl transition-all duration-300 mb-1"
                            :class="{
                                'bg-blue-500/30 translate-y-[-2px] shadow-lg shadow-blue-500/30': $route.path === '/product',
                                'bg-white/5 group-hover:bg-blue-500/20 group-hover:translate-y-[-2px] group-hover:shadow-lg group-hover:shadow-blue-500/30': $route.path !== '/product'
                            }">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 transition-all duration-300" :class="{
                                'scale-110': $route.path === '/product',
                                'group-hover:scale-110': $route.path !== '/product'
                            }" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                stroke-linecap="round" stroke-linejoin="round">
                                <rect width="7" height="7" x="3" y="3" rx="1" />
                                <rect width="7" height="7" x="14" y="3" rx="1" />
                                <rect width="7" height="7" x="14" y="14" rx="1" />
                                <rect width="7" height="7" x="3" y="14" rx="1" />
                            </svg>
                        </div>
                        <span class="text-xs transition-all duration-300" :class="{
                            'font-semibold': $route.path === '/product',
                            'font-medium group-hover:font-semibold': $route.path !== '/product'
                        }">Products</span>
                    </NuxtLink>
                </li>

                <li>
                    <NuxtLink to="/blog"
                        class="flex flex-col items-center text-sm transition-all duration-300 text-white/70 hover:text-white group px-2 py-1 rounded-xl"
                        :class="{
                            'text-white font-semibold': $route.path === '/blog',
                            'text-white/70': $route.path !== '/blog'
                        }">
                        <div class="w-10 h-10 flex items-center justify-center rounded-xl transition-all duration-300 mb-1"
                            :class="{
                                'bg-blue-500/30 translate-y-[-2px] shadow-lg shadow-blue-500/30': $route.path === '/blog',
                                'bg-white/5 group-hover:bg-blue-500/20 group-hover:translate-y-[-2px] group-hover:shadow-lg group-hover:shadow-blue-500/30': $route.path !== '/blog'
                            }">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 transition-all duration-300" :class="{
                                'scale-110': $route.path === '/blog',
                                'group-hover:scale-110': $route.path !== '/blog'
                            }" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                stroke-linecap="round" stroke-linejoin="round">
                                <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z" />
                                <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z" />
                            </svg>
                        </div>
                        <span class="text-xs transition-all duration-300" :class="{
                            'font-semibold': $route.path === '/blog',
                            'font-medium group-hover:font-semibold': $route.path !== '/blog'
                        }">Blog</span>
                    </NuxtLink>
                </li>

                <li>
                    <NuxtLink to="/aboutus"
                        class="flex flex-col items-center text-sm transition-all duration-300 text-white/70 hover:text-white group px-2 py-1 rounded-xl"
                        :class="{
                            'text-white font-semibold': $route.path === '/aboutus',
                            'text-white/70': $route.path !== '/aboutus'
                        }">
                        <div class="w-10 h-10 flex items-center justify-center rounded-xl transition-all duration-300 mb-1"
                            :class="{
                                'bg-blue-500/30 translate-y-[-2px] shadow-lg shadow-blue-500/30': $route.path === '/aboutus',
                                'bg-white/5 group-hover:bg-blue-500/20 group-hover:translate-y-[-2px] group-hover:shadow-lg group-hover:shadow-blue-500/30': $route.path !== '/aboutus'
                            }">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 transition-all duration-300" :class="{
                                'scale-110': $route.path === '/aboutus',
                                'group-hover:scale-110': $route.path !== '/aboutus'
                            }" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                stroke-linecap="round" stroke-linejoin="round">
                                <circle cx="12" cy="8" r="6" />
                                <path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11" />
                            </svg>
                        </div>
                        <span class="text-xs transition-all duration-300" :class="{
                            'font-semibold': $route.path === '/aboutus',
                            'font-medium group-hover:font-semibold': $route.path !== '/aboutus'
                        }">About Us</span>
                    </NuxtLink>
                </li>

                <li>
                    <button v-if="isLoggedIn" @click="confirmLogout"
                        class="flex flex-col items-center text-sm transition-all duration-300 text-white/70 hover:text-white group px-2 py-1 rounded-xl w-full">
                        <div
                            class="w-10 h-10 flex items-center justify-center rounded-xl bg-white/5 group-hover:bg-red-500/20 group-hover:translate-y-[-2px] group-hover:shadow-lg group-hover:shadow-red-500/30 transition-all duration-300 mb-1">
                            <svg xmlns="http://www.w3.org/2000/svg"
                                class="w-5 h-5 transition-all duration-300 group-hover:scale-110" viewBox="0 0 24 24"
                                fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round">
                                <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4" />
                                <polyline points="16 17 21 12 16 7" />
                                <line x1="21" x2="9" y1="12" y2="12" />
                            </svg>
                        </div>
                        <span
                            class="text-xs font-medium transition-all duration-300 group-hover:font-semibold">Logout</span>
                    </button>
                    <NuxtLink v-else to="/auth"
                        class="flex flex-col items-center text-sm transition-all duration-300 text-white/70 hover:text-white group px-2 py-1 rounded-xl"
                        :class="{
                            'text-white font-semibold': $route.path === '/auth',
                            'text-white/70': $route.path !== '/auth'
                        }">
                        <div class="w-10 h-10 flex items-center justify-center rounded-xl transition-all duration-300 mb-1"
                            :class="{
                                'bg-blue-500/30 translate-y-[-2px] shadow-lg shadow-blue-500/30': $route.path === '/auth',
                                'bg-white/5 group-hover:bg-blue-500/20 group-hover:translate-y-[-2px] group-hover:shadow-lg group-hover:shadow-blue-500/30': $route.path !== '/auth'
                            }">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 transition-all duration-300" :class="{
                                'scale-110': $route.path === '/auth',
                                'group-hover:scale-110': $route.path !== '/auth'
                            }" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                stroke-linecap="round" stroke-linejoin="round">
                                <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4" />
                                <polyline points="10 17 15 12 10 7" />
                                <line x1="15" x2="3" y1="12" y2="12" />
                            </svg>
                        </div>
                        <span class="text-xs transition-all duration-300" :class="{
                            'font-semibold': $route.path === '/auth',
                            'font-medium group-hover:font-semibold': $route.path !== '/auth'
                        }">Login</span>
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