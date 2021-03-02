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
import router from '../router'
export default {
  name: "Login",

  data: () => ({
    user: {
      name: '',
      password: ''
    },
    valid: true,
    loading: false,
    showPassword: false,
  }),

  methods: {
    login() {
      if(this.$refs.form.validate()) {
        this.loading = true
        if(this.user) {
          this.$session.start();
          this.$session.set('user', this.user);
          router.push('/')
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