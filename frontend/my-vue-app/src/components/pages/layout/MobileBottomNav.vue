<template>
    <nav class="mobile-bottom-nav">
      <router-link to="/" class="nav-item">
        <span>🏠</span>
        <small>Home</small>
      </router-link>
      <router-link to="/products" class="nav-item">
        <span>🛍️</span>
        <small>Shop</small>
      </router-link>
      <router-link to="/cart" class="nav-item">
        <span>🛒</span>
        <small>Cart</small>
      </router-link>
      <router-link to="/auth" class="nav-item">
        <span>👤</span>
        <small>Account</small>
      </router-link>
    </nav>
  </template>
  
  <script>
  export default {
    name: 'MobileBottomNav',
  };
  </script>
  
<style scoped>



  .mobile-bottom-nav {
    display: none;
  }
  
  @media (max-width: 768px) {
    .mobile-bottom-nav {
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      background: #003f88;
      color: white;
      display: flex;
      justify-content: space-around;
      padding: 0.5rem 0;
      box-shadow: 0 -2px 8px rgba(0,0,0,0.2);
      z-index: 1000;
    }
  
    .nav-item {
      color: #cbe4ff;
      text-decoration: none;
      text-align: center;
      font-size: 1rem;
    }
  
    .nav-item small {
      display: block;
      font-size: 0.75rem;
    }
  
    .nav-item:hover {
      color: #00b4d8;
    }
  }


  </style>
  