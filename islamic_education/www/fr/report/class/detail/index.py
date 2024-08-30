import frappe

def get_context(context):
    context.classe = frappe.get_doc("Class", frappe.form_dict)
    # get active academic years
    print('\n\n\n\n\n\n\n bbbb')
    return context

