import frappe
from frappe.model.document import Document

class ClassEnrolment(Document):
    def on_trash(self):
        # Retrieve the student document
        student = frappe.get_doc("Student", self.student)

        # Retrieve the specific 'student_graduated_class' child to be removed
        to_remove = None
        for d in student.get("student_graduated_class"):
            if d.classe == self.classe:
                to_remove = d
                break

        # Check if we found the entry and then remove it
        if to_remove:
            student.remove(to_remove)
            student.save()
            frappe.db.commit()

    def before_save(self):
        # Retrieve the student document
        student = frappe.get_doc("Student", self.student)
        
        # Ensure the Status field is set
        if not student.status:
            frappe.throw("This student is not active")

        # Query current class enrollments excluding the current one if it's an update
        class_enrolments = frappe.get_list("Class Enrolment", 
                                           filters={"student": self.student, 
                                                    "classe": self.classe,
                                                    "name": ["!=", self.name]}, 
                                           fields=["name"])

        # Check if the student is already enrolled in this class
        if class_enrolments:
            frappe.throw("Student is already enrolled in this class")
        else:
            # Check if 'student_graduated_class' field list exists in the student document
            if not hasattr(student, 'student_graduated_class'):
                student.student_graduated_class = []

            # Check if student has a current class set before appending to 'student_graduated_class'
            if student.classe:
                student.append("student_graduated_class", {
                    "classe": self.classe,  # Use the classe from ClassEnrolment, not from Student
                    "parent": student.name,
                    "parenttype": "Student",
                    "parentfield": "student_graduated_class"
                })

            # Update student's current class after adding to graduated class
            student.classe = self.classe

            # Save changes to the student document
            student.save()
            frappe.db.commit()
