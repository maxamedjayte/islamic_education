// Copyright (c) 2024, Maxamed Jayte and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Salary Report"] = {
	"filters": [
        {
            "fieldname": "salary_month",
            "label": "Salary Month",
            "fieldtype": "Link",
            "options": "Monthly Financial",
            "width": "200px"
        },
        {
            "fieldname": "employee",
            "label": "Employee",
            "fieldtype": "Link",
            "options": "Worker",
            "width": "200px"
        }
    ]

};

