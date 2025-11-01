<template>
    <transition name="fade">
        <div v-if="isOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"
            @click.self="closeModal">
            <transition name="scale">
                <div v-if="isOpen" class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl max-w-lg w-full p-6 relative">
                    <button @click="closeModal"
                        class="absolute top-4 right-4 text-gray-500 hover:text-gray-700 dark:hover:text-gray-300 transition">
                        ✕
                    </button>

                    <div>
                        <slot name="header">
                            <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-100">Modal Title</h2>
                        </slot>

                        <slot name="body">
                            <p class="mt-2 text-gray-600 dark:text-gray-300">
                                This is the default modal content.
                            </p>
                        </slot>

                        <slot name="footer" class="mt-4 flex justify-end gap-2">
                            <button @click="closeModal"
                                class="px-4 py-2 bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-200 rounded hover:bg-gray-300 dark:hover:bg-gray-600 transition">
                                Close
                            </button>
                        </slot>
                    </div>
                </div>
            </transition>
        </div>
    </transition>
</template>

<script setup>
import { ref, defineExpose } from 'vue'

const isOpen = ref(false)

function openModal() {
    isOpen.value = true
}

function closeModal() {
    isOpen.value = false
}

defineExpose({
    openModal,
    closeModal
})
</script>

<style>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.25s;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}

.scale-enter-active {
    transition: transform 0.25s, opacity 0.25s;
}

.scale-enter-from {
    transform: scale(0.95);
    opacity: 0;
}

.scale-leave-to {
    transform: scale(0.95);
    opacity: 0;
}
</style>
