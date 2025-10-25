<template>
  <footer class="footer mt-auto text-white bg-dark">
    <div class="container py-5">
      <div class="row g-4">

        <!-- Brand -->
        <div class="col-md-3">
          <h2 class="brand">Household Appliances</h2>
          <p class="text-light">Your trusted partner in home appliances.</p>
        </div>

        <!-- Quick Links -->
        <div class="col-md-2">
          <h5 class="mb-3">Quick Links</h5>
          <ul class="list-unstyled">
            <li><router-link to="/aboutus" class="link-hover">About Us</router-link></li>
            <li><router-link to="/contactus" class="link-hover">Contact Us</router-link></li>
          </ul>
        </div>

        <!-- Contact -->
        <div class="col-md-3">
          <h5 class="mb-3">Contact</h5>
          <p class="mb-1">📍 123 Blue Street, Tech City</p>
          <p class="mb-1">📞 +1 (800) 123-4567</p>
          <p class="mb-0">📧 support@coolhome.com</p>
        </div>

        <!-- Newsletter -->
        <div class="col-md-4">
          <h5 class="mb-3">Subscribe to Our Newsletter</h5>
          <p class="text-light mb-2">Stay updated with the latest offers and news. Enter your email below:</p>
          <form @submit.prevent="subscribe" class="d-flex flex-wrap gap-2">
            <input v-model="email" type="email" placeholder="Your email address" required class="form-control flex-grow-1" />
            <button type="submit" class="btn btn-gradient">Subscribe</button>
          </form>
        </div>

      </div>


    </div>
  </footer>
</template>

<script>
export default {
  name: 'FooterSection',
  data() {
    return {
      email: '',
    };
  },
  methods: {
    subscribe() {
      alert(`Thank you for subscribing, ${this.email}!`);
      this.email = '';
    },
  },
};
</script>

<style scoped>



.link-hover {
  color: #fff;
  text-decoration: none;
  transition: color 0.3s;
}
.link-hover:hover {
  color: #ffd166;
}

.btn-gradient {
  background: linear-gradient(90deg, #ffd166, #ef476f);
  border: none;
  color: white;
  transition: transform 0.3s, box-shadow 0.3s;
}
.btn-gradient:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.3);
}

.social-icons .icon {
  display: inline-block;
  margin: 0 5px;
  font-size: 1.2rem;
  transition: transform 0.3s;
}
.social-icons .icon:hover {
  transform: scale(1.2);
}



</style>
