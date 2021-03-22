<template>
  <v-row class="fill-height">
    <v-col>
      <v-calendar
        ref="calendar"
        v-model="focus"
        color="primary"
        :events="events"
        :type="type"
        @click:event="showEvent"
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
export default {
name: "Events",

  components: {
    Event
  },

  data: () => {
    return {
      showDetails: false,
      focus: '',
      type: 'month',
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
          start: '2021-03-23 12:30',
          end: '2021-03-23 13:30',
        },
        {
          name: 'Test Event 2',
          details: 'This is another event to test my code',
          color: 'red',
          start: '2021-03-23 14:30',
          end: '2021-03-23 16:30',
        },
      ],
    }
  },

  methods: {
    showEvent(event) {
      console.log(event.event)
      this.selectedEvent = event.event;
      this.showDetails = true;
    },
  }
}
</script>

<style scoped>

</style>