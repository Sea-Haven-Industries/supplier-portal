<template>
	<div v-if="!invoice.loading && documents.invoice">
		<div class="container mt-5 py-3 border">
			<div class="row mb-3 vr-aligned">
				<div class="col-6">
					<h1 class="text-gray-900 font-bold text-[32px]">
						Supplier Invoice: {{ documents.invoice.name }}
						<Badge>
							{{ documents.invoice.status }}
						</Badge>
					</h1>
				</div>
				<div class="col-6">
					<div class="d-flex">
						<div class="ms-auto">
							<div class="btn-group" role="group" aria-label="Basic example">
								<button type="button" class="btn btn-primary btn-dark">
									<router-link to="/">Back</router-link>
								</button>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div :class="documents.invoice.items ? 'container border-bottom pb-3' : 'container pb-3'">
				<div class="mb-1 row">
					<div class="col">
						<div class="row">
							<label for="suppplier_id" class="col-sm-3 col-form-label">Supplier ID</label>
							<div class="col-sm-8">
								<input
									type="text"
									readonly
									class="form-control-plaintext"
									id="suppplier_id"
									:value="documents.invoice.supplier" />
							</div>
						</div>
					</div>
					<div class="col">
						<div class="row mb-1">
							<label for="service_date" class="col-sm-3 col-form-label">Service Date</label>
							<div class="col-sm-8">
								<TextInput
									:type="'date'"
									size="lg"
									variant="outline"
									placeholder="Payment Date"
									id="service_date"
									:disabled="true"
									v-model="documents.invoice.service_date" />
							</div>
						</div>
					</div>
				</div>
				<div class="mb-1 row">
					<div class="col">
						<div class="row">
							<label for="suppplier_name" class="col-sm-3 col-form-label">Supplier Name</label>
							<div class="col-sm-8">
								<input
									type="text"
									readonly
									class="form-control-plaintext"
									id="suppplier_name"
									:value="documents.invoice.supplier_name" />
							</div>
						</div>
					</div>
					<div class="col">
						<div class="row mb-1">
							<label for="posting_date" class="col-sm-3 col-form-label">Invoice Date</label>
							<div class="col-sm-8">
								<TextInput
									:type="'date'"
									size="lg"
									variant="outline"
									placeholder="Invoice Date"
									id="posting_date"
									:disabled="true"
									v-model="documents.invoice.posting_date" />
							</div>
						</div>
					</div>
				</div>
				<div class="mb-1 row">
					<div class="col"></div>
					<div class="col">
						<div class="row mb-1">
							<label for="due_date" class="col-sm-3 col-form-label">Due Date</label>
							<div class="col-sm-8">
								<TextInput
									:type="'date'"
									size="lg"
									variant="outline"
									placeholder="Due Date"
									id="due_date"
									:disabled="true"
									v-model="documents.invoice.due_date" />
							</div>
						</div>
					</div>
				</div>
				<div class="mb-1 row">
					<div class="col"></div>
					<div class="col">
						<div class="row">
							<label for="payment_terms_template" class="col-sm-3 col-form-label">Invoice Terms</label>
							<div class="col-sm-8">
								<input
									type="text"
									readonly
									class="form-control-plaintext h-100 d-inline-block"
									id="payment_terms_template"
									:value="documents.invoice.payment_terms_template" />
							</div>
						</div>
					</div>
				</div>
				<div class="mb-1 row">
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
										aria-controls="collapseOne">
										Service Address
									</button>
								</h2>
								<div id="collapseOne" class="accordion-collapse collapse" data-bs-parent="#service-address-accordion">
									<div class="accordion-body">
										<div class="row mb-1">
											<label for="site_code" class="col-sm-3 col-form-label">Site Code</label>
											<div class="col-sm-8">
												<input
													type="text"
													readonly
													class="form-control-plaintext"
													id="site_code"
													:value="documents?.address?.doc?.site_code" />
											</div>
										</div>
										<div class="row mb-1">
											<label for="street" class="col-sm-3 col-form-label">Street</label>
											<div class="col-sm-8">
												<input
													type="text"
													readonly
													class="form-control-plaintext"
													id="street"
													:value="documents?.address?.doc?.address_line1" />
											</div>
										</div>
										<div class="row mb-1">
											<label for="city" class="col-sm-3 col-form-label">City</label>
											<div class="col-sm-8">
												<input
													type="text"
													readonly
													class="form-control-plaintext"
													id="city"
													:value="documents?.address?.doc?.city" />
											</div>
										</div>
										<div class="row mb-1">
											<label for="state" class="col-sm-3 col-form-label">State</label>
											<div class="col-sm-8">
												<input
													type="text"
													readonly
													class="form-control-plaintext"
													id="state"
													:value="documents?.address?.doc?.state" />
											</div>
										</div>
										<div class="row mb-1">
											<label for="zip_code" class="col-sm-3 col-form-label">Zip Code</label>
											<div class="col-sm-8">
												<input
													type="text"
													readonly
													class="form-control-plaintext"
													id="zip_code"
													:value="documents?.address?.doc?.pincode" />
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
										aria-controls="collapse-2">
										Notes
									</button>
								</h2>
								<div id="collapse-2" class="accordion-collapse collapse" data-bs-parent="#address-accordion">
									<div class="accordion-body">
										<div class="row mb-1">
											<label for="remarks" class="col-sm-4 col-form-label">Notes</label>
											<div class="col-sm-8">
												<Textarea
													:variant="'subtle'"
													size="md"
													placeholder="Enter Notes Here"
													:disabled="true"
													v-model="documents.invoice.remarks"
													label=""
													id="remarks" />
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>

			<div class="container" v-if="documents.invoice.items">
				<table class="table">
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
						<tr v-for="(item, index) in documents.invoice.items" :key="item.name">
							<th scope="row">{{ index + 1 }}</th>
							<td>{{ item.item_code }}</td>
							<td>{{ item.qty }}</td>
							<td><i class="bi bi-currency-dollar"></i> {{ item.rate }}</td>
							<td><i class="bi bi-currency-dollar"></i> {{ item.amount }}</td>
						</tr>
					</tbody>
				</table>
			</div>

			<div class="container">
				<div class="mb-1 row">
					<div class="col"></div>
					<div class="col">
						<div class="input-group">
							<label for="grand_total" class="col-sm-3 col-form-label">Total Amount</label>
							<div class="cols-sm-5">
								<div class="input-group">
									<span class="input-group-text"><i class="bi bi-currency-dollar"></i> </span>
									<input type="text" readonly class="form-control" v-model.number="documents.invoice.grand_total" />
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
import { createDocumentResource, createListResource, Badge } from 'frappe-ui'
import Textarea from 'frappe-ui/src/components/Textarea.vue'
import TextInput from 'frappe-ui/src/components/TextInput.vue'
import { reactive, watch } from 'vue'

const { supplierInvoiceNumber } = defineProps<{
	supplierInvoiceNumber: string
}>()

const documents = reactive({})
const invoice = createDocumentResource({
	doctype: 'Purchase Invoice',
	name: supplierInvoiceNumber,
	onSuccess: (data) => {
		documents.invoice = data
		documents.address = createDocumentResource({
			doctype: 'Address',
			name: data.supplier_address,
			auto: true
		})
	}
})
</script>

<style lang="css" scoped>
.vr-aligned {
	vertical-align: middle;
}

button.accordion-button[aria-expanded='true'] {
	color: black;
}

input.form-control-plaintext:focus,
.input-group > input.form-control:focus,
input.form-control,
.input-group > span {
	background-color: #fff;
	border-color: #fff;
	box-shadow: none;
}

.disabled-date {
	color: black;
	background: transparent;
	border: none !important;
	border-bottom: 1px solid #ced4da !important;
}

a {
	text-decoration: none;
	color: inherit;
}
</style>
