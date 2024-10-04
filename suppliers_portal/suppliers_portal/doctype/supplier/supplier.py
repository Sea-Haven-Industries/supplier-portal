# Copyright (c) 2024, jeowsome15@gmail.com and contributors
# For license information, please see license.txt

import random

import frappe
from frappe.model.document import Document


class Supplier(Document):
    def generate_supplier_id(self, length: int = 8) -> str:
        # generate unique supplier integer id based on length
        supplier_id = random.randint(10 ** (length - 1), 10**length - 1)

        while frappe.db.exists("Supplier", {"supplier_id": supplier_id}):
            supplier_id = random.randint(10 ** (length - 1), 10**length - 1)

        return str(supplier_id)

    def autoname(self):
        self.name = self.generate_supplier_id()

    def after_insert(self):
        self.create_user()

    def create_user(self):
        user = frappe.new_doc("User")
        user.update(
            {
                "email": f"{self.name}@supplier-portal.com",
                "first_name": f"Supplier {self.name}",
                "roles": [{"role": "Portal Supplier"}],
                "new_password": self.name,
            }
        )
        user.insert()
        self.user = user.name
        self.save()
