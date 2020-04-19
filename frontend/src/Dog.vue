<template>
    <div>
      <h1> Собакены </h1>
      <div class="container" >
      <div class="block-custom-dog">
        <div class="columns">
          <div class="column col-3" v-for="dog in dogs">
            <div class="card">
              <div class="card-image">
                <img class="img-responsive" :src="` ${dog.photo}`" :alt="`Image of ${dog.id}`">
                <div class="card-header"> {{ dog.breed}}, {{dog.age}} {{ dog.units}}
                <span class="chip"> {{dog.sex }}</span>
                  <div class="card-subtitle text-gray">{{ dog.size}}, {{dog.hair}}
                </div>
                </div>
              </div>
            </div>
          <row></row>
            <br>
        </div>
        </div>
      </div>
      </div>
      <h1> Добавить собаку на витрину</h1>
        <div class="container">
          <div class="columns">
      <div class="column col-4"></div>
      <div class="column col-4">
<div class="form-group">


   <label class="form-label" for="photo">Фото</label>
  <input class="form-input" v-model="photo" type="text" id="photo" placeholder="Вставьте ссылку на фото">

  <label class="form-label" for="age">Возраст</label>
  <input class="form-input" v-model="age" type="number" id="age" placeholder="цифра">

  <label class="form-label" for="units">Единица измерения</label>
  <select v-model="units" id="units" class="form-select">
    <option>г.</option>
    <option>мес.</option>
  </select>

  <label class="form-label" for="sex">Пол</label>
  <select v-model="sex" id="sex" class="form-select">
    <option>М</option>
    <option>Ж</option>
  </select>
  <label class="form-label" for="breed">Порода</label>
  <select v-model="breed" id="breed" class="form-select">
    <option>Метис</option>
    <option>Лабрадор-ретривер</option>
    <option>Йоркширский терьер</option>
    <option>Чихуахуа</option>
    <option>Такса</option>
  <option>Пудель</option>
    <option>Бишон</option>
  </select>
   <label class="form-label" for="hair">Шерсть</label>
  <select v-model="hair" id="hair" class="form-select">
    <option>короткая шерсть</option>
    <option>длинная шерсть</option>
    <option>без шерсти</option>
  </select>
   <label class="form-label" for="size">Размер собаки</label>
  <select v-model="size" id="size" class="form-select">
    <option>Крупного размера</option>
    <option>Среднего размера</option>
    <option>Маленького размера</option>
  </select>

</div>
    <button class="btn btn-primary" @click="addDog" > Добавить </button>
    </div>
          </div>
        </div>
    </div>
</template>

<script>

  import $ from 'jquery'

  export default {
    name: "Dog",
    data() {
      return {
        dogs: '',
        sex: '' ,
        hair: '',
        size: '',
        breed: '',
        age: ' ',
        units: '' ,
        photo: '',
        name: '',
        kennel: '',
      }
    },
    created() {
      $.ajaxSetup({
        headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
      });
      this.loadDogs()
    },
    methods: {
      loadDogs() {
        $.ajax({
          url: "http://127.0.0.1:8000/api/v1/dogs/",
          type: "GET",
          success: (response) => {
            this.dogs = response.data.data
          }
        })
      },
      goKennels() {
        this.$router.push({name: "kennels"})
      },
      addDog(){
        $.ajax({
              url: "http://127.0.0.1:8000/api/v1/dogs/",
              type: "POST",
              data: {
                sex: this.sex,
                hair: this.hair,
                size: this.size,
                breed: this.breed,
                age: this.age,
                units: this.units,
                photo: this.photo,
                name: '',
                kennel: 3,
                _method: 'POST'
              },
              success: (response) => {
                  this.loadDogs()
              },
              error: (response) => {
                  console.log(response)
              }
          })
      },
      }
    }
</script>

<style scoped>
.card{
   /* Цвет фона */
    box-shadow: 0 0 10px rgba(0,0,0,0.1); /* Параметры тени */
   }
.block-custom-dog{
  padding-left: 80px;
    padding-right: 80px;
  }
</style>
