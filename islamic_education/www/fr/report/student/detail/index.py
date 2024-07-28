import frappe

def get_context(context):
    print(f"{frappe.form_dict}\n\n\n\\n\n\n\n\nn\n\n\n\n")
    context.student = frappe.get_doc("Student", frappe.form_dict)
    print(context.student)
    return context