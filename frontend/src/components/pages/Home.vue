<script>
  import BaseHeader from '@/components/comps/BaseHeader.vue'
  import URLShortenForm from '@/components/forms/URLShortenForm.vue'
  export default {
    name: 'MainComponent',
    components: { BaseHeader , URLShortenForm},

  }
</script>

<template>
  <section class="hero">
    <BaseHeader/>
    <div class="hero-body">
      <div class="container">
        <h1 class="title">
          <img src="img/icons/shurly_main.png" alt="Shurly">
        </h1>
      </div>
    </div>
    <div class="columns is-mobile url-container">
      <div class="column is-one-third"><h2 class="subtitle">Shorten your url</h2></div>
      <div class="column"><URLShortenForm/></div>
    </div>

</section>
</template>

<style lang="scss" scoped>
  .hero-body{
    background:#000;
  }
  h1 {
    text-align: center;
  }
  .subtitle{
    text-align: center;
    font-size:32px;
    font-family: Verdana;
  }
  .url-container{
    margin:20px;
  }
</style>
