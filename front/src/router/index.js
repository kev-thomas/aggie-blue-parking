import Vue from 'vue'
import VueRouter from 'vue-router'

// Used for checking routes
import {decode} from "jsonwebtoken";

Vue.use(VueRouter)
//add routes here
const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import(/* webpackChunkName: home */ '../views/Home')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import(/* webpackChunkName: login */ '../views/Login'),
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
    component: () => import(/* webpackChunkName: register */ '../views/Register')
  },
  {
    path: '/events',
    name: 'Events',
    component: () => import(/* webpackChunkName: events */ '../views/Events'),
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
    component: () => import(/* webpackChunkName: list */ '../views/List')
  },
  {
    path: '/account',
    name: 'Account',
    component: () => import(/* webpackChunkName: account */ '../views/Account'),
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
