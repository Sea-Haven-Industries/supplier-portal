# Copyright (c) 2024, jeowsome15@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import add_days, flt, getdate, nowdate


class Invoices(Document):
    def validate(self):
        self.set_total_amount()
        self.set_due_date()
        self.set_total_paid()
        self.update_amount_due()
        self.update_status()

    def on_update(self):
        self.update_suppliers_invoice()

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

    def set_total_paid(self):
        total_paid = 0
        for item in self.payment_references:
            total_paid += item.paid_amount
        self.db_set("paid_amount", total_paid)

    def update_status(self):
        if self.paid_amount == 0:
            self.status = "Unpaid"
        elif self.paid_amount < self.total_amount and self.paid_amount > 0:
            self.status = "Partially Paid"
        elif self.paid_amount == self.total_amount:
            self.status = "Paid"

        if getdate(nowdate()) > getdate(self.due_date):
            if self.paid_amount == 0:
                self.status = "Overdue"
            elif self.paid_amount < self.total_amount:
                self.status = "Partially Paid and Overdue"

        self.db_set("status", self.status, update_modified=False, commit=True)

    def update_amount_due(self):
        self.amount_due = self.total_amount - self.paid_amount

    def update_suppliers_invoice(self):
        supplier = frappe.get_doc("Supplier", self.supplier)

        # check if invoice already exists
        for invoice in supplier.invoices:
            if invoice.invoice_number == self.name:
                if invoice.total_due != self.total_amount:
                    invoice.total_amount = self.total_amount
                if invoice.invoice_date != self.invoice_date:
                    invoice.invoice_date = self.invoice_date
                if invoice.status != self.status:
                    invoice.status = self.status
                supplier.save()
                return

        supplier.append(
            "invoices",
            {"invoice_number": self.name},
        )
        supplier.save()
