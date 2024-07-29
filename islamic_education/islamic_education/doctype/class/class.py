# Copyright (c) 2024, Maxamed Jayte and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


def update_student_counts():
    classes = frappe.get_list("Class", filters={}, fields=["name"])
    # make loop to get all students for each class
    for classe in classes:
        enrolment = frappe.get_list("Student Class Enrolment", filters={"current_class": classe.name}, fields=["name"])
        # update student_counts in this classe
        frappe.db.set_value("Class", classe.name, "student_counts", len(enrolment))
        frappe.db.commit()


class Class(Document):
    def before_save(self):
	    update_student_counts()




@frappe.whitelist()
def get_active_academic_year():
    # Replace the following line with the actual logic to get the active academic year
    active_academic_year = frappe.db.get_value('Academic Year', {'active_academic_year': 1}, 'name')
    return active_academic_year





# frappe.listview_settings['Class'] = {
#     onload: function(listview) {
#         // Add your default filters here
# 		console.log("asdfghjh")
# 		frappe.call({
# 	method: "islamic_education.islamic_education.doctype.academic_year.get_active_academic_year",
# 	callback: function(response) {
# 		var active_academic_year = response.message;
# 		if (active_academic_year) {
# 			console.log("Active Academic Year: " + active_academic_year);
# 			// Add the default filter with the active academic year
# 			listview.filter_area.add([
# 				['Class', 'academic_year', '=', active_academic_year]
# 			]);
# 			listview.refresh();
# 		}
# 	}
# });
#         listview.filter_area.add([
#             ['Class', 'academic_year', '=', '1445 - 1446']
#         ]);
#         listview.refresh( );  

#     },
#     post_render: function(listview) {
#         // Add your default filters here
# 		console.log("asdfghjh")
#         listview.filter_area.add([
#             ['Class', 'academic_year', '=', '1445 - 1446']
#         ]);
#         listview.refresh( );  

#     },
    
# };