import Vue from 'vue';
import Router from 'vue-router';
import Temperature from '../components/Temperature.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Temperature',
      component: Temperature,
    },
  ],
});
