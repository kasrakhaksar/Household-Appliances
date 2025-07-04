<template>
  <header class="navbar">
    <div class="navbar__logo"><router-link to="/">Household Appliances</router-link></div>
    <nav class="navbar__menu">
      <ul>
        <li class="has-mega">
          Products
          <div class="mega-menu" v-if="categories.length">
            <div
              class="mega-column"
              v-for="(category, index) in categories"
              :key="index"
            >
              <h4>{{ category.label }}</h4>
              <ul>
                <li><a href="#">View All</a></li>
                <li><a href="#">Best Sellers</a></li>
                <li><a href="#">New Arrivals</a></li>
              </ul>
            </div>
          </div>
          <div v-else class="mega-menu">
            <p>Loading categories...</p>
          </div>
        </li>
        <li><router-link to="/" class="nav-link">Home</router-link></li>
        <li><router-link to="/aboutus" class="nav-link">About Us</router-link></li>
        <li><router-link to="/contactus" class="nav-link">Contact Us</router-link></li>
      </ul>
    </nav>
    <div class="navbar__icons">
      <span class="icon">🔍</span>
      <span class="icon">🛒</span>
      <span>
        <router-link v-if="!isLoggedIn" to="/auth" class="icon">👤</router-link>
        <a v-else @click="logout" class="icon logout-btn">🚪</a>
      </span>
    </div>
  </header>
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



.navbar {
  border-bottom: 1px solid #669fef;
  display: flex;
  justify-content: space-between;
  padding: 1rem 2rem;
  position: relative;
  align-items: center;
  direction: ltr;
}


.navbar__logo {
  font-size: 1.7rem;
  font-weight: bold;
  color: #003f88;
  animation: blinkSoft 2.5s ease-in-out infinite;

}

.navbar__logo a {
  text-decoration: none;
  color: inherit; 
}


@keyframes blinkSoft {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.7;
  }
}


.navbar__menu ul {
  list-style: none;
  display: flex;
  gap: 2rem;
  margin: 0;
  padding: 0;
}

.navbar__menu li {
  position: relative;
  cursor: pointer;
  font-weight: 500;
  transition: color 0.3s ease;
}

.navbar__menu li a {
  text-decoration: none;
  color: #0a2540;
  font-size: 1rem;
}

.navbar__menu li a:hover {
  color: #0077b6;
}

.navbar__menu li:hover > .mega-menu {
  display: flex;
}

.mega-menu {
  display: none;
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  background: #ffffff;
  box-shadow: 0 10px 24px rgba(0, 63, 136, 0.15);
  padding: 2rem;
  max-width: 1000px;
  width: 90vw;
  justify-content: space-between;
  z-index: 1000;
  border-radius: 10px;
  gap: 2rem;
  flex-wrap: wrap;
  border-top: 4px solid #0077b6;
}

.mega-column {
  flex: 1 1 200px;
  min-width: 180px;
}

.mega-column h4 {
  margin-bottom: 0.8rem;
  font-size: 1.1rem;
  color: #0077b6;
  border-bottom: 2px solid #cce3ff;
  padding-bottom: 4px;
}

.mega-column ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.mega-column li {
  margin-bottom: 0.5rem;
}

.mega-column li a {
  color: #0a2540;
  text-decoration: none;
  transition: 0.2s;
}

.mega-column li a:hover {
  color: #003f88;
}

.navbar__icons {
  display: flex;
  gap: 1rem;
  font-size: 1.3rem;
  color: #003f88;
}

.icon {
  cursor: pointer;
  transition: transform 0.2s ease, color 0.2s ease;
}

.icon:hover {
  transform: scale(1.2);
  color: #0077b6;
}

@media (max-width: 768px) {
  .navbar__menu ul {
    flex-direction: column;
    gap: 1rem;
    background-color: #ffffff;
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    padding: 1rem;
    display: none;
    box-shadow: 0 8px 16px rgba(0, 63, 136, 0.1);
  }

  .navbar__menu ul.show {
    display: flex;
  }

  .mega-menu {
    flex-direction: column;
    width: 90vw;
    overflow-x: auto;
    max-height: 60vh;
    gap: 1rem;
  }

  .navbar__icons {
    margin-left: 1rem;
  }


  .logout-btn {
    background: none;
    border: none;
    cursor: pointer;
    font-size: 1.2rem;
  }
}
</style>
