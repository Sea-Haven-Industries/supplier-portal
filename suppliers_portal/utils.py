import frappe


def daily_invoice_status_update():
	invoices = frappe.get_all(
		"Invoices",
		filters={"status": ["in", ["Unpaid", "Partially Paid", "Partially Paid and Overdue"]]},
		fields=["name"],
	)
	for invoice in invoices:
		invoice_doc = frappe.get_doc("Invoices", invoice.name)
		invoice_doc.update_status()
		invoice_doc.save()
	frappe.db.commit()
