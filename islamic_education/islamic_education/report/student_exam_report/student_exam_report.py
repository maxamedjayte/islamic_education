# Copyright (c) 2024, Maxamed Jayte and contributors
# For license information, please see license.txt

import frappe


def get_columns(filters=None):
	columns = []
	the_student = frappe.get_doc("Student",filters.get("student"))
	
	subjects = frappe.get_all("Subject",filters={"the_classe":the_student.classe}, fields=["name", "subject_name"])

	columns.extend([{"fieldname": subject.subject_name, "label": subject.subject_name, "fieldtype": "Float", "width": 120} for subject in subjects])
	columns.extend({"label": "مجموع", "fieldname": "total", "fieldtype": "Float", "width": 100})

	return columns , the_student ,subjects
def execute(filters=None):
	columns,the_student,subjects = get_columns(filters)

	data = []

	for subject in subjects:
		exam_marks = frappe.get_all("Exam Marks", filters={"subject": subject.name,"student":the_student.name}, fields=["name"])
		print(exam_marks)





	return columns, data
