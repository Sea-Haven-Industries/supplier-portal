<template>
	<form @submit.prevent="">
		<div class="container mt-5 py-3 border">
			<div class="row mb-3">
				<div class="col-6">
					<h1 class="text-gray-900 font-bold text-[32px]">New Invoice</h1>
				</div>
				<div class="col-6">
					<div class="d-flex">
						<div class="ms-auto">
							<div class="btn-group" role="group" aria-label="Basic example">
								<button type="button" class="btn btn-primary btn-light">
									<router-link to="/">Cancel</router-link>
								</button>
								<button
									type="button"
									class="btn btn-primary btn-dark"
									@click="saveInvoice"
								>
									Save
								</button>
							</div>
						</div>
					</div>
				</div>
			</div>

			<div class="container border-bottom pb-3">
				<div class="mb-2 row">
					<div class="col">
						<div class="row">
							<label for="supplier_invoice_number" class="col-sm-3 col-form-label"
								>Invoice Number</label
							>
							<div class="col-sm-8">
								<input
									type="text"
									class="form-control"
									id="supplier_invoice_number"
									v-model.number="invoiceData.supplier_invoice_number"
								/>
							</div>
						</div>
					</div>
					<div class="col">
						<div class="row">
							<label for="service_date" class="col-sm-3 col-form-label"
								>Service Date</label
							>
							<div class="col-sm-8">
								<TextInput
									:type="'date'"
									size="lg"
									variant="outline"
									placeholder="Service Date"
									id="service_date"
									:disabled="false"
									v-model="invoiceData.service_date"
								/>
							</div>
						</div>
					</div>
				</div>

				<div class="mb-2 row">
					<div class="col">
						<div class="row">
							<label for="supplier_id" class="col-sm-3 col-form-label"
								>Supplier ID</label
							>
							<div class="col-sm-8">
								<input
									type="text"
									readonly
									class="form-control-plaintext"
									id="supplier_id"
									v-model="invoiceData.supplier"
								/>
							</div>
						</div>
					</div>
					<div class="col">
						<div class="row">
							<label for="invoice_date" class="col-sm-3 col-form-label"
								>Invoice Date</label
							>
							<div class="col-sm-8">
								<TextInput
									:type="'date'"
									size="lg"
									variant="outline"
									placeholder="Invoice Date"
									id="invoice_date"
									:disabled="false"
									v-model="invoiceData.invoice_date"
								/>
							</div>
						</div>
					</div>
				</div>

				<div class="mb-2 row">
					<div class="col">
						<div class="row">
							<label for="supplier_name" class="col-sm-3 col-form-label"
								>Supplier Name</label
							>
							<div class="col-sm-8">
								<input
									type="text"
									readonly
									class="form-control-plaintext"
									id="supplier_name"
									:value="invoiceData.supplier_name"
									v-if="!isAdministrator"
								/>
								<Autocomplete
									id="supplier_name"
									:options="portalSuppliers.data"
									:placeholder="'Supplier Name'"
									:hideSearch="!invoiceData.supplier_invoice_number"
									:label="'company_name'"
									v-model="invoiceData.supplier_name"
									v-else
								/>
							</div>
						</div>
					</div>
					<div class="col">
						<div class="row">
							<label for="invoice_terms" class="col-sm-3 col-form-label"
								>Invoice Terms</label
							>
							<div class="col-sm-8">
								<select
									class="form-select form-select-mb h-100 d-inline-block"
									aria-label="Invoice Terms"
									v-model="invoiceData.invoice_terms"
								>
									<option readonly></option>
									<option
										v-for="option in invoiceTermOptions"
										:value="option.value"
									>
										{{ option.label }}
									</option>
								</select>
							</div>
						</div>
					</div>
				</div>
				<div class="mb-2 row">
					<div class="col"></div>
					<div class="col">
						<div class="row">
							<label for="invoice_date" class="col-sm-3 col-form-label"
								>Due Date</label
							>
							<div class="col-sm-8">
								<TextInput
									:type="'date'"
									size="lg"
									variant="outline"
									placeholder="Due Date"
									id="due_date"
									:disabled="true"
									v-model="invoiceDueDate"
								/>
							</div>
						</div>
					</div>
				</div>

				<div class="mb-2 row">
					<div class="col">
						<div class="accordion accordion-flush" id="service-address-accordion">
							<div class="accordion-item">
								<h2 class="accordion-header ps-0">
									<button
										class="accordion-button"
										type="button"
										data-bs-toggle="collapse"
										data-bs-target="#collapseOne"
										aria-expanded="true"
										aria-controls="collapseOne"
									>
										Service Address
									</button>
								</h2>
								<div
									id="collapseOne"
									class="accordion-collapse collapse show"
									data-bs-parent="#service-address-accordion"
								>
									<div class="accordion-body">
										<div class="row mb-1">
											<label for="street" class="col-sm-3 col-form-label"
												>Street</label
											>
											<div class="col-sm-8">
												<input
													type="text"
													class="form-control"
													id="street"
													v-model="invoiceData.street"
												/>
											</div>
										</div>
										<div class="row mb-1">
											<label for="city" class="col-sm-3 col-form-label"
												>City</label
											>
											<div class="col-sm-8">
												<input
													type="text"
													class="form-control"
													id="city"
													v-model="invoiceData.city"
												/>
											</div>
										</div>
										<div class="row mb-1">
											<label for="state" class="col-sm-3 col-form-label"
												>State</label
											>
											<div class="col-sm-8">
												<input
													type="text"
													class="form-control"
													id="state"
													v-model="invoiceData.state"
												/>
											</div>
										</div>
										<div class="row mb-1">
											<label for="zip_code" class="col-sm-3 col-form-label"
												>Zip Code</label
											>
											<div class="col-sm-8">
												<input
													type="text"
													class="form-control"
													id="zip_code"
													v-model="invoiceData.zip_code"
												/>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div class="col">
						<div class="accordion accordion-flush" id="address-accordion">
							<div class="accordion-item">
								<h2 class="accordion-header ps-0">
									<button
										class="accordion-button"
										type="button"
										data-bs-toggle="collapse"
										data-bs-target="#collapse-2"
										aria-expanded="true"
										aria-controls="collapse-2"
									>
										{{
											sessionSupplierId()
												? 'Notes'
												: 'Payment Reference and Notes'
										}}
									</button>
								</h2>
								<div
									id="collapse-2"
									class="accordion-collapse collapse show"
									data-bs-parent="#address-accordion"
								>
									<div class="accordion-body">
										<div class="row mb-1" v-if="!sessionSupplierId()">
											<label
												for="payment_reference_no"
												class="col-sm-3 col-form-label"
												>Payment Reference</label
											>
											<div class="col-sm-5">
												<input
													type="text"
													class="form-control"
													id="payment_reference_no"
													v-model="invoiceData.payment_reference_no"
												/>
											</div>
										</div>
										<div class="row mb-1" v-if="!sessionSupplierId()">
											<label
												for="payment_reference_date"
												class="col-sm-3 col-form-label"
												>Payment Date</label
											>
											<div class="col-sm-5">
												<TextInput
													:type="'date'"
													size="lg"
													variant="outline"
													placeholder="Payment Date"
													id="payment_reference_date"
													:disabled="false"
													v-model="invoiceData.payment_reference_date"
												/>
											</div>
										</div>
										<div class="row mb-1">
											<label for="notes" class="col-sm-3 col-form-label"
												>Notes</label
											>
											<div class="col-md-8">
												<Textarea
													:variant="'subtle'"
													size="md"
													placeholder="Enter Notes Here"
													:disabled="false"
													v-model="invoiceData.notes"
													id="notes"
												/>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>

			<div class="container">
				<h4>Line Items</h4>
				<table class="table" v-if="invoiceItems.length !== 0">
					<thead>
						<tr>
							<th scope="col">#</th>
							<th scope="col" width="30%">Service Type</th>
							<th scope="col">Quantity</th>
							<th scope="col">Rate</th>
							<th scope="col">Amount</th>
						</tr>
					</thead>
					<tbody class="table-group-divider">
						<tr v-for="(item, index) in invoiceItems" :key="index">
							<th scope="row">{{ index + 1 }}</th>
							<td>
								<div class="col-mb-12">
									<select
										class="form-select form-select-mb h-100 d-inline-block"
										aria-label="Service Types"
										v-model="item.service_type"
									>
										<option readonly></option>
										<option
											v-for="option in serviceTypeOption"
											:value="option.value"
										>
											{{ option.label }}
										</option>
									</select>
								</div>
							</td>
							<td>
								<input type="text" class="form-control" v-model="item.quantity" />
							</td>
							<td>
								<div class="input-group">
									<span class="input-group-text"
										><i class="bi bi-currency-dollar"></i>
									</span>
									<input
										type="text"
										class="form-control"
										v-model.number="item.rate"
									/>
								</div>
							</td>
							<td>
								<div class="input-group">
									<span class="input-group-text"
										><i class="bi bi-currency-dollar"></i>
									</span>
									<input
										type="text"
										readonly
										class="form-control"
										v-model.number="item.amount"
									/>
								</div>
							</td>
							<td>
								<button type="button" class="btn btn-dark btn-sm">
									<i @click="deleteRow(index)" class="bi bi-trash"></i>
								</button>
							</td>
						</tr>
					</tbody>
				</table>
				<div class="d-flex">
					<div :class="invoiceItems.length === 0 ? 'ms-auto pt-3' : 'ms-auto'">
						<div class="btn-group" role="group" aria-label="Basic example">
							<button type="button" class="btn btn-dark btn-sm" @click="addRow">
								<i class="bi bi-plus"></i>
							</button>
						</div>
					</div>
				</div>
			</div>
			<div class="container">
				<div class="mb-2 row">
					<div class="col"></div>
					<div class="col">
						<div class="input-group">
							<label for="total_amount" class="col-sm-3 col-form-label"
								>Total Amount</label
							>
							<div class="cols-sm-5">
								<div class="input-group">
									<span class="input-group-text currency-fmt"
										><i class="bi bi-currency-dollar"></i>
									</span>
									<input
										type="text"
										readonly
										class="form-control"
										v-model.number="invoiceData.total_amount"
									/>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</form>
