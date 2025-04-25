import frappe


def execute(filters=None):
	columns = [
		{
			"fieldname": "invoice_number",
			"label": "Invoice Number",
			"fieldtype": "Link",
			"options": "Invoices",
		},
		{
			"fieldname": "supplier_name",
			"label": "Supplier Name",
			"fieldtype": "Data",
			"width": 200,
		},
		{"fieldname": "status", "label": "Status", "fieldtype": "Data", "width": 100},
		{"fieldname": "invoice_date", "label": "Invoice Date", "fieldtype": "Date"},
		{"fieldname": "due_date", "label": "Due Date", "fieldtype": "Date"},
		{"fieldname": "total_amount", "label": "Total Amount", "fieldtype": "Currency"},
	]

	conditions = ""
	if filters.get("invoice_date_from"):
		conditions += " AND invoice_date >= %(invoice_date_from)s"
	if filters.get("invoice_date_to"):
		conditions += " AND invoice_date <= %(invoice_date_to)s"
	if filters.get("supplier"):
		conditions += " AND supplier = %(supplier)s"
	if filters.get("status"):
		if not filters.get("status") == "All":
			conditions += " AND status = %(status)s"

	query = f"""
    SELECT
      name as invoice_number,
      supplier_name,
      status,
      invoice_date,
      due_date,
      total_amount
    FROM
      `tabInvoices`
    WHERE
      docstatus = 0 {conditions}
  """
	data = frappe.db.sql(query, filters, as_dict=True)
	return columns, data
