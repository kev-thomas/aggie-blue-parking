<template>
  <v-card>
    <!-- Rform for register -->
    <v-form ref="Rform">
      <v-card-title>Create a new account</v-card-title>
      <v-card-text>
        <v-text-field
          v-model="user['firstname']"
          label="Firstname"
          required
        ></v-text-field>

        <v-text-field
          v-model="user['lastname']"
          label="Lastname"
          required
        ></v-text-field>
      </v-card-text>
      <v-card-text>
        <v-text-field
          v-model="user['username']"
          label="Username"
          :rules="usernameRules"
          required
        ></v-text-field>

        <v-text-field
          v-model="user['email']"
          label="Email"
          :rules="emailRules"
          required
        ></v-text-field>

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
        @click="register"
        :loading="loading"
      >Create account</v-btn>
    </v-form>
  </v-card>
</template>

<script>
  import parking from '../plugins/axios'
  export default {
    name: "Register",

    data: () => ({
      // !Why does this fail if user is changed??!
      user: {
        firstname: '',
        lastname: '',
        username: '',
        email: '',
        password: '',
        renter: 'True',
        owner: 'False',
      },
      person: null,
      valid: true,
      loading: false,
      showPassword: false,
    }),

    methods: {
      async register() {
        try {
              let response = await parking.post('register', this.user);
              // this.person = response.data;
              
              if(response.data == "OK") {
                await this.$router.push('/login', () => {})
              }
              else {
                window.alert("There has been an error with registering your account, please try again at another time.");
              }
            }
        catch(error) {
          console.log(error);
        }
      }
    }
  }
</script>
