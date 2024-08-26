import frappe

def get_columns(filters=None):
    columns = [
        {"label": "EMPLOYEE NAME", "fieldname": "employee_name", "fieldtype": "Data", "width": 200},
        {"label": "SALARY MONTH", "fieldname": "salary_month", "fieldtype": "Link", "options": "Monthly Financial", "width": 150},
        {"label": "SALARY", "fieldname": "salary", "fieldtype": "Currency", "width": 150},
        {"label": "BANK NAME", "fieldname": "bank_name", "fieldtype": "Data", "width": 150},
        {"label": "BANK ACCOUNT", "fieldname": "bank_acc", "fieldtype": "Data", "width": 150},
        {"label": "MOBILE NUMBER", "fieldname": "mobile_number", "fieldtype": "Data", "width": 150},
        {"label": "PAID MONEY", "fieldname": "paid_money", "fieldtype": "Currency", "width": 150},
        {"label": "BALANCE", "fieldname": "balance", "fieldtype": "Currency", "width": 150},
    ]
    return columns

def execute(filters=None):
    columns = get_columns(filters)
    data = []
    
    # Define filter criteria including docstatus = 1 to get only submitted salary records
    filter_criteria = {"docstatus": 1}
    
    if filters.get("salary_month"):
        filter_criteria["salary_month"] = filters.get("salary_month")
    
    if filters.get("employee"):
        filter_criteria["employee"] = filters.get("employee")
    
    # Fetch all submitted salary records based on filter criteria
    salaries = frappe.get_all("Employee Salary", filters=filter_criteria, fields=["employee_name", "salary_month", "salary", "paid_money", "balance", "bank_name", "bank_acc", "mobile_number"])
    
    for salary in salaries:
        # Add the salary details for each employee
        data.append({
            "employee_name": salary.employee_name,
            "salary_month": salary.salary_month,
            "salary": salary.salary,
            "bank_name": salary.bank_name,
            "bank_acc": salary.bank_acc,
            "mobile_number": salary.mobile_number,
            "paid_money": salary.paid_money,
            "balance": salary.balance,
        })

    return columns, data
