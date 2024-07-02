// Copyright (c) 2024, Maxamed Jayte and contributors
// For license information, please see license.txt

frappe.ui.form.on('Class', {
	refresh: function(frm) {
		// filter the academic year based on the selected academic term
		frm.set_query("academic_year", function() {
			return {
				"filters": {
					"active_academic_year": 1
				}
			};
		}
	);
	}
});


