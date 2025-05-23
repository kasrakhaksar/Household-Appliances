<template>



    <HeaderSection/>
    

    <div class="container">
        <ProductHome/>
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
                poster="https://uiparadox.co.uk/templates/powerex/assets/media/about/about-image-1.png"
                >
                <source src="https://uiparadox.co.uk/templates/powerex/assets/media/store.mp4" type="video/mp4" />
                Your browser does not support the video tag.
                </video>
            </div>
            </div>
        </section>
    </div>


    <FooterSection/>
</template>
  

  
<script>

  
    import ProductHome from './ProductHome.vue';
    import HeaderSection from './HeaderSection.vue';
    import FooterSection from './FooterSection.vue';

    export default {
        name: 'App',
        components: {
        ProductHome,
        HeaderSection,
        FooterSection
    }}


</script>
  



<style scoped>
.container {
  background-color: #f0f6fc;
  min-height: 100vh;
  font-family: 'Segoe UI', sans-serif;
  color: #0a2540;
}

.product-card {
  background-color: #ffffff;
  border-radius: 12px;
  padding: 1rem;
  box-shadow: 0 2px 10px rgba(0, 63, 136, 0.1);
  transition: transform 0.2s ease;
}
.product-card:hover {
  transform: scale(1.02);
}

.section-title,
h2 {
  color: #003f88;
  font-weight: bold;
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

.about-section {
  background-color: #e3f2fd;
  padding: 3rem 1.5rem;
  border-radius: 12px;
  margin-top: 2rem;
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

@media (min-width: 768px) {
  .about-content {
    flex-direction: row;
  }
}

.video-content video {
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 63, 136, 0.2);
}

</style>
  