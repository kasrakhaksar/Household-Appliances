<template>
  <section class="py-5 bg-light">
    <div class="container text-center">
      <h1 class="mb-4 text-primary">About Us</h1>
      <p class="mb-5 fs-5 text-muted">
        Welcome to <strong>Household Appliances</strong> – your go-to destination for premium home appliances. 
        We are proud to provide top-quality products and outstanding customer service.
      </p>
      <div class="row g-4 justify-content-center">
        <!-- Feature 1 -->
        <div class="col-md-4">
          <div class="card h-100 border-0 shadow-sm text-center p-4 hover-card">
            <img src="https://cdn-icons-png.flaticon.com/512/190/190411.png" class="card-img-top mx-auto mb-3" alt="Quality" style="width: 60px;">
            <div class="card-body">
              <h5 class="card-title text-dark">Top Quality</h5>
              <p class="card-text text-muted">All of our products are crafted with the highest standards in mind.</p>
            </div>
          </div>
        </div>
        <!-- Feature 2 -->
        <div class="col-md-4">
          <div class="card h-100 border-0 shadow-sm text-center p-4 hover-card">
            <img src="https://cdn-icons-png.flaticon.com/512/1524/1524633.png" class="card-img-top mx-auto mb-3" alt="Support" style="width: 60px;">
            <div class="card-body">
              <h5 class="card-title text-dark">24/7 Support</h5>
              <p class="card-text text-muted">We’re here for you at any hour, every day of the week.</p>
            </div>
          </div>
        </div>
        <!-- Feature 3 -->
        <div class="col-md-4">
          <div class="card h-100 border-0 shadow-sm text-center p-4 hover-card">
            <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" class="card-img-top mx-auto mb-3" alt="Team" style="width: 60px;">
            <div class="card-body">
              <h5 class="card-title text-dark">Professional Team</h5>
              <p class="card-text text-muted">Our team is composed of experienced and passionate individuals.</p>
            </div>
          </div>
        </div>
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
.hover-card {
  transition: transform 0.3s;
}

.hover-card:hover {
  transform: translateY(-10px);
}
</style>
