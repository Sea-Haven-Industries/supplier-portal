from pathlib import Path

import frappe
from erpnext.accounts.utils import get_account_name
from frappe.contacts.doctype.address.address import get_address_display
from frappe.core.doctype.data_import.importer import Importer, Row
from frappe.utils import flt, getdate, update_progress_bar

######################## PATCH PREREQUISITES ########################
# - This patch should be run on a fresh site with ERPNext installed
# - There should be fiscal years made for 2020, 2024 and 2025


def execute():
	create_items()
	create_payment_terms_template()

	frappe.flags.in_import = True
	import_suppliers()
	import_invoices()
	frappe.flags.in_import = False


def create_items():
	for item in ["Preventive Maintence", "Repair"]:
		if not frappe.db.exists("Item", item):
			item_doc = frappe.new_doc("Item")
			item_doc.update(
				{
					"item_code": item,
					"item_name": item,
					"item_group": "Services",
					"stock_uom": "Unit",
				}
			)
			item_doc.insert(ignore_permissions=True)


def create_payment_terms_template():
	for credit_days in [0, 10, 15, 30, 45, 60]:
		template_name = f"NET {credit_days}" if credit_days else "Due On Receipt"

		if not frappe.db.exists("Payment Terms Template", template_name):
			term = frappe.new_doc("Payment Term")
			term.update(
				{
					"payment_term_name": template_name,
					"invoice_portion": 100,
					"due_date_based_on": "Day(s) after invoice date",
					"credit_days": credit_days,
				}
			)
			term.save(ignore_permissions=True)

			template = frappe.new_doc("Payment Terms Template")
			template.template_name = template_name
			template.allocate_payment_based_on_payment_terms = True
			template.append(
				"terms",
				{
					"payment_term": term.name,
					"invoice_portion": term.invoice_portion,
					"due_date_based_on": term.due_date_based_on,
					"credit_days": term.credit_days,
				},
			)
			template.save(ignore_permissions=True)


def import_suppliers():
	suppliers_file = Path(__file__).parent / "data" / "supplier.csv"
	supplier_importer = Importer("Supplier", file_path=str(suppliers_file), console=True)
	suppliers = supplier_importer.import_file.data

	supplier: Row
	for idx, supplier in enumerate(suppliers):
		update_progress_bar("Importing Suppliers", idx, (len(suppliers)))
		(
			# supplier details
			_,
			supplier_id,
			created_on,
			created_by,
			company_name,
			street,
			city,
			state,
			pincode,
			# supplier invoices; not importing using this sheet
			*extra,
		) = supplier.as_list()

		# ignore child rows
		if not company_name:
			continue

		# skip if supplier already exists
		supplier_id = supplier_id.replace('"', "")
		if frappe.db.exists("Supplier", {"name": supplier_id}):
			continue

		supplier_doc = frappe.new_doc("Supplier")
		supplier_doc.update(
			{
				"name": supplier_id,
				"supplier_name": company_name,
				"owner": created_by,
				"creation": created_on,
			}
		)
		supplier_doc.insert(ignore_permissions=True)

		if street:
			address = frappe.new_doc("Address")
			address.update(
				{
					"address_type": "Billing",
					"address_title": company_name,
					"address_line1": street,
					"city": city or "Unknown",
					"state": state,
					"pincode": pincode,
					"country": "United States",
					"is_primary_address": True,
					"is_shipping_address": True,
					"links": [
						{"link_doctype": "Supplier", "link_name": supplier_doc.name},
					],
				}
			)
			address.insert(ignore_permissions=True)
			address_display = get_address_display(address.name)
			supplier_doc.db_set("supplier_primary_address", address.name)
			supplier_doc.db_set("primary_address", address_display)


