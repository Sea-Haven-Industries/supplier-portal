import frappe


@frappe.whitelist(allow_guest=True)
def validate_supplier_id(supplier_id: str) -> dict:
    if frappe.db.exists("Supplier", {"name": supplier_id}):
        user = frappe.get_doc("User", f"{supplier_id}@supplier-portal.com")
        portal_supplier = frappe.get_doc("Supplier", supplier_id)
        # login user
        frappe.local.login_manager.user = user.name
        frappe.local.login_manager.post_login()
        return {
            "status": "success",
            "message": "User logged in successfully",
            "supplier_id": supplier_id,
            "supplier_name": portal_supplier.company_name,
        }
    else:
        frappe.local.response["http_status_code"] = 404
        frappe.throw("Supplier not found", frappe.AuthenticationError)
