import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import session from './plugins/session'
import token from './plugins/jwt'
import parking from './plugins/axios'
import EventList from './components/EventList'

Vue.component('app-message', EventList)

//MIXINS
import rules from './mixins/rules'

Vue.mixin(rules)

Vue.config.productionTip = false
Vue.use(session)

new Vue({
  vuetify,
  router,
  session,
  token,
  parking,
  render: h => h(App)
}).$mount('#app')
