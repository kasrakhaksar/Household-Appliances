<template>
  <div class="todo-app">
    <h2>لیست کارها</h2>

    <input type="text" v-model="newTask" placeholder="کار جدید..." />
    <button @click="addTask">افزودن</button>

    <ul>
      <li v-for="(task, index) in tasks" :key="index">
        {{ task }}
        <button @click="removeTask(index)">حذف</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newTask: '',
      tasks: []
    }
  },
  methods: {
    addTask() {
      const trimmed = this.newTask.trim()
      if (trimmed) {
        this.tasks.push(trimmed)
        this.newTask = ''
      }
    },
    removeTask(index) {
      this.tasks.splice(index, 1)
    }
  }
}
</script>

<style scoped>
.todo-app {
  padding: 20px;
  max-width: 400px;
  margin: auto;
}
input {
  padding: 8px;
  width: 70%;
}
button {
  padding: 8px;
  margin: 5px;
}
li {
  margin: 8px 0;
  background: #f0f0f0;
  padding: 10px;
  border-radius: 5px;
}
</style>
