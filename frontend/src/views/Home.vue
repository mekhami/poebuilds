<template>
  <div class="container home">
    <div class="is-child featured">
      <p>New Build 1</p>
      <p>New Build 2</p>
      <p>New Build 3</p>
    </div>
    <div class="is-child">
      <p>Ad Placeholder</p>
    </div>
    <div class="tile is-child is-12">
      <p>Horizontal Full Tile</p>
      <p>Featured Builds</p>
    </div>
  </div>
</template>

<script>

export default {
  name: 'home'
}
</script>

<style lang="scss" scoped>
@import "../assets/scss/_variables.scss";
.home {
  div.is-child {
    min-height: 200px;
    padding: 20px;
    margin: 20px 20px;
    border: 1px solid $soft-gray;
    border-top: 4px solid $primary-gold;
  }
}
p {
  display: block;
}
</style>
