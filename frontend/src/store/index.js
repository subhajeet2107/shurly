import Vue from 'vue'
import Vuex from 'vuex'

import users from '@/store/services/users'
import shortner from '@/store/services/shortner'
import auth from '@/store/modules/auth'
import VuexPersist from 'vuex-persist'

Vue.use(Vuex)


const vuexPersist = new VuexPersist({
  key: 'shurly',
  storage: localStorage,
  filter: (mutation) => mutation.type == 'login' || mutation.type == 'setProfile'
})


const store = new Vuex.Store({
  modules: {
    users,
    shortner,
    auth
  },
  plugins: [vuexPersist.plugin]
})

export default store
