import json
import re

import frappe
from erpnext.accounts.doctype.account.account import update_account_number
from erpnext.accounts.utils import get_account_name
from erpnext.setup.utils import enable_all_roles_and_domains
from frappe.contacts.doctype.address.address import get_address_display
from frappe.desk.page.setup_wizard.setup_wizard import setup_complete
from frappe.utils import getdate, update_progress_bar

######################## PATCH PREREQUISITES ########################
# - This patch should be run on a fresh site with ERPNext installed (`suppliers_portal` should be installed after `erpnext`)
# - The following files (containing exported doctype records) must be setup in the
#   site's private backups folder:
#   - users.json (the 'send_welcome_email' field should be set to 0 otherwise it'll
#     try to send welcome emails)
#   - suppliers.json (remove duplicate entry for 'Superior Backflow Services, LLC')
#   - invoices.json


def execute():
	setup_site()
	setup_accounts()
	create_fiscal_years()
	create_roles()
	import_users()
	create_items()
	create_payment_terms_template()
	import_suppliers()
	import_invoices()


def setup_site():
	print("Setting up site")
	frappe.clear_cache()
	today = getdate()
	setup_complete(
		{
			"currency": "USD",
			"full_name": "Administrator",
			"company_name": "Sea Haven Industries",
			"timezone": "America/New_York",
			"company_abbr": "SHI",
			"domains": ["Services"],
			"country": "United States",
			"fy_start_date": today.replace(month=1, day=1).isoformat(),
			"fy_end_date": today.replace(month=12, day=31).isoformat(),
			"language": "en-US",
			"company_tagline": "Sea Haven Industries",
			"email": "support@seahavenindustries.com",
			"password": "admin",
			"chart_of_accounts": "Standard with Numbers",
			"bank_account": "Primary Checking",
		}
	)
	enable_all_roles_and_domains()
	for module in frappe.get_all("Module Onboarding"):
		frappe.db.set_value("Module Onboarding", module, "is_complete", True)
	frappe.db.set_value("User", "Administrator", "time_zone", "America/New_York")
	frappe.db.commit()


def setup_accounts():
	abbr = frappe.db.get_value("Company", "Sea Haven Industries", "abbr")

	frappe.rename_doc(
		"Account",
		f"1000 - Application of Funds (Assets) - {abbr}",
		f"1000 - Assets - {abbr}",
		force=True,
	)
	frappe.rename_doc(
		"Account",
		f"2000 - Source of Funds (Liabilities) - {abbr}",
		f"2000 - Liabilities - {abbr}",
		force=True,
	)
	frappe.rename_doc(
		"Account",
		f"1310 - Debtors - {abbr}",
		f"1310 - Accounts Receivable - {abbr}",
		force=True,
	)
	frappe.rename_doc(
		"Account",
		f"2110 - Creditors - {abbr}",
		f"2110 - Accounts Payable - {abbr}",
		force=True,
	)
	update_account_number(f"1110 - Cash - {abbr}", "Petty Cash", account_number="1110")
	update_account_number(f"Primary Checking - {abbr}", "Primary Checking", account_number="1201")


def create_fiscal_years():
	for year in range(2020, 2027):
		if not frappe.db.exists("Fiscal Year", str(year)):
			fiscal_year = frappe.new_doc("Fiscal Year")
			fiscal_year.update(
				{
					"year": str(year),
					"year_start_date": getdate(f"{year}-01-01"),
					"year_end_date": getdate(f"{year}-12-31"),
				}
			)
			fiscal_year.insert(ignore_permissions=True)


def create_roles():
	roles = ["Portal Supplier", "Supplier"]
	for role in roles:
		if not frappe.db.exists("Role", role):
			role_doc = frappe.new_doc("Role")
			role_doc.update(
				{
					"role_name": role,
					"desk_access": False,
				}
			)
			role_doc.insert(ignore_permissions=True)


def import_users():
	print("Importing users")
	users_file = frappe.get_site_path("private", "backups", "users.json")
	frappe.import_doc(users_file)


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


def create_address(doc):
	address = frappe.new_doc("Address")
	address.update(
		{
			"address_type": "Billing",
			"address_title": doc.get("title"),
			"address_line1": doc.get("street"),
			"city": doc.get("city") or "Unknown",
			"state": doc.get("state"),
			"pincode": doc.get("zip_code"),
			"country": "United States",
			"is_primary_address": True,
			"is_shipping_address": True,
			"links": [
				{
					"link_doctype": doc.get("ref_doctype"),
					"link_name": doc.get("ref_name"),
				},
			],
		}
	)

	try:
		address.insert(ignore_permissions=True)
	except Exception as e:
		print(f"Error inserting address for {doc.get('ref_name')}: {e}")
		return frappe._dict()

	return address


