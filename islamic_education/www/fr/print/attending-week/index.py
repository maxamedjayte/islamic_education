import frappe

import frappe

def get_context(context):
    if 'attend_week' in frappe.form_dict:
        context.attending_week = frappe.get_doc("Attend Week", frappe.form_dict['attend_week'])
    if 'classe' in frappe.form_dict:
        context.classe = frappe.get_doc("Class", frappe.form_dict['classe'])
    context.days = frappe.get_all("Day", fields=["name"] )
    context.days.reverse()
    context.class_periods_by_day = {}
    for day in context.days:
        # Fetch class periods for each day
        class_periods = frappe.get_all("Class Period", filters={"parent": context.classe.name, "day": day.name}, fields=["name", "subject_name", "day_name", "period_time"])
        context.class_periods_by_day[day.name] = class_periods
    context.students = frappe.get_all("Student Class Enrolment", filters={"current_class": context.classe.name}, fields=["name", "student_name"]) if context.get('classe') else []
    
    return context
