<template>
 <div class="form-group">
   <label class="form-label">Gender</label>
  <label class="form-radio">
    <input type="radio" name="gender" checked>
    <i class="form-icon"></i> М
  </label>
  <label class="form-radio">
    <input type="radio" name="gender">
    <i class="form-icon"></i> Ж
  </label>
   <label class="form-label" for="name">Порода</label>
   <input class="form-input"  id="name" v-model="login"  type="text" placeholder="Имя"/>
            <label class="form-label" for="breed">Порода</label>
            <input class="form-input"  id="breed" v-model="login"  type="text" placeholder="Порода"/>
            <label class="form-label" for="description">Описание</label>
          <input  class="form-input"  id="description" v-model="password" type="text" placeholder="Описание"/>
        </div>
</template>

<script>
    export default {
        name: "NewDog",
      methods: {
          addObject() {
          $.ajax({
            url: "http://127.0.0.1:8000/api/v1/dogs",
            type: "POST",
            data: {
              name: this.size,
              size: this.size,
              hair: this.hair,
              age: this.age,
              units: this.units,
              breed: this.breed
              sex: this.sex,
              _method: 'POST'
            },
            success: (response) => {
              this.loadDog()
            },
            error: (response) => {
              console.log(response)
            }
          })
        }
      }
    }
</script>

<style scoped>

</style>
