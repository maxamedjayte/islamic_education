import frappe

def get_context(context):
    context.attending_week = frappe.get_doc("Attend Week", frappe.form_dict)
    # get active academic years
    active_academic_year = frappe.get_all("Academic Year", filters={"active_academic_year": 1}, fields=["name"])
    context.classes = frappe.get_all("Class", fields=["name", "class_name"],filters={"academic_year": active_academic_year[0].name},)
    context.days = frappe.get_all("Day", fields=["name"])
    return context



def get_class_day_periods_with_students(attending_week,class_name, day_name):
    class_doc = frappe.get_doc("Class", class_name)
    day_doc = frappe.get_doc("Day", day_name)
    return {}
