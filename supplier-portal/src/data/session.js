import router from '@/router'
import { computed, reactive } from 'vue'
import { createResource } from 'frappe-ui'

import { userResource } from './user'

export function sessionUser() {
	const cookies = new URLSearchParams(document.cookie.split('; ').join('&'))
	let _sessionUser = cookies.get('user_id')
	if (_sessionUser === 'Guest') {
		_sessionUser = null
	}
	return _sessionUser
}

export function sessionSupplierId() {
	const cookies = new URLSearchParams(document.cookie.split('; ').join('&'))
	return cookies.get('supplier_id')
}

export function sessionSupplierName() {
	const cookies = new URLSearchParams(document.cookie.split('; ').join('&'))
	return cookies.get('supplier_name')
}

export const session = reactive({
	supplier_login: createResource({
		url: 'suppliers_portal.suppliers_portal.api.validate_supplier_id',
		makeParams({ supplier_id }) {
			return {
				supplier_id,
			}
		},
		onSuccess(data) {
			if (data && data.status === 'success') {
				userResource.reload()
				session.user = sessionUser()
				document.cookie = `supplier_id=${data.supplier_id}`
				document.cookie = `supplier_name=${data.supplier_name}`
				session.supplier_id = data.supplier_id
				session.supplier_name = data.supplier_name
				session.login.reset()
				router.replace({ name: 'SupplierInvoiceList' })
			}
		},
		onError(error) {
			console.error('Login failed', error)
		},
	}),
	login: createResource({
		url: 'login',
		makeParams({ email, password }) {
			return {
				usr: email,
				pwd: password,
			}
		},
		onSuccess(data) {
			if (data) {
				userResource.reload()
				session.user = sessionUser()
				// clear supplier_id and supplier_name
				document.cookie = `supplier_id=${session.supplier_id}; expires=Thu, 01 Jan 1970 00:00:00 UTC'`
				document.cookie = `supplier_id=${session.supplier_name}; expires=Thu, 01 Jan 1970 00:00:00 UTC'`
				session.supplier_id = ''
				session.supplier_name = ''
				session.login.reset()
				router.replace({ name: 'SupplierInvoiceList' })
			}
		},
		onError(error) {
			console.error('Login failed', error)
		},
	}),
	logout: createResource({
		url: 'logout',
		onSuccess() {
			document.cookie = `supplier_id=${session.supplier_id}; expires=Thu, 01 Jan 1970 00:00:00 UTC'`
			document.cookie = `supplier_id=${session.supplier_name}; expires=Thu, 01 Jan 1970 00:00:00 UTC'`
			session.supplier_id = ''
			session.supplier_name = ''
			userResource.reset()
			session.user = sessionUser()
			router.replace({ name: 'Login' })
		},
	}),
	user: sessionUser(),
	supplier_id: sessionSupplierId(),
	supplier_name: sessionSupplierName(),
	isLoggedIn: computed(() => !!session.user),
})
