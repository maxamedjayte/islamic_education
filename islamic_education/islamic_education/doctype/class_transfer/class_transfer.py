import frappe
from frappe.model.document import Document

class ClassTransfer(Document):
    def before_save(self):
        from_class = frappe.get_doc("Class", self.from_class)
        to_class = frappe.get_doc("Class", self.to_class)
        
        if from_class.academic_year != to_class.academic_year:
            if self.transfer_type == "By Student":
                # Properly indented to align with the if statement
                students = frappe.get_list("Student", filters={"classe": from_class.name}, fields=["name"])
                for std in students:
                    if not std.status == "Active":
                        pass
                    enrolment = frappe.get_list("Class Enrolment", filters={"student": std.name, "current_class": from_class.name}, fields=["name"])
                    if not enrolment:
                        new_enrolment = frappe.new_doc("Class Enrolment")
                        new_enrolment.student = std.name
                        new_enrolment.current_classe = from_class.name
                        new_enrolment.enrolment_date = from_class.registered_date
                        new_enrolment.save()
                    
                    to_class_enrolment = frappe.get_list("Class Enrolment", filters={"student": std.name, "current_class": to_class.name}, fields=["name"])
                    if not to_class_enrolment:
                        new_enrolment = frappe.new_doc("Class Enrolment")
                        new_enrolment.student = std.name
                        new_enrolment.current_classe = to_class.name
                        new_enrolment.enrolment_date = to_class.registered_date
                        new_enrolment.save()

                        frappe.db.set_value("Student", std.name, "classe", to_class.name)
                        frappe.db.commit()
            else:
                # If the transfer_type is not "By Student"
                from_enrolment_students = frappe.get_list("Class Enrolment", filters={"current_class": from_class.name}, fields=["student"])
                for std in from_enrolment_students:
                    if not std.status:
                        std.status = "Active"
                    enrolment = frappe.get_list("Class Enrolment", filters={"student": std.student, "current_class": to_class.name}, fields=["name"])
                    if not enrolment:
                        new_enrolment = frappe.new_doc("Class Enrolment")
                        new_enrolment.student = std.student
                        new_enrolment.classe = to_class.name
                        new_enrolment.enrolment_date = to_class.registered_date
                        new_enrolment.save()
                        frappe.db.set_value("Student", std.student, "classe", to_class.name)
