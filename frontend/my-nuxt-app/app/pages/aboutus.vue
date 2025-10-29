<template>
  <section class="relative overflow-hidden bg-gradient-to-b from-slate-900 via-slate-800 to-slate-900 text-white py-24">

    <!-- Decorative Glow -->
    <div class="absolute top-0 left-0 w-full h-full bg-[radial-gradient(circle_at_top_left,_rgba(59,130,246,0.15),_transparent_70%)]"></div>

    <!-- Hero Section -->
    <div class="container mx-auto px-6 text-center relative z-10">
      <h1 class="text-6xl font-extrabold mb-6 tracking-tight">
        About <span class="text-blue-400">Us</span>
      </h1>
      <p class="max-w-2xl mx-auto text-gray-300 text-lg leading-relaxed mb-16">
        Welcome to <strong class="text-blue-300">Household Appliances</strong> — where technology meets style.  
        We create innovative, high-quality home appliances designed to elevate your lifestyle and simplify your world.
      </p>
    </div>

    <!-- Feature Cards -->
    <div class="container mx-auto px-6 grid md:grid-cols-3 gap-10 text-center relative z-10">

      <!-- Card 1 -->
      <div class="group relative bg-gradient-to-b from-slate-800 to-slate-900 border border-slate-700 
                  rounded-2xl shadow-lg p-10 hover:-translate-y-3 transition-all duration-300 
                  hover:shadow-[0_0_40px_rgba(56,189,248,0.4)] animate-floating">
        <div class="absolute inset-0 rounded-2xl opacity-0 group-hover:opacity-100 
                    bg-gradient-to-r from-blue-500 via-cyan-400 to-blue-600 blur-xl transition-opacity duration-500 -z-10"></div>
        <div class="bg-gradient-to-tr from-blue-500 to-cyan-400 rounded-full w-20 h-20 
                    flex items-center justify-center mx-auto mb-6 shadow-md">
          <img src="https://cdn-icons-png.flaticon.com/512/190/190411.png" alt="Quality" class="w-10 brightness-200" />
        </div>
        <h3 class="text-2xl font-bold text-white mb-3">Top Quality</h3>
        <p class="text-gray-300 leading-relaxed">
          Crafted with precision and excellence — every product we make is built to last with unmatched durability and performance.
        </p>
      </div>

      <!-- Card 2 -->
      <div class="group relative bg-gradient-to-b from-slate-800 to-slate-900 border border-slate-700 
                  rounded-2xl shadow-lg p-10 hover:-translate-y-3 transition-all duration-300 
                  hover:shadow-[0_0_40px_rgba(250,204,21,0.4)] animate-floating"
           style="animation-delay: 0.5s">
        <div class="absolute inset-0 rounded-2xl opacity-0 group-hover:opacity-100 
                    bg-gradient-to-r from-yellow-400 via-amber-300 to-yellow-500 blur-xl transition-opacity duration-500 -z-10"></div>
        <div class="bg-gradient-to-tr from-yellow-400 to-amber-300 rounded-full w-20 h-20 
                    flex items-center justify-center mx-auto mb-6 shadow-md">
          <img src="https://cdn-icons-png.flaticon.com/512/1524/1524633.png" alt="Support" class="w-10 brightness-150" />
        </div>
        <h3 class="text-2xl font-bold text-white mb-3">24/7 Support</h3>
        <p class="text-gray-300 leading-relaxed">
          We believe service never sleeps. Our expert team is available around the clock to help you with anything, anytime.
        </p>
      </div>

      <!-- Card 3 -->
      <div class="group relative bg-gradient-to-b from-slate-800 to-slate-900 border border-slate-700 
                  rounded-2xl shadow-lg p-10 hover:-translate-y-3 transition-all duration-300 
                  hover:shadow-[0_0_40px_rgba(99,102,241,0.5)] animate-floating"
           style="animation-delay: 1s">
        <div class="absolute inset-0 rounded-2xl opacity-0 group-hover:opacity-100 
                    bg-gradient-to-r from-indigo-500 via-purple-400 to-blue-600 blur-xl transition-opacity duration-500 -z-10"></div>
        <div class="bg-gradient-to-tr from-indigo-500 to-purple-400 rounded-full w-20 h-20 
                    flex items-center justify-center mx-auto mb-6 shadow-md">
          <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" alt="Team" class="w-10 brightness-200" />
        </div>
        <h3 class="text-2xl font-bold text-white mb-3">Professional Team</h3>
        <p class="text-gray-300 leading-relaxed">
          Our passionate and skilled professionals are the driving force behind our success — dedicated to excellence in every detail.
        </p>
      </div>

    </div>

    <!-- Bottom Section -->
    <div class="container mx-auto px-6 mt-24 text-center relative z-10">
      <div class="max-w-3xl mx-auto">
        <h2 class="text-4xl font-bold text-white mb-6">Our Mission</h2>
        <p class="text-gray-300 text-lg leading-relaxed">
          To redefine home living through innovation and design.  
          We aim to empower every household with sustainable, energy-efficient, and beautifully crafted products that make life easier — and smarter.
        </p>
      </div>
    </div>

  </section>
</template>

<script>
export default {
  name: 'AboutUs',
};
</script>

<style scoped>
@keyframes floating {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.animate-floating {
  animation: floating 3.5s ease-in-out infinite;
}
</style>
