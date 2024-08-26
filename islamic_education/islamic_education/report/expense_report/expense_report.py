import frappe

def get_columns(filters=None):
    columns = [
        {"label": "EXPENSE NAME", "fieldname": "expense_name", "fieldtype": "Data", "width": 200},
        {"label": "OBJECT NAME", "fieldname": "object_name", "fieldtype": "Data", "width": 200},
        {"label": "QUANTITY", "fieldname": "quantity", "fieldtype": "Int", "width": 100},
        {"label": "AMOUNT", "fieldname": "amount", "fieldtype": "Currency", "width": 150},
    ]
    return columns

def execute(filters=None):
    columns = get_columns(filters)
    data = []
    grand_total = 0
    
    # Define filter criteria including docstatus = 1 to get only submitted expenses
    filter_criteria = {"docstatus": 1}
    if filters and filters.get("expense_month"):
        filter_criteria["expense_month"] = filters.get("expense_month")
    
    # Fetch all submitted expenses based on filter criteria (or all submitted expenses if no filters are applied)
    expenses = frappe.get_all("Expense", filters=filter_criteria, fields=["name", "expense_name", "amount"])
    
    for expense in expenses:
        # Fetch all expense objects related to the expense
        expense_objects = frappe.get_all("Expense Object", filters={"parent": expense.name}, fields=["object_name", "quantity", "amount"])
        
        # Calculate the total amount for the expense
        if expense_objects:
            expense_total = sum(obj['amount'] for obj in expense_objects)
        else:
            expense_total = expense.amount
        
        grand_total += expense_total

        # Add the main expense row with bold and uppercase text for expense_name
        data.append({
            "expense_name": f"<b>{expense.expense_name.upper()}</b>",  # Bold and uppercase text for the expense name
            "amount": expense_total,  # Show the total amount (either sum of objects or expense amount)
            "indent": 0  # No indentation for the main expense
        })
        
        # Add each expense object as a sub-row under the expense
        for obj in expense_objects:
            data.append({
                "expense_name": "",  # Leave empty to align under the expense name
                "object_name": obj.object_name,
                "quantity": obj.quantity,
                "amount": obj.amount,
                "indent": 1  # Indent this row under the main expense
            })

    # Add a final row for the grand total
    data.append({
        "expense_name": "<b>TOTAL</b>",
        "amount": grand_total,  # Show the numeric value without HTML tags
        "indent": 0
    })

    return columns, data
