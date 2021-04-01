import Vue from 'vue'
import VueRouter from 'vue-router'
//import views here
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Events from '../views/Events.vue'
import List from '../views/List.vue'
import Account from '../views/Account.vue'

//stuff for checking routes
import {decode} from "jsonwebtoken";

Vue.use(VueRouter)
//add routes here
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    beforeEnter: (to, from, next) => {
      if(from.name === 'Login') {
        next(false)
      }
      else {
        next();
      }
    }
  },
  {
    path: '/logout',
    redirect: '/login',
    beforeEnter: (to, from, next) => {
      Vue.prototype.$session.destroy();
      next();
    }
  },
  {
    path: '/register',
    Name: 'Register',
    component: Register,
  },
  {
    path: '/events',
    name: 'Events',
    component: Events,
    beforeEnter: (to, from, next) => {
      if(Vue.prototype.$session.getAll()) {
        console.log(Vue.prototype.$session.getAll())
        if(decode(Vue.prototype.$session.get('user'))['permissions'] === 1) {
          next();
        }
      }
    }
  },
  {
    path: '/list',
    name: 'List',
    component: List,
  },
  {
    path: '/account',
    name: 'Account',
    component: Account,
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
