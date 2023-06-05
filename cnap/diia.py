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
    jtotal = 500#len(json_object["entries"])
    for entrie in json_object["entries"]: 
        i = i + 1
        frappe.publish_progress(percent=i / jtotal * 100, title=frappe._("Download"))
        if i > jtotal:
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
        doc.sowner = entrie["owner"]
        doc.service_provider = json.dumps(entrie["service_provider"], indent=4, ensure_ascii=False)
        doc.legal_base = entrie["legal_base"]
        doc.refusal_grounds = json.dumps(entrie["refusal_grounds"], indent=4, ensure_ascii=False)
        doc.applicant_type = json.dumps(entrie["applicant_type"], indent=4, ensure_ascii=False)
        doc.access_link = entrie["access_link"]
        doc.regulatory_documents = json.dumps(entrie["regulatory_documents"], indent=4, ensure_ascii=False)
        doc.events = json.dumps(entrie["events"], indent=4, ensure_ascii=False)
        doc.refusal_appeal_person = json.dumps(entrie["refusal_appeal_person"], indent=4, ensure_ascii=False)
        doc.is_appealed_in_court = entrie["is_appealed_in_court"]
        doc.refusal_appeal_rules = json.dumps(entrie["refusal_appeal_rules"], indent=4, ensure_ascii=False)
        doc.produces = json.dumps(entrie["produces"], indent=4, ensure_ascii=False)
        doc.input = entrie["input"]
        doc.application_ways = json.dumps(entrie["application_ways"], indent=4, ensure_ascii=False)
        doc.receiving_ways = json.dumps(entrie["receiving_ways"], indent=4, ensure_ascii=False)
        doc.processing_durations = entrie["processing_durations"]
        doc.costs = entrie["costs"]
        doc.variations = json.dumps(entrie["variations"], indent=4, ensure_ascii=False)
       # doc.data = json.dumps(entrie)
        doc.save()
        doc.notify_update()
    doc.save()
    doc.notify_update()
    frappe.msgprint('Updated', 'Done')
    return r.text