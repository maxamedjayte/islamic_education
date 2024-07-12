// Copyright (c) 2024, Maxamed Jayte and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student', {
	refresh: function(frm) {
		frm.add_custom_button(__("Exam Report"), function () {
			// delete all students in the table from the database
            window.location.href = `/report/student-exam-detail/${frm.doc.name}`;
		}).css({
			"background-color": "#6F4E37",
			"border-color": "#28a745",
			"color": "#fff"
		});
		frm.add_custom_button(__("Attendece Report"), function () {
			// delete all students in the table from the database
			window.location.href = '/report/student-attendence-detail.html';

		}).css({
			"background-color": "#28a745",
			"border-color": "#28a745",
			"color": "#fff"
		});
	}
});
