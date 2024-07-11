// Copyright (c) 2024, Maxamed Jayte and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Student Exam Report"] = {
	"filters": [
		{
            "fieldname": "student",
            "label": __("Student"),
            "fieldtype": "Link",
            "options": "Student",
            "reqd": 1,
            "width":"300px"
        }
        
	]
};
