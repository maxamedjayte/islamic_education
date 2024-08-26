frappe.ui.form.on('Employee Salary', {
    before_submit: function(frm) {
        if (frm.doc.balance != 0) {
            frappe.confirm(
                `The balance is not zero (${frm.doc.balance}). Are you sure you want to submit?`,
                function() {
                    // If the user confirms, submit the document
                    frm.savesubmit();
                },
                function() {
                    // If the user cancels, do nothing
                    frappe.msgprint('Submission cancelled.');
                }
            );

            // Prevent the automatic submission
            frappe.validated = false;
        }
    }
});
