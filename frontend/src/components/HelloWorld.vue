<template>
  <div class="hello">
    <rack-item :item="item"/>
  </div>
</template>

<script>
import testData from '@/testData.json'

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data () {
    return {
      item: testData
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
