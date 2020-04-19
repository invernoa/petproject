<template xmlns="http://www.w3.org/1999/html">
    <div>
      <Breed></Breed>
    <br>
      <Dog></Dog>

    </div>
</template>

<script>

  import Dog from './Dog.vue'
  import Breed from './Breeds.vue'

  export default {
    name: "Home",
    components: {
      Dog,
      Breed

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
      }

    },
  }
</script>

<style scoped>

</style>
