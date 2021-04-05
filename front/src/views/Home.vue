<template>
  <v-row>
      <v-col>
          <UserInfo></UserInfo>
      </v-col>
      <v-col></v-col>
  </v-row>
</template>

<script>
// @ is an alias to /src
import UserInfo from '@/components/UserInfo'

export default {
  name: 'Home',

    components: {
      UserInfo,
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
