<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const message = ref('Carregando...');
onMounted(() => {
  axios.get('http://127.0.0.1:8000')
    .then(response => {
      message.value = response.data.message;
    })
    .catch(error => {
      console.error("Houve um erro!", error);
      message.value = 'Erro ao conectar com o backend.';
    });
});
</script>

<template>
  <div id="app-container">
    <h1>{{ message }}</h1>
  </div>
</template>

<style>
#app-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  font-family: sans-serif;
  background-color: #2c3e50;
  color: #ffffff;
}
</style>