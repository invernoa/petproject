<template>
    <div>
       <h1> Породы </h1>
        <div class="container" >
          <div class="block-custom-dog">
            <div class="columns">
                <div class="column col-2" v-for="breed in breeds">
                  <div class="card" height=400>
                     <div class="card-header">
                        <div class="card-title ">{{breed.name  }}</div>
                      </div>
                      <div class="card-image">
                        <img class="img-responsive" :src="` ${breed.photo}`" :alt="`Image of ${breed.id}`">
                      </div>
                  </div>
              </div>
              <row></row>
            </div>
          </div>
        </div>
    </div>
</template>

<script>

  import $ from 'jquery'

  export default {
      name: "Breed",
      data() {
            return {
                breeds: '',
            }
        },
      created() {
          $.ajaxSetup({
              headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
          });
          this.loadBreeds()
      },
    computed: {
      auth() {
        if (sessionStorage.getItem("auth_token")) {
          return true
            }
        }
    },
      methods: {
        // Загружаю список
        loadBreeds() {
          $.ajax({
            url: "http://127.0.0.1:8000/api/v1/breeds/",
            type: "GET",
            success: (response) => {
              this.breeds = response.data.data
            }
          })
        },
      },
    }
</script>

<style scoped>
.card{
   /* Цвет фона */
    box-shadow: 0 0 10px rgba(0,0,0,0.05);
  padding: 0px;
  border-radius: 0px;
  border-color: white;
   },
  .card-image{
    border-radius: 25px;
  }
  .img-responsive{
    border-radius: 25px;
  }
  .block-custom-dog{
  padding-left: 20px;
    padding-right: 20px;
  }
  .container{
    padding-top: 10px;
    padding-bottom: 70px;
  }
</style>
