<template
    v-bind:pEvent="pEvent"
    v-bind:showRent="showRent"
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
        <v-list
            two-line
        >
          <v-list-item
              v-for="space in parking.available_spots"
              :key="space.id"
          >
            <v-list-item-avatar>
              <v-icon>mdi-parking</v-icon>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title v-text="space.address"></v-list-item-title>
              <v-list-item-subtitle>
                Price: {{ space.price }}
              </v-list-item-subtitle>
            </v-list-item-content>
            <v-list-item-action>
              <v-tooltip left>
                <template slot="activator" slot-scope="{ on }">
                  <v-btn
                      icon
                      @click="rentThisSpace(space.id)"
                      v-on="on"
                  >
                    <v-icon>mdi-currency-usd</v-icon>
                  </v-btn>
                </template>
                <span>Rent this space!</span>
              </v-tooltip>
            </v-list-item-action>
          </v-list-item>
        </v-list>

      </v-card-text>
      <v-card-actions>
        <v-btn
            text
            color="secondary"
            @click="showDialog = false"
        >
          Close
        </v-btn>
      </v-card-actions>
      <v-alert
          :value="alert"
          type="success"
          dismissible
          transition="scale-transition"
      >
        Success!
      </v-alert>
    </v-card>
  </v-dialog>
</template>

<script>
import parking from "@/plugins/axios";

export default {
  name: "Rent",

  props: {
    pEvent: Object,
    showRent: {
      type: Boolean,
      default: false
    }
  },

  data: () => {
    return {
      mapsUrl: 'https://www.google.com/maps/embed/v1/place?key=AIzaSyDxSFPq0nxltyh3jq0xhfqgzzuT1LPL6aI&q=',
      parking: {
        'available_spots': null,
      },
      alert: false,
    }
  },

  methods: {
    async getParkingForEvent() {
      if(this.$session.exists()) {
        try {
          let newParking = await parking.get(`event/${this.pEvent.id}`, {
            headers: {
              Authorization: this.$session.get('user')
            }
          });
          this.parking = newParking.data

        }
        catch(error) {
          console.error(error)
          console.log('sum ting wong');
        }
      }
      else {
        await this.$router.push('/login');
      }
    },

    async rentThisSpace(spaceId) {
      if(this.$session.exists()) {
        let response;
        try {
          let rentalData = {
            "eventId": this.pEvent.id,
            "spotId": spaceId,
            "userId": this.$session.get('user-details').user.id
          }
          let rentedSpace = await parking.post('makeRental', rentalData, {
            headers: {
              Authorization: this.$session.get('user')
            }
          });
          response = rentedSpace.data;
        }
        catch(error) {
          console.error(error)
          console.log('sum ting wong');
        }
        if(response.message === "success") {
          this.alert = true;
        }
      }
      else {
        await this.$router.push('/login');
      }
    },
  },

  watch: {
    showDialog: function(value) {
      if(value) {
        this.mapsQuery =  this.pEvent["streetAddress"].replaceAll(' ', '+') + ',' +
            this.pEvent["city"] + ",UT,84321&zoom=14&center=41.7420,-111.8230";
        this.getParkingForEvent();
      }
    }
  },

  computed: {
    showDialog: {
      get() {
        return this.showRent;
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
  }
}
</script>

<style scoped>

</style>