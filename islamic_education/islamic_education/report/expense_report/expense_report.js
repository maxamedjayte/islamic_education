// Copyright (c) 2024, Maxamed Jayte and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Expense Report"] = {
    "filters": [
        {
            "fieldname": "expense_month",
            "label": __("Monthly Financial"),
            "fieldtype": "Link",
            "options": "Monthly Financial",
            "width": "300px",
        },
    ]
};
