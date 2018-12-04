<template>
  <div class="section-editor">
    <section-editor
       v-if="editing"
       :section="section"
       @input="updateSection($event)"/>
    <section-display
      v-else
      @editing="editing = true"
      :allowChildren="allowChildren"
      @addChild="$emit('addChild', section)"
      :section="section"/>
    <div class="children">
      <editable-section
        v-for="section in section.children"
        :section="section"
        :key="`${section.title}-${section.order}`"
        :allowChildren="false"
        @input="$emit('input', $event)"></editable-section>
    </div>
  </div>
</template>

<script>
import SectionDisplay from '@/components/SectionDisplay'
import SectionEditor from '@/components/SectionEditor'

export default {
  name: 'editable-section',
  props: {
    section: Object,
    allowChildren: {
      type: Boolean,
      default: true
    }
  },
  methods: {
    updateSection (section) {
      this.editing = false
      this.$emit('input', section)
    }
  },
  components: { SectionEditor, SectionDisplay },
  data () {
    return {
      editing: false
    }
  }
}
</script>

<style lang="scss" scoped>
.section-editor {
  width: 90%;
  margin: 25px 0;
  input {
    width: 100%;
  }
}
.children {
  margin-left: 50px;
}
</style>
