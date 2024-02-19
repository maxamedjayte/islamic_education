# Copyright (c) 2024, Maxamed Jayte and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MonthlyFinancial(Document):
    pass
    def after_insert(self):
        # get all employess
        employees = frappe.get_all("Employee", filters={"status": "Active"}, fields=["*"])
        for employee in employees:
            salary = frappe.new_doc("Salary")
            salary.salary_month=self.name
            salary.employee = employee.name
            salary.salary = employee.ctc
            salary.paided = 0
            salary.balance = employee.ctc
            salary.save()



@frappe.whitelist()
def get_monthly_financial():
    return frappe.get_all("Monthly Financial", fields=["*"])
