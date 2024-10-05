import { createRouter, createWebHistory } from 'vue-router'
import { session } from './data/session'
import { userResource } from '@/data/user'

const routes = [
  {
    name: 'Login',
    path: '/login',
    component: () => import('@/pages/Login.vue'),
  },
  {
    name: 'SupplierInvoiceList',
    path: '/',
    component: () => import('@/pages/SupplierInvoiceList.vue'),
  },
  {
    name: 'SupplierInvoice',
    path: '/invoices/:supplierInvoiceNumber',
    component: () => import('@/pages/SupplierInvoice.vue'),
    props: true,
  },
  {
    name: 'SupplierInvoiceCreate',
    path: '/invoices/new',
    component: () => import('@/pages/NewInvoice.vue'),
  },
]

let router = createRouter({
  history: createWebHistory('/supplier-portal'),
  routes,
})

router.beforeEach(async (to, from, next) => {
  let isLoggedIn = session.isLoggedIn
  try {
    await userResource.promise
  } catch (error) {
    isLoggedIn = false
  }

  if (to.name === 'Login' && isLoggedIn) {
    next({ name: 'SupplierInvoiceList' })
  } else if (to.name !== 'Login' && !isLoggedIn) {
    next({ name: 'Login' })
  } else {
    next()
  }
})

export default router