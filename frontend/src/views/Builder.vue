<template>
  <div class="section-wrapper">
    <editable-section
      v-for="section in sections"
      :key="`${section.title}-${section.order}`"
      :section="section"
      @input="updateSection($event)"
      @addChild="addChild(section)"></editable-section>
    <button @click="addNewSection">Add Section</button>
  </div>
</template>

<script>
import EditableSection from '@/components/EditableSection'

export default {
  components: { EditableSection },
  data () {
    return {
      sections: [
        {
          path: [0],
          title: 'Section Title',
          content: '# Start a new Section',
          children: []
        }
      ]
    }
  },
  methods: {
    addChild (section) {
      this.sections[section.path[0]].children.push({
        title: 'New Child Section',
        content: 'New Child Content',
        path: [section.path[0], this.sections[section.path[0]].children.length]
      })
    },
    addNewSection () {
      this.sections.push({
        title: 'Section Title',
        content: '# Start a new Section',
        path: [this.sections.length],
        children: []
      })
    },
    updateSection (section) {
      let path = section.path
      if (path.length === 1) {
        this.$set(this.sections, path[0], Object.assign({}, this.sections[path[0]], section))
      } else {
        this.$set(
          this.sections[path[0]].children,
          path[1],
          Object.assign({}, this.sections[path[0]].children[path[1]], section)
        )
      }
    }
  }
}
</script>

<style lang="scss" scoped>
</style>
