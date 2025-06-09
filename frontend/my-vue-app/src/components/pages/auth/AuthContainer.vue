<template>
    <div class="auth-page">
      <div class="flip-card" :class="{ flipped: !showLogin }">
        <div class="flip-card-inner">
          

          <div class="flip-card-front">
            <div class="left-side login-bg"></div>
            <div class="right-side">
              <div class="form-card">
                <div class="form-header">
                  <span>Don't have an account?</span>
                  <a href="#" @click.prevent="showLogin = false">Sign Up</a>
                </div>
                <LoginForm />
              </div>
            </div>
          </div>
  
          
          <div class="flip-card-back">
            <div class="left-side signup-bg"></div>
            <div class="right-side">
              <div class="form-card">
                <div class="form-header">
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
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
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
    display: flex;
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    backface-visibility: hidden;
  }
  
  .flip-card-front {
    z-index: 2;
    transform: rotateY(0deg);
  }
  
  .flip-card-back {
    transform: rotateY(180deg);
  }
  
  .left-side {
    flex: 1;
    background-size: cover;
    background-position: center;
  }
  
  .left-side.login-bg {
    background-image: url('@/assets/auth/login.jpg');
  }
  
  .left-side.signup-bg {
    background-image: url('@/assets/auth/signup.jpg');
  }
  
  .right-side {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .form-card {
    width: 350px;
    padding: 30px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border-radius: 16px;
  }
  
  .form-header {
    margin-bottom: 20px;
    text-align: right;
  }
  
  .form-header a {
    color: #007bff;
    text-decoration: none;
    margin: 0 5px;
    cursor: pointer;
  }
  
  .form-header a:hover {
    text-decoration: underline;
  }
</style>
  