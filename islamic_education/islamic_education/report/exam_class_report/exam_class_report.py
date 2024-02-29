import frappe

def get_columns(filters=None):
    columns = [
        {"label": "الطالاب", "fieldname": "student", "fieldtype": "Link", "options": "Student", "width": 200},
    ]

    subjects = frappe.get_all("Subject", fields=["name", "subject_name"])
    for subject in subjects:
        columns.append({"label": subject.subject_name, "fieldname": subject.name, "fieldtype": "Float", "width": 100})

    columns.append({"label": "مجموع", "fieldname": "total", "fieldtype": "Float", "width": 100})
    return columns

def execute(filters=None):
    columns = get_columns(filters)
    data = []

    # get student with this class
    students = frappe.get_all("Student", filters={"classe": filters.get("the_class")}, fields=["name", "student_name"])
    for student in students:
        subject_total = 0
        row = {"student": student.student_name}
        subjects = frappe.get_all("Subject", fields=["name", "subject_name"])
        for subject in subjects:
            # Get the marks of the student for the subject
            exam_marks = frappe.get_all("Exam Marks", filters={"subject": subject.name,"exam_announcement":filters.get("the_exam")}, fields=["name"])
            if exam_marks:
                exam_entry_marks = frappe.get_all("Exam Entry Marks", filters={"student": student.name, "parent" :exam_marks[0].name }, fields=["mark"])
                if exam_entry_marks:
                    row[subject.name] = exam_entry_marks[0].mark
                    subject_total += exam_entry_marks[0].mark
                    row["total"] = subject_total
            # row[subject.subject_name] = 0
        data.append(row)

    return columns, data
