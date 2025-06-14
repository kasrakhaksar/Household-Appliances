<template>
  <FeaturedProducts />
  <SpecialOffers />
  <AboutSection />
  <TrustedBrands />
  <CustomerReviews />
  <LatestBlogPosts />
</template>



<script>
  import FeaturedProducts from './FeaturedProducts.vue';
  import SpecialOffers from './SpecialOffers.vue';
  import AboutSection from './AboutSection.vue';
  import TrustedBrands from './TrustedBrands.vue';
  import CustomerReviews from './CustomerReviews.vue';
  import LatestBlogPosts from './LatestBlogPosts.vue';

  export default {
    name: 'HomePage',
    components: {
      FeaturedProducts,
      SpecialOffers,
      AboutSection,
      TrustedBrands,
      CustomerReviews,
      LatestBlogPosts,
    },
  };
</script>

