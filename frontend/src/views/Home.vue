<template>
  <div class="home">
    <div class="input-wrapper">
      <input type="text" v-model="searchField" autofocus/>
      <section v-if="searchField && foundItems.length">
        <div v-if="$apollo.loading">Loading...</div>
        <div v-for="item in foundItems.slice(0, 5)" :key="item.name">
          <search-result-item :item="item" @click="selectItem"/>
        </div>
      </section>
    </div>
    <section id="selected-item">
      <div>
        {{ selectedFullItem }}
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
      update: data => data.baseItemList
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
  methods: {
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
  position: absolute;
}
section {
  width: 400px;
  position: relative;
  top: 40px;
}
</style>
