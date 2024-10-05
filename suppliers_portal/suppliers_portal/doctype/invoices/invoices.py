# Copyright (c) 2024, jeowsome15@gmail.com and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.utils import add_days, flt, nowdate


class Invoices(Document):
    def validate(self):
        self.set_total_amount()
        self.set_due_date()
        self.update_status()

    def set_total_amount(self):
        if self.get("supplier_invoice_items"):
            total_amount = 0
            for item in self.get("supplier_invoice_items"):
                item.amount = flt(item.rate) * flt(item.quantity)
                total_amount += item.amount
            self.db_set("total_amount", total_amount)

    def set_due_date(self):
        if self.invoice_terms:
            if self.invoice_terms == "NET 10":
                self.due_date = add_days(self.invoice_date, 10)
            elif self.invoice_terms == "NET 15":
                self.due_date = add_days(self.invoice_date, 15)
            elif self.invoice_terms == "NET 30":
                self.due_date = add_days(self.invoice_date, 30)
            elif self.invoice_terms == "NET 45":
                self.due_date = add_days(self.invoice_date, 45)
            elif self.invoice_terms == "NET 60":
                self.due_date = add_days(self.invoice_date, 60)

    def update_status(self):
        if self.payment_reference_no and self.payment_reference_date:
            self.status = "Paid"
        elif self.status == "Unpaid" and nowdate() > self.due_date:
            self.status = "Overdue"
        else:
            self.status = "Unpaid"
