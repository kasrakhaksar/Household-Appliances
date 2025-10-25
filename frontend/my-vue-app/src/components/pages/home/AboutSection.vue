<template>
  <section class="py-5">
    <div class="container">
      <div class="row align-items-center g-4">
        
        <div class="col-md-6 order-md-1 order-2">
          <h2 class="text-primary">High-Quality Refrigerators and Washing Machines</h2>
          <div class="decorative-underline mb-3"></div>
          <p class="text-secondary">
            Discover the latest generation of home appliances designed to make your life easier.
            Our refrigerators and washing machines combine performance, energy efficiency, and a sleek modern look to bring unmatched value to your home.
          </p>
          <ul class="text-primary">
            <li>✅ Energy Efficient Technologies</li>
            <li>✅ Modern Design & Quiet Operation</li>
            <li>✅ Trusted by Thousands of Families</li>
          </ul>
        </div>

        <div class="col-md-6 order-md-2 order-1">
          <video
            class="w-100 rounded shadow-sm"
            controls
            :poster="require('@/assets/home_media/poster-video.png')"
          >
            <source :src="require('@/assets/home_media/video.mp4')" type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'AboutSection',
};
</script>

<style scoped>
.decorative-underline {
  width: 160px;
  height: 10px;
  margin-bottom: 20px;
  border-radius: 50px;
  background: linear-gradient(90deg, #00b4d8, #d87a07, #023e8a);
  background-size: 200% 100%;
  animation: gradientShift 4s ease infinite;
}

@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
</style>
