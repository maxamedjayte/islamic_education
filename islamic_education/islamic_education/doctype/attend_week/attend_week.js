// Copyright (c) 2024, Maxamed Jayte and contributors
// For license information, please see license.txt

frappe.ui.form.on('Attend Week', {
	refresh: function(frm) {
		
		frm.add_custom_button(__("Xaadirinta Ardada"), function () {
			// delete all students in the table from the database
			window.location.href = '/fr/attending-week/'+frm.doc.name;

		}).css({
			"background-color": "#28a745",
			"border-color": "#28a745",
			"color": "#fff"
		});
	}
});
