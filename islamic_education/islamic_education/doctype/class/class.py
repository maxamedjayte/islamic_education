# Copyright (c) 2024, Maxamed Jayte and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


def update_student_counts():
    classes = frappe.get_list("Class", filters={}, fields=["*"])
    # make loop to get all students for each class
    for classe in classes:
        students = frappe.get_list("Student", filters={"classe": classe.name}, fields=["*"])
        # update student_counts in this classe
        frappe.db.set_value("Class", classe.name, "student_counts", len(students))
        frappe.db.commit()


class Class(Document):
    def before_save(self):
	    update_student_counts()

