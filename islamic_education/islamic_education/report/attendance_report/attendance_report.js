// Copyright (c) 2024, Maxamed Jayte and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Attendance Report"] = {
	"filters": [
		{
            "fieldname": "the_class",
            "label": __("Class"),
            "fieldtype": "Link",
            "options": "Class",
            "reqd": 1,
            "width":"300px",
        },
		{
            "fieldname": "the_week",
            "label": __("Week"),
            "fieldtype": "Link",
            "options": "Attend Week",
            "reqd": 1,
            "width":"300px",
        },
		// {
        //     "fieldname": "the_day",
        //     "label": __("Day"),
        //     "fieldtype": "Link",
        //     "options": "Day",
        //     "reqd": 1,
        //     "width":"300px",
        // },
	]
};
