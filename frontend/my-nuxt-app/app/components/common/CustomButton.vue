<template>
  <button
    :class="[
      'inline-flex items-center justify-center font-medium rounded-xl transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed',
      sizeClasses,
      variantClasses,
      { 'cursor-wait': loading }
    ]"
    :disabled="disabled || loading"
    @click="$emit('click')"
  >
    <!-- Loading spinner -->
    <svg
      v-if="loading"
      class="animate-spin -ml-1 mr-2 h-5 w-5 text-current"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
    >
      <circle
        class="opacity-25"
        cx="12"
        cy="12"
        r="10"
        stroke="currentColor"
        stroke-width="4"
      ></circle>
      <path
        class="opacity-75"
        fill="currentColor"
        d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"
      ></path>
    </svg>

    <!-- Default slot for button text/content -->
    <slot />
  </button>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  variant: {
    type: String,
    default: 'primary', // 'primary', 'secondary', 'outline', 'danger', etc.
  },
  size: {
    type: String,
    default: 'md', // 'sm', 'md', 'lg'
  },
  loading: {
    type: Boolean,
    default: false,
  },
  disabled: {
    type: Boolean,
    default: false,
  },
})

const variantClasses = computed(() => {
  switch (props.variant) {
    case 'brand':
      return 'bg-brand-600 text-white hover:bg-brand-700 focus:ring-brand-400'
    case 'accent':
      return 'bg-accent-500 text-white hover:bg-accent-600 focus:ring-accent-300'
    case 'outline':
      return 'border border-border text-text hover:bg-brand-50'
    default:
      return 'bg-surface text-text'
  }
})

const sizeClasses = computed(() => {
  switch (props.size) {
    case 'sm':
      return 'px-3 py-1.5 text-sm'
    case 'lg':
      return 'px-6 py-3 text-lg'
    default:
      return 'px-4 py-2 text-base'
  }
})
</script>
