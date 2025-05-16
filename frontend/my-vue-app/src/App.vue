<template>
  <div class="container">

    <UserCard/>

  </div>
</template>



<script>
import UserCard from './components/UserCard.vue'

export default {
    name: 'App',
    components: {
      UserCard
    }}
</script>

<style scoped>
.container {
  padding: 20px;
}
</style>
