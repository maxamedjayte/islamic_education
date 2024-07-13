import frappe
from frappe.model.document import Document

class ClassEnrolment(Document):
    def before_save(self):
        # Retrieve the student document
        student = frappe.get_doc("Student", self.student)
        
        # Ensure the Status field is set
        # You might need to adjust this logic based on your application's rules
        if not student.status:
            student.status = 'Active'  # Or any other default or calculated status

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

            # Create a new entry in 'student_graduated_class'
            student.append("student_graduated_class", {
                "classe": student.classe,
                "parent": student.name,
                "parenttype": "Student",
                "parentfield": "student_graduated_class"
            })

            # Save changes to the student document
            student.save()
            frappe.db.commit()
