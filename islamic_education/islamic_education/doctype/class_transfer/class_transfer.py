import frappe
from frappe.model.document import Document

class ClassTransfer(Document):
    def before_save(self):
        from_class = frappe.get_doc("Class", self.from_class)
        to_class = frappe.get_doc("Class", self.to_class)
        
        # Ensure transfer only happens if academic years are different
        if from_class.academic_year != to_class.academic_year:
            if self.transfer_type == "By Student":
                students = frappe.get_list("Student", filters={"classe": from_class.name}, fields=["name", "status"])
                for student in students:
                    if student.status == "Active":
                        # Check existing enrollment in from_class
                        enrolment = frappe.get_list("Student Class Enrolment", filters={
                            "student": student.name,
                            "current_class": from_class.name
                        }, fields=["name"])
                        if not enrolment:
                            # Create enrolment in from_class if it doesn't exist
                            new_enrolment = frappe.new_doc("Student Class Enrolment")
                            new_enrolment.student = student.name
                            new_enrolment.current_class = from_class.name
                            new_enrolment.enrolment_date = from_class.registered_date
                            new_enrolment.save()
                        
                        # Check existing enrolment in to_class
                        to_class_enrolment = frappe.get_list("Student Class Enrolment", filters={
                            "student": student.name,
                            "current_class": to_class.name
                        }, fields=["name"])
                        if not to_class_enrolment:
                            # Create enrolment in to_class if it doesn't exist
                            new_to_enrolment = frappe.new_doc("Student Class Enrolment")
                            new_to_enrolment.student = student.name
                            new_to_enrolment.current_class = to_class.name
                            new_to_enrolment.enrolment_date = to_class.registered_date
                            new_to_enrolment.save()
                            
                            # Update student's class
                            frappe.db.set_value("Student", student.name, "classe", to_class.name)
            else:
                # Handle other transfer types (e.g., "By Enrolment")
                from_enrolment_students = frappe.get_list("Student Class Enrolment", filters={
                    "current_class": from_class.name
                }, fields=["student"])
                for enrolment in from_enrolment_students:
                    # Check and create enrolment in to_class
                    if not frappe.get_value("Student Class Enrolment", {"student": enrolment.student, "current_class": to_class.name}, "name"):
                        new_enrolment = frappe.new_doc("Student Class Enrolment")
                        new_enrolment.student = enrolment.student
                        new_enrolment.current_class = to_class.name
                        new_enrolment.enrolment_date = to_class.registered_date
                        new_enrolment.save()
                        frappe.db.set_value("Student", enrolment.student, "classe", to_class.name)

        frappe.db.commit()  # Ensure all database transactions are committed after processing
