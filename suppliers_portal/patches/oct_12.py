import frappe


def execute():
    update_supplier_invoices()
    update_invoice_status()


def update_supplier_invoices():
    suppliers = frappe.get_list("Supplier", pluck="name")

    for supplier in suppliers:
        supplier_doc = frappe.get_doc("Supplier", supplier)
        invoices = frappe.get_list(
            "Invoices", filters={"supplier": supplier}, pluck="name"
        )
        if len(invoices) == 0:
            continue

        supplier_doc.set("invoices", [])
        for invoice in invoices:
            supplier_doc.append("invoices", {"invoice_number": invoice})

        supplier_doc.save()

    frappe.db.commit()


def update_invoice_status():
    invoices = frappe.get_list("Invoices", pluck="name")

    for invoice in invoices:
        invoice_doc = frappe.get_doc("Invoices", invoice)
        invoice_doc.update_status()

    frappe.db.commit()
