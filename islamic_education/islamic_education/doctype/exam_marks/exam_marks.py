# Copyright (c) 2024, Maxamed Jayte and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ExamMarks(Document):
	pass
	
	def before_save(self):
		exam_announcement = frappe.get_value("Exam Announcement", self.exam_announcement, "exam_type")
		classe = frappe.get_value("Class", self.the_class, "class_name")
		subject = frappe.get_value("Subject", self.subject, "subject_name")
		exam_type= frappe.get_list("Exam Types",filters={"name": exam_announcement}, fields=["*"] )
		
		
		self.exam_info = f'[ {exam_type[0]["exam_name"]} ]- {classe} - {subject}'



@frappe.whitelist()
def get_exam_marks(exam_announcement,the_class,subject):
	# get the exam marks
	exam_marks = frappe.get_list("Exam Marks", filters={
		"exam_announcement": exam_announcement,
		"subject": subject,
		"the_class": the_class
	}, fields=["*"])
	return exam_marks


@frappe.whitelist()
def get_students(class_id):
	students = frappe.get_list(
		"Student", filters={"classe": class_id}, fields=["*"])
	return students

@frappe.whitelist()
def delete_exam_marks(exam_id):
	exam = frappe.get_doc("Exam Marks", exam_id)
	for i in exam.exam_entry_marks:
		# clear this child table
		i.delete()
		frappe.db.commit()
	return "Exam Deleted Successfully"