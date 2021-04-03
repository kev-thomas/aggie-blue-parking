<template>
  <v-card>
    <!-- Can the ref be Lform for login? -->
    <v-form ref="form">
    <v-card-title>Login</v-card-title>
    <v-card-text>
      <v-text-field
          v-model="user['username']"
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
      username: '',
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
          try {
            let response = await parking.post('login', this.user);
            this.person = response.data;
          }
          catch(error) {
            console.log('wtf')
            console.log(error)
          }

        }
        console.log(this.person)
        if(!this.person.ERROR) {
          this.$session.start();
          this.$session.set('user', this.person.token);
          console.log(this.person)
          await this.$router.push('/', () => {})
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