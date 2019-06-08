<template>
        <form action="." method="POST">

            <b-field>
                <b-input placeholder="Paste URL" type="url" size="is-large" icon="link"></b-input>
            </b-field>

            <button type="submit" class="button is-large is-dark"><span class="icon is-medium"> <i class="fas fa-cut"></i></span> <span>Shorten</span></button>
        </form>
</template>

<script>
export default {
  name: 'URLShortenForm'
}
</script>
