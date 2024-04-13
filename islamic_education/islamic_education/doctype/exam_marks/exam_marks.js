// Copyright (c) 2024, Maxamed Jayte and contributors
// For license information, please see license.txt

frappe.ui.form.on("Exam Marks", {
	refresh: function (frm) {
		// check if there are any students in the table
		var exam_entry_marks = frm.doc.exam_entry_marks;
		// // if there are students in the table, show clear students button
		if (exam_entry_marks.length > 0 && frm.doc.docstatus == 0) {
			frm.add_custom_button(__("Clear Students"), function () {
				// delete all students in the table from the database
				frappe.call({
					method:
						"islamic_education.islamic_education.doctype.exam_marks.exam_marks.delete_exam_marks",
					args: {
						exam_id: frm.doc.name,
					},
					callback: function (r) {
						console.log(r);
						if (!r.exc) {
							console.log(r.message);
							frm.clear_table("exam_entry_marks");
							frm.save();
							cur_frm.reload_doc();
						}
					},
				});
			});
			frm.add_custom_button(__("Update Students"), function () {
				// delete all students in the table from the database
				frappe.call({
					method:
						"islamic_education.islamic_education.doctype.exam_marks.exam_marks.get_students",
					args: {
						class_id: frm.doc.the_class,
					},
					callback: function (r) {
						
						if (!r.exc) {
							console.log(r.message);
							$.each(r.message, function (i, d) {
								// chech if the student is already in the table
								var student_in_table = false;
								$.each(frm.doc.exam_entry_marks, function (i, e) {
									if (e.student == d.name) {
										student_in_table = true;
									}
								});
								if (!student_in_table) {
									var row = frm.add_child("exam_entry_marks");
									row.student = d.name;
									row.marks=0;
								}
								
							});
							frm.refresh_field("exam_entry_marks");
							frm.save();
						}

					},
				});
			}).css({
				"background-color": "#28a745",
				"border-color": "#28a745",
				"color": "#fff"
			}); ;
		} else if (exam_entry_marks.length == 0 && frm.doc.docstatus == 0) {

			frm.add_custom_button(__("Get Students"), function () {
				frappe.call({
					method:
						"islamic_education.islamic_education.doctype.exam_marks.exam_marks.get_students",
					args: {
						class_id: frm.doc.the_class
					},
					callback: function (r) {
						if (!r.exc) {
							try {
							frm.clear_table("exam_entry_marks");
							$.each(r.message, function (i, d) {
								var row = frm.add_child("exam_entry_marks");
								row.student = d.name;
								row.marks=0;
							});
							frm.refresh_field("exam_entry_marks");
							frm.save();
							} catch (error) {
								// alert
								frappe.msgprint("No students found for this class")
							}
						}
					},
				});
			});
		}
	},
	// validate
	validate: function (frm) {
			if(frm.doc.creation){
				console.log('creation')
			}else{
				frappe.call({
					method:
						"islamic_education.islamic_education.doctype.exam_marks.exam_marks.get_exam_marks",
					args: {
						exam_announcement: frm.doc.exam_announcement,
						the_class: frm.doc.the_class,
						subject: frm.doc.subject,
					},
					callback: function (r) {
						console.log(r);
						console.log('callback')
						if (!r.exc) {
							console.log(r.message);
							console.log('message')
							if (r.message) {
								//   if there r.message arraly greater than 0
								if (r.message.length > 0) {
									frappe.validated = false;
									// redirect to the exam marks with this name
									frappe.set_route("Form", "Exam Marks", r.message[0].name);
								} else {
									frappe.validated = true;
								}
							}
						}
					}
				});
			};

			
		

	},

	the_class: function (frm) {
		// clear subjects field
		frm.set_value("subject", "");
		frm.set_query("subject", function () {
			return {
				filters: {
					the_classe: frm.doc.the_class
				},
			};
		});
	},
});

