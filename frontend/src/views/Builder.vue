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
          order: 0,
          title: 'Section Title',
          content: '# Start a new Section',
          children: []
        }
      ]
    }
  },
  methods: {
    addChild (section) {
      this.sections[section.order].children.push({
        title: 'New Child Section',
        content: 'New ChildContent',
        order: this.sections[section.order].children.length 
      })
    },
    addNewSection () {
      this.sections.push({
        title: 'Section Title',
        content: '# Start a new Section',
        order: this.sections.length,
        children: []
      })
    },
    updateSection (section) {
      console.log(section)
      this.sections[section.order].title = section.title
      this.sections[section.order].content = section.content
      this.sections[section.order].order = section.order
    }
  }
}
</script>

<style lang="scss" scoped>
</style>
