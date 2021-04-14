<template>
  <v-card>
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
// import parking from '../plugins/axios'
// import token from '../plugins/jwt.js'
export default {
  name: "CreateSpace",

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
  }
}
</script>

<style scoped>

</style>