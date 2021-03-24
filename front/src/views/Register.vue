<template>
  <v-card>
    <!-- Rform for register -->
    <v-form ref="Rform">
      <v-card-title>AHOY, YEE WANNA REGISTER DO YEE</v-card-title>
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
    >Login</v-btn>
    </v-form>
  </v-card>
</template>

<script>
// import parking from '../plugins/axios'
export default {
  name: "Register",

  data: () => ({
    // !Why does this fail if user is changed??!
    user: {
      firstname: '',
      lastname: '',
      username: '',
      email: '',
      password: ''
    },
    person: null,
    valid: true,
    loading: false,
    showPassword: false,
  }),

  methods: {
    async register() {
      console.log("HOWDY PIRATE");
    }
  }
}
</script>

<!--
// if(this.$refs.form.validate()) {
//         this.loading = true
//         console.log(`posting to ${parking.defaults.baseURL}`)
//         if(this.user) {
//           try {
//             let response = await parking.post('login', this.user);
//             this.person = response.data;
//           }
//           catch(error) {
//             console.log('wtf')
//             console.log(error)
//           }

//         }
//         console.log(this.person)
//         if(!this.person.ERROR) {
//           this.$session.start();
//           this.$session.set('user', this.person.token);
//           console.log(this.person)
//           await this.$router.push('/')
//         }
//       }
//       else {
//         this.valid = false
//       }
-->
