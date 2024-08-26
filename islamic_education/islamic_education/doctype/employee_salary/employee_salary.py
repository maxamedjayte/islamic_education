# Copyright (c) 2024, Maxamed Jayte and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class EmployeeSalary(Document):
    def before_save(self):
        self.balance = self.salary - self.paid_money

    def on_submit(self):
        if self.balance != 0:
            frappe.throw(f"Cannot submit because the balance is not zero. Please confirm to proceed.")
        else:
            frappe.db.set_value("Monthly Financial", self.salary_month, "total_salary", get_total_employee_salary(self.salary_month))


@frappe.whitelist()
def get_total_employee_salary(salary_month):
    result = frappe.db.sql("""SELECT SUM(paid_money) FROM `tabEmployee Salary` WHERE salary_month = %s AND docstatus = 1""", (salary_month,), as_list=True)
    total_salary = result[0][0] if result and result[0][0] is not None else 0
    return total_salary
