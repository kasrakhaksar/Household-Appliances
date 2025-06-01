<template>
    <section class="contact-container">
      <div class="form-wrapper">
        <h2>Contact Us 💬</h2>
  
        <form @submit.prevent="submitForm">
          <label>
            Name
            <input v-model="form.name" type="text" placeholder="Your Name" required />
          </label>
  
          <label>
            Email
            <input v-model="form.email" type="email" placeholder="you@example.com" required />
          </label>
  
          <label>
            Message
            <textarea v-model="form.message" placeholder="Your message..." required></textarea>
          </label>
  
          <button type="submit">Send Message ✉️</button>
        </form>
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
  .contact-container {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 2rem;
  }
  
  .form-wrapper {
    background: white;
    padding: 2.5rem;
    border-radius: 20px;
    max-width: 600px;
    width: 100%;
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
  }
  
  .form-wrapper h2 {
    margin-bottom: 1.5rem;
    text-align: center;
    font-size: 2rem;
    color: #333;
  }
  
  form {
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
  }
  
  label {
    font-size: 0.95rem;
    color: #444;
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
  }
  
  input,
  textarea {
    padding: 0.8rem 1rem;
    border: 1px solid #ccc;
    border-radius: 10px;
    font-size: 1rem;
    transition: border 0.3s, box-shadow 0.3s;
  }
  
  input:focus,
  textarea:focus {
    outline: none;
    border-color: #003f88;
    box-shadow: 0 0 0 3px #003f88;
  }
  
  textarea {
    resize: vertical;
    min-height: 120px;
  }
  
  button {
    background-color: #009be8;
    color: white;
    padding: 0.9rem;
    font-size: 1.1rem;
    font-weight: bold;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    transition: background 0.3s;
  }
  
  button:hover {
    background-color: #003f88;
  }
</style>
  