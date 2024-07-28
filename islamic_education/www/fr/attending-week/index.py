import frappe

def get_context(context):
    context.attending_week = frappe.get_doc("Attend Week", frappe.form_dict)
    context.classes = frappe.get_all("Class", fields=["name", "class_name"])
    context.days = frappe.get_all("Day", fields=["name"])
    print(context)
    return context



def get_class_day_periods_with_students(attending_week,class_name, day_name):
    class_doc = frappe.get_doc("Class", class_name)
    day_doc = frappe.get_doc("Day", day_name)
    return {}
