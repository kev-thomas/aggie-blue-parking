<template>
  <div id="app">
    <navbar></navbar>
    <v-main>
      <v-container fluid>
        <v-app>
          <router-view/>
        </v-app>
      </v-container>
    </v-main>
  </div>
</template>

<script>
export default {
  name: 'Home',

  data: () => ({
    loggingOut: false,
    appDrawer: false,
    title: process.env.VUE_APP_TITLE,

  }),

  beforeCreate() {
    if(!this.$session.exists()) {
      if(this.$router.currentRoute.name !== 'Login')
      this.$router.push('/login');
    }
  },

  methods: {
    login() {
      this.$router.replace('/login');
    },
    logout() {
      this.$router.replace('/logout');
    },
    register() {
      this.$router.replace('/register');
    },
    goToDash() {
      this.$router.push('/');
    },
    goToEvents() {
      this.$router.push('/events');
    },
    goToEventList() {
      this.$router.push('/list');
    },
    goToAccount() {
      this.$router.push('/account');
    }
  },

  components: {
  },

}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
