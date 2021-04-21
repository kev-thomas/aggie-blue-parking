<template>
  <v-card>
    <!-- Rform for register -->
    <v-form ref="Cform">
      <v-card-title>Register a new parking spot</v-card-title>
      <v-card-text>
        <v-text-field
          v-model="newParkingSpot['streetAddress']"
          label="Address"
          required
        ></v-text-field>

        <v-text-field
          v-model="newParkingSpot['city']"
          label="City"
          required
        ></v-text-field>
      </v-card-text>
      <v-card-text>
        <v-text-field
          v-model="newParkingSpot['zip']"
          label="Zipcode"
          required
        ></v-text-field>

        <v-text-field
          v-model="newParkingSpot['price']"
          label="Rental price"
          required
        ></v-text-field>
      </v-card-text>
      <v-btn
        :disabled="!valid && loading"
        @click="createSpot"
        :loading="loading"
      >Register parking spot</v-btn>
    </v-form>
  </v-card>
</template>

<script>
  import parking from '../plugins/axios'
  export default {
    name: "CreateSpot",

    data: () => ({
      newParkingSpot: {
        streetAddress: '',
        city: '',
        zip: '',
        price: '',
      },
      person: null,
      valid: true,
      loading: false,
      showPassword: false,
    }),

    methods: {
      async createSpot() {
        console.log("TEST");

        try {
          if(this.$session.exists()) {
            let newSpot = await parking.post('createParking', this.newParkingSpot, {
              headers: {
                Authorization: this.$session.get('user')
              }
            });

            console.log(newSpot.data);
          }
        }
        catch(error) {
          console.log(error);
        }
      },
    }
  }
</script>
