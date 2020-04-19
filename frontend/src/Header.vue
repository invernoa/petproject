<template>
<div>
    <header class="navbar">

  <section class="navbar-section">
    <a href="..." class="btn btn-link"></a>
    <a href="..." class="btn btn-link"></a>
    <a href="..." class="btn btn-link"></a>
   <a href="..." class="navbar-brand mr-2"><h1>Petmi</h1></a>
  </section>
  <section class="navbar-center">
  </section>
  <section class="navbar-section " >
    <button class="btn btn-link" @click="goDogs" >Объявления</button>
    <button class="btn btn-link" @click="goBreeds" >Породы</button>
    <a href="#" class="btn btn-link" @click="goKennels">Питомники</a>
    <button class="btn btn-primary" @click="goAddDog" >Подать объявление</button>
    <button class="btn"  v-if="!auth" @click="goLogin">Вход</button>
    <button class="btn"  v-else @click="logout">Выход</button>
    <a href="..." class="btn btn-link"></a>
    <a href="..." class="btn btn-link"></a>
  </section>

</header>
      <img  width="250" src="../assets/mail.jpeg">
</div>
</template>

<script>

  import Dog from './Dog.vue'
  import Breed from './Breeds.vue'
    import Login from './Login.vue'
  import Kennel from './Kennels.vue'
  import DogsCreate from './DogsCreate'


  export default {
    name: "Header",
    components: {
      Dog,
      Breed,
      Login,
      Kennel
    },
    computed: {
      auth() {
        if (sessionStorage.getItem("auth_token")) {
          return true
        }
      }
    },
    methods: {
      goLogin() {
        this.$router.push({name: "login"})
      },
      logout() {
        sessionStorage.removeItem("auth_token")
        window.location = '/'
      },
      goBreeds(){
        this.$router.push({name: 'breeds'})
      },
      goKennels() {
        this.$router.push({name: 'kennels'})
      },
      goDogs() {
        this.$router.push({name: 'dogs'})
      },

    },
  }
</script>

<style >
  .btn-primary{
    padding-right: 5px;
  }
  .btn btn-primary {
    margin-right: 10px;
  }

</style>
