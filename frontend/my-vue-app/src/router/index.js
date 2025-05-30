import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/pages/home/HomePage.vue'
import AboutUs from '../components/pages/aboutus/AboutUs.vue'


const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/aboutus', name: 'AboutUs', component: AboutUs }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
