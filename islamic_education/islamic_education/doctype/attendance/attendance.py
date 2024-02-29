# Copyright (c) 2024, Maxamed Jayte and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Attendance(Document):
	pass


@frappe.whitelist()
def get_class_periods(the_class, day):
	# get class
	classe = frappe.get_doc("Class", the_class)
	# this classe.class_period list of dict i want to filter where day = day
	
	return classe.class_period