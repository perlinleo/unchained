<template>
  <div id="app">
    <h1> {{timeMessage[0].msg + timeMessage[0].time}} </h1>
    <AddTodo 
      @add-todo="AddTodo"
    />
    <hr>
    <TodoList
      v-bind:todos="todos"
      @remove-todo="removeTodo"
     />
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
import AddTodo from '@/components/AddTodo'
export default {
  name: 'App',
  data(){
    return {
      todos: [
        {id:1 , title: 'listitem1', completed: false},
        {id:2 , title: 'listitem2', completed: false},
        {id:3 , title: 'listitem3', completed: false}
      ],
      timeMessage: [
        {msg: 'Current date: ', time: new Date().toLocaleString()}
      ]
    }
  },
  methods: {
    removeTodo(id){
      this.todos = this.todos.filter(t => t.id !== id)
    },
    AddTodo(todo) {
      this.todos.push(todo)
    }
  },
  components: {
      TodoList, AddTodo
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
