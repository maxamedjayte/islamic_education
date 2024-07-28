// Copyright (c) 2024, Maxamed Jayte and contributors
// For license information, please see license.txt

frappe.ui.form.on('Class', {
	refresh: function(frm) {
		// filter the academic year based on the selected academic term
	// 	frm.set_query("academic_year", function() {
	// 		return {
	// 			"filters": {
	// 				"active_academic_year": 1
	// 			}
	// 		};
	// 	}
	// );

	frm.fields_dict['class_period'].grid.get_field('subject').get_query = function(doc, cdt, cdn) {
		var child = locals[cdt][cdn];
		return {
			filters: [
				['the_classe', '=', frm.doc.name] // Ensure this field name and condition match your use case
			]
		};
	};

	}
});


