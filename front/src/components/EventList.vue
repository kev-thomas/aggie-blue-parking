// Vue.component('EventList', {
//   data: function() {
//     return {

//     }
//   }
// });

// new Vue({
//   el: '#app',
//   data
// })

<template>
  <v-card
    class="mx-auto"
    max-width="300"
    align-content="flex-start"
    outlined
  >
    <v-list dense>
      <v-subheader>Events coming up</v-subheader>
      <v-list-item-group
        v-model="selectedItem"
        color="primary"
      >
        <v-list-item
          v-for="(event, i) in events"
          :key="i"
        >
          <v-list-item-content>
            <v-list-item-title v-text="event.name"></v-list-item-title>
            <v-list-item-subtitle>
              Event start: {{ event.start }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-card>
  <!-- <v-card>
    <v-list>
      <v-list-item v-for="event in events" :key="event">
        <v-card>
          <h3 class="title">{{ event.name }}</h3>
        </v-card>
      </v-list-item> -->
 



    
    <!-- </v-list> -->
  <!-- </v-card> -->
</template>

<script>
// import Event from '@/components/Event'
import parking from '../plugins/axios'
export default {
name: "EventList",

  // components: {
  //   Event
  // },

  data: () => {
    return {
      events: [
        {
          name: 'Day on the Quad',
          details: 'This is an event to test my code',
          color: 'blue',
          start: '2021-03-23 12:30',
          end: '2021-03-23 13:30',
        },
        {
          name: 'Free Aggie ice cream',
          details: 'This is another event to test my code',
          color: 'red',
          start: '2021-03-23 14:30',
          end: '2021-03-23 16:30',
        },
      ],
      selectedEvent: {
        name: '',
        details: '',
        color: '',
        start: '',
        end: '',
      },
    }
  },

  methods: {
    // async getEvents() {
    //   if(this.$session.exists()) {
    //     try {
    //       this.events = await parking.get('allevents', {
    //         headers: {
    //           Authorization: this.$session.get('user')
    //         }
    //       }).events;
    //     }
    //     catch(error) {
    //       console.error('OHNO');
    //     }
    //   }
    //   else {
    //     this.$router.push('/login');
    //   }
    // },
  }
}
</script>

<style scoped>

</style>