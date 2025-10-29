<template>
  <section class="py-16 relative bg-gradient-to-b from-slate-900 via-slate-800 to-slate-900 text-white overflow-hidden">

    <!-- Decorative floating circles -->
    <div class="absolute top-[-10%] left-[-10%] w-72 h-72 bg-blue-500/30 rounded-full blur-3xl animate-float-slow"></div>
    <div class="absolute bottom-[-10%] right-[-5%] w-56 h-56 bg-pink-400/20 rounded-full blur-2xl animate-float-slow"></div>

    <div class="container mx-auto px-6 text-center relative z-10">
      <h2 class="text-4xl md:text-5xl font-extrabold text-white mb-12">
        Customer Reviews
      </h2>

      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-10">
        <!-- Review 1 -->
        <div class="relative bg-slate-800 rounded-3xl p-8 shadow-2xl hover:shadow-[0_20px_40px_rgba(59,130,246,0.5)] transition-all duration-500 animate-floating">
          <p class="text-gray-300 mb-4 italic text-lg">
            "Amazing quality and great customer service!"
          </p>
          <h5 class="font-semibold text-blue-400 text-lg">John D.</h5>
        </div>

        <!-- Review 2 -->
        <div class="relative bg-slate-800 rounded-3xl p-8 shadow-2xl hover:shadow-[0_20px_40px_rgba(250,204,21,0.4)] transition-all duration-500 animate-floating">
          <p class="text-gray-300 mb-4 italic text-lg">
            "Fast delivery and reliable products!"
          </p>
          <h5 class="font-semibold text-yellow-400 text-lg">Sarah K.</h5>
        </div>

        <!-- Review 3 -->
        <div class="relative bg-slate-800 rounded-3xl p-8 shadow-2xl hover:shadow-[0_20px_40px_rgba(99,102,241,0.5)] transition-all duration-500 animate-floating">
          <p class="text-gray-300 mb-4 italic text-lg">
            "Highly recommend for modern appliances!"
          </p>
          <h5 class="font-semibold text-indigo-400 text-lg">Michael L.</h5>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'CustomerReviews',
};
</script>

<style scoped>
@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}
.animate-floating {
  animation: float 4s ease-in-out infinite;
}

@keyframes float-slow {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-15px); }
}
.animate-float-slow {
  animation: float-slow 12s ease-in-out infinite;
}
</style>
