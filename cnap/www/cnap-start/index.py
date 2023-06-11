import frappe

def get_context(context):
    them_areas = frappe.db.get_list('CNAP Thematic area',
                                    fields=['name', 'description'],)
    context.them_areas = them_areas
    return context 