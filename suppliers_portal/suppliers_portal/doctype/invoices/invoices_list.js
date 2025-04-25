frappe.listview_settings['Invoices'] = {
	before_render() {
		$('button[data-label="Add Invoices"]>span>span').html('Add Invoice')
	},
}
