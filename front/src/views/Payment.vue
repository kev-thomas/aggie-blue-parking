<template>
  <v-card>
    <v-form ref="Pform">
      <v-card-title>Payment Information</v-card-title>
      <v-card-text>
        <v-text-field
          v-model="payment['fullName']"
          label="Full name"
          required
        ></v-text-field>

        <v-text-field
          v-model="payment['ccNumber']"
          label="Credit card number"
          required
        ></v-text-field>
        <v-text-field
          v-model="payment['exprDate']"
          label="Expiration date"
          required
        ></v-text-field>

        <v-text-field
          v-model="payment['secCode']"
          label="Security code"
          required
        ></v-text-field>
        <v-text-field
          v-model="payment['amount']"
          label="$ Amount"
          required
        ></v-text-field>
      </v-card-text>
      <v-btn
        :disabled="!valid && loading"
        @click="pay"
        :loading="loading"
      >Add money</v-btn>
    </v-form>
  </v-card> 
</template>

<script>
// import parking from '../plugins/axios'
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
    payment: {
      fullName: '',
      ccNumber: '',
      exprDate: '',
      secCode: '',
      amount: '',
    },
    person: null,
    valid: true,
    loading: false,
    showPassword: false,
  }),

  methods: {
    async pay() {
      console.log("WIP");
    //   try {
    //         let response = await parking.post('register', this.user);
    //         // this.person = response.data;
    //         console.log(response.data);
    //       }
    //       catch(error) {
    //         console.log('OHNO');
    //         console.log(error);
    //       }
    }
  }
}
</script>
