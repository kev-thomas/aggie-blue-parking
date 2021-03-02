import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import session from './plugins/session'

//MIXINS
import rules from './mixins/rules'

Vue.mixin(rules)

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  session,
  render: h => h(App)
}).$mount('#app')
