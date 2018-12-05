<template>
  <span class="item">{{ info.value }}</span>
</template>

<script>
export default {
  props: {
    info: Object  
  }
}
</script>

<style lang="scss" scoped>
.item {
  color: green;
}
</style>
