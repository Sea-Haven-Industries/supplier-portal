<template>
	<div v-if="!invoice.loading && invoice.doc">
		<div class="container mt-5 py-3 border">
			<div class="row mb-3 vr-aligned">
				<div class="col-6">
					<h1 class="text-gray-900 font-bold text-[32px]">
						Supplier Invoice: {{ invoice.doc.name }}
						<Badge>
							{{ invoice.doc.status }}
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
			<div
				:class="
					invoice.doc.supplier_invoice_items
						? 'container border-bottom pb-3'
						: 'container pb-3'
				"
			>
				<div class="mb-1 row">
					<div class="col">
						<div class="row">
							<label for="suppplier_id" class="col-sm-3 col-form-label"
								>Supplier ID</label
							>
							<div class="col-sm-8">
								<input
									type="text"
									readonly
									class="form-control-plaintext"
									id="suppplier_id"
									:value="invoice.doc.supplier"
								/>
							</div>
						</div>
					</div>
					<div class="col">
						<div class="row mb-1">
							<label for="service_date" class="col-sm-3 col-form-label"
								>Service Date</label
							>
							<div class="col-sm-8">
								<TextInput
									:type="'date'"
									size="lg"
									variant="outline"
									placeholder="Payment Date"
									id="service_date"
									:disabled="true"
									v-model="invoice.doc.service_date"
								/>
							</div>
						</div>
					</div>
				</div>
				<div class="mb-1 row">
					<div class="col">
						<div class="row">
							<label for="suppplier_name" class="col-sm-3 col-form-label"
								>Supplier Name</label
							>
							<div class="col-sm-8">
								<input
									type="text"
									readonly
									class="form-control-plaintext"
									id="suppplier_name"
									:value="invoice.doc.supplier_name"
								/>
							</div>
						</div>
					</div>
					<div class="col">
						<div class="row mb-1">
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
									:disabled="true"
									v-model="invoice.doc.invoice_date"
								/>
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
									v-model="invoice.doc.due_date"
								/>
							</div>
						</div>
					</div>
				</div>
				<div class="mb-1 row">
					<div class="col"></div>
					<div class="col">
						<div class="row">
							<label for="invoice_terms" class="col-sm-3 col-form-label"
								>Invoice Terms</label
							>
							<div class="col-sm-8">
								<input
									type="text"
									readonly
									class="form-control-plaintext h-100 d-inline-block"
									id="invoice_terms"
									:value="invoice.doc.invoice_terms"
								/>
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
										aria-controls="collapseOne"
									>
										Service Address
									</button>
								</h2>
								<div
									id="collapseOne"
									class="accordion-collapse collapse"
									data-bs-parent="#service-address-accordion"
								>
									<div class="accordion-body">
										<div class="row mb-1">
											<label for="site_code" class="col-sm-3 col-form-label"
												>Site Code</label
											>
											<div class="col-sm-8">
												<input
													type="text"
													readonly
													class="form-control-plaintext"
													id="site_code"
													:value="invoice.doc.site_code"
												/>
											</div>
										</div>
										<div class="row mb-1">
											<label for="street" class="col-sm-3 col-form-label"
												>Street</label
											>
											<div class="col-sm-8">
												<input
													type="text"
													readonly
													class="form-control-plaintext"
													id="street"
													:value="invoice.doc.street"
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
													readonly
													class="form-control-plaintext"
													id="city"
													:value="invoice.doc.city"
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
													readonly
													class="form-control-plaintext"
													id="state"
													:value="invoice.doc.state"
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
													readonly
													class="form-control-plaintext"
													id="zip_code"
													:value="invoice.doc.zip_code"
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
										Notes
									</button>
								</h2>
								<div
									id="collapse-2"
									class="accordion-collapse collapse"
									data-bs-parent="#address-accordion"
								>
									<div class="accordion-body">
										<div class="row mb-1">
											<label for="notes" class="col-sm-4 col-form-label"
												>Notes</label
											>
											<div class="col-sm-8">
												<Textarea
													:variant="'subtle'"
													size="md"
													placeholder="Enter Notes Here"
													:disabled="true"
													v-model="invoice.doc.notes"
													label=""
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

			<div class="container" v-if="invoice.doc.supplier_invoice_items">
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
						<tr
							v-for="(item, index) in invoice.doc.supplier_invoice_items"
							:key="item.name"
						>
							<th scope="row">{{ index + 1 }}</th>
							<td>{{ item.service_type }}</td>
							<td>{{ item.quantity }}</td>
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
							<label for="total_amount" class="col-sm-3 col-form-label"
								>Total Amount</label
							>
							<div class="cols-sm-5">
								<div class="input-group">
									<span class="input-group-text"
										><i class="bi bi-currency-dollar"></i>
									</span>
									<input
										type="text"
										readonly
										class="form-control"
										v-model.number="invoice.doc.total_amount"
									/>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { createDocumentResource, createListResource, Badge } from 'frappe-ui'
import Textarea from 'frappe-ui/src/components/Textarea.vue'
import TextInput from 'frappe-ui/src/components/TextInput.vue'

const props = defineProps({
	supplierInvoiceNumber: {
		type: String,
		required: true,
	},
})

const invoice = createDocumentResource({
	doctype: 'Invoices',
	name: props.supplierInvoiceNumber,
	auto: true,
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
