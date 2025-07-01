import json
import re

import frappe
from frappe.utils import getdate, update_progress_bar

from suppliers_portal.patches.move_invoices_to_erpnext import get_site_code


def execute():
	migrate_site_code_address()
	fix_invoices_shipping_addresses()
	remove_supplier_links()


def remove_supplier_links():
	suppliers_file = frappe.get_site_path("private", "backups", "suppliers.json")
	with open(suppliers_file) as f:
		suppliers = json.load(f)
		for idx, supplier in enumerate(suppliers):
			if not frappe.db.exists("Supplier", supplier.get("name")):
				continue
			update_progress_bar(f"Updating Supplier Addresses: {idx}", idx, (len(suppliers)))
			linked_addresses = frappe.get_all(
				"Dynamic Link",
				{"link_doctype": "Supplier", "link_name": supplier.get("name"), "parenttype": "Address"},
				["name", "parent"],
			)
			address = frappe.new_doc("Address")
			address.update(
				{
					"address_type": "Billing",
					"address_title": supplier.get("company_name"),
					"address_line1": supplier.get("street") or "No Street Address",
					"city": supplier.get("city") or "Unknown",
					"state": supplier.get("state"),
					"pincode": supplier.get("zip_code"),
					"country": "United States",
					"is_primary_address": True,
					"is_shipping_address": True,
					"links": [
						{
							"link_doctype": "Supplier",
							"link_name": supplier.get("name"),
						},
					],
				}
			)
			address.insert(ignore_permissions=True)
			if len(linked_addresses):
				for linked_address in linked_addresses:
					frappe.rename_doc("Address", linked_address.parent, address.name, merge=True, force=True)


def fix_invoices_shipping_addresses():
	invoices = frappe.get_all("Purchase Invoice", {"site_code": ["is", "set"]}, ["name", "site_code"])
	for idx, invoice in enumerate(invoices):
		update_progress_bar("Updating invoice addresses", idx, (len(invoices)))
		frappe.db.set_value(
			"Purchase Invoice", invoice.name, "shipping_address", invoice.site_code, update_modified=False
		)
		if frappe.db.exists("Address", invoice.site_code):
			frappe.db.set_value(
				"Purchase Invoice", invoice.name, "shipping_address", invoice.site_code, update_modified=False
			)


def migrate_site_code_address():
	linked_addresses = frappe.get_all(
		"Dynamic Link", {"link_doctype": "Site Code", "parenttype": "Address"}, ["parent", "link_name"]
	)
	for idx, site in enumerate(linked_addresses):
		update_progress_bar("Updating Site Codes", idx, (len(linked_addresses)))
		if site.parent[-1].isdigit():
			merge = True if frappe.db.exists("Address", site.link_name) else False
			frappe.rename_doc("Address", site.parent, f"{site.link_name}", merge=merge)
			continue
		frappe.db.set_value("Site Code", site.link_name, "address", site.parent)
		frappe.db.set_value("Address", site.parent, "address_title", site.link_name)
		frappe.db.set_value("Address", site.parent, "address_title", site.link_name)
		try:
			frappe.rename_doc("Address", site.parent, f"{site.link_name}")
		except frappe.ValidationError:
			frappe.rename_doc("Address", site.parent, f"{site.link_name}", merge=True)
