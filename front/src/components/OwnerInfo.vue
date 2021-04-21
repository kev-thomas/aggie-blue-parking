<template>
  <v-container>
    <v-card>
      <v-btn 
        block
        color="primary"
        @click="goToCreateSpot"
      >
        Create a spot
      </v-btn>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "OwnerInfo",
  
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
          goToCreateSpot() {
            this.$router.push('/createspot', () => {});
          }
  },
}
</script>

<style scoped>

</style>