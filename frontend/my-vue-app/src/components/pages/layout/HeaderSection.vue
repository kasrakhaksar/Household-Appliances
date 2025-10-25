<template>
  <nav class="navbar navbar-expand-lg bg-dark shadow-sm text-light py-3 sticky-top">
    <div class="container">

      <router-link class="navbar-brand text-light fw-bold fs-4" to="/">
        Household Appliances
      </router-link>

      <button
        class="navbar-toggler border-0"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
      </button>

      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item dropdown position-static" v-if="categories.length">
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
            <div
              class="dropdown-menu mega-menu mt-2 shadow-lg p-4 border-0 animate__animated animate__fadeIn"
              aria-labelledby="productsDropdown"
            >
              <div class="row g-4">
                <div
                  class="col-12 col-sm-6 col-md-4 col-lg-3"
                  v-for="(category, index) in categories"
                  :key="index"
                >
                  <h6 class="text-primary fw-bold mb-2">{{ category.label }}</h6>
                  <ul class="list-unstyled">
                    <li><a class="dropdown-item" href="#">View All</a></li>
                    <li><a class="dropdown-item" href="#">Best Sellers</a></li>
                    <li><a class="dropdown-item" href="#">New Arrivals</a></li>
                  </ul>
                </div>
              </div>
            </div>
          </li>

          <!-- Other Links -->
          <li class="nav-item">
            <router-link class="nav-link" to="/">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/aboutus">About Us</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/contactus">Contact Us</router-link>
          </li>
        </ul>

        <!-- Icons -->
        <div class="d-flex align-items-center gap-3">
          <button class="btn btn-link text-light fs-5 p-0">🔍</button>
          <button class="btn btn-link text-light fs-5 p-0">🛒</button>
          <span>
            <router-link
              v-if="!isLoggedIn"
              to="/auth"
              class="fs-5 text-primary text-decoration-none"
              >👤</router-link
            >
            <button
              v-else
              @click="logout"
              class="btn btn-link fs-5 text-danger p-0"
              title="Logout"
            >
              🚪
            </button>
          </span>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const categories = ref([]);
const router = useRouter();
const isLoggedIn = ref(false);

onMounted(async () => {
  try {
    const res = await axios.get("http://localhost:8000/products/categories/");
    categories.value = res.data;
    isLoggedIn.value = !!localStorage.getItem("access_token");
  } catch (error) {
    console.error("Error fetching categories:", error);
  }
});

const logout = () => {
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");
  isLoggedIn.value = false;
  router.push("/auth");
};
</script>

<style scoped>
.mega-menu {
  left: 0;
  right: 0;
  width: 100%;
  border-radius: 12px;
  background-color: #fff;
  color: #333;
}

.mega-menu .dropdown-item {
  color: #333;
  padding: 4px 0;
  font-size: 0.95rem;
}

.mega-menu .dropdown-item:hover {
  color: #0077b6;
  text-decoration: underline;
  background: none;
}

.nav-link {
  color: #ccc !important;
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: #00b4d8 !important;
}

@media (max-width: 992px) {
  .mega-menu {
    position: static !important;
    box-shadow: none !important;
    background-color: #222 !important;
    color: #fff;
  }
  .mega-menu h6 {
    color: #00b4d8 !important;
  }
  .mega-menu .dropdown-item {
    color: #ddd !important;
  }
}


.navbar .fs-5 {
  text-decoration: none !important;
  line-height: 1; 
}

.navbar a,
.navbar router-link {
  text-decoration: none !important;
}

</style>
