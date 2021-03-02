<template>
  <div class="home">

  </div>
</template>

<script>
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
  },

}
</script>
