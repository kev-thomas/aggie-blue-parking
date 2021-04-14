<template>
  <v-container>
    <v-card>
      <v-toolbar
          flat
          color="light-blue"
      >
        <v-toolbar-title class="title white--text pl-0">Events coming up: </v-toolbar-title>
      </v-toolbar>
      <v-card-text>
        <v-list
            two-line
        >
            <v-list-item
              v-for="event in events"
              :key="event.title"
            >
              <v-list-item-avatar>
                <v-icon>mdi-calendar-outline</v-icon>
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title v-text="event.name"></v-list-item-title>
                <v-list-item-subtitle>
                  Event start: {{ event.start }}
                </v-list-item-subtitle>
              </v-list-item-content>
              <v-list-item-action>
                <v-btn icon @click="showEvent(event)">
                  <v-icon>mdi-information-outline</v-icon>
                </v-btn>
              </v-list-item-action>
              <Event
                  v-bind:p-event="selectedEvent"
                  v-bind:show-details="showDetails"
                  @close="showDetails = false"
              >
              </Event>
            </v-list-item>
        </v-list>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import Event from '@/components/Event'
import parking from '../plugins/axios'
export default {
name: "EventList",

  components: {
    Event
  },

  data: () => {
    return {
      showDetails: false,
      focus: '',
      type: 'month',
      types: {
        month: "Month",
        week: "Week",
        day: "Day"
      },
      months: [
          'January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December'
      ],
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
    async getEvents() {
      if(this.$session.exists()) {
        try {
          let newEvents = await parking.get('allevents', {
            headers: {
              Authorization: this.$session.get('user')
            }
          });
          this.events = newEvents.data

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

    showEvent(event) {
      console.log(event)
      this.selectedEvent = event;
      this.showDetails = true;
    },
  }
}
</script>

<style scoped>

</style>