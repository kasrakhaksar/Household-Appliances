<template>
  <section class="py-16 bg-gradient-to-b from-slate-900 via-slate-800 to-slate-900 text-white">
    <div class="container mx-auto px-6 text-center relative z-10">

      <!-- Heading -->
      <h2 class="text-4xl md:text-5xl font-extrabold text-white mb-4">
        Featured Products
      </h2>
      <p class="text-gray-300 mb-12 text-lg md:text-xl">
        Explore our top-rated appliances selected just for you.
      </p>

      <!-- Product Grid -->
      <div >
        <ProductHome class="animate-fade-in" />
      </div>

      <!-- Optional decorative circles -->
      <div class="absolute top-[-10%] left-[-10%] w-72 h-72 bg-blue-500/20 rounded-full blur-3xl animate-float-slow"></div>
      <div class="absolute bottom-[-10%] right-[-5%] w-56 h-56 bg-pink-400/20 rounded-full blur-2xl animate-float-slow"></div>

    </div>
  </section>
</template>

<script>
import ProductHome from './ProductHome.vue';

export default {
  name: 'FeaturedProducts',
  components: { ProductHome },
};
</script>

<style scoped>
@keyframes fade-in {
  0% { opacity: 0; transform: translateY(10px); }
  100% { opacity: 1; transform: translateY(0); }
}
.animate-fade-in {
  animation: fade-in 0.8s ease forwards;
}

@keyframes float-slow {
  0%,100% { transform: translateY(0); }
  50% { transform: translateY(-15px); }
}
.animate-float-slow {
  animation: float-slow 12s ease-in-out infinite;
}
</style>
