<template>
  <div class="form-container">
    <h2 class="form-title">Login</h2>
    <form @submit.prevent="handleLogin" class="form">
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
      <button type="submit" class="btn btn-primary">Login</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const email = ref('')
const password = ref('')

const handleLogin = () => {
  console.log('Logging in with:', email.value, password.value)
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
  border-color: #007bff;
  box-shadow: 0 0 8px rgba(0, 123, 255, 0.3);
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

.btn-primary {
  background-color: #007bff;
  color: #fff;
}

.btn-primary:hover {
  background-color: #0056b3;
}
</style>
