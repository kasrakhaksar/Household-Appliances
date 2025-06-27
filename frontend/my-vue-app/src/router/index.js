import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/pages/home/HomePage.vue'
import AboutUs from '../components/pages/aboutus/AboutUs.vue'
import ContactUs from '../components/pages/contactus/ContactUs.vue'
import AuthContainer from '../components/pages/auth/AuthContainer.vue'
import ProductDetail from '../components/pages/product/ProductDetail.vue';

const routes = [
  { path: '/', name: 'Home', component: Home, meta: { layout: 'default' } },
  { path: '/aboutus', name: 'AboutUs', component: AboutUs, meta: { layout: 'default' } },
  { path: '/contactus', name: 'ContactUs', component: ContactUs, meta: { layout: 'default' } },
  { path: '/auth', name: 'AuthContainer', component: AuthContainer, meta: { layout: 'auth' } },
  { path: '/product/:id', name: 'ProductDetail', component: ProductDetail , meta: { layout: 'default' }},
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
