// Copyright (c) 2024, Maxamed Jayte and contributors
// For license information, please see license.txt

frappe.ui.form.on('Attendance', {
	refresh: function(frm) {

	},
	day: function (frm) {

		// get the class from the form
		var the_class = frm.doc.class;
		var day = frm.doc.day;
		// period table in the class by the day
		frappe.call({
			method: "islamic_education.islamic_education.doctype.attendance.attendance.get_class_periods",
			args: {
				the_class: the_class,
				day: day
			},
			callback: function (r) {
				if (!r.exc) {
					// there select field called period in the form fill it with the periods
					// in the class
					var periods = r.message;
					var options = [];
					console.log(periods);
					// Build options based on fetched data
					periods.forEach(function (period, index) {
						options.push(period.subject_name + ' - ' + period.period_time);
					});
					// Set options to the select field
					frm.set_df_property('period', 'options', options.join('\n'));
					frm.set_df_property('period', 'read_only', 0);
					frm.refresh_field('period');
				}
			}
		});
		
	}
});
