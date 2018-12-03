<template>
  <div class="builder">
    <div class="input-wrapper">
      <input type="text" v-model="searchField" autofocus/>
      <section v-if="searchField && foundItems.length">
        <div v-if="$apollo.loading">Loading...</div>
        <div v-for="item in foundItems.slice(0, 5)" :key="item.name">
          <search-result-item :item="item" @click="selectItem"/>
        </div>
      </section>
    </div>
    <section id="selected-item" v-if="selectedFullItem">
      <div>
        <rack-item :item="rackItemFromSelected"/>
      </div>
    </section>
  </div>
</template>

<script>
import SearchResultItem from '@/components/SearchResultItem'

export default {
  name: 'home',
  components: { SearchResultItem },
  apollo: {
    foundItems: {
      query: require('@/graphql/queries/baseItemList.gql'),
      variables () {
        return {
          name: this.searchField
        }
      },
      update: data => data.baseItemList,
      skip () { return this.searchField === '' }
    },
    selectedFullItem: {
      query: require('@/graphql/queries/baseItem.gql'),
      variables () {
        return {
          name: this.selectedItem.name
        }
      },
      update: data => data.baseItem,
      skip () {
        return !this.selectedItem
      }
    }
  },
  computed: {
    rackItemFromSelected () {
      return {
        name: this.selectedFullItem.name,
        icon: this.selectedFullItem.icon,
        w: this.selectedFullItem.width,
        h: this.selectedFullItem.height,
        frameType: this.selectedFullItem.frame,
        typeLine: this.selectedFullItem.type ? this.selectedFullItem.type : '',
        descrText: this.selectedFullItem.descriptions.description,
        flavourText: this.htmlDecode(this.selectedFullItem.descriptions.flavourText),
        explicitMods: this.selectedFullItem.mods.length ? this.selectedFullItem.mods.map(mod => mod.nameOrig) : [],
        identified: true
      }
    }
  },
  methods: {
    htmlDecode (input) {
      let doc = new DOMParser().parseFromString(input, 'text/html')
      return doc.documentElement.textContent.split('<br />')
    },
    selectItem (item) {
      this.selectedItem = item
      this.searchField = ''
    }
  },
  data () {
    return {
      searchField: '',
      selectedItem: null,
      foundItems: []
    }
  }
}
</script>

<style lang="scss">
input {
  height: 40px;
  width: 400px;
  padding: 10px 10px;
  font-size: 28px;
}
.input-wrapper {
  display: flex;
  order: 1;
}
section {
  width: 400px;
}
.builder {
  display: flex;
}
#selected-item {
  display: flex;
  order: 2;
}
</style>
