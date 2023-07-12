// Copyright (c) 2023, Maxim Sysoev and contributors
// For license information, please see license.txt

// frappe.ui.form.on("CNAP Office", {
// 	refresh(frm) {

// 	},
// });
function UpdateMap(frm) {
    let lat = frm.doc.latitude;
    let lon = frm.doc.longitude;//frm.get_value('latitude');
    var map = frm.get_field("map").map;
    map.eachLayer((layer) => {
        if (layer['_latlng'] != undefined)
            layer.remove();
    });
    var latlng = L.latLng({ 'lat': lat, 'lng': lon });
    var marker = L.marker(latlng);

    map.flyTo(latlng, map.getZoom());
    marker.addTo(map);
}

frappe.ui.form.on("CNAP Office", {
    // btn_get_adress: {
    refresh(frm) {
        UpdateMap(frm);

    }
    ,
    btn_get_adress(frm) {
        let address = frm.doc.adress;
        frappe.call({
            type: "GET",
            url: 'https://nominatim.openstreetmap.org/search.php',
            args: {
                'q': address,
                'format': 'jsonv2'
            },
            error: function (r) {
                console.log(r);
            },
            callback: function (r) {
                // frm.set_value("template", r.message);
                console.log(r[0].lon);
                frm.set_value('latitude', r[0].lat);
                frm.set_value('longitude', r[0].lon);
                UpdateMap(frm);

            }
        })

    },
});
