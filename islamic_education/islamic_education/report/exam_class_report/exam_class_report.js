// Copyright (c) 2024, Maxamed Jayte and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Exam Class Report"] = {
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
            "fieldname": "the_exam",
            "label": __("Exam"),
            "fieldtype": "Link",
            "options": "Exam Announcement",
            "reqd": 1,
            "width":"300px",
        }
    ]
};
