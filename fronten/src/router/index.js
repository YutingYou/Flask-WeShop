import Vue from 'vue'
import Router from 'vue-router'
import WeShop from '@/components/WeShop'
import AddressEdit from '@/components/AddressEdit'
import AddressList from '@/components/AddressList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'WeShop',
      component: WeShop
    },
    {
      path: '/address/edit',
      name: 'AddressEdit',
      component: AddressEdit
    },
    {
      path: '/address',
      name: 'AddressList',
      component: AddressList
    }
  ]
})
