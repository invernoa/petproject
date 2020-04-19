<template>
    <div>
       <h1> Питомники и приюты собак </h1>
    <br>
        <div class="container" >

    <div class="columns">

        <div class="column col-2" v-for="kennel in kennels">
          <div class="card" height=400>
             <div class="card-header">
    <div class="card-title ">{{kennel.name  }}</div>
             </div>
            <div class="card-image">
              <img class="img-responsive" :src="` ${kennel.photo}`" :alt="`Image of ${kennel.id}`">
        </div>

      </div>

    </div>
          <row></row>
              <br>
  </div>
</div>
</div>
</template>

<script>

  import $ from 'jquery'

  export default {
      name: "Kennel",
      data() {
            return {
                kennels: '',
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadKennels()
        },
      methods: {
        // Загружаю список
        loadKennels() {
          $.ajax({
            url: "http://127.0.0.1:8000/api/v1/kennels/",
            type: "GET",
            success: (response) => {
              this.kennels = response.data.data
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
    border-radius: 0px;
  }
  .img-responsive{
    border-radius: 0px;
  }
</style>