</template>

<script setup>
import { computed, reactive, readonly, watch } from 'vue'
import { createListResource } from 'frappe-ui'
import { sessionSupplierId, sessionSupplierName, sessionUser } from '../data/session'
import { addDays, parseInvoiceTerms } from '../data/utils'
import router from '../router'
import TextInput from 'frappe-ui/src/components/TextInput.vue'
import Textarea from 'frappe-ui/src/components/Textarea.vue'
import Autocomplete from 'frappe-ui/src/components/Autocomplete.vue'

const isAdministrator = sessionUser() === 'Administrator'

const portalInvoice = createListResource({
	doctype: 'Invoices',
	insert: {
		onSuccess() {
			router.push({ name: 'SupplierInvoiceList' })
		},
	},
})

const invoiceTermOptions = [
	{
		label: 'NET 10',
		value: 'NET 10',
	},
	{
		label: 'NET 15',
		value: 'NET 15',
	},
	{
		label: 'NET 30',
		value: 'NET 30',
	},
	{
		label: 'NET 45',
		value: 'NET 45',
	},
	{
		label: 'NET 60',
		value: 'NET 60',
	},
	{
		label: 'Due on Receipt',
		value: 'Due on Receipt',
	},
]

const serviceTypeOption = [
	{
		label: 'Repair',
		value: 'Repair',
	},
	{
		label: 'Preventive Maintenance',
		value: 'Preventive Maintenance',
	},
]

