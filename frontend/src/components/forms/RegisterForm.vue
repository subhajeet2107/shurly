<template>
    <form @submit.prevent="register">
        <div class="modal-card" style="width:300px;">
            <section class="modal-card-body">
              <b-field label="Name">
                    <b-input
                        type="text"
                        placeholder="Your name"
                        required v-model="name">
                    </b-input>
                </b-field>
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
            </section>
            <footer class="modal-card-foot">
                <button class="button is-primary">Register</button>
            </footer>
        </div>
    </form>
</template>

<script>
export default {
    name: 'RegisterForm',
    data(){
        return {
            name : "",
            email : "",
            password : "",
        }
    },
    methods: {
      register: function () {
        let data = {
          name: this.name,
          email: this.email,
          password: this.password
        }
        this.$store.dispatch('postRegister', data)
       .then(() => this.$router.push('/'))
       .catch(err => console.log(err))
      }
    }
}
</script>
