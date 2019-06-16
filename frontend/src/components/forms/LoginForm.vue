<template>
    <form @submit.prevent="login">
        <div class="modal-card" style="width:300px;">
            <section class="modal-card-body">
                <b-field label="Email">
                    <b-input
                        type="email"
                        placeholder="Your email"
                        required v-model="email">
                    </b-input>
                </b-field>

                <b-field label="Password">
                    <b-input
                        type="password"
                        password-reveal
                        placeholder="Your password"
                        required v-model="password">
                    </b-input>
                </b-field>

                <b-checkbox>Remember me</b-checkbox>
            </section>
            <footer class="modal-card-foot">
                <button class="button is-primary">Login</button>
            </footer>
        </div>
    </form>
</template>

<script>
export default {
    name: 'LoginForm',
    data(){
        return {
            email : "",
            password : ""
        }
    },
    methods: {
      login: function () {
        let email = this.email
        let password = this.password
        this.$store.dispatch('postLogin', { email, password })
       .then(() => this.$router.push('/'))
       .catch(err => console.log(err))
      }
    }
}
</script>
