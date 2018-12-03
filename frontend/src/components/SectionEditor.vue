<template>
  <div style="height: 100%; width: 100%;">
    <textarea 
      v-model="inputText" 
      placeholder="Input your Markdown Here"></textarea>
    <button @click="$emit('input', inputText)">Save</button>
  </div>
</template>

<script>
export default {
  props: {
    sectionText: String
  },
  data () {
    return {
      inputText: this.sectionText
    }
  }
}
</script>

<style lang="scss" scoped>
textarea {
  height: 100%;
  width: 100%;
}
</style>