const invoiceData = reactive({
	supplier_invoice_number: '',
	supplier: sessionSupplierId(),
	service_date: new Date().toISOString().split('T')[0],
	invoice_date: new Date().toISOString().split('T')[0],
	supplier_name: sessionSupplierName(),
	invoice_terms: '',
	total_amount: 0,
	street: '',
	city: '',
	state: '',
	zip_code: '',
	payment_reference_no: '',
	payment_reference_date: new Date().toISOString().split('T')[0],
	notes: '',
})

const invoiceItems = reactive([])
let invoiceDueDate = computed(() => {
	if (invoiceData.invoice_terms) {
		let result = addDays(
			invoiceData.invoice_date,
			parseInvoiceTerms(invoiceData.invoice_terms),
		)
		// return as string
		return result.toISOString().split('T')[0]
	}
	return ''
})

const addRow = () => {
	const rowObject = reactive({
		service_type: '',
		quantity: 0,
		rate: 0,
		amount: 0,
	})
	rowObject.amount = computed(() => rowObject.quantity * rowObject.rate)
	invoiceItems.push(rowObject)
}

const deleteRow = (index) => {
	invoiceItems.splice(index, 1)
}

invoiceData.total_amount = computed(() => {
	return invoiceItems.reduce((acc, item) => acc + item.amount, 0)
})

const saveInvoice = () => {
	portalInvoice.insert.submit({
		supplier_invoice_number: invoiceData.supplier_invoice_number,
		supplier: invoiceData.supplier,
		service_date: invoiceData.service_date,
		invoice_date: invoiceData.invoice_date,
		supplier_name: invoiceData.supplier_name,
		invoice_terms: invoiceData.invoice_terms,
		street: invoiceData.street,
		city: invoiceData.city,
		state: invoiceData.state,
		zip_code: invoiceData.zip_code,
		payment_reference_date: invoiceData.payment_reference_date,
		payment_reference_no: invoiceData.payment_reference_no,
		notes: invoiceData.notes,
		supplier_invoice_items: invoiceItems.map((item) => {
			return {
				service_type: item.service_type,
				quantity: item.quantity,
				rate: item.rate,
			}
		}),
	})
}
const portalSuppliers = createListResource({
	doctype: 'Supplier',
	fields: ['name as value', 'company_name as label'],
	orderBy: 'creation desc',
})
portalSuppliers.fetch()

// watch for changes in invoiceData.supplier_name
watch(
	() => invoiceData.supplier_name,
	(newVal) => {
		if (newVal) {
			invoiceData.supplier = newVal.value
		}
	},
)
</script>

<style lang="css" scoped>
input.form-control-plaintext:focus,
.currency-fmt {
	background-color: #fff;
	border-color: #fff;
	box-shadow: none;
}

.currency-fmt + input.form-control {
	background-color: #fff;
	border-color: #fff;
	box-shadow: none;
}

tr {
	vertical-align: middle;
}
</style>
