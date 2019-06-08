<template>
        <form action="." method="POST">

            <b-field>
                <b-input placeholder="Paste URL" type="url" size="is-large" icon="link"></b-input>
            </b-field>
            <!-- <b-button tag="input"
                type="is-dark"
                native-type="submit"
                size="is-large"
                value="Shorten" icon-left="link" icon-pack="fas" /> -->

                <button type="submit" class="button is-large is-dark"><span class="icon is-medium"> <i class="fas fa-cut"></i></span> <span>Shorten</span></button>
        </form>
</template>

<script>
export default {
  name: 'URLShortenForm'
}
</script>

<style lang="scss" scoped>
</style>
