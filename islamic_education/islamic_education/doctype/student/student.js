// Copyright (c) 2024, Maxamed Jayte and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student', {
	refresh: function(frm) {
		// add button student report
		frm.add_custom_button(__('Student Report'), function() {
			window.location.href = '/fr/report/student/detail/'+frm.doc.name;

		}
		).css({"background-color": "#097969", "color": "white"});
		// add button student report
	}
});
