<template>
  <v-row class="fill-height">
    <v-col>
      <v-toolbar flat>
        <v-btn
          outlined
          class="mr-4"
          color="grey darken-2"
          @click="setToday"
        >
          Today
        </v-btn>
        <v-btn
            fab
            text
            small
            color="grey darken-2"
            @click="previous"
        >
          <v-icon small>
            mdi-chevron-left
          </v-icon>
        </v-btn>
        <v-btn
            fab
            text
            small
            color="grey darken-2"
            @click="next"
        >
          <v-icon small>
            mdi-chevron-right
          </v-icon>
        </v-btn>
        <v-toolbar-title v-if="$refs.calendar">
          {{ $refs.calendar.title}}
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-menu
            top
            right
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
                outlined
                color="grey darken-2"
                v-bind="attrs"
                v-on="on"
                id="selector"
            >
              <span>{{ types[type] }}</span>
              <v-icon right>
                mdi-menu-down
              </v-icon>
            </v-btn>
          </template>
          <v-list>
            <v-list-item @click="type = 'day'">
              <v-list-item-title>Day</v-list-item-title>
            </v-list-item>
            <v-list-item @click="type = 'week'">
              <v-list-item-title>Week</v-list-item-title>
            </v-list-item>
            <v-list-item @click="type = 'month'">
              <v-list-item-title>Month</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-toolbar>
      <v-calendar
        ref="calendar"
        v-model="focus"
        color="primary"
        :events="events"
        :type="type"
        @click:event="showEvent"
        @click:date="setDay"
        @click:more="setDay"
        @change="updateRange"
      >
      </v-calendar>
      <Event
          v-bind:p-event="selectedEvent"
          v-bind:show-details="showDetails"
          @close="showDetails = false"
      >
      </Event>
    </v-col>
  </v-row>
</template>

<script>
import Event from '@/components/Event'
import parking from '../plugins/axios'
export default {
name: "Events",

  components: {
    Event
  },

  mounted() {
    this.$refs.calendar.move(0);
    this.$refs.calendar.checkChange();
    this.getEvents();
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

      selectedEvent: {
        name: 'Test Event',
        details: 'This is an event to test my code',
        color: 'blue',
        start: '2021-03-23 12:30',
        end: '2021-03-23 13:30',
      },
      events: [
        {
          name: 'Test Event',
          details: 'This is an event to test my code',
          color: 'blue',
          start: '2021-04-23 12:30',
          end: '2021-04-23 13:30',
        },
        {
          name: 'Test Event 2',
          details: 'This is another event to test my code',
          color: 'red',
          start: '2021-04-23 14:30',
          end: '2021-04-23 16:30',
        },
      ],
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
      console.log(event.event)
      this.selectedEvent = event.event;
      this.showDetails = true;
    },

    setToday() {
      this.focus = ''
    },

    setDay({date}) {
      this.focus = date;
      this.type = 'day';
    },

    previous() {
      this.$refs.calendar.prev()
    },

    next() {
      this.$refs.calendar.next();
    },
    updateRange({start, end}) {
      this.start = start;
      this.end = end;

      let y = this.start.year;
      let m = this.start.month-1;

      this.title = this.months[m] + " " + y;


    }
  }
}
</script>

<style scoped>

</style>