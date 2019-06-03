import Vue from 'vue'
import store from '@/store'
import router from '@/router'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'


import axios from 'axios'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'






import App from '@/App.vue'
import './registerServiceWorker'

import Header from '@/components/comps/Header.vue'

Vue.config.productionTip = false
Vue.use(Buefy)







new Vue({
  router,
  store,

  render: h => h(App)
}).$mount('#app')
