# Copyright (c) 2024, Maxamed Jayte and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MonthlyFinancial(Document):
    # on refresh
    pass
    # monthly_financials = frappe.get_all("Monthly Financial", fields=["*"])
    # for monthly in monthly_financials:
    #     # get all expenses
    #     expenses = frappe.get_all("Expense", filters={"expense_month": monthly.name}, fields=["*"])
    #     # get all salaries
    #     salaries = frappe.get_all("Employee Salary", filters={"salary_month": monthly.name}, fields=["*"])
        
    #     total_expense = 0
    #     total_salary = 0
    #     for expense in expenses:
    #         total_expense += expense.amount
    #     for salary in salaries:
    #         total_salary += salary.paid_money
        
    #     frappe.db.set_value("Monthly Financial", monthly.name, "total_expence",total_expense)
    #     frappe.db.set_value("Monthly Financial", monthly.name, "total_salary",total_salary)
    #     frappe.db.commit()
        
    

    # def after_insert(self):
    #     # get all employess
    #     employees = frappe.get_all("Employee", filters={"status": "Active"}, fields=["*"])
    #     for employee in employees:
    #         salary = frappe.new_doc("Employee Salary")
    #         salary.salary_month=self.name
    #         salary.employee = employee.name
    #         salary.salary = employee.ctc
    #         salary.paid_money = 0
    #         salary.balance = employee.ctc
    #         salary.save()



@frappe.whitelist()
def get_monthly_financial():
    return frappe.get_all("Monthly Financial", fields=["*"])


@frappe.whitelist()
def get_total_expence(monthly_financial):
    result = frappe.db.sql("""SELECT SUM(amount) FROM `tabExpense Task` WHERE expense_month = %s AND docstatus = 1""", (monthly_financial,), as_list=True)
    total_expence = result[0][0] if result and result[0][0] is not None else 0
    return total_expence


@frappe.whitelist()
def get_total_employee_salary(monthly_financial):
    result = frappe.db.sql("""SELECT SUM(paid_money) FROM `tabExpense Task` WHERE expense_month = %s AND docstatus = 1""", (monthly_financial,), as_list=True)
    total_expence = result[0][0] if result and result[0][0] is not None else 0
    return total_expence




@frappe.whitelist()
def generate_salaries(monthly_financial_name):
    employees = frappe.get_all('Worker', filters={'ctc': ['>', 0]}, fields=['name', 'employee_name', 'ctc', 'bank_name', 'bank_ac_no', 'cell_number'])

    generated_count = 0
    for employee in employees:
        if not frappe.db.exists('Employee Salary', {'employee': employee['name'], 'salary_month': monthly_financial_name}):
            salary_doc = frappe.get_doc({
                'doctype': 'Employee Salary',
                'employee': employee['name'],
                'employee_name': employee['employee_name'],
                'salary': employee['ctc'],
                'salary_month': monthly_financial_name,
                'bank_name': employee['bank_name'],
                'bank_acc': employee['bank_ac_no'],
                'mobile_number': employee['cell_number'],
                'paid_money': employee['ctc'],
                'docstatus': 0  # Draft status
            })
            salary_doc.insert()
            generated_count += 1

    return f"{generated_count} salaries generated successfully."