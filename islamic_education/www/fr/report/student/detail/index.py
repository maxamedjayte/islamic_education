import frappe

def get_context(context):
    context.student_detail = frappe.get_doc("Student", frappe.form_dict)
    context.student_classes = frappe.get_all("Student Class Enrolment", filters={"student": context.student_detail.name}, fields=["*"])
    
    # Dictionary to hold attendance data week by week
    context.weekly_attendance = {}

    for student_enrolment in context.student_classes:
        # Get all attendance records for this student enrolment
        attendance_records = frappe.get_all("Attendance", filters={"student": student_enrolment.name}, fields=["student","week","present","day","period","period_time"])
        
        for record in attendance_records:
            week = record.get('week')  # Assuming 'week' is the field linking to the Attend Week doc
            if week not in context.weekly_attendance:
                context.weekly_attendance[week] = {
                    'attendance': [],
                    'total_present': 0,
                    'total_apsent': 0,
                }
            
            context.weekly_attendance[week]['attendance'].append(record)
            context.weekly_attendance[week]['total_present'] += 1 if record.get('present') else 0
            context.weekly_attendance[week]['total_apsent'] += 1 if not record.get('present') else 0

    # Optionally, fetch more details for each week if needed
    print('n\n\n\n\n\n\n\n\n\n\    ')
    print(context.weekly_attendance)
    context.attend_weeks = []
    for week_key in context.weekly_attendance.keys():
        week_details = frappe.get_doc("Attend Week", week_key)
        context.attend_weeks.append(week_details)

    return context
