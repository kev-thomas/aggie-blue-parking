<template>
  <div id="app">
    <v-navigation-drawer
        app
        absolute
        v-model="appDrawer"
        bottom
        temporary>
      <v-list nav>
        <v-list-item>Dashboard</v-list-item>
        <v-list-item @click="goToEvents">Events</v-list-item>
        <v-list-item>Account</v-list-item>
        <v-list-item bottom>
          <v-btn
              @click="logout"
              :loading="loggingOut"
              v-show="this.$session.exists()"
          >Log out</v-btn>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
        app
        prominent
        :src="require('./assets/images/usu-fall.jpg')">
      <v-app-bar-nav-icon
          @click="appDrawer = !appDrawer"
          v-show="this.$session.exists()"
      ></v-app-bar-nav-icon>
      <v-toolbar-title>{{this.title}}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon
           @click="logout"
           v-show="this.$session.exists()">
        <v-icon>mdi-export</v-icon>
      </v-btn>
    </v-app-bar>
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
    logout() {
      this.$router.replace('/logout');
    },
    goToEvents() {
      this.$router.push('/events');
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
