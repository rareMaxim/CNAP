// Copyright (c) 2023, Maxim Sysoev and contributors
// For license information, please see license.txt

frappe.ui.form.on("test", {

    refresh(frm) {
        // your code here
        // Custom buttons in groups
        frm.add_custom_button('Closed', () => {
            frm.doc.status = 'Closed'
        }, 'Set Status');
    },

});
