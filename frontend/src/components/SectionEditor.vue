<template>
  <div style="height: 100%; width: 100%;">
    <input type="text" v-model="inputTitle"/>
    <drop @drop="handleDrop">
      <textarea
        v-model="inputContent"
        placeholder="Input your Markdown Here"></textarea>
    </drop>
    <button @click="saveSection">Save</button>
  </div>
</template>

<script>
export default {
  props: {
    section: Object
  },
  methods: {
    handleDrop (data, event) {
      this.inputContent += '\n'
      this.inputContent += data
    },
    saveSection () {
      let updatedSection = {
        title: this.inputTitle,
        content: this.inputContent,
        path: this.section.path
      }
      this.$emit('input', updatedSection)
    }
  },
  data () {
    return {
      inputContent: this.section.content,
      inputTitle: this.section.title
    }
  }
}
</script>

<style lang="scss" scoped>
textarea {
  min-height: 300px;
  width: 100%;
}
</style>
