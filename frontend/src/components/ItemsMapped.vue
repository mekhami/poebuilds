<template>
  <section class="item-list">
    <drag
      v-for="(item, key) in items"
      :transferData="itemDragValue(key)">
      <rack-item
        :item="item"
        :key="`mappedItem-${key}`"/>
    </drag>
  </section>
</template>

<script>
export default {
  props: {
    items: {
      type: Object
    }
  },
  methods: {
    itemDragValue (key) {
      return `[BuildItem:${key}]`
    }
  }
}
</script>

<style lang="scss" scoped>
</style>
