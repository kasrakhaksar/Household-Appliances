<template>
  <nav class="d-lg-none fixed-bottom text-light d-flex justify-content-around align-items-center py-2 shadow nav-custom">
    <router-link 
      to="/" 
      class="text-center text-light nav-item-link"
      :class="{ active: isActive('/') }"
    >
      <span class="fs-5 d-block">🏠</span>
    </router-link>

    <router-link 
      to="/products" 
      class="text-center text-light nav-item-link"
      :class="{ active: isActive('/products') }"
    >
      <span class="fs-5 d-block">🛍️</span>
    </router-link>

    <router-link 
      to="/cart" 
      class="text-center text-light nav-item-link"
      :class="{ active: isActive('/cart') }"
    >
      <span class="fs-5 d-block">🛒</span>
    </router-link>

    <router-link 
      to="/auth" 
      class="text-center text-light nav-item-link"
      :class="{ active: isActive('/auth') }"
    >
      <span class="fs-5 d-block">👤</span>
    </router-link>
  </nav>
</template>

<script>
export default {
  name: 'MobileBottomNav',
  methods: {
    isActive(route) {
      return this.$route.path === route;
    }
  }
};
</script>



<style scoped>



.nav-custom {
  background: linear-gradient(135deg, #182c86, #00695c);
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
  box-shadow: 0 -5px 15px rgba(0,0,0,0.3);
  transition: all 0.3s ease;
}

.nav-item-link {
  flex: 1;
  padding: 8px 0;
  border-radius: 12px;
  transition: all 0.2s ease;
  position: relative;

  text-decoration: none !important;
  line-height: 1; 
}

.nav-item-link span {
  display: block;
  font-size: 1.4rem;
}

.nav-item-link small {
  display: block;
  font-size: 0.7rem;
  font-weight: 500;
}

.nav-item-link:hover {
  background-color: rgba(255, 255, 255, 0.1);
  transform: translateY(-3px);
}

.nav-item-link.active {
  background-color: rgba(255, 255, 255, 0.2);
  box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
}

</style>
