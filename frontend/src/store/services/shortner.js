import axios from 'axios'

const state = {
  shortendUrlResponse: null
}

const getters = {}

const mutations = {
  setShortenedUrl (state, shortendUrlResponse) {
    state.shortendUrlResponse = shortendUrlResponse
  }
}

const actions = {
  getShortendUrl (context, payload) {
    return axios.post('/api/directors/', payload)
      .then(response => { context.commit('setShortenedUrl', response.data) })
      .catch(e => { console.log(e) })
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
