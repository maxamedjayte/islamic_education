import frappe



@frappe.whitelist(allow_guest=True)
def blog_detail(student_id):
    # Render the template and pass the blog details to it
    return frappe.render_template("islamic_education/www/report/student-exam-detail/index.html", {"student_id": student_id})