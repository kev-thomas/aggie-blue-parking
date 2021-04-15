<template
    v-bind:userInfo="userInfo"
    v-bind:userRentals="userRentals"
    :key="userInfo.id"
>
    <v-container>
        <v-card>
            <v-img
                height="200px"
                :src="require('../assets/images/night-sky.jpeg')"
            >
                <v-toolbar
                    flat
                    color="rgba(0,0,0,0)"
                >
                    <v-toolbar-title class="title white--text pl-0">Welcome back, {{userInfo.firstName}}!</v-toolbar-title>
                </v-toolbar>
            </v-img>
            <v-card-actions>
                <v-btn
                    text
                    @click="showRentals = !showRentals"
                >
                    Your rentals
                </v-btn>
                <v-btn
                    text
                    @click="goToEvents"
                >
                    Find an event
                </v-btn>
            </v-card-actions>
            <v-card-text v-if="showRentals">
                <v-timeline
                    align-top
                    dense
                >
                    <v-timeline-item
                        v-for="rental in userRentals"
                        :key="rental.streetAddress"
                        :color="rental.color ? rental.color : 'blue'"
                        small
                    >
                        <div>
                            <div class="font-weight-normal"><strong>{{rental.streetAddress}}</strong></div>
                            <div>{{rental.date}}</div>
                        </div>
                    </v-timeline-item>
                </v-timeline>
            </v-card-text>
        </v-card>
    </v-container>
</template>

<script>
    import parking from "@/plugins/axios";

    export default {
        name: "UserInfo",

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