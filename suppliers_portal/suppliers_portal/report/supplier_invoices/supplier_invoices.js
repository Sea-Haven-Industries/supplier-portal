frappe.query_reports["Supplier Invoices"] = {
    "filters": [
        {
            "fieldname": "invoice_date_from",
            "label": __("Invoice Date From"),
            "fieldtype": "Date",
            "default": frappe.datetime.add_months(frappe.datetime.get_today(), -1), // Default to last month
            "placeholder": __("Invoice Date From")
        },
        {
            "fieldname": "invoice_date_to",
            "label": __("Invoice Date To"),
            "fieldtype": "Date",
            "default": frappe.datetime.get_today(), // Default to today
        },
        {
            "fieldname": "supplier",
            "label": __("Supplier"),
            "fieldtype": "Link",
            "options": "Supplier"
        },
        {
            "fieldname": "status",
            "label": __("Status"),
            "fieldtype": "Select",
            "options": "All\nPaid\nUnpaid\nOverdue",
            "default": "All",
        }
    ]
};