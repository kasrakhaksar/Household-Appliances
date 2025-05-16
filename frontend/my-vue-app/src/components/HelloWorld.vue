<template>
    <div class="container">
      <h2>لیست علاقه‌مندی‌ها:</h2>
      <ul>
        <li v-for="(item) in favorites" :key="item">
          {{ item }}
        </li>
      </ul>
    </div>

    <UserCard name="رضا" :age="27" job="مدیر محصول" />
  </template>
  

  <script>

    import UserCard from './UserCard.vue'

    export default {
    components: {
        UserCard
    },

    
    data() {
        return {
        favorites: ['موسیقی', 'برنامه‌نویسی', 'کتاب', 'ورزش']
        }
    }
    }


  </script>



  



  <style scoped>
  .container {
    padding: 20px;
  }
  ul {
    list-style: none;
    padding: 0;
  }
  li {
    background: #eee;
    margin-bottom: 8px;
    padding: 10px;
    border-radius: 5px;
  }
  </style>
  