frappe.listview_settings['Supplier Portal Invoices'] = {
    before_render() {
        $('button[data-label="Add Supplier Portal Invoices"]>span>span').html('Add Invoice')
    },
}