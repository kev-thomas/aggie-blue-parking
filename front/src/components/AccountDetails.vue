<template
    v-bind:userInfo="userInfo"
    v-bind:userRentals="userRentals"
    :key="userInfo.id"
>
  <v-container>
    <v-card>
      <v-toolbar
          flat
          color="primary"
      >
        <v-toolbar-title class="title white--text pl-0">Account Details</v-toolbar-title>
        <v-spacer/>
        <v-subheader class="subtitle white--text pl-0">Contact your administrator for assistance.</v-subheader>
      </v-toolbar>
      <v-card-text>
        <v-list>
          <v-list-item>
            <v-list-item-title>Email: </v-list-item-title>
            <v-list-item-subtitle>{{userInfo.email}}</v-list-item-subtitle>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>Username: </v-list-item-title>
            <v-list-item-subtitle>{{userInfo.username}}</v-list-item-subtitle>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>Account Balance: </v-list-item-title>
            <v-list-item-subtitle>${{userInfo.money}}</v-list-item-subtitle>
          </v-list-item>
        </v-list>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import parking from "@/plugins/axios";

export default {
  name: "AccountDetails",

  props: {
    userInfo: {
      default: null
    },
    userRentals: {
      default: null
    },
  },

  mounted() {
    this.getRentals()
  },

  data: () => {
    return {
      // userRentals: [
      //     {
      //         name: 'Test Event',
      //         details: 'This is an event to test my code',
      //         color: 'blue',
      //         start: '2021-03-23 12:30',
      //         end: '2021-03-23 13:30',
      //     },
      //     {
      //         name: 'Test Event 2',
      //         details: 'This is another event to test my code',
      //         color: 'red',
      //         start: '2021-03-23 14:30',
      //         end: '2021-03-23 16:30',
      //     },
      // ],
      showRentals: false,
    }
  },

  methods: {
    async getRentals() {
      if(this.$session.exists()) {
        try {
          let newRentals = await parking.get('rentals', {
            headers: {
              Authorization: this.$session.get('user')
            }
          });
          this.rentals = newRentals.data

        }
        catch(error) {
          console.error(error)
          console.log('sum ting wong');
        }
      }
      else {
        this.$router.push('/login');
      }
    },
    goToEvents() {
      this.$router.push('/events', () => {});
    },
  }
}
</script>

<style scoped>

</style>