def import_invoices():
	invoices_file = Path(__file__).parent / "data" / "invoices.csv"
	invoice_importer = Importer("Purchase Invoice", file_path=str(invoices_file), console=True)
	invoices = invoice_importer.import_file.data

	invoice: Row
	invoices_map = {}
	current_invoice_number = None
	for invoice in invoices:
		(
			# invoice details
			_,
			_,
			supplier_invoice_number,
			_,
			invoice_date,
			invoice_terms,
			created_on,
			created_by,
			supplier,
			due_date,
			_,
			_,
			_,
			site_code,
			_,
			_,
			_,
			_,
			notes,
			# invoice items
			_,
			item_id,
			_,
			_,
			service_type,
			quantity,
			rate,
			_,
			# invoice payments
			_,
			payment_id,
			_,
			_,
			reference_number,
			payment_date,
			payment_amount,
		) = invoice.as_list()

		if supplier_invoice_number:
			current_invoice_number = supplier_invoice_number

			# parent row
			if frappe.db.exists("Purchase Invoice", {"name": supplier_invoice_number}):
				continue

			remarks = ""
			if site_code:
				remarks += f"Site Code: {site_code}\n"
			if notes:
				remarks += f"Notes: {notes}\n"

			invoices_map[supplier_invoice_number] = {
				"invoice_date": getdate(invoice_date),
				"terms": invoice_terms,
				"supplier": supplier,
				"due_date": getdate(due_date),
				"remarks": remarks,
				"creation": created_on,
				"owner": created_by,
				"items": [],
				"payments": [],
			}

		invoice_map = invoices_map.get(current_invoice_number)
		if invoice_map:
			if item_id:
				invoice_map["items"].append(
					{
						"item_code": service_type,
						"qty": flt(quantity),
						"rate": flt(rate),
					}
				)
			if payment_id and flt(payment_amount) > 0:
				invoice_map["payments"].append(
					{
						"reference_number": reference_number,
						"payment_date": payment_date,
						"payment_amount": flt(payment_amount),
					}
				)

	for idx, invoice_id in enumerate(invoices_map):
		update_progress_bar("Importing Invoices", idx, (len(invoices_map)))
		invoice_map = invoices_map[invoice_id]
		invoice_doc = frappe.new_doc("Purchase Invoice")
		invoice_doc.update(
			{
				"name": invoice_id,
				"supplier": invoice_map.get("supplier"),
				"bill_no": invoice_id,
				"bill_date": getdate(invoice_map.get("invoice_date")),
				"set_posting_time": True,
				"posting_date": getdate(invoice_map.get("invoice_date")),
				"due_date": getdate(invoice_map.get("due_date")),
				"payment_terms_template": invoice_map.get("invoice_terms"),
				"remarks": invoice_map.get("remarks"),
				"owner": invoice_map.get("owner"),
				"creation": invoice_map.get("creation"),
			}
		)

		for item in invoice_map.get("items"):
			invoice_doc.append(
				"items",
				{
					"item_code": item.get("item_code"),
					"received_qty": item.get("qty"),
					"qty": item.get("qty"),
					"rate": item.get("rate"),
				},
			)

		try:
			invoice_doc.insert(ignore_permissions=True)
			invoice_doc.submit()
		except Exception as e:
			print(f"Error importing invoice {invoice_id}: {e}")
			continue

		for payment in invoice_map.get("payments"):
			payment_doc = frappe.new_doc("Payment Entry")
			payment_doc.update(
				{
					"payment_type": "Pay",
					"posting_date": getdate(payment.get("payment_date")),
					"party_type": "Supplier",
					"party": invoice_map.get("supplier"),
					"paid_amount": payment.get("payment_amount"),
					"received_amount": payment.get("payment_amount"),
					"paid_from": get_account_name("Bank", "Asset"),
					"reference_no": payment.get("reference_number")
					or "Note: Missing reference during ERPNext import",
					"reference_date": getdate(payment.get("payment_date")),
					"references": [
						{
							"reference_doctype": "Purchase Invoice",
							"reference_name": invoice_id,
							"allocated_amount": payment.get("payment_amount"),
						}
					],
				}
			)

			try:
				payment_doc.insert(ignore_permissions=True)
				payment_doc.submit()
			except Exception as e:
				print(f"Error importing payment for invoice {invoice_id}: {e}")
