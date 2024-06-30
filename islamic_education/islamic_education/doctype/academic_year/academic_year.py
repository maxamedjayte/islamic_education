# Copyright (c) 2024, Maxamed Jayte and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AcademicYear(Document):
	
	def before_save(self):
		if self.active_academic_year == 1:
			active_years = frappe.get_all('Academic Year', filters={'active_academic_year': 1, 'name': ('!=', self.name)})

			for year in active_years:
				doc = frappe.get_doc('Academic Year', year.name)
				doc.active_academic_year = 0
				doc.save()