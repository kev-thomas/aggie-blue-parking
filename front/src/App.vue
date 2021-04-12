<template>
  <div id="app">
    <v-navigation-drawer
        app
        bottom
        v-model="appDrawer"
    >
      <v-list nav>
        <v-list-item @click="goToHome">
          <v-list-item-avatar>
            <v-icon>
              mdi-view-dashboard
            </v-icon>
          </v-list-item-avatar>
          Dashboard
        </v-list-item>
        <v-list-item @click="goToEvents"><v-list-item-avatar>
          <v-icon>
            mdi-calendar
          </v-icon>
        </v-list-item-avatar>
          Events</v-list-item>
        <v-list-item @click="goToAccount">
          <v-list-item-avatar>
            <v-icon>
              mdi-account
            </v-icon>
          </v-list-item-avatar>
          Account</v-list-item>
        <v-list-item bottom>
          <v-btn
              @click="logout"
              :loading="loggingOut"
              v-show="loggedIn()"
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
          v-show="loggedIn()"
      ></v-app-bar-nav-icon>
      <v-toolbar-title class="title black--text pl-0">Aggie Blue Parking</v-toolbar-title>
      <v-spacer></v-spacer>

      <div v-show="!loggedIn()">
        <v-tooltip bottom>
          <template slot="activator" slot-scope="{ on }">
            <v-btn
                icon
                @click="register"
                v-on="on"
            >
              <v-icon>mdi-account-plus-outline</v-icon>
            </v-btn>
          </template>
          <span>Register</span>
        </v-tooltip>
      </div>

      <div v-show="!loggedIn()">
        <v-tooltip bottom>
          <template slot="activator" slot-scope="{ on }">
            <v-btn
                icon
                @click="login"
                v-on="on"
            >
              <v-icon>mdi-account-arrow-left-outline</v-icon>
            </v-btn>
          </template>
          <span>Login</span>
        </v-tooltip>
      </div>


      <div v-show="loggedIn()">
        <v-tooltip bottom>
          <template slot="activator" slot-scope="{ on }">
            <v-btn
                icon
                @click="logout"
                v-on="on"
            >
              <v-icon>mdi-home-export-outline</v-icon>
            </v-btn>
          </template>
          <span>Logout</span>
        </v-tooltip>
      </div>

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
    else {
      this.$router.replace('/', () => {});
    }
  },

  methods: {
    login() {
      this.$router.replace('/login', () => {});
    },
    logout() {
      this.appDrawer = false;
      this.$session.destroy();
      this.$router.replace('/logout', () => {});
    },
    register() {
      this.$router.replace('/register', () => {});
    },
    goToEvents() {
      this.$router.push('/events', () => {});
    },
    goToHome() {
      this.$router.push('/', () => {});
    },
    goToAccount() {
      this.$router.push('/account', () => {});
    },
    loggedIn() {
      return this.$session.exists();
    }
  },

  components: {
  },

}
</script>

<style lang="scss">
#app {
  font-family: Roboto, sans-serif;
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
