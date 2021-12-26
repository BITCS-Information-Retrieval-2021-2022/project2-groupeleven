// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import axios from 'axios'
import VueRouter from 'vue-router'
import routes from './router/index'
import VueAxios from 'vue-axios'
import ElementUI from 'element-ui';
import Video from 'video.js'
import 'video.js/dist/video-js.css'

import 'element-ui/lib/theme-chalk/index.css';
import App from './App'
import store from './store'
import 'lib-flexible'

import echarts from 'echarts'
Vue.prototype.$echarts = echarts

//import VueResource from 'vue-resource'//Belle


Vue.config.productionTip = false
Vue.use(ElementUI);
Vue.use(VueAxios, axios);
Vue.use(VueRouter);
//Vue.use( VueResource )//Belle
Vue.prototype.$video = Video;


const router = new VueRouter({
	routes
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
