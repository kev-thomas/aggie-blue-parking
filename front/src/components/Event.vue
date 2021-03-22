<template
    v-bind:pEvent="pEvent"
    v-bind:showDetails="showDetails"
>
  <v-dialog
    v-model="showDialog"
  >
    <v-card>
      <v-toolbar :color="pEvent.color">
        <v-toolbar-title>
          <span class="headline">{{pEvent.name}}</span>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon>
          <v-icon>mdi-heart</v-icon>
        </v-btn>
      </v-toolbar>
      <v-card-text>
        <span class="v-event">{{pEvent.details}}</span>
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
            @click="showDialog = false"
        >
          Rent a space
        </v-btn>

      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
name: "Event",

  props: {
    pEvent: Object,
    showDetails: {
      type: Boolean,
      default: false
    }
  },

  data: () => {
    return {
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
    }
  }
}
</script>

<style scoped>

</style>