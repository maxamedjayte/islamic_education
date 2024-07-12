# Copyright (c) 2024, Maxamed Jayte and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Expense(Document):
    def before_save(self):
        total_amount = 0
        for obj in self.expence_object:
            total_amount += obj.amount

        self.amount= total_amount
        pass


    def on_submit(self):
        frappe.db.set_value("Monthly Financial", self.expense_month, "total_expence", get_total_expence(self.expense_month))




@frappe.whitelist()
def get_total_expence(monthly_financial):
    result = frappe.db.sql("""SELECT SUM(amount) FROM `tabExpense` WHERE expense_month = %s AND docstatus = 1""", (monthly_financial,), as_list=True)
    total_expence = result[0][0] if result and result[0][0] is not None else 0
    return total_expence

