<template
  v-bind:userInfo="userInfo"
>
  <v-container>
    <v-card>
      ${{ userInfo.money }} left in your account
      <v-divider
        vertical
      ></v-divider>
      <v-btn 
        block
        color="primary"
        @click="goToAddPayment"
      >
        Add money
      </v-btn>
    </v-card>
  </v-container>
</template>

<script>
    // import parking from "@/plugins/axios";

    export default {
        name: "Money",

        props: {
          userInfo: {
            default: null
          },
        },

        // mounted() {
        //   this.getUserData()
        // },

        // data: () => {
        //     return {
        //         showRentals: false,
        //     }
        // },

        methods: {
          goToAddPayment() {
            this.$router.push('/payment', () => {});
          }
        }
    }
</script>

<style scoped>

</style>