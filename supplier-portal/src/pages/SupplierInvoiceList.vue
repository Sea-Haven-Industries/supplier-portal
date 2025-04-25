<template>
	<div class="container-fluid">
		<div class="container mx-auto mt-5">
			<div class="row">
				<div class="col">
					<h1 class="text-gray-900 font-bold text-[32px]">Invoices</h1>
					<div class="d-flex">
						<div>
							<div class="btn-group" role="group" aria-label="Basic example"></div>
						</div>
					</div>
				</div>
				<div class="col">
					<div class="d-flex">
						<div class="ms-auto d-flex" style="gap: 2px">
							<router-link to="/invoices/new">
								<button type="button" class="btn btn-primary btn-dark">New</button>
							</router-link>
							<button type="button" class="btn btn-primary btn-dark" @click="session.logout.submit">Logout</button>
						</div>
					</div>
				</div>
			</div>
			<div class="container mx-auto mb-3 mt-5" v-if="invoice.data">
				<table class="table">
					<thead>
						<tr>
							<th scope="col">Invoice Number</th>
							<th scope="col">Supplier</th>
							<th scope="col">Status</th>
							<th scope="col">Amount</th>
						</tr>
					</thead>
					<tbody class="table-group-divider">
						<tr v-for="(item, index) in invoice.data" :key="index">
							<td>
								<router-link
									:to="{
										name: 'SupplierInvoice',
										params: { supplierInvoiceNumber: item.name },
									}"
									>{{ item.name }}</router-link
								>
							</td>
							<td>{{ item.supplier }}</td>
							<td>
								<Badge>{{ item.status }}</Badge>
							</td>
							<td><i class="bi bi-currency-dollar"></i> {{ item.total_amount }}</td>
						</tr>
					</tbody>
				</table>
			</div>
		</div>
		<div class="flex justify-between mt-4" v-if="invoice.length > 10">
			<Button @click="invoice.previous()"> Previous Page </Button>
			<Button @click="invoice.next()"> Next Page </Button>
		</div>
	</div>
</template>
<script setup>
import { createListResource, Badge } from 'frappe-ui'
import { session } from '../data/session'
import { onBeforeMount } from 'vue'

onBeforeMount(() => {
	if (window.location.origin === 'https://accounting.seahavenind.com') {
		window.location.replace('https://accounting.seahavenind.com/app')
	}
})

let invoiceParams = {
	doctype: 'Invoices',
	fields: ['*'],
	orderBy: 'creation desc',
	start: 0,
	pageLength: 5,
	auto: true,
}
let invoice = null

if (session.supplier_id && session.isLoggedIn) {
	invoiceParams.filters = [['supplier', '=', session.supplier_id]]
	invoice = createListResource(invoiceParams)
} else {
	invoice = createListResource(invoiceParams)
}
invoice.fetch()
</script>

<style lang="css" scoped>
a {
	text-decoration: none;
	color: inherit;
}
</style>
