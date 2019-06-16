<template>
  <nav class="navbar">
    <div class="navbar-brand">
        <a class="navbar-item">
            Shurly
        </a>
    </div>

    <div class="navbar-menu">
        <div class="navbar-end" v-if="loggedIn">
            <a class="navbar-item">
            {{ profile.name }}
            </a>
        </div>
        <div class="navbar-end" v-else>
            <b-dropdown position="is-bottom-left" aria-role="menu">
                <a
                    class="navbar-item"
                    slot="trigger"
                    role="button">
                    <span>Login</span>
                    <b-icon icon="menu-down"></b-icon>
                </a>
                <b-dropdown-item aria-role="menu-item" custom paddingless>
                    <LoginForm/>
                </b-dropdown-item>
            </b-dropdown>
             <b-dropdown position="is-bottom-left" aria-role="menu">
                <a
                    class="navbar-item"
                    slot="trigger"
                    role="button">
                    <span>Register</span>
                    <b-icon icon="menu-down"></b-icon>
                </a>
                <b-dropdown-item aria-role="menu-item" custom paddingless>
                    <RegisterForm/>
                </b-dropdown-item>
            </b-dropdown>
        </div>
    </div>
</nav>
</template>

<script>
  import { mapState } from 'vuex'
  import LoginForm from '@/components/forms/LoginForm.vue'
  import RegisterForm from '@/components/forms/RegisterForm.vue'
  export default {
    name: 'BaseHeader',
    components: {LoginForm, RegisterForm},
    computed: mapState({
        loggedIn: state => state.auth.loggedIn,
        profile: state => state.auth.profile
    })
  }
</script>
