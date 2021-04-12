<template>
    <v-container fluid>
      <v-row no-gutters>
          <v-col no-gutters cols="6" rows="4">
              <UserInfo></UserInfo>
          </v-col>
          <v-col no-gutters cols="6" rows="4">
              <EventList></EventList>
          </v-col>
      </v-row>
    </v-container>
</template>

<script>
// @ is an alias to /src
import UserInfo from '@/components/UserInfo'
import EventList from '@/components/EventList'

export default {
  name: 'Home',

    components: {
      UserInfo,
      EventList
    },

  data: () => ({
    loggingOut: false,
    appDrawer: false,

  }),

  beforeCreate() {
    if(!this.$session.exists()) {
      this.$router.push('/login', () => {});
    }
  },

  methods: {
    logout() {
      this.$session.destroy();
      this.$router.push('/login', () => {});
    }
  },

}
</script>
