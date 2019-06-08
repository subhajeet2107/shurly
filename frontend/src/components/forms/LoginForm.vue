<template>
    <form action="">
        <div class="modal-card" style="width:300px;">
            <section class="modal-card-body">
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
  name: 'LoginForm'
}
</script>
