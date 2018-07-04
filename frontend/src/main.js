/*Copyright 2015 Province of British Columbia

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.*/

import Vue from 'vue'
import 'es6-promise/auto'
import App from './App'
import { store } from './store/'



import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
Vue.use(BootstrapVue)

import 'es6-promise/auto'
import axios from 'axios'

require('Keycloak')
var keycloak = Keycloak(process.env.KEYCLOAK_JSON_URL)
console.log(process.env.KEYCLOAK_JSON_URL)

export const axiosInstance = axios.create({
  baseURL: process.env.API_URL,
  withCredentials: true
})

Vue.prototype.$keycloak = keycloak
Vue.prototype.$axios = axiosInstance

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  template: '<App />',
  components: { App }
})
