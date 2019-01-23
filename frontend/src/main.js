import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { RackItem, RackItemDetails, RackItemIcon } from 'poe-item-rack'
import '../node_modules/poe-item-rack/dist/poeRack.css'
import { createProvider } from './vue-apollo'
import { Drag, Drop } from 'vue-drag-drop'
import './assets/scss/main.scss'

Vue.config.productionTip = false
Vue.component('rack-item', RackItem)
Vue.component('rack-item-details', RackItemDetails)
Vue.component('rack-item-icon', RackItemIcon)
Vue.component('drop', Drop)
Vue.component('drag', Drag)

new Vue({
  router,
  apolloProvider: createProvider(),
  render: h => h(App)
}).$mount('#app')
