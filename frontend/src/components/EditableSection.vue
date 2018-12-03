<template>
  <div class="section-editor">
    <section-editor 
       v-if="editing"
       :sectionText="sectionText"
       @input="sectionText = $event; editing=false"/>
    <section-display
      v-else
      @editing="editing = true"
      :sectionText="sectionText"/>
  </div>
</template>

<script>
import SectionDisplay from '@/components/SectionDisplay'
import SectionEditor from '@/components/SectionEditor'

export default {
  props: [],
  components: { SectionEditor, SectionDisplay },
  data () {
    return {
      sectionText: '# Hello World',
      editing: true
    }
  },
  methods: {

  }
}
</script>

<style lang="scss" scoped>
.section-editor {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  height: 300px;
  width: 400px;
}
</style>
