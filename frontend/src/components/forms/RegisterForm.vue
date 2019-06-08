<template>
    <form action="">
        <div class="modal-card" style="width:300px;">
            <section class="modal-card-body">
              <b-field label="Name">
                    <b-input
                        type="text"
                        placeholder="Your name"
                        required>
                    </b-input>
                </b-field>
                <b-field label="Email">
                    <b-input
                        type="email"
                        placeholder="Your email"
                        required>
                    </b-input>
                </b-field>

                <b-field label="Password">
                    <b-input
                        type="password"
                        password-reveal
                        placeholder="Your password"
                        required>
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
  name: 'RegisterForm'
}
</script>
