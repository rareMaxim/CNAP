import frappe

def get_context(context):
    doc_id = frappe.form_dict.docname
    context.service = frappe.get_doc("CNAP Service", doc_id)
    return context
