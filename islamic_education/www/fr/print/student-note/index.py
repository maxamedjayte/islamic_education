import frappe

import frappe

def get_context(context):
    if 'classe' in frappe.form_dict:
        context.classe = frappe.get_doc("Class", frappe.form_dict['classe'])
    context.students = frappe.get_all("Student", filters={"classe": context.classe.name}, fields=["name", "student_name"])
    print('hellllllllll')
    print('\n\n\n\n\n\s')
    return context
