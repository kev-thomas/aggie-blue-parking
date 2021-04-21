<template>
    <v-container fluid>
      <v-row v-if="!!user" no-gutters>
          <v-col no-gutters cols="6" rows="4">
              <UserInfo
                  v-bind:user-info="user"
                  v-bind:user-rentals="rentals"
              >
              </UserInfo>
          </v-col>
          <v-col no-gutters cols="6" rows="4">
              <EventList></EventList>
          </v-col>
          <v-col no-gutters cols="3" rows="4">
              <Money
                  v-bind:user-info="user"
              >
              </Money>
          </v-col>
          <v-col no-gutters cols="3" rows="4">
              <OwnerInfo>
              </OwnerInfo>
          </v-col>
      </v-row>
    </v-container>
</template>

<script>
// @ is an alias to /src
import UserInfo from '@/components/UserInfo'
import EventList from '@/components/EventList'
import Money from '@/components/Money'
import OwnerInfo from '@/components/OwnerInfo';
import parking from "@/plugins/axios";


export default {
  name: 'Home',

    components: {
      UserInfo,
      EventList,
      Money,
      OwnerInfo,
    },

  data: () => ({
    loggingOut: false,
    appDrawer: false,
    user: null,
    rentals: null,
  }),

  beforeCreate() {
    if(!this.$session.exists()) {
      this.$router.push('/login', () => {});
    }
  },
  mounted() {
    this.getUser()
  },

  methods: {
    logout() {
      this.$session.destroy();
      this.$router.push('/login', () => {});
    },
    async getUser() {
      if(this.$session.exists()) {
        try {
          let response = await parking.get('getUserDetail', {
            headers: {
              Authorization: this.$session.get('user')
            }
          });
          this.person = response.data;
        }
        catch(error) {
          console.log('wtf')
          console.log(error)
        }
      }
      console.log(this.person)
      if(!this.person.ERROR) {
        this.$session.set('user-details', this.person);
        await this.$router.push('/', () => {})
      }
      this.user = this.person.user
      this.rentals = this.person.rentals
    }
  },

}
</script>
