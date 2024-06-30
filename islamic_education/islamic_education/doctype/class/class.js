// Copyright (c) 2024, Maxamed Jayte and contributors
// For license information, please see license.txt

frappe.ui.form.on('Class', {
	// refresh: function(frm) {

	// }
});

// Inside a client-side script file or form script
frappe.call({
    method: "islamic_education.doctype.class.class.redirect_to_year",
    args: {
        "academic_year": "2024-2025"
    },
    callback: function(r) {
        if (!r.exc) {
            window.location.href = r.message;
        }
    }
});
