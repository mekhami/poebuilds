import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { RackItem, RackItemDetails, RackItemIcon } from 'poe-item-rack'
import '../node_modules/poe-item-rack/dist/poeRack.css'

Vue.config.productionTip = false
Vue.component('rack-item', RackItem)
Vue.component('rack-item-details', RackItemDetails)
Vue.component('rack-item-icon', RackItemIcon)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
