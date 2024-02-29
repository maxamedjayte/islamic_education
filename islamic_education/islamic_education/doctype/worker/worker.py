# Copyright (c) 2024, Maxamed Jayte and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Worker(Document):
    # after save
    def after_insert(self):
        # employee_name = first name + last name 
        self.employee_name  = self.first_name +" " + self.middle_name + " " + self.last_name
        self.save()