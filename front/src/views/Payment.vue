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
          v-model="payment['money']"
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
import parking from '../plugins/axios'
export default {
  name: "Payment",

  data: () => ({
    payment: {
      // fullName: '',
      // ccNumber: '',
      // exprDate: '',
      // secCode: '',
      money: '',
    },
    person: null,
    valid: true,
    loading: false,
    showPassword: false,
  }),

  methods: {
    async pay() {
      console.log("WIP");
      try {
          if(this.$session.exists()) {
            let newSpot = await parking.post('addMoney', this.payment, {
              headers: {
                Authorization: this.$session.get('user')
              }
            });

            if(newSpot.data == "OK") {
              await this.$router.push('/', () => {})
            }
          }
        }
        catch(error) {
          console.log(error);
        }
    }
  }
}
</script>
