# Copyright (c) 2024, Maxamed Jayte and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Student(Document):
	pass





@frappe.whitelist(allow_guest=True)
def student_exam_detail(student_id):
    # Render the template and pass the student details to it
    return frappe.render_template("/report/student-exam-detail/index.html", {"student": student_id})
