<template>
        <form @submit.prevent="shorten">

            <b-field>
                <b-input placeholder="Paste URL" type="url" size="is-large" icon="link" v-model="original_url"></b-input>
            </b-field>

            <b-message title="Your short url" type="is-success" has-icon aria-close-label="Close message" v-if="shortend_url_response">
                {{base_url}}r{{ shortend_url_response.short_url }}
            </b-message>

            <button type="submit" class="button is-large is-dark"><span class="icon is-medium"> <i class="fas fa-cut"></i></span> <span>Shorten</span></button>
        </form>
</template>

<script>
    import { mapState } from 'vuex'
    import { Snackbar } from 'buefy/dist/components/snackbar'
    export default {
        name: 'URLShortenForm',
        data(){
            return {
                original_url : "",
                base_url: window.location.href,
            }
        },
        computed:mapState({
                shortend_url_response: state => state.shortner.shortendUrlResponse
        }),
        methods: {
          shorten: function () {
            let original_url = this.original_url
            this.$store.dispatch('getShortendUrl', { original_url })
           .then(() => Snackbar.open('Your short Url is ready'))
           .catch(err => console.log(err))
          }
        }
    }
</script>
