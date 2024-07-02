import frappe
from frappe.model.document import Document

class ClassTransfer(Document):
    def on_submit(self):
        from_class = frappe.get_doc("Class", self.from_class)
        to_class = frappe.get_doc("Class", self.to_class)
        
		
        if from_class.academic_year != to_class.academic_year:
            students = frappe.get_list("Student", filters={"classe": from_class.name,"status":"Active"}, fields=["*"])
            for std in students:
                student = frappe.get_doc("Student", std.name)
                new_student = frappe.copy_doc(student)
                new_student.classe = to_class.name
                new_student.insert()
