# Copyright (c) 2026, Maxamed Jayte and contributors
# For license information, please see license.txt
import frappe
from frappe.utils import flt, formatdate

def execute(filters=None):
    columns, data = get_columns(), get_data(filters)
    return columns, data

def get_columns():
    return [
        {"label": "Student Name", "fieldname": "student_name", "fieldtype": "Data", "width": 200},
        {"label": "Gender", "fieldname": "gender", "fieldtype": "Data", "width": 100},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 100},
        {"label": "Surah", "fieldname": "surah", "fieldtype": "Data", "width": 200},
        {"label": "Surah Number", "fieldname": "surah_number", "fieldtype": "Int", "width": 120},
        {"label": "Ayah", "fieldname": "ayah", "fieldtype": "Data", "width": 120},
        {"label": "Month", "fieldname": "month", "fieldtype": "Data", "width": 120}
    ]

def get_data(filters):
    if not filters:
        filters = {}

    conditions = []
    params = {}

    if filters.get("madarasa_class"):
        conditions.append("sqp.madarasa_class = %(madarasa_class)s")
        params["madarasa_class"] = filters['madarasa_class']

    if filters.get("from_month"):
        conditions.append("sqp.month >= %(from_month)s")
        params["from_month"] = filters['from_month']

    if filters.get("to_month"):
        conditions.append("sqp.month <= %(to_month)s")
        params["to_month"] = filters['to_month']

    # Only show submitted documents
    conditions.append("sqp.docstatus = 1")

    condition_str = " AND ".join(conditions)
    if condition_str:
        condition_str = "WHERE " + condition_str

    # Fetch student progress
    progress = frappe.db.sql(f"""
        SELECT
            ms.student_name,
            ms.gender,
            ms.status,
            t.surah,
            t.surah_number,
            t.ayah_number as ayah,
            sqp.month
        FROM `tabStudent Quran Progress` sqp
        INNER JOIN `tabMadarasa Students Quran Level` t
            ON sqp.name = t.parent
        INNER JOIN `tabMadarasa Student` ms
            ON t.madarasa_student = ms.name
        {condition_str}
        ORDER BY ms.student_name, sqp.month
    """, params, as_dict=True)

    # Organize data by student
    student_dict = {}
    for row in progress:
        student = row['student_name']
        if student not in student_dict:
            student_dict[student] = {
                "student_name": student,
                "gender": row.get('gender'),
                "status": row.get('status'),
                "progress": []
            }
        student_dict[student]['progress'].append(row)
    
    # Sort progress by month for each student and calculate surah taken (last - first)
    for student, data in student_dict.items():
        # Sort progress by month (handle None values)
        data['progress'].sort(key=lambda x: x.get('month') or '1900-01-01')
        # Calculate surah taken: last_month surah_number - first_month surah_number
        if data['progress']:
            first_surah = flt(data['progress'][0].get('surah_number', 0))
            last_surah = flt(data['progress'][-1].get('surah_number', 0))
            data['surah_taken'] = last_surah - first_surah
        else:
            data['surah_taken'] = 0

    # Build final result with collapsible effect using indent pattern
    final_result = []
    grand_total = 0
    
    for student, data in student_dict.items():
        # Parent row: student info with bold formatting
        final_result.append({
            "student_name": f"<b>{data['student_name']}</b>",
            "gender": f"<b>{data['gender'] or ''}</b>",
            "status": f"<b>{data['status'] or ''}</b>",
            "surah_number": data['surah_taken'],  # Show surah taken (last - first) as number
            "indent": 0  # No indentation for parent row
        })
        grand_total += data['surah_taken']

        # Child rows: Quran progress indented
        for prog in data['progress']:
            month_value = prog.get('month')
            month_display = formatdate(month_value) if month_value else ""
            final_result.append({
                "student_name": "",  # Empty to align under student name
                "surah": prog.get('surah', ''),
                "surah_number": prog.get('surah_number', 0),
                "ayah": prog.get('ayah', ''),
                "month": month_display,
                "indent": 1  # Indent this row under the main student
            })
        
        # Summary row: surah taken with month range (indented, no "Total" label)
        valid_months = [prog.get('month') for prog in data['progress'] if prog.get('month')]
        if valid_months:
            month_range = f"{formatdate(min(valid_months))} - {formatdate(max(valid_months))}"
        else:
            month_range = ""
        final_result.append({
            "student_name": "",  # Empty, no "Total" label
            "surah_number": data['surah_taken'],  # Show surah taken as number
            "month": f"<b>{month_range}</b>",  # Bold month range
            "indent": 1  # Indent this row under the main student
        })

    # Add grand total row
    final_result.append({
        "student_name": "<b>TOTAL</b>",
        "surah_number": grand_total,  # Show grand total as number
        "indent": 0
    })

    return final_result