def import_suppliers():
	suppliers_file = frappe.get_site_path("private", "backups", "suppliers.json")
	with open(suppliers_file) as f:
		suppliers = json.load(f)
		print(len(suppliers))
		for idx, supplier in enumerate(suppliers):
			update_progress_bar(f"Importing Suppliers: {idx}", idx, (len(suppliers)))
			supplier_doc = frappe.new_doc("Supplier")
			supplier_doc.update(
				{
					"supplier_name": supplier.get("name"),
					"portal_users": [{"user": supplier.get("user")}],
					"owner": supplier.get("owner"),
					"creation": supplier.get("creation"),
				}
			)
			supplier_doc.save()
			supplier_docname = frappe.rename_doc(
				"Supplier", supplier_doc.name, supplier.get("name"), force=True
			)
			frappe.db.set_value('Supplier', supplier_docname, 'supplier_name', supplier.get("company_name"))

			if supplier.get("street"):
				address = create_address(
					{
						**supplier,
						"title": supplier.get("company_name"),
						"ref_doctype": "Supplier",
						"ref_name": supplier_docname,
					}
				)

				if address:
					address_display = get_address_display(address.name)
					supplier_doc.db_set("supplier_primary_address", address.name)
					supplier_doc.db_set("primary_address", address_display)


def import_invoices():
	invoices_file = frappe.get_site_path("private", "backups", "invoices.json")
	with open(invoices_file) as f:
		invoices = json.load(f)
		for idx, invoice in enumerate(invoices):
			update_progress_bar("Importing invoices", idx, (len(invoices)))

			# skip if purchase invoice already exists
			if frappe.db.exists("Purchase Invoice", {"name": invoice.get("name")}):
				continue

			site_code = get_site_code(invoice)
			invoice_doc = frappe.new_doc("Purchase Invoice")
			supplier = frappe.db.get_value('Supplier', invoice.get("supplier"), 'name')
			invoice_doc.update(
				{
					"supplier": invoice.get("supplier"),
					"bill_no": invoice.get("supplier_invoice_number"),
					"supplier_name": frappe.get_value('Supplier', invoice.get("supplier"), 'supplier_name'),
					"site_code": site_code or "",
					"set_posting_time": True,
					"bill_date": getdate(invoice.get("invoice_date")),
					"posting_date": getdate(invoice.get("invoice_date")),
					"service_date": getdate(invoice.get("service_date")),
					"due_date": getdate(invoice.get("due_date")),
					"payment_terms_template": invoice.get("invoice_terms"),
					"remarks": invoice.get("notes"),
					"owner": invoice.get("owner"),
					"creation": invoice.get("creation"),
				}
			)

			for item in invoice.get("supplier_invoice_items"):
				invoice_doc.append(
					"items",
					{
						"item_code": item.get("service_type"),
						"received_qty": item.get("quantity"),
						"qty": item.get("quantity"),
						"rate": item.get("rate"),
					},
				)

			# to avoid validating the custom due dates based on payment terms
			invoice_doc.ignore_default_payment_terms_template = True

			try:
				invoice_doc.insert(ignore_permissions=True)
			except Exception as e:
				print(f"Error inserting invoice {invoice_doc.bill_no}: {e}")
				continue

			if invoice.get("street"):
				if site_code:
					if frappe.db.exists("Site Code", site_code):
						site_code_doc = frappe.get_doc("Site Code", site_code)
					else:
						site_code_doc = frappe.new_doc("Site Code")
						site_code_doc.site_code = site_code
						site_code_doc.save(ignore_permissions=True)

					address = create_address(
						{
							**invoice,
							"title": site_code,
							"ref_doctype": "Site Code",
							"ref_name": site_code_doc.name,
						}
					)
					invoice_doc.dispatch_address = address.name
					invoice_doc.save()
				else:
					address = create_address(
						{
							**invoice,
							"title": invoice.get("supplier"),
							"ref_doctype": "Supplier",
							"ref_name": invoice.get("supplier"),
						}
					)
					invoice_doc.supplier_address = address.name
					invoice_doc.save()

			try:
				invoice_doc.submit()
			except Exception as e:
				print(f"Error submitting invoice {invoice_doc.bill_no}: {e}")
				continue

			for payment in invoice.get("payment_references"):
				payment_doc = frappe.new_doc("Payment Entry")
				payment_doc.update(
					{
						"payment_type": "Pay",
						"posting_date": getdate(payment.get("payment_reference_date")),
						"party_type": "Supplier",
						"party": invoice.get("supplier"),
						"paid_amount": payment.get("paid_amount"),
						"received_amount": payment.get("paid_amount"),
						"paid_from": get_account_name("Bank", "Asset"),
						"reference_no": payment.get("payment_reference_number")
						or "Note: Missing reference during ERPNext import",
						"reference_date": getdate(payment.get("payment_reference_date")),
						"references": [
							{
								"reference_doctype": invoice_doc.doctype,
								"reference_name": invoice_doc.name,
								"allocated_amount": payment.get("paid_amount"),
							}
						],
					}
				)

				try:
					payment_doc.insert(ignore_permissions=True)
					payment_doc.submit()
				except Exception as e:
					print(f"Error importing payment for invoice {invoice_doc.bill_no}: {e}")


def get_site_code(invoice):
	if invoice.get("site_code"):
		return invoice["site_code"].upper()

	# try to find it in the notes
	site_pattern = re.compile(r"\bsite\s+([A-Z0-9]+)", re.IGNORECASE)
	notes = invoice.get("notes", "")
	if notes:
		matches = site_pattern.findall(notes)
		if len(matches) > 0:
			return ", ".join(matches).upper()
