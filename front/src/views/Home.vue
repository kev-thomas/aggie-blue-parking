<template>
  <div class="home">
    <event-list></event-list>
  </div>
</template>

<script>
import EventList from '../components/EventList.vue';
// @ is an alias to /src

export default {
  name: 'Home',

  data: () => ({
    loggingOut: false,
    appDrawer: false,

  }),

  beforeCreate() {
    if(!this.$session.exists()) {
      this.$router.push('/login');
    }
  },

  methods: {
    logout() {
      this.$session.destroy();
      this.$router.push('/login');
    }
  },

  components: {
    EventList
  },

}
</script>
