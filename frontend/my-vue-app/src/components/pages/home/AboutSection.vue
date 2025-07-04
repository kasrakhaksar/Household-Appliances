<template>
  <section class="about-section">
    <div class="about-content">
      <div class="text-content">
        <h2>High-Quality Refrigerators and Washing Machines</h2>
        <div class="decorative-underline"></div>
        <p>
          Discover the latest generation of home appliances designed to make your life easier.
          Our refrigerators and washing machines combine performance, energy efficiency, and a sleek modern look to bring unmatched value to your home.
        </p>
        <ul>
          <li>✅ Energy Efficient Technologies</li>
          <li>✅ Modern Design & Quiet Operation</li>
          <li>✅ Trusted by Thousands of Families</li>
        </ul>
      </div>
      <div class="video-content">
        <video
          width="100%"
          height="auto"
          controls
          :poster="require('@/assets/home_media/poster-video.png')"
        >
          <source :src="require('@/assets/home_media/video.mp4')" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
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
.about-section {
  padding: 3rem 1.5rem;
  border-radius: 12px;
  margin-top: 2rem;
  margin-bottom: 2rem;
}

.about-content {
  display: flex;
  flex-direction: column-reverse;
  gap: 2rem;
}

.text-content h2 {
  font-size: 1.8rem;
  color: #003f88;
}

.text-content p {
  font-size: 1rem;
  line-height: 1.6;
  color: #0a2540;
}

.text-content ul {
  margin-top: 1rem;
  padding-left: 1.2rem;
  color: #003f88;
}

.decorative-underline {
  width: 160px;
  height: 10px;
  margin: 10px 0 20px 0;
  border-radius: 50px;
  background: linear-gradient(90deg, #00b4d8, #d87a07, #023e8a);
  background-size: 200% 100%;
  animation: gradientShift 4s ease infinite;
}

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

.video-content video {
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 63, 136, 0.2);
}

@media (min-width: 768px) {
  .about-content {
    flex-direction: row;
  }
}
</style>
