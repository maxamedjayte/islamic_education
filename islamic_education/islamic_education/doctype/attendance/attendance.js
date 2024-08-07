// Copyright (c) 2024, Maxamed Jayte and contributors
// For license information, please see license.txt

frappe.ui.form.on('Attendance', {
	refresh: function(frm) {
		console.log(frm.doc);
		var attending_table = frm.doc.attending_table;
		// // if there are students in the table, show clear students button
		if (attending_table.length > 0 && frm.doc.docstatus == 0) {
			frm.add_custom_button(__("Clear Students"), function () {
				// delete all students in the table from the database
				frappe.call({
					method:
						"islamic_education.islamic_education.doctype.attendance.attendance.delete_attendance",
					args: {
						attendance_id: frm.doc.name,
					},
					callback: function (r) {
						console.log(r);
						if (!r.exc) {
							console.log(r.message);
							frm.clear_table("attending_table");
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
						class_id: frm.doc.class,
					},
					callback: function (r) {
						
						if (!r.exc) {
							console.log(r.message);
							$.each(r.message, function (i, d) {
								// chech if the student is already in the table
								var student_in_table = false;
								$.each(frm.doc.attending_table, function (i, e) {
									if (e.student == d.name) {
										student_in_table = true;
									}
								});
								if (!student_in_table) {
									var row = frm.add_child("attending_table");
									row.student = d.name;
									row.present=1;
								}
								
							});
							frm.refresh_field("attending_table");
							frm.save();
						}

					},
				});
			}).css({
				"background-color": "#28a745",
				"border-color": "#28a745",
				"color": "#fff"
			}); ;
		} else if (attending_table.length == 0 && frm.doc.docstatus == 0) {

			frm.add_custom_button(__("Get Students"), function () {
				frappe.call({
					method:
						"islamic_education.islamic_education.doctype.exam_marks.exam_marks.get_students",
					args: {
						class_id: frm.doc.class
					},
					callback: function (r) {
						if (!r.exc) {
							try {
							frm.clear_table("attending_table");
							$.each(r.message, function (i, d) {
								var row = frm.add_child("attending_table");
								row.student = d.name;
								row.marks=0;
							});
							frm.refresh_field("attending_table");
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
	// validation
	validation: function (frm) {
		
	},
	day: function (frm) {

		// get the class from the form
		var the_class = frm.doc.classe;
		var day = frm.doc.day;
		// period table in the class by the day
		frappe.call({
			method: "islamic_education.islamic_education.doctype.attendance.attendance.get_class_periods",
			args: {
				the_class: the_class
			},
			callback: function (r) {
				if (!r.exc) {
					// there select field called period in the form fill it with the periods
					// in the class
					var periods = r.message;
					var options = [];
					// Build options based on fetched data
					periods.forEach(function (period, index) {
						if (period.day==day) {
							options.push(period.subject_name);
						}
					});
					// Set options to the select field
					frm.set_df_property('period', 'options', options.join('\n'));
					frm.set_df_property('period', 'read_only', 0);
					frm.refresh_field('period');
				}
			}
		});
		
	},
	// when period changes update period_time field
	// period: function (frm) {
	// 	console.log("\n\n\n\n\n\n\n")
	// 	console.log(frm.doc.period);
	// 	// get the class from the form
	// 	var the_class = frm.doc.class;
	// 	var period = frm.doc.period;
	// 	// period table in the class by the day
		
	// },
});
