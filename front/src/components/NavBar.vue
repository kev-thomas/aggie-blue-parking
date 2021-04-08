<template>
  <v-card>
    <v-navigation-drawer
        app
        absolute
        v-model="appDrawer"
        bottom
        temporary>
      <v-list nav>
        <v-list-item @click="goToDash">Dashboard</v-list-item>
        <v-list-item @click="goToEvents">Events</v-list-item>
        <v-list-item @click="goToAccount">Account</v-list-item>
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
        :src="require('../assets/images/usu-fall.jpg')">
      <v-app-bar-nav-icon
          @click="appDrawer = !appDrawer"
          v-show="this.$session.exists()"
      ></v-app-bar-nav-icon>
      <v-toolbar-title>{{this.title}}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        icon
        @click="login"
        v-show="!this.$session.exists()"
      >
        <v-img
          max-height="40"
          max-width="34"
          :src="require('../assets/images/login.png')">
        </v-img>
      </v-btn>

      <v-btn
          icon
          @click="register"
          v-show="!this.$session.exists()"
      >
        <v-img
          max-height="40"
          max-width="40"
          :src="require('../assets/images/register.png')">
        </v-img>
      </v-btn>
      
      <v-btn icon
           @click="logout"
           v-show="this.$session.exists()">
        <v-icon>mdi-export</v-icon>
      </v-btn>
    </v-app-bar>
  </v-card>

</template>

<script>
export default {
  name: "NavBar",

  data: () => ({
    appDrawer: false,
    loggingOut: false,
  }),

  methods: {
    logout() {
      this.$session.destroy();
      this.$router.push('/login');
    },
    login() {
      this.$router.replace('/login');
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
    goToAccount() {
      this.$router.push('/account');
    }
  }
}
</script>

<style scoped>

</style>