<template>
    <section class="about-container">
        <div class="about-content">
        <h1>About Us</h1>
        <p>
            Welcome to <strong>Household Appliances</strong> – your go-to destination for premium home appliances. We are proud to provide top-quality products and outstanding customer service.
        </p>
        <div class="features">
            <div class="feature-box">
            <img src="https://cdn-icons-png.flaticon.com/512/190/190411.png" alt="Quality">
            <h3>Top Quality</h3>
            <p>All of our products are crafted with the highest standards in mind.</p>
            </div>
            <div class="feature-box">
            <img src="https://cdn-icons-png.flaticon.com/512/1524/1524633.png" alt="Support">
            <h3>24/7 Support</h3>
            <p>We’re here for you at any hour, every day of the week.</p>
            </div>
            <div class="feature-box">
            <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" alt="Team">
            <h3>Professional Team</h3>
            <p>Our team is composed of experienced and passionate individuals.</p>
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
    .about-container {
    padding: 3rem 1rem;
    }

    .about-content {
    max-width: 1000px;
    margin: auto;
    text-align: center;
    }

    .about-content h1 {
    font-size: 2.5rem;
    color: #2c3e50;
    margin-bottom: 1rem;
    }

    .about-content p {
    font-size: 1.2rem;
    color: #555;
    margin-bottom: 2rem;
    }

    .features {
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
    justify-content: center;
    }

    .feature-box {
    background-color: #fff;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    padding: 2rem;
    width: 280px;
    transition: transform 0.3s;
    text-align: center;
    }

    .feature-box:hover {
    transform: translateY(-10px);
    }

    .feature-box img {
    width: 60px;
    margin-bottom: 1rem;
    }

    .feature-box h3 {
    font-size: 1.5rem;
    color: #34495e;
    margin-bottom: 0.5rem;
    }

    .feature-box p {
    font-size: 1rem;
    color: #777;
    }

    @media (max-width: 768px) {
        .features {
            flex-direction: column;
            align-items: center;
        }

        .feature-box {
            width: 90%;
        }
    }
</style>
