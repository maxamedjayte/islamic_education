// Copyright (c) 2024, Maxamed Jayte and contributors
// For license information, please see license.txt

frappe.ui.form.on("Exam Marks", {
	refresh: function (frm) {
		// check if there are any students in the table

		var exam_entry_marks = frm.doc.exam_entry_marks;
		// if there are students in the table, show clear students button
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
		} else if (exam_entry_marks.length == 0 && frm.doc.docstatus == 0) {

			frm.add_custom_button(__("Get Students"), function () {
				frappe.call({
					method:
						"islamic_education.islamic_education.doctype.exam_marks.exam_marks.get_students",
					args: {
						class_id: frm.doc.the_class
					},
					callback: function (r) {
						console.log('before');
						console.log(r);
						if (!r.exc) {
							console.log('after');
							console.log(r.message);

							frm.clear_table("exam_entry_marks");
							$.each(r.message, function (i, d) {
								console.log('inside')
								console.log(d.name);
								var row = frm.add_child("exam_entry_marks");
								row.student = d.name;
							});
							frm.refresh_field("exam_entry_marks");
							frm.save();
							// cur_frm.reload_doc();
						}
					},
				});
			});
		}
	},
	// validate
	validate: function (frm) {
		// check if there are any students in the table
		// check if there any Exam marks with filters exam_announcement, student_class, subject exists
		try {
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
					if (!r.exc) {
						console.log(r.message);
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
		} catch (error) {
			console.log('errroror')
			console.log(error)
		}

	},

	the_class: function (frm) {
		// clear subjects field
		frm.set_value("subject", "");
		frm.set_query("subject", function () {
			return {
				filters: {
					the_classe: frm.doc.the_class,
				},
			};
		});
	},
});

