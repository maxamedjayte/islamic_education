# Copyright (c) 2024, Maxamed Jayte and contributors
# For license information, please see license.txt

import frappe

def get_columns(filters=None):
	columns = [
		{"label": "الطالاب", "fieldname": "student", "fieldtype": "Link", "options": "Student", "width": 200},
	]
	the_class = frappe.get_doc("Class", filters.get("the_class"))
	for period in the_class.class_period:
		columns.append({"label": period.subject_name +'-'+ period.period_time, "fieldname": period.name, "fieldtype": "Data", "width": 100})	
	return columns

def execute(filters=None):
	columns = get_columns(filters)
	data = []

	attendance = frappe.get_all("Attendance", filters={"class": filters.get("the_class"),"week":filters.get("the_week")}, fields=["*"])
	if not attendance:
		return columns, data
	else:
		attendance = attendance[0]

		attendance_table = frappe.get_all("Attending Table", filters={"parent": attendance.name}, fields=["*"])
	
		for std_attend in attendance_table:
			row = {"student": std_attend.student_name}
			
			data.append(row)

	return columns, data
