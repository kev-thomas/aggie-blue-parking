<template
    v-bind:pEvent="pEvent"
    v-bind:showDetails="showDetails"
    :key="pEvent.streetAddress"
>
  <v-dialog
    v-model="showDialog"
    max-width="900"
  >
    <v-card color="grey lighten-4"
            flat
    >
      <v-toolbar :color="pEvent.color" dark>
        <v-toolbar-title v-html="pEvent.name">
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon>
          <v-icon>mdi-heart</v-icon>
        </v-btn>
      </v-toolbar>
      <v-card-text>
        <span v-html="pEvent.details"></span>
        <iframe
          width="800"
          height="400"
          style="border: 0;"
          :src="mapsQuery"
        >
        </iframe>
      </v-card-text>
      <v-card-actions>
        <v-btn
          text
          color="secondary"
          @click="showDialog = false"
          >
          Close
        </v-btn>
        <v-btn
            text
            color="secondary"
            @click="rentSpace()"
        >
          Rent a space
        </v-btn>
      </v-card-actions>
      <Rent v-bind:pEvent="pEvent"
            v-bind:showRent="showRent"
            @close="showRent = false"
      >
      </Rent>
    </v-card>
  </v-dialog>
</template>

<script>
import Rent from '@/components/Rent'
export default {
name: "Event",

  components: {
    Rent
  },

  props: {
    pEvent: Object,
    showDetails: {
      type: Boolean,
      default: false
    }
  },

  data: () => {
    return {
      mapsUrl: 'https://www.google.com/maps/embed/v1/place?key=AIzaSyDxSFPq0nxltyh3jq0xhfqgzzuT1LPL6aI&q=',
      showRent: false,
    }
  },

  watch: {
    showDialog: function(value) {
      if(value) {
        this.mapsQuery =  this.pEvent["streetAddress"].replaceAll(' ', '+') + ',' +
            this.pEvent["city"] + ",UT,84321&zoom=14&center=41.7420,-111.8230";
      }
    }
  },

  computed: {
    showDialog: {
      get() {
        return this.showDetails;
      },
      set(value) {
        this.$emit('close', value)
      }
    },
    mapsQuery: {
      get() {
        return this.mapsUrl;
      },
      set(value) {
        this.mapsUrl = 'https://www.google.com/maps/embed/v1/place?key=AIzaSyDxSFPq0nxltyh3jq0xhfqgzzuT1LPL6aI&q=' + value;
        console.log(this.mapsUrl)
      }
    },
  },

  methods: {
    rentSpace() {
      this.showRent = !this.showRent;
    },
  }
}
</script>

<style scoped>

</style>