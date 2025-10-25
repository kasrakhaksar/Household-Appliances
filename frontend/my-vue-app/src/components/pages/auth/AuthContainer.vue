<template>
  <div class="auth-page d-flex justify-content-center align-items-center vh-100">
    <div class="flip-card" :class="{ flipped: !showLogin }">
      <div class="flip-card-inner">

        <!-- Login Side -->
        <div class="flip-card-front row g-0">
          <div class="col-md-6 login-bg"></div>
          <div class="col-md-6 d-flex justify-content-center align-items-center">
            <div class="card p-4 shadow form-card">
              <div class="form-header text-end mb-3">
                <span>Don't have an account?</span>
                <a href="#" @click.prevent="showLogin = false">Sign Up</a>
              </div>
              <LoginForm />
            </div>
          </div>
        </div>

        <!-- Signup Side -->
        <div class="flip-card-back row g-0">
          <div class="col-md-6 signup-bg"></div>
          <div class="col-md-6 d-flex justify-content-center align-items-center">
            <div class="card p-4 shadow form-card">
              <div class="form-header text-end mb-3">
                <span>Already have an account?</span>
                <a href="#" @click.prevent="showLogin = true">Login</a>
              </div>
              <SignupForm />
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import LoginForm from './LoginForm.vue'
import SignupForm from './SignupForm.vue'

const showLogin = ref(true)
</script>

<style scoped>
.auth-page {
  perspective: 1500px;
}

.flip-card {
  width: 80%;
  max-width: 1000px;
  height: 600px;
  position: relative;
  transform-style: preserve-3d;
  transition: transform 1s;
}

.flip-card.flipped {
  transform: rotateY(180deg);
}

.flip-card-inner {
  width: 100%;
  height: 100%;
  position: absolute;
  transform-style: preserve-3d;
}

.flip-card-front,
.flip-card-back {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  backface-visibility: hidden;
  display: flex;
}

.flip-card-front {
  transform: rotateY(0deg);
  z-index: 2;
}

.flip-card-back {
  transform: rotateY(180deg);
}

.login-bg, .signup-bg {
  flex: 1;
  background-size: cover;
  background-position: center;
}

.login-bg {
  background-image: url('@/assets/auth/login.jpg');
}

.signup-bg {
  background-image: url('@/assets/auth/signup.jpg');
}

.form-card {
  width: 100%;
  max-width: 350px;
  backdrop-filter: blur(10px);
  border-radius: 16px;
}

.form-header a {
  color: #0d6efd;
  text-decoration: none;
  margin-left: 5px;
}

.form-header a:hover {
  text-decoration: underline;
}
</style>
