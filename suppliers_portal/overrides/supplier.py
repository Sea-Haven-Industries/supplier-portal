import random

import frappe


def generate_supplier_id(supplier, method=None):
	# skip ID creation during patch migrations
	if frappe.flags.in_patch:
		return

	length = 8
	supplier_id = random.randint(10 ** (length - 1), 10**length - 1)
	while frappe.db.exists("Supplier", {"supplier_id": supplier_id}):
		supplier_id = random.randint(10 ** (length - 1), 10**length - 1)
	supplier.name = str(supplier_id)


def create_user(supplier, method=None):
	# skip user creation during patch migrations
	if frappe.flags.in_patch:
		return

	# create role if it doesn't exist
	if not frappe.db.exists("Role", "Portal Supplier"):
		frappe.get_doc(
			{
				"doctype": "Role",
				"role_name": "Portal Supplier",
				"desk_access": False,
			}
		).insert()

	user = frappe.new_doc("User")
	user.update(
		{
			"email": f"{supplier.name}@supplier-portal.com",
			"first_name": supplier.supplier_name,
			"roles": [{"role": "Portal Supplier"}],
			"new_password": supplier.name,
			"send_welcome_email": False,
		}
	)
	user.flags.ignore_password_policy = True
	user.insert()

	supplier.append("portal_users", {"user": user.name})
	supplier.save()
