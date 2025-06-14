<template>
  <footer class="site-footer">
    <div class="footer-top">
      <div class="footer-brand">
        <h2>Household Appliances 🏠</h2>
        <p>Your trusted partner in home appliances.</p>
      </div>

      <div class="footer-links">
        <h3>Quick Links</h3>
        <ul>
          <li><router-link to="/aboutus">About Us</router-link></li>
          <li><router-link to="/contactus">Contact Us</router-link></li>
        </ul>
      </div>

      <div class="footer-contact">
        <h3>Contact</h3>
        <p>📍 123 Blue Street, Tech City</p>
        <p>📞 +1 (800) 123-4567</p>
        <p>📧 support@coolhome.com</p>
      </div>



      <div class="footer-newsletter">
        <h3>Subscribe to Our Newsletter</h3>
        <p>Stay updated with the latest offers and news. Enter your email below:</p>
        <form @submit.prevent="subscribe">
          <input v-model="email" type="email" placeholder="Your email address" required />
          <button type="submit">Subscribe</button>
        </form>
      </div>
    </div>

    <div class="footer-bottom">
      <p>© 2025 CoolHome Inc. All rights reserved.</p>
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
.site-footer {
  background-color: #003f88;
  color: #ffffff;
  padding: 3rem 1.5rem 2rem;
}

.footer-top {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.footer-brand h2 {
  font-size: 1.8rem;
  color: #ffffff;
}

.footer-brand p {
  margin-top: 0.5rem;
  color: #cfe4ff;
}

.footer-links h3,
.footer-contact h3,
.footer-social h3,
.footer-newsletter h3 {
  margin-bottom: 1rem;
  font-size: 1.2rem;
  color: #cbe2ff;
}

.footer-links ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer-links li {
  margin-bottom: 0.5rem;
}

.footer-links a {
  color: #ffffff;
  text-decoration: none;
  transition: color 0.2s ease;
}

.footer-links a:hover {
  color: #00b4d8;
}

.footer-contact p {
  margin: 0.3rem 0;
  color: #cfe4ff;
}

.footer-social .icons {
  display: flex;
  gap: 1rem;
}

.footer-social a {
  color: #ffffff;
  font-size: 1.3rem;
  transition: color 0.2s ease;
}

.footer-social a:hover {
  color: #00b4d8;
}

.footer-newsletter p {
  color: #cfe4ff;
  margin-bottom: 1rem;
}

.footer-newsletter form {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.footer-newsletter input {
  padding: 0.8rem;
  border-radius: 5px;
  border: none;
  width: 250px;
}

.footer-newsletter button {
  background: #00b4d8;
  color: #fff;
  padding: 0.8rem 1.5rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.footer-newsletter button:hover {
  background: #0090b3;
}

.footer-bottom {
  text-align: center;
  padding-top: 2rem;
  border-top: 1px solid #285ec7;
  margin-top: 2rem;
  font-size: 0.9rem;
  color: #cfe4ff;
}

@media (max-width: 768px) {
  .footer-top {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
