import frappe

def get_context(context):
    them_areas = frappe.db.get_list('CNAP Thematic area',
                                    fields=['name', 'description'],)
    config = frappe.get_doc('Cnap Config')
    context.config = config                
    context.them_areas = them_areas

    return context 