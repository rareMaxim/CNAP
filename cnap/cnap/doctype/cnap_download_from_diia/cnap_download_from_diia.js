// Copyright (c) 2023, Maxim Sysoev and contributors
// For license information, please see license.txt

frappe.ui.form.on("CNAP Download From Diia", {
    refresh(frm) {
        frm.add_custom_button('Download', () => {
            frappe.call({
                method: "cnap.diia.download_json",
                args: {
                    url: "https://guide.diia.gov.ua/register/download/json/"
                },
                callback: function (r) {
                    // frm.set_value("template", r.message);
                    console.log('fff');
                }
            })
        });
        frm.change_custom_button_type('Download', null, 'primary');
    }
});
