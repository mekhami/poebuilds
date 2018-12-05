<template>
  <div class="section-wrapper">
    <div class="column left">
      <editable-section
        v-for="section in sections"
        :key="`${section.title}-${section.path}`"
        :section="section"
        :itemMap="itemMap"
        @input="updateSection"
        @remove="removeSection"
        @addChild="addChild(section)"></editable-section>
      <button @click="addNewSection">Add Section</button>
    </div>
    <div class="column right">
      <item-builder @selectItem="addToItems"/>
      <items-mapped
        :items="itemMap"/>
    </div>
  </div>
</template>

<script>
import EditableSection from '@/components/EditableSection'
import ItemBuilder from '@/components/ItemBuilder'
import ItemsMapped from '@/components/ItemsMapped'

export default {
  components: { EditableSection, ItemBuilder, ItemsMapped },
  data () {
    return {
      sections: [
        {
          path: [0],
          title: 'Section Title',
          content: '# Write your section content here',
          children: []
        }
      ],
      itemMap: {}
    }
  },
  methods: {
    addToItems (item) {
      const keys = Object.keys(this.itemMap)
      let start = item.name
      let counter = 1
      if (keys.includes(start)) {
        start += counter.toString()
      }
      while (keys.includes(start)) {
        start = item.name
        counter++
        start += counter.toString()
      }
      this.$set(this.itemMap, String(start), item)
    },
    addChild (section) {
      this.sections[section.path[0]].children.push({
        title: 'Child Section Title',
        content: '### Write your child section here',
        path: [section.path[0], this.sections[section.path[0]].children.length]
      })
    },
    removeSection (section) {
      if (section.path.length === 1) {
        this.$delete(this.sections, section.path[0])
      } else {
        this.$delete(this.sections[section.path[0]].children, section.path[1])
      }
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
.section-wrapper {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  width: 100%;
}
.column {
  display: flex;
  flex-direction: column;
  flex-basis: 100%;
  flex: 1;
  min-height: 100px;
}
</style>
