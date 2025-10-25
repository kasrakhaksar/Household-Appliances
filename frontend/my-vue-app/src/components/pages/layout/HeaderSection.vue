<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light shadow-sm">
    <div class="container">
      <!-- Logo -->
      <router-link class="navbar-brand text-primary fw-bold" to="/">
        Household Appliances
      </router-link>

      <!-- Toggler for mobile -->
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- Menu -->
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <!-- Products Mega Menu -->
          <li class="nav-item dropdown" v-if="categories.length">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              id="productsDropdown"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Products
            </a>
            <ul class="dropdown-menu p-3" aria-labelledby="productsDropdown">
              <div class="d-flex flex-wrap gap-4">
                <div
                  class="mega-column"
                  v-for="(category, index) in categories"
                  :key="index"
                >
                  <h6 class="text-primary">{{ category.label }}</h6>
                  <ul class="list-unstyled mb-0">
                    <li><a class="dropdown-item" href="#">View All</a></li>
                    <li><a class="dropdown-item" href="#">Best Sellers</a></li>
                    <li><a class="dropdown-item" href="#">New Arrivals</a></li>
                  </ul>
                </div>
              </div>
            </ul>
          </li>

          <!-- Other Links -->
          <li class="nav-item"><router-link class="nav-link" to="/">Home</router-link></li>
          <li class="nav-item"><router-link class="nav-link" to="/aboutus">About Us</router-link></li>
          <li class="nav-item"><router-link class="nav-link" to="/contactus">Contact Us</router-link></li>
        </ul>

        <!-- Icons -->
        <div class="d-flex align-items-center gap-3">
          <span class="fs-5 text-primary">🔍</span>
          <span class="fs-5 text-primary">🛒</span>
          <span>
            <router-link v-if="!isLoggedIn" to="/auth" class="fs-5 text-primary">👤</router-link>
            <button v-else @click="logout" class="btn btn-link fs-5 text-primary p-0">🚪</button>
          </span>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const categories = ref([])
const router = useRouter()
const isLoggedIn = ref(false)

onMounted(async () => {
  try {
    const res = await axios.get('http://localhost:8000/products/categories/')
    categories.value = res.data
    isLoggedIn.value = !!localStorage.getItem('access_token')
  } catch (error) {
    console.error('Error fetching categories:', error)
  }
})

const logout = () => {
  localStorage.removeItem('access_token')
  localStorage.removeItem('refresh_token')
  isLoggedIn.value = false
  router.push('/auth')
}
</script>

<style scoped>
.mega-column h6 {
  margin-bottom: 0.5rem;
}

.dropdown-menu {
  width: 100%;
  max-width: 800px;
  border-radius: 12px;
}

.dropdown-menu a:hover {
  color: #0077b6;
}
</style>
