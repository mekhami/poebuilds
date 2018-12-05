<template>
  <section
    class="result-html"
    @mouseover="hovering = true"
    @mouseleave="hovering = false">
    <div class="overlay" v-if="hovering">
      <div class="buttons">
        <button @click="$emit('editing')">Edit</button>
        <button v-if="allowChildren" @click="$emit('addChild')">Add Child</button>
      </div>
    </div>
    <h1>{{ section.title }}</h1>
    <custom-markdown
      class="editor" 
      :itemMap="itemMap"
      :source="section.content"></custom-markdown>
  </section>
</template>

<script>
import CustomMarkdown from '@/components/CustomMarkdown'
import testData from '@/testData.json'

export default {
  props: {
    section: Object,
    allowChildren: {
      type: Boolean,
      default: false
    }
  },
  components: { CustomMarkdown },
  data () {
    return {
      hovering: false,
      itemMap: [
        testData
      ]
    }
  },
  methods: {
    postrender (outhtml) {
      return outhtml.replace(/\[\[(.*)\]\]/, (match, p1) => { 
        let formatted = `<test :info="{ value: '${p1}' }"></test>`
        return formatted
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.result-html {
  border: 1px solid #ccc;
  position: relative;
}
.overlay {
  height: 100%;
  width: 100%;
  position: absolute;
  display: inline;
  .buttons {
    z-index: 2;
    position: absolute;
    top: 0;
    right: 0;
  }
}
.editor {
  height: 100%;
  width: 100%;
}
</style>
