<template>
  <section class="d-flex justify-content-center align-items-center min-vh-100 py-5 bg-light">
    <div class="card shadow-sm w-100" style="max-width: 600px;">
      <div class="card-body p-4">
        <h2 class="text-center mb-4">Contact Us 💬</h2>
        <form @submit.prevent="submitForm" class="d-flex flex-column gap-3">
          <div class="mb-3">
            <label class="form-label">Name</label>
            <input
              v-model="form.name"
              type="text"
              placeholder="Your Name"
              required
              class="form-control"
            />
          </div>

          <div class="mb-3">
            <label class="form-label">Email</label>
            <input
              v-model="form.email"
              type="email"
              placeholder="you@example.com"
              required
              class="form-control"
            />
          </div>

          <div class="mb-3">
            <label class="form-label">Message</label>
            <textarea
              v-model="form.message"
              placeholder="Your message..."
              required
              class="form-control"
              rows="5"
            ></textarea>
          </div>

          <button type="submit" class="btn btn-primary w-100">Send Message ✉️</button>
        </form>
      </div>
    </div>
  </section>
</template>

<script setup>
import { reactive } from 'vue'

const form = reactive({
  name: '',
  email: '',
  message: ''
})

function submitForm() {
  alert(`Thank you, ${form.name}! Your message has been sent.`)
  form.name = ''
  form.email = ''
  form.message = ''
}
</script>

<style scoped>
.form-control:focus {
  border-color: #0d6efd;
  box-shadow: 0 0 6px rgba(13, 110, 253, 0.3);
}
</style>