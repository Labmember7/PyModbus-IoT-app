import BootstrapVue from 'bootstrap-vue';
import VueThermometer from 'vuejs-thermometer';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';
import vuetify from './plugins/vuetify';

Vue.use(VueThermometer);

Vue.use(BootstrapVue);

Vue.config.productionTip = false;

new Vue({
  router,
  vuetify,
  render: (h) => h(App),
}).$mount('#app');
