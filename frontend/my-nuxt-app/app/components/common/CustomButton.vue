<template>
  <button :class="buttonClasses" :disabled="disabled || loading" @click="$emit('click')">
    <span v-if="loading" class="animate-spin mr-2">
      <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"
        xmlns="http://www.w3.org/2000/svg">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
          d="M4 4v5h.582m0 0A5.002 5.002 0 0112 4v0a5.002 5.002 0 017.418 5H20v-5m-8 8v5m0 0a5.002 5.002 0 01-7.418-5H4v5m8-5h8">
        </path>
      </svg>
    </span>

    <span v-if="icon && !loading" class="mr-2">
      <component :is="icon" />
    </span>

    <span>{{ label }}</span>

    <span v-if="iconRight && !loading" class="ml-2">
      <component :is="iconRight" />
    </span>
  </button>
</template>

<script setup>
import { computed } from 'vue'
import { defineProps, defineEmits } from 'vue'

const props = defineProps({
  label: { type: String, required: true },
  color: { type: String, default: 'blue' },
  size: { type: String, default: 'md' },
  outline: { type: Boolean, default: false },
  disabled: { type: Boolean, default: false },
  loading: { type: Boolean, default: false },
  rounded: { type: Boolean, default: true },
  icon: { type: Object, default: null },
  iconRight: { type: Object, default: null },
})

const emits = defineEmits(['click'])

const buttonClasses = computed(() => {
  const base = 'font-semibold focus:outline-none transition-all flex items-center justify-center'
  const roundedClass = props.rounded ? 'rounded-lg' : 'rounded-sm'

  let sizeClass = ''
  switch (props.size) {
    case 'sm':
      sizeClass = 'px-3 py-1 text-sm'
      break
    case 'lg':
      sizeClass = 'px-6 py-3 text-lg'
      break
    default:
      sizeClass = 'px-4 py-2 text-md'
  }

  const colors = {
    blue: props.outline
      ? 'text-blue-600 border border-blue-600 hover:bg-blue-600 hover:text-white'
      : 'bg-blue-600 text-white hover:bg-blue-700',
    red: props.outline
      ? 'text-red-600 border border-red-600 hover:bg-red-600 hover:text-white'
      : 'bg-red-600 text-white hover:bg-red-700',
    green: props.outline
      ? 'text-green-600 border border-green-600 hover:bg-green-600 hover:text-white'
      : 'bg-green-600 text-white hover:bg-green-700',
    gray: props.outline
      ? 'text-gray-600 border border-gray-600 hover:bg-gray-600 hover:text-white'
      : 'bg-gray-600 text-white hover:bg-gray-700',
  }

  const disabledClass = props.disabled || props.loading ? 'opacity-50 cursor-not-allowed' : ''

  return [base, roundedClass, sizeClass, colors[props.color] || colors.blue, disabledClass].join(' ')
})
</script>
