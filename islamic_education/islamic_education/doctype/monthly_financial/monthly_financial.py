# Copyright (c) 2024, Maxamed Jayte and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MonthlyFinancial(Document):
    # on refresh
    
    monthly_financials = frappe.get_all("Monthly Financial", fields=["*"])
    for monthly in monthly_financials:
        # get all expenses
        expenses = frappe.get_all("Expense", filters={"expense_month": monthly.name}, fields=["*"])
        # get all salaries
        salaries = frappe.get_all("Salary", filters={"salary_month": monthly.name}, fields=["*"])
        
        total_expense = 0
        total_salary = 0
        for expense in expenses:
            print(expense)
            print(expense.amount)
            total_expense += expense.amount
        for salary in salaries:
            total_salary += salary.paided
        
        frappe.db.set_value("Monthly Financial", monthly.name, "total_expence",total_expense)
        frappe.db.set_value("Monthly Financial", monthly.name, "total_salary",total_salary)
        frappe.db.commit()
        
    

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
