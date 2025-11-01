<template>
  <section class="relative overflow-hidden py-24 bg-gradient-to-b from-slate-900 via-slate-800 to-slate-900 text-white">

    <div class="absolute top-[-20%] left-[-20%] w-96 h-96 bg-blue-500/30 rounded-full blur-3xl animate-float-slow">
    </div>
    <div class="absolute bottom-[-20%] right-[-10%] w-72 h-72 bg-pink-400/20 rounded-full blur-2xl animate-float-slow">
    </div>

    <div class="container mx-auto px-6 relative z-10 flex flex-col-reverse lg:flex-row items-center gap-12">

      <div class="lg:w-1/2 text-center lg:text-left">
        <h1 class="text-5xl md:text-6xl font-extrabold tracking-tight mb-6 relative inline-block">
          High-Quality <span class="text-blue-400">Refrigerators</span> & <span class="text-pink-400">Washing
            Machines</span>
          <span
            class="absolute inset-0 blur-xl opacity-20 bg-gradient-to-r from-blue-400 via-pink-400 to-blue-600 rounded-lg"></span>
        </h1>

        <div
          class="w-40 h-3 mb-6 rounded-full bg-gradient-to-r from-blue-400 via-pink-400 to-blue-600 bg-[length:200%_100%] animate-gradientShift">
        </div>

        <p class="text-gray-300 mb-6 text-lg md:text-xl">
          Discover the latest generation of home appliances designed to make your life easier.
          Our refrigerators and washing machines combine performance, energy efficiency, and a sleek modern look to
          bring unmatched value to your home.
        </p>

        <ul class="space-y-3 text-blue-400 font-semibold text-lg">
          <li class="flex items-center gap-3">✅ Energy Efficient Technologies</li>
          <li class="flex items-center gap-3">✅ Modern Design & Quiet Operation</li>
          <li class="flex items-center gap-3">✅ Trusted by Thousands of Families</li>
        </ul>
      </div>

      <div class="lg:w-1/2">
        <video
          class="w-full rounded-3xl shadow-2xl ring-4 ring-blue-500/30 hover:ring-pink-400/40 transition-all duration-500"
          controls poster="~/assets/home_media/poster-video.png">
          <source src="~assets/home_media/video.mp4" type="video/mp4" />
        </video>
      </div>

    </div>
  </section>
</template>



<style scoped>
@keyframes gradientShift {
  0% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }

  100% {
    background-position: 0% 50%;
  }
}

.animate-gradientShift {
  animation: gradientShift 4s ease infinite;
}

@keyframes float-slow {

  0%,
  100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-20px);
  }
}

.animate-float-slow {
  animation: float-slow 10s ease-in-out infinite;
}
</style>
