// Copyright (c) 2025, jeowsome15@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on("Site Code", {
	refresh(frm) {
		if (!frm.doc.__islocal) {
			frappe.contacts.render_address_and_contact(frm)
		} else {
			frappe.contacts.clear_address_and_contact(frm)
		}
	},
});
