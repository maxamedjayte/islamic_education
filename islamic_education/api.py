import frappe
import json


@frappe.whitelist(allow_guest=True)
def blog_detail(student_id):
    # Render the template and pass the blog details to it
    return frappe.render_template("islamic_education/www/report/student-exam-detail/index.html", {"student_id": student_id})

@frappe.whitelist(methods=['POST'])
def get_class_day_periods_with_students():
    data = frappe.local.form_dict
    try:
        classe = data.get('classe')
        day = data.get('day')
        attend_week = data.get("attend_week")

        students = frappe.get_all("Student Class Enrolment", filters={'current_class': classe}, fields=["name","student", "student_name"])
        class_periods = frappe.get_all("Class Period", filters={'parent': classe}, fields=["name", "subject_name", "day_name", "instructor", "period_time"])
        attendance = frappe.get_all("Attendance", filters={'classe': classe, "week": attend_week, 'day': day}, fields=["name", "period", "day", "week","student","student_name","present"])

    

        frappe.response['data'] = {
            'students': students,
            'class_periods': class_periods,
            'attendance': attendance
        }

        return frappe.response['data']
        
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), 'get_class_day_periods_with_students failed')
        return {"error": str(e)}



@frappe.whitelist(methods=['POST'])
def attend_student():
    data = frappe.local.form_dict
    print(data)
    try:
        student = data.get('student')
        period = data.get('period')
        classe = data.get('classe')
        day = data.get('day')
        week = data.get('attend_week')
        present = data.get('present')

        attendance = frappe.get_all("Attendance", filters={'classe':classe,'student': student, 'period': period, 'day': day, 'week': week}, fields=["name", "student", "period", "day", "week", "present"])
        if attendance:
            attendance = frappe.get_doc("Attendance", attendance[0].name)
            attendance.present = present
            attendance.save()
        else:
            attendance = frappe.new_doc("Attendance")
            attendance.student = student
            attendance.period = period
            attendance.day = day
            attendance.classe = classe
            attendance.week = week
            attendance.present = present
            attendance.save()

        return {"message": "Attendance taken successfully"}
        
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), 'attend_student failed')
        return {"error": str(e)}



@frappe.whitelist(methods=['POST'])
def get_attending_week_detail():
    data = frappe.local.form_dict
    days = frappe.get_all("Day", fields=["name"])
    days.reverse()  # This modifies the list in place

    classe = frappe.get_doc("Class", data.get('classe'))
    students = frappe.get_all("Student Class Enrolment", filters={"current_class": classe.name}, fields=["name", "student_name"])
    frappe.response['data'] = {
            'days': days,
            'classe': classe,
            'students': students
        }
    return frappe.response['data']



@frappe.whitelist(methods=['POST'])
def save_student_attendance():
    try:
        data = frappe.local.form_dict
        attend_data = json.loads(data.get('data'))
        print(attend_data)
        print('\n\n\n\n\n\n')
        
        for atd in attend_data:
            student_id = atd['student_id']
            classe = atd['class']
            day = atd['day']
            attend_week = atd['attend_week']
            period = atd['period']
            present = atd['present']
            
            attendance = frappe.get_all("Attendance", filters={
                'classe': classe,
                'student': student_id,
                'day': day,
                'week': attend_week,
                'period': period
            }, fields=["name", "student", "day", "week"])
            if attendance:
                attendance = frappe.get_doc("Attendance", attendance[0].name)
                attendance.present = present
                attendance.save()
            else:
                attendance = frappe.new_doc("Attendance")
                attendance.student = student_id
                attendance.day = day
                attendance.classe = classe
                attendance.period = period
                attendance.week = attend_week
                attendance.present = present
                attendance.save()

        return {"message": "Attendance taken successfully"}
        
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), 'save_student_attendance failed')
        return {"error": str(e)}