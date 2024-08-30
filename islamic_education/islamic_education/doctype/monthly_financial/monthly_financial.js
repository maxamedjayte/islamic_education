// Copyright (c) 2024, Maxamed Jayte and contributors
// For license information, please see license.txt

frappe.ui.form.on('Monthly Financial', {
	refresh: function(frm) {
		frm.add_custom_button(__('Generate Salary'), function() {
            frappe.call({
                method: 'islamic_education.islamic_education.doctype.monthly_financial.monthly_financial.generate_salaries',
                args: {
                    monthly_financial_name: frm.doc.name
                },
                callback: function(response) {
                    frappe.msgprint(response.message);
					frm.doc.refresh()
                }
            });
        });
	},
	validate: function (frm) {
		// check if there any montly financial in the table with the same month and year
		frappe.call({
			method:
				"islamic_education.islamic_education.doctype.monthly_financial.monthly_financial.get_monthly_financial",
			
			callback: function (r) {
				console.log('before');
				console.log(r);
				if (!r.exc) {
					console.log('after');
					console.log(r.message);
					var salary_date = fcm.doc.salary_date;

					var salary_month = salary_date.getMonth();
					var slaray_year = salary_date.getFullYear();

					if (r.message.length > 0) {
						$.each(r.message, function (i, d) {
							if (d.month == salary_month && d.year == slaray_year) {
								frappe.msgprint("Monthly Financial for " + slaray_month + " " + slaray_year + " already exists");
								frappe.validated = false;
								return;
							}
						});
					}else{
						frappe.validated = true;
					}

					
					// cur_frm.reload_doc();
				}
			},
		});
		
	}
});
