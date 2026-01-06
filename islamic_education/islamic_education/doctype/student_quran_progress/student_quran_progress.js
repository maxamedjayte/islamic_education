// Copyright (c) 2025, Maxamed Jayte and contributors
// For license information, please see license.txt

frappe.ui.form.on("Student Quran Progress", {
    // refresh(frm) {

    // },
    surah: function (frm) {
        (frm.doc.madarasa_students_quran_level || []).forEach(row => {
            row.surah = frm.doc.surah;
        });
        frm.refresh_field("madarasa_students_quran_level");
    }

});


frappe.ui.form.on("Student Quran Progress", {
    madarasa_class: function (frm) {
        if (!frm.doc.madarasa_class) return;

        // تأكيد قبل المسح
        if (frm.doc.madarasa_students_quran_level && frm.doc.madarasa_students_quran_level.length > 0) {
            frappe.confirm(
                __("This will clear existing students. Continue?"),
                () => load_students(frm)
            );
        } else {
            load_students(frm);
        }
    },
    month: function (frm) {
        if (!frm.doc.month) return;
        (frm.doc.madarasa_students_quran_level || []).forEach(row => {
            row.month = frm.doc.month;
        });
        frm.refresh_field("madarasa_students_quran_level");
    }
});


function load_students(frm) {
    frm.clear_table("madarasa_students_quran_level");
    frm.refresh_field("madarasa_students_quran_level");

    frappe.call({
        method: "islamic_education.islamic_education.doctype.student_quran_progress.student_quran_progress.get_madarasa_students_by_class",
        args: {
            madarasa_class: frm.doc.madarasa_class
        },
        callback: function (r) {
            if (!r.message) return;
            console.log(r)

            r.message.forEach(student => {
                console.log(student)
                let row = frm.add_child("madarasa_students_quran_level");
                row.madarasa_student = student.name;
                row.student_name = student.student_name
                row.month = frm.doc.month;
            });

            frm.refresh_field("madarasa_students_quran_level");
            frm.reload_doc();
        }
    });
}
