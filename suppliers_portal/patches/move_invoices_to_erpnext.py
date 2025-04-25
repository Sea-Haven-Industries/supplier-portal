from pathlib import Path

import frappe
from frappe.contacts.doctype.address.address import get_address_display
from frappe.core.doctype.data_import.importer import Importer, Row
from frappe.utils import update_progress_bar


# NOTE: This patch should be run on a fresh site with ERPNext installed
def execute():
	import_suppliers()


def import_suppliers():
	suppliers_file = Path(__file__).parent / "data" / "supplier.csv"
	supplier_importer = Importer("Supplier", file_path=str(suppliers_file), console=True)
	suppliers = supplier_importer.import_file.data

	supplier: Row
	frappe.flags.in_import = True

	for idx, supplier in enumerate(suppliers):
		update_progress_bar("Importing Suppliers", idx, (len(suppliers)))
		(
			_,
			supplier_id,
			created_on,
			created_by,
			company_name,
			street,
			city,
			state,
			pincode,
			*extra,
		) = supplier.as_list()

		# ignore child rows
		if not company_name:
			continue

		supplier_doc = frappe.new_doc("Supplier")
		supplier_doc.update(
			{
				"name": supplier_id.replace('"', ""),
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

	frappe.flags.in_import = False


def import_invoices():
	# invoices_file = Path(__file__).parent / "data" / "invoices.csv"
	pass
