<template>
  <div class="search-result-item" @mouseup="$emit('click', item)">
    <img :src="item.icon"/>
    <span>{{ item.name }}</span>
  </div>
</template>

<script>
export default {
  props: {
    item: Object
  }
}
</script>

<style lang="scss" scoped>
.search-result-item {
  border: 1px solid lightgray;
  margin: 5px;
}
</style>
