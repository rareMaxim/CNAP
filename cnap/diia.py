import json
import frappe
import requests


@frappe.whitelist()
def download_json(url):
    headers = {'content-type': 'application/json'}
    r = requests.get(url, headers=headers)
    doc = frappe.get_doc('CNAP Download From Diia')
    json_object = json.loads(r.text)
    i = 0
    for entrie in json_object["entries"]: 
        i = i + 1
        if i > 20:
            break
        if not frappe.db.exists('CNAP Diia RAW', entrie["identifier"]):
            doc = frappe.new_doc('CNAP Diia RAW')
            doc.identifier = entrie["identifier"]
            doc.insert()
        else:
            doc = frappe.get_doc('CNAP Diia RAW', entrie["identifier"])
            doc.identifier = entrie["identifier"]
        doc.thematic_area = entrie["thematic_area"]
        doc.sector = entrie["sector"]
        doc.sname = entrie["name"]
        doc.level = entrie["level"]
        doc.keyword = entrie["keyword"]
        doc.short_description_plain = entrie["short_description_plain"]
        doc.spatial = entrie["spatial"]
        doc.moderation_status = entrie["moderation_status"]
        doc.created_at = entrie["created_at"]
       # doc.data = json.dumps(entrie)
        doc.save()
        doc.notify_update()
    doc.save()
    doc.notify_update()
    frappe.msgprint('Updated', 'Done')
    return r.text