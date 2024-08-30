import frappe

def get_context(context):
    context.attending_week = frappe.get_doc("Attend Week", frappe.form_dict)
    # get active academic years
    active_academic_year = frappe.get_all("Academic Year", filters={"active_academic_year": 1}, fields=["name"])
    context.classes = frappe.get_all("Class", fields=["name", "class_name","academic_year"],filters={"academic_year": active_academic_year[0].name},)
    context.days = frappe.get_all("Day", fields=["name"])
    return context

