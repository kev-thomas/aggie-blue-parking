<template>
  <v-card>
    HOWDY
  </v-card>
  
</template>

<script>
import parking from '../plugins/axios'
export default {
  name: "Payment",

  data: () => ({
    // !Why does this fail if user is changed??!
    user: {
      firstname: '',
      lastname: '',
      username: '',
      email: '',
      password: '',
      renter: 'true',
      owner: 'false',
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
            console.log(response.data);
          }
          catch(error) {
            console.log('OHNO');
            console.log(error);
          }
    }
  }
}
</script>
