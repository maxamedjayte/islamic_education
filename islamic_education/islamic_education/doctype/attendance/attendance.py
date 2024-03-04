# Copyright (c) 2024, Maxamed Jayte and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Attendance(Document):
	pass


@frappe.whitelist()
def get_class_periods(the_class):
	# get class
	classe = frappe.get_doc("Class", the_class)
	return classe.class_period



@frappe.whitelist()
def delete_attendance(attendance_id):
	exam = frappe.get_doc("Attendance", attendance_id)
	for i in exam.attending_table:
		# clear this child table
		i.delete()
		frappe.db.commit()
	return "Attendance Deleted Successfully"

