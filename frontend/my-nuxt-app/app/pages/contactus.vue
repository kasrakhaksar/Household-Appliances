<template>
    <section class="flex justify-center items-center min-h-screen py-12 
                  bg-gradient-to-b from-slate-900 via-slate-800 to-slate-900 text-white">
        <div class="bg-slate-800 rounded-3xl shadow-2xl w-full max-w-lg p-8 relative">

            <h2 class="text-3xl font-bold text-white mb-6 text-center">Contact Us 💬</h2>

            <form @submit.prevent="submitForm" class="space-y-5">

                <div class="relative">
                    <input v-model="form.email" type="email" placeholder=" " required
                        class="peer w-full px-4 py-3 border border-gray-600 rounded-xl
                   focus:border-blue-400 focus:ring-2 focus:ring-blue-300 focus:outline-none transition bg-slate-700 text-white" />
                    <label
                        class="absolute left-4 top-3 text-gray-400 text-sm transition-all
                   peer-placeholder-shown:top-3 peer-placeholder-shown:text-gray-400 peer-placeholder-shown:text-base
                   peer-focus:top-0.5 peer-focus:text-xs peer-focus:text-blue-300
                   peer-[&:not(:placeholder-shown)]:top-0.5 peer-[&:not(:placeholder-shown)]:text-xs peer-[&:not(:placeholder-shown)]:text-blue-300">
                        Email
                    </label>
                </div>

                <div class="relative">
                    <input v-model="form.subject" type="text" placeholder=" " required
                        class="peer w-full px-4 py-3 border border-gray-600 rounded-xl 
                   focus:border-blue-400 focus:ring-2 focus:ring-blue-300 focus:outline-none transition bg-slate-700 text-white" />
                    <label
                        class="absolute left-4 top-3 text-gray-400 text-sm transition-all
                   peer-placeholder-shown:top-3 peer-placeholder-shown:text-gray-400 peer-placeholder-shown:text-base
                   peer-focus:top-0.5 peer-focus:text-xs peer-focus:text-blue-300
                   peer-[&:not(:placeholder-shown)]:top-0.5 peer-[&:not(:placeholder-shown)]:text-xs peer-[&:not(:placeholder-shown)]:text-blue-300">
                        Subject
                    </label>
                </div>

                <div class="relative">
                    <textarea v-model="form.message" placeholder=" " required rows="5"
                        class="peer w-full px-4 py-3 border border-gray-600 rounded-xl 
                   focus:border-blue-400 focus:ring-2 focus:ring-blue-300 focus:outline-none transition resize-none bg-slate-700 text-white"></textarea>
                    <label
                        class="absolute left-4 top-3 text-gray-400 text-sm transition-all
                   peer-placeholder-shown:top-3 peer-placeholder-shown:text-gray-400 peer-placeholder-shown:text-base
                   peer-focus:top-0.5 peer-focus:text-xs peer-focus:text-blue-300
                   peer-[&:not(:placeholder-shown)]:top-0.5 peer-[&:not(:placeholder-shown)]:text-xs peer-[&:not(:placeholder-shown)]:text-blue-300">
                        Message
                    </label>
                </div>

                <CustomButton :label="'Send Message ✉️'" color="blue" size="md" :loading="loading" class="w-full"
                    @click="submitForm" />
            </form>
        </div>
    </section>
</template>



<script setup lang="ts">
import { reactive, ref } from 'vue'
import CustomButton from '@/components/common/CustomButton.vue'

interface ContactForm {
    email: string
    subject: string
    message: string
}

const form = reactive < ContactForm > ({
    email: '',
    subject: '',
    message: ''
})

const loading = ref < boolean > (false)

function submitForm(): void {
    loading.value = true
    setTimeout(() => {
        alert(`Thank you! Your message has been sent.`)
        form.email = ''
        form.subject = ''
        form.message = ''
        loading.value = false
    }, 1500)
}
</script>
