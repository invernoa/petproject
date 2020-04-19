<template>
  <div>
    <div class="container">
      <div class="columns">
        <div class="column col-4"></div>
          <div class="column col-4">
              <div class="form-group">
                <label class="form-label" for="log">Логин</label>
                <input class="form-input"  id="log" v-model="login"  type="text" placeholder="Логин"/>
                <label class="form-label" for="pass">Пароль</label>
              <input  class="form-input"  id="pass" v-model="password" type="password" placeholder="Пароль"/>
            </div>
            <button class="btn" @click="setLogin">Войти</button>
          </div>
      </div>
    </div>
  </div>
</template>

<script>

  import $ from 'jquery'
    export default {
        name: "Login",
      data(){
          return {
            login: '',
            password: '',
          }
      },
      methods: {
          setLogin(){
            $.ajax({
              url: "http://127.0.0.1:8000/auth/token/create/",
              type: "POST",
              data: {
                username: this.login,
                  password:  this.password,
              },
              success: (response) => {
                console.log(response)
                sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
                        this.$router.push({name: "home"})
              },
              error: (response) => {
                if (response.status === 400) {
                  alert("Логин или пароль не верен")
                }
              }
            })

        },
      }
    }
</script>

<style scoped>

</style>
