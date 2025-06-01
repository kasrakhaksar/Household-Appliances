import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/pages/home/HomePage.vue'
import AboutUs from '../components/pages/aboutus/AboutUs.vue'
import ContactUs from '../components/pages/contactus/ContactUs.vue'


const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/aboutus', name: 'AboutUs', component: AboutUs },
  { path: '/contactus', name: 'ContactUs', component: ContactUs },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
