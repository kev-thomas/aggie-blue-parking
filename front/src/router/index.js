import Vue from 'vue'
import VueRouter from 'vue-router'
//import views here
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'

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
      this.$session.destroy();
      next();
    }
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
