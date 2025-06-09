<template>
  <div class="form-container">
    <h2 class="form-title">Sign Up</h2>
    <form @submit.prevent="handleSignup" class="form">
      <input
        type="text"
        placeholder="Name"
        v-model="name"
        required
        class="input-field"
      />
      <input
        type="email"
        placeholder="Email"
        v-model="email"
        required
        class="input-field"
      />
      <input
        type="password"
        placeholder="Password"
        v-model="password"
        required
        class="input-field"
      />
      <button type="submit" class="btn btn-success">Sign Up</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const name = ref('')
const email = ref('')
const password = ref('')

const handleSignup = () => {
  console.log('Signing up with:', name.value, email.value, password.value)
}
</script>

<style scoped>
.form-container {
  max-width: 360px;
  margin: 40px auto;
  padding: 30px 25px;
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.form-title {
  margin-bottom: 25px;
  font-weight: 700;
  font-size: 1.8rem;
  color: #222;
  text-align: center;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.input-field {
  padding: 12px 14px;
  font-size: 1rem;
  border-radius: 10px;
  border: 1.5px solid #ccc;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
  outline: none;
}

.input-field:focus {
  border-color: #28a745;
  box-shadow: 0 0 8px rgba(40, 167, 69, 0.3);
}

.btn {
  padding: 12px 0;
  border-radius: 10px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.25s ease;
  border: none;
}

.btn-success {
  background-color: #28a745;
  color: #fff;
}

.btn-success:hover {
  background-color: #1e7e34;
}
</style>
