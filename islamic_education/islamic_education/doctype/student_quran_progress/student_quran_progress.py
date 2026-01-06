# Copyright (c) 2025, Maxamed Jayte and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime, date
from calendar import monthrange


class StudentQuranProgress(Document):
	def validate(self):
		# Validate duplicate students in the table
		students = set()
		for row in self.madarasa_students_quran_level:
			if row.madarasa_student in students:
				frappe.throw(f"Duplicate student: {row.student_name}")
			students.add(row.madarasa_student)
		
		# Validate duplicate month and class combination
		if self.month and self.madarasa_class:
			# Parse the month date - handle string, date, or datetime objects
			if isinstance(self.month, str):
				month_date = datetime.strptime(self.month, "%Y-%m-%d").date()
			elif isinstance(self.month, datetime):
				month_date = self.month.date()
			elif isinstance(self.month, date):
				month_date = self.month
			else:
				# Fallback: try to convert to string and parse
				month_date = datetime.strptime(str(self.month), "%Y-%m-%d").date()
			
			year = month_date.year
			month = month_date.month
			
			# Calculate first and last day of the month
			last_day = monthrange(year, month)[1]
			first_day = f"{year}-{month:02d}-01"
			last_day_str = f"{year}-{month:02d}-{last_day:02d}"
			
			# Build filters to check for existing documents with same month and class
			filters = {
				"madarasa_class": self.madarasa_class,
				"month": ["between", [first_day, last_day_str]]
			}
			
			# Exclude current document if it's an update
			if self.name:
				filters["name"] = ["!=", self.name]
			
			existing_doc = frappe.get_all(
				"Student Quran Progress",
				filters=filters,
				limit=1
			)
			
			if existing_doc:
				# Format month name for error message
				month_names = ["January", "February", "March", "April", "May", "June",
							   "July", "August", "September", "October", "November", "December"]
				month_name = f"{month_names[month - 1]} {year}"
				frappe.throw(
					f"Student Quran Progress for {self.madarasa_class} in {month_name} already exists. "
					f"Please use the existing document or select a different month."
				)

	def on_submit(self):
		self.push_quran_progress_to_students()

	def push_quran_progress_to_students(self):
		for row in self.madarasa_students_quran_level:
			self.add_student_quran_level(row)

	def add_student_quran_level(self, row):
		student = frappe.get_doc("Madarasa Student", row.madarasa_student)
		print(row)
		student.append("student_quran_level", {
			"surah": row.surah,
			"surah_number": row.surah_number,
			"ayah_number": row.ayah_number,
			"month": row.month
		})

		student.save(ignore_permissions=True)




@frappe.whitelist()
def get_madarasa_students_by_class(madarasa_class):
    return frappe.get_all(
		"Madarasa Student",
		filters={
			"madarasa_class":madarasa_class,
			"status":"Active"
		},
		fields=[
			"name","student_name","gender"
		]
	)