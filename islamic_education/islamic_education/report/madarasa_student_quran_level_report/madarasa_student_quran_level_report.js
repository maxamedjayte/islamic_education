// Copyright (c) 2026, Maxamed Jayte and contributors
// For license information, please see license.txt

frappe.query_reports["Madarasa Student Quran Level Report"] = {
	"filters": [
		{
			"fieldname": "madarasa_class",
			"label": "Madarasa Class",
			"fieldtype": "Link",
			"options": "Madarasa Class",
			"reqd": 1,
			"in_filter": 1
		},
		{
			"fieldname": "teacher",
			"label": "Teacher",
			"fieldtype": "Data",
			"read_only": 1
		},
		{
			"fieldname": "from_month",
			"label": "From Month",
			"fieldtype": "Date",
			"reqd": 0
		},
		{
			"fieldname": "to_month",
			"label": "To Month",
			"fieldtype": "Date",
			"reqd": 0
		}
	]

};
