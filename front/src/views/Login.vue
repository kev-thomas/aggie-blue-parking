<template>
  <v-card>
    <v-form ref="form">
    <v-card-title>Login</v-card-title>
    <v-card-text>
      <v-text-field
          v-model="user['name']"
          label="Username"
          :rules="usernameRules"
          required
      ></v-text-field>
    </v-card-text>
    <v-card-text>
      <v-text-field
          :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
          :type="showPassword ? 'text' : 'password'"
          @click:append="showPassword = !showPassword"
          v-model="user['password']"
          label="Password"
          :rules="passwordRules"
          required
      ></v-text-field>
    </v-card-text>
    <v-btn
        :disabled="!valid && loading"
        @click="login"
        :loading="loading"
    >Login</v-btn>
    </v-form>
  </v-card>
</template>

<script>
import parking from '../plugins/axios'
export default {
  name: "Login",

  data: () => ({
    user: {
      name: '',
      password: ''
    },
    person: null,
    valid: true,
    loading: false,
    showPassword: false,
  }),

  methods: {
    async login() {
      if(this.$refs.form.validate()) {
        this.loading = true
        console.log(`posting to ${parking.defaults.baseURL}`)
        if(this.user) {
          let response = await parking({
            method: 'POST',
            url: 'http://localhost:8000/login',
            data: this.user
          })
          this.person = response.data
        }
        console.log(this.person)
        if(!this.person.ERROR) {
          this.$session.start();
          this.$session.set('user', this.person);
          console.log(this.person)
          this.$router.push('/')
        }
      }
      else {
        this.valid = false
      }
    }
  }
}
</script>

<style scoped>

</style